"""
Nodes' configurations for *fieldmap_query* workflow
"""
import nipype.pipeline.engine as pe
from dmriprep.workflows.dwi.fieldmap_query.configurations import (
    OPPOSITE_PHASE_QUERY_KWARGS,
)
from nipype.interfaces import utility as niu


def is_same_size(fmap: str, dwi: str):
    """
    Checks if the fieldmap and the DWI are of the same size
    """
    from pathlib import Path

    import numpy as np
    import pandas as pd

    fmap, dwi = Path(fmap), Path(dwi)
    fmap_bval_file, dwi_bval_file = [
        f.parent / f"{f.name.split('.')[0]}.bval" for f in [fmap, dwi]
    ]
    fmap_bval, dwi_bval = [
        pd.read_csv(bval_file, sep=" ", header=None).values[0]
        for bval_file in [fmap_bval_file, dwi_bval_file]
    ]
    return np.count_nonzero(fmap_bval < 100) == np.count_nonzero(
        dwi_bval < 100
    )


def locate_opposite_phase(dwi_file: str):
    """
    Locates

    Parameters
    ----------
    dwi_file : str
        _description_
    """
    from bids.layout import parse_file_entities
    from dmriprep.config import config
    from dmriprep.workflows.dwi.fieldmap_query.utils import check_opposite

    layout = config.execution.layout
    # Parse entities from dwi_file
    entities = parse_file_entities(dwi_file)
    _ = entities.pop("direction", None)
    # Query DWI file's phase direction
    dwi_pe_dir = layout.get_metadata(dwi_file).get("PhaseEncodingDirection")
    # Check if opposite phase DWI is available
    fieldmap_is_dwi = True
    available_dwis = layout.get("file", **entities)
    available_dwis.remove(str(dwi_file))
    opposite_dwis = []
    for dwi in available_dwis:
        if check_opposite(dwi_pe_dir, dwi, layout):
            opposite_dwis.append(dwi)
    if len(opposite_dwis) == 1:
        return opposite_dwis[0], fieldmap_is_dwi, dwi_pe_dir
    elif len(opposite_dwis) > 1:
        config.logger.warning(
            """Located more than one opposite phase DWI.
            Will use the first one."""
        )
        return opposite_dwis[0], fieldmap_is_dwi, dwi_pe_dir
    fieldmap_is_dwi = False
    # If no opposite phase DWI is available, look for dedicated fieldmaps
    fieldmaps = layout.get_fieldmap(dwi_file, return_list=True)
    if fieldmaps:
        fnames = [list(val.values())[0] for val in fieldmaps]
    opposite_fmaps = []
    for fname in fnames:
        if check_opposite(dwi_pe_dir, fname, layout):
            opposite_fmaps.append(fname)
    if len(opposite_fmaps) == 1:
        return opposite_fmaps[0], fieldmap_is_dwi, dwi_pe_dir
    elif len(opposite_fmaps) > 1:
        config.logger.warning(
            """Located more than one opposite phase fieldmap.
            Will use the first one."""
        )
        return opposite_fmaps[0], fieldmap_is_dwi, dwi_pe_dir
    # If no opposite phase fieldmap is available, raise error
    raise NotImplementedError(
        """No opposite phase fieldmap/DWI series found.
    Workflows that do not include PEPOLAR SDC are not currently supported."""
    )


#: Building blocks
OPPOSITE_PHASE_NODE = pe.Node(
    niu.Function(
        **OPPOSITE_PHASE_QUERY_KWARGS, function=locate_opposite_phase
    ),
    name="locate_opposite_phase",
)
