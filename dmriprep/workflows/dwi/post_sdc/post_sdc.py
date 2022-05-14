import nipype.pipeline.engine as pe
from dmriprep.workflows.dwi.post_sdc.edges import (
    BIASCORRECT_TO_EXTRACT_EDGES,
    BIASCORRECT_TO_NII_EDGES,
    INPUT_TO_BIASCORRECT_EDGES,
    INPUT_TO_EXTRACT_EDGES,
)


def init_post_sdc_wf(name: str = "post_sdc_wf") -> pe.Workflow:
    """
    Post-SDC workflow

    Parameters
    ----------
    name : str, optional
        Name of workflow. Defaults to "post_sdc_wf".

    Returns
    -------
    post_sdc_wf : nipype.pipeline.engine.Workflow
        Post-SDC workflow.
    """
    from dmriprep.config import config
    from dmriprep.workflows.dwi.conversions.mif_to_nii.nodes import (
        init_conversion_node,
    )
    from dmriprep.workflows.dwi.post_sdc.bias_correction import (
        init_bias_correction_node,
    )
    from dmriprep.workflows.dwi.post_sdc.nodes import init_inputnode
    from dmriprep.workflows.dwi.utils.extract_bzero.extract_bzero import (
        init_extract_bzero_wf,
    )

    wf = pe.Workflow(name=name)
    inputnode = init_inputnode()
    biascorrect = init_bias_correction_node()
    nii_conversion = init_conversion_node(is_dwi=True)
    extract_bzero = init_extract_bzero_wf()
    if "biascorrect" not in config.workflow.ignore:
        wf.connect(
            [
                (inputnode, biascorrect, INPUT_TO_BIASCORRECT_EDGES),
                (biascorrect, nii_conversion, BIASCORRECT_TO_NII_EDGES),
                (biascorrect, extract_bzero, BIASCORRECT_TO_EXTRACT_EDGES),
            ]
        )
    else:
        wf.connect(
            [
                (inputnode, nii_conversion, INPUT_TO_BIASCORRECT_EDGES),
                (inputnode, extract_bzero, INPUT_TO_EXTRACT_EDGES),
            ]
        )

    return wf
