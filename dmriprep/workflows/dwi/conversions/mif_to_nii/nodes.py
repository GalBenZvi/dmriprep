import nipype.pipeline.engine as pe
from dmriprep.workflows.dwi.conversions.mif_to_nii.configurations import (
    DWI_CONVERSION_KWARGS,
    NON_DWI_CONVERSION_KWARGS,
)
from nipype.interfaces import mrtrix3 as mrt


def init_conversion_node(
    is_dwi: bool, name: str = "conversion_node"
) -> pe.Node:
    """
    Conversion node

    Parameters
    ----------
    is_dwi : bool
        Whether the node is for DWI conversion.
    name : str, optional
        Name of workflow. Defaults to "conversion_node".

    Returns
    -------
    conversion_node : nipype.pipeline.engine.Node
        Conversion node.
    """

    if is_dwi:
        return pe.Node(
            mrt.MRConvert(**DWI_CONVERSION_KWARGS), name=f"dwi_{name}"
        )
    else:
        return pe.Node(
            mrt.MRConvert(**NON_DWI_CONVERSION_KWARGS), name=f"non_dwi_{name}"
        )
