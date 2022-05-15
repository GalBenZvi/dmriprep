from dmriprep.workflows.dwi.utils.outputs.derivatives.configurations import (
    COREG_DWI_KWARGS,
    COREG_DWI_MASK_KWARGS,
    COREG_DWIREF_KWARGS,
    EPI_TO_T1_AFF_KWARGS,
    NATIVE_DWI_KWARGS,
    NATIVE_DWI_MASK_KWARGS,
    NATIVE_DWIREF_KWARGS,
    T1_to_EPI_AFF_KWARGS,
)
from dmriprep.workflows.dwi.utils.outputs.derivatives.edges import (
    COREG_DWI_LIST_TO_DDS_EDGES,
    COREG_DWIREF_LIST_TO_DDS_EDGES,
    INPUT_TO_COREG_DWI_DDS_EDGES,
    INPUT_TO_COREG_DWI_LIST_EDGES,
    INPUT_TO_COREG_DWI_MASK_EDGES,
    INPUT_TO_COREG_DWIREF_DDS_EDGES,
    INPUT_TO_COREG_DWIREF_LIST_EDGES,
    INPUT_TO_EPI_TO_T1_EDGES,
    INPUT_TO_NATIVE_DWI_DDS_EDGES,
    INPUT_TO_NATIVE_DWI_LIST_EDGES,
    INPUT_TO_NATIVE_DWI_MASK_EDGES,
    INPUT_TO_NATIVE_DWIREF_DDS_EDGES,
    INPUT_TO_NATIVE_DWIREF_LIST_EDGES,
    INPUT_TO_T1_TO_EPI_EDGES,
    NATIVE_DWI_LIST_TO_DDS_EDGES,
    NATIVE_DWIREF_LIST_TO_DDS_EDGES,
)
from dmriprep.workflows.dwi.utils.outputs.derivatives.nodes import (
    init_dwi_dds_node,
    init_dwi_list_node,
    init_dwiref_dds_node,
    init_dwiref_list_node,
    init_inputnode,
)
from niworkflows.engine.workflows import LiterateWorkflow as Workflow


def init_derivatives_wf(name="dmri_derivatives_wf") -> Workflow:
    """
    Initiates a workflow comprised of a battery of DerivativesDataSinks to store output files in their correct locations.

    Parameters
    ----------
    name : str, optional
        Workflow's name, by default "dmri_derivatives_wf"

    Returns
    -------
    pe.Workflow
        An initiated workflow for storing output files in their correct locations.
    """
    wf = Workflow(name=name)
    inputnode = init_inputnode()
    native_dwi_list_node = init_dwi_list_node("list_native_dwi_inputs")
    native_dwi_dds_node = init_dwi_dds_node("ds_native_dwi", NATIVE_DWI_KWARGS)
    coreg_dwi_list_node = init_dwi_list_node("list_coreg_dwi_inputs")
    coreg_dwi_dds_node = init_dwi_dds_node("ds_coreg_dwi", COREG_DWI_KWARGS)
    native_dwiref_list_node = init_dwiref_list_node(
        "list_native_dwiref_inputs"
    )
    native_dwiref_dds_node = init_dwiref_dds_node(
        "ds_native_dwiref", NATIVE_DWIREF_KWARGS
    )
    coreg_dwiref_list_node = init_dwiref_list_node("list_coreg_dwiref_inputs")
    coreg_dwiref_dds_node = init_dwiref_dds_node(
        "ds_coreg_dwiref", COREG_DWIREF_KWARGS
    )
    epi_to_t1_node = init_dwiref_dds_node(
        "ds_epi_to_t1_aff", EPI_TO_T1_AFF_KWARGS
    )
    t1_to_epi_node = init_dwiref_dds_node(
        "ds_t1_to_epi_aff", T1_to_EPI_AFF_KWARGS
    )
    native_dwi_mask_node = init_dwiref_dds_node(
        "ds_native_dwi_mask", NATIVE_DWI_MASK_KWARGS
    )
    coreg_dwi_mask_node = init_dwiref_dds_node(
        "ds_coreg_dwi_mask", COREG_DWI_MASK_KWARGS
    )
    wf.connect(
        [
            # Native DWI
            (
                inputnode,
                native_dwi_list_node,
                [
                    ("native_dwi_file", "in1"),
                    ("native_dwi_json", "in2"),
                    ("native_dwi_bvec", "in3"),
                    ("native_dwi_bval", "in4"),
                    ("native_dwi_grad", "in5"),
                ],
            ),
            (
                inputnode,
                native_dwi_dds_node,
                [
                    ("source_file", "source_file"),
                    ("base_directory", "base_directory"),
                ],
            ),
            (
                native_dwi_list_node,
                native_dwi_dds_node,
                [("out", "in_file")],
            ),
            # Coreg DWI
            (
                inputnode,
                coreg_dwi_list_node,
                [
                    ("coreg_dwi_file", "in1"),
                    ("coreg_dwi_json", "in2"),
                    ("coreg_dwi_bvec", "in3"),
                    ("coreg_dwi_bval", "in4"),
                ],
            ),
            (
                inputnode,
                coreg_dwi_dds_node,
                [
                    ("source_file", "source_file"),
                    ("base_directory", "base_directory"),
                ],
            ),
            (
                coreg_dwi_list_node,
                coreg_dwi_dds_node,
                [("out", "in_file")],
            ),
            # Native DWI Reference
            (
                inputnode,
                native_dwiref_list_node,
                [
                    ("native_dwiref_file", "in1"),
                    ("native_dwiref_json", "in2"),
                ],
            ),
            (
                inputnode,
                native_dwiref_dds_node,
                [
                    ("source_file", "source_file"),
                    ("base_directory", "base_directory"),
                ],
            ),
            (
                native_dwiref_list_node,
                native_dwiref_dds_node,
                [("out", "in_file")],
            ),
            # Coreg DWI Reference
            (
                inputnode,
                coreg_dwiref_list_node,
                [
                    ("coreg_dwiref_file", "in1"),
                    ("coreg_dwiref_json", "in2"),
                ],
            ),
            (
                inputnode,
                coreg_dwiref_dds_node,
                [
                    ("source_file", "source_file"),
                    ("base_directory", "base_directory"),
                ],
            ),
            (
                coreg_dwiref_list_node,
                coreg_dwiref_dds_node,
                [("out", "in_file")],
            ),
            # Transformations
            (
                inputnode,
                epi_to_t1_node,
                [
                    ("epi_to_t1w_aff", "in_file"),
                    ("source_file", "source_file"),
                    ("base_directory", "base_directory"),
                ],
            ),
            (
                inputnode,
                t1_to_epi_node,
                [
                    ("t1w_to_epi_aff", "in_file"),
                    ("source_file", "source_file"),
                    ("base_directory", "base_directory"),
                ],
            ),
            # Masks
            (
                inputnode,
                native_dwi_mask_node,
                [
                    ("native_dwi_mask", "in_file"),
                    ("source_file", "source_file"),
                    ("base_directory", "base_directory"),
                ],
            ),
            (
                inputnode,
                coreg_dwi_mask_node,
                [
                    ("coreg_dwi_mask", "in_file"),
                    ("source_file", "source_file"),
                    ("base_directory", "base_directory"),
                ],
            ),
        ]
    )
    return wf
