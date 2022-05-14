import nipype.pipeline.engine as pe
from dmriprep.workflows.dwi.post_sdc.edges import (
    BIASCORRECT_TO_NII_EDGES,
    INPUT_TO_BIASCORRECT_EDGES,
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
    from dmriprep.workflows.dwi.post_sdc.epi_reg.epi_reg import init_epireg_wf
    from dmriprep.workflows.dwi.post_sdc.nodes import init_inputnode
    from dmriprep.workflows.dwi.utils.extract_bzero.extract_bzero import (
        init_extract_bzero_wf,
    )

    # from dmriprep.workflows.dwi.utils.extract_bzero.nodes import (
    #     init_extract_node,
    #     init_mean_b0_node,
    # )

    wf = pe.Workflow(name=name)
    inputnode = init_inputnode()
    biascorrect = init_bias_correction_node()
    nii_conversion = init_conversion_node(is_dwi=True)
    extract_bzero = init_extract_bzero_wf()
    epireg_wf = init_epireg_wf()
    # extract_bzero = init_extract_node()
    # mean_bzero = init_mean_b0_node()
    if "biascorrect" not in config.workflow.ignore:
        wf.connect(
            [
                (inputnode, biascorrect, INPUT_TO_BIASCORRECT_EDGES),
                (biascorrect, nii_conversion, BIASCORRECT_TO_NII_EDGES),
                (
                    biascorrect,
                    extract_bzero,
                    [("out_file", "extract_b0.in_file")],
                ),
            ]
        )
    else:
        wf.connect(
            [
                (inputnode, nii_conversion, INPUT_TO_BIASCORRECT_EDGES),
                (
                    inputnode,
                    extract_bzero,
                    [("dwi_file", "extract_b0.in_file")],
                ),
            ]
        )
    wf.connect(
        [
            (
                extract_bzero,
                epireg_wf,
                [("outputnode.mean_bzero", "inputnode.in_file")],
            ),
            (
                inputnode,
                epireg_wf,
                [
                    ("t1w_head", "inputnode.t1w_head"),
                    ("t1w_brain", "inputnode.t1w_brain"),
                ],
            ),
        ]
    )
    return wf
