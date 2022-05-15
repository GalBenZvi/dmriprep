import nipype.pipeline.engine as pe
from dmriprep.config import config
from dmriprep.workflows.dwi.conversions.mif_to_nii.nodes import (
    init_conversion_node,
)
from dmriprep.workflows.dwi.post_sdc.bias_correction import (
    init_bias_correction_node,
)
from dmriprep.workflows.dwi.post_sdc.epi_reg.epi_reg import init_epireg_wf
from dmriprep.workflows.dwi.post_sdc.nodes import (
    init_inputnode,
    init_outputnode,
)
from dmriprep.workflows.dwi.utils.extract_bzero.extract_bzero import (
    init_extract_bzero_wf,
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

    # from dmriprep.workflows.dwi.utils.extract_bzero.nodes import (
    #     init_extract_node,
    #     init_mean_b0_node,
    # )

    wf = pe.Workflow(name=name)
    inputnode = init_inputnode()
    outputnode = init_outputnode()
    biascorrect = init_bias_correction_node()
    nii_conversion = init_conversion_node(is_dwi=True)
    extract_bzero = init_extract_bzero_wf()
    epireg_wf = init_epireg_wf()
    # extract_bzero = init_extract_node()
    # mean_bzero = init_mean_b0_node()
    if "biascorrect" not in config.workflow.ignore:
        wf.connect(
            [
                (inputnode, biascorrect, [("dwi_file", "in_file")]),
                (biascorrect, nii_conversion, [("out_file", "in_file")]),
                (
                    biascorrect,
                    extract_bzero,
                    [("out_file", "extract_b0.in_file")],
                ),
                (biascorrect, outputnode, [("out_file", "dwi_mif")]),
            ]
        )
    else:
        wf.connect(
            [
                (inputnode, nii_conversion, [("dwi_file", "in_file")]),
                (
                    inputnode,
                    extract_bzero,
                    [("dwi_file", "extract_b0.in_file")],
                ),
                (inputnode, outputnode, [("dwi_file", "dwi_mif")]),
            ]
        )
    wf.connect(
        [
            (
                extract_bzero,
                outputnode,
                [
                    ("outputnode.mean_bzero", "mean_bzero"),
                    ("outputnode.bzero", "bzero"),
                    ("outputnode.bzero_json", "bzero_json"),
                ],
            ),
            (
                nii_conversion,
                outputnode,
                [
                    ("out_file", "dwi_nii"),
                    ("out_bvec", "dwi_bvec"),
                    ("out_bval", "dwi_bval"),
                    ("json_export", "dwi_json"),
                    ("out_grad_mrtrix", "dwi_grad"),
                ],
            ),
        ]
    )
    return wf
