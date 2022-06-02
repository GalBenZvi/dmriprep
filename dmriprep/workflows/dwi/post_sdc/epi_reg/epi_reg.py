from dmriprep.workflows.dwi.conversions.mif_to_nii.nodes import (
    init_conversion_node,
)
from dmriprep.workflows.dwi.post_sdc.epi_reg.edges import (
    CONVERTXFM_TO_OUTPUT_EDGES,
    EPIREG_TO_CONVERTXFM_EDGES,
    EPIREG_TO_OUTPUT_EDGES,
    INPUT_TO_EPIREG_EDGES,
)
from dmriprep.workflows.dwi.post_sdc.epi_reg.nodes import (
    init_apply_xfm_mask_node,
    init_apply_xfm_node,
    init_fsl_to_mrtrix_xfm_node,
    init_resample_mask_node,
)
from niworkflows.engine.workflows import LiterateWorkflow as Workflow

# EPI_REG = [
#     (INPUT_NODE, EPIREG_NODE, INPUT_TO_EPIREG_EDGES),
#     (EPIREG_NODE, CONVERTXFM_NODE, EPIREG_TO_CONVERTXFM_EDGES),
#     (EPIREG_NODE, OUTPUT_NODE, EPIREG_TO_OUTPUT_EDGES),
#     (CONVERTXFM_NODE, OUTPUT_NODE, CONVERTXFM_TO_OUTPUT_EDGES),
# ]


def init_epireg_wf(
    name="epi_reg_wf",
) -> Workflow:
    """
    Initiates a FSL's epi_reg-based workflow to coregister EPI images to structural ones.

    Parameters
    ----------
    name : str, optional
        Workflow's name, by default "epi_reg_wf"

    Returns
    -------
    pe.Workflow
        An initiated workflow for coregistering EPI images to structural ones.
    """
    from dmriprep.workflows.dwi.post_sdc.epi_reg.nodes import (
        init_epireg_node,
        init_inputnode,
        init_invert_xfm_node,
        init_outputnode,
    )

    wf = Workflow(name=name)

    (
        inputnode,
        outputnode,
        epireg_node,
        invert_xfm_node,
        convert_xfm_node,
        apply_xfm_dwi_node,
        resample_mask_node,
        apply_xfm_mask_node,
    ) = (
        init_inputnode(),
        init_outputnode(),
        init_epireg_node(),
        init_invert_xfm_node(),
        init_fsl_to_mrtrix_xfm_node(),
        init_apply_xfm_node(),
        init_resample_mask_node(),
        init_apply_xfm_mask_node(),
    )
    nii_conversion_node = init_conversion_node(is_dwi=True)

    wf.connect(
        [
            (
                inputnode,
                epireg_node,
                [
                    ("t1w_brain", "t1_brain"),
                    ("t1w_head", "t1_head"),
                    ("dwi_reference", "epi"),
                ],
            ),
            (epireg_node, invert_xfm_node, [("epi2str_mat", "in_file")]),
            (invert_xfm_node, outputnode, [("out_file", "t1w_to_epi_aff")]),
            (
                epireg_node,
                outputnode,
                [
                    ("epi2str_mat", "epi_to_t1w_aff"),
                    ("out_file", "dwi_ref_to_t1w"),
                ],
            ),
            (
                inputnode,
                convert_xfm_node,
                [("t1w_brain", "reference"), ("dwi_reference", "in_file")],
            ),
            (
                epireg_node,
                convert_xfm_node,
                [("epi2str_mat", "in_transform")],
            ),
            (
                invert_xfm_node,
                apply_xfm_mask_node,
                [("out_file", "in_matrix_file")],
            ),
            (
                convert_xfm_node,
                apply_xfm_dwi_node,
                [("out_transform", "linear_transform")],
            ),
            (
                inputnode,
                apply_xfm_dwi_node,
                [("dwi_file", "in_files")],
                # [("dwi_file", "in_files"), ("t1w_brain", "template_image")],
            ),
            (apply_xfm_dwi_node, outputnode, [("out_file", "coreg_dwi")]),
            (
                apply_xfm_dwi_node,
                nii_conversion_node,
                [("out_file", "in_file")],
            ),
            (
                inputnode,
                resample_mask_node,
                [
                    ("t1w_mask", "source"),
                ],
            ),
            (
                nii_conversion_node,
                resample_mask_node,
                [("out_file", "target")],
            ),
            (
                resample_mask_node,
                outputnode,
                [("out_file", "coreg_dwi_mask")],
            ),
            (
                inputnode,
                apply_xfm_mask_node,
                [("t1w_mask", "in_file"), ("dwi_reference", "reference")],
            ),
            (
                apply_xfm_mask_node,
                outputnode,
                [("out_file", "native_dwi_mask")],
            ),
        ]
    )
    return wf