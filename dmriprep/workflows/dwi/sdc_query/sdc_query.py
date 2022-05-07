import re
from pathlib import Path
from typing import Union

from sdcflows.fieldmaps import get_identifier


def sdc_query(dwi_file: Union[str, Path], layout) -> dict:
    """
    Query SDC for dwi data.

    Parameters
    ----------
    dwi_file : str
        Path to dwi file.
    layout : _type_
        Pybids layout object.

    Returns
    -------
    dict
        Dictionary of SDC-relevant data.
    """
    dwi_file = Path(dwi_file)
    dwi_rel = re.sub(
        r"^sub-[a-zA-Z0-9]*/", "", str(dwi_file.relative_to(layout.root))
    )
    estimator_key = get_identifier(dwi_rel)
    if not estimator_key:
        has_fieldmap = False
        config.loggers.workflow.critical(
            f"None of the available B0 fieldmaps are associated to <{dwi_rel}>"
        )
