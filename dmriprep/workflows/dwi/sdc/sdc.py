from dmriprep.workflows.dwi.sdc.configurations import SDC_NO_DWI_KWARGS
from dmriprep.workflows.dwi.sdc.edges import (
    MERGE_TO_MRCAT_EDGES,
    MRCAT_TO_SDC_EDGES,
    SDC_TO_OUTPUT_EDGES,
)
from dmriprep.workflows.dwi.sdc.nodes import (
    init_inputnode,
    init_merge_node,
    init_mrcat_node,
    init_outputnode,
    init_sdc_node,
)
from dmriprep.workflows.dwi.utils.extract_bzero.extract_bzero import (
    init_extract_bzero_wf,
)
from dmriprep.workflows.dwi.utils.outputs.reports.nodes import (
    init_eddy_report_node,
)
from niworkflows.engine.workflows import LiterateWorkflow as Workflow


def init_sdc_wf(is_seepi: bool, name="sdc_wf") -> Workflow:
    """
    Workflow for Susceptibility Distortion Correction.

    Parameters
    ----------
    name : str, optional
        Name of workflow. Defaults to "sdc_wf".

    Returns
    -------
    Workflow
        Workflow for Susceptibility Distortion Correction.
    """
    #: i/o
    (inputnode, outputnode, merge_node, mrcat_node, sdc_node,) = (
        init_inputnode(),
        init_outputnode(),
        init_merge_node(),
        init_mrcat_node(),
        init_sdc_node(kwargs=SDC_NO_DWI_KWARGS),
    )
    eddy_report = init_eddy_report_node()
    fmap_b0_wf = init_extract_bzero_wf(name="fmap_b0_sdc")
    extract_bzero_after_wf = init_extract_bzero_wf(name="b0_after_sdc")
    wf = Workflow(name=name)
    if is_seepi:
        wf.connect(
            [
                (
                    inputnode,
                    merge_node,
                    [("dwi_bzero", "in1")],
                ),
                (fmap_b0_wf, merge_node, [("outputnode.bzero", "in2")]),
            ]
        )
    else:
        wf.connect(
            [
                (
                    inputnode,
                    merge_node,
                    [("mean_bzero", "in1")],
                ),
                (fmap_b0_wf, merge_node, [("outputnode.mean_bzero", "in2")]),
            ]
        )
    wf.connect(
        [
            (inputnode, fmap_b0_wf, [("fmap_file", "extract_b0.in_file")]),
            (merge_node, mrcat_node, MERGE_TO_MRCAT_EDGES),
            (mrcat_node, sdc_node, MRCAT_TO_SDC_EDGES),
            (
                inputnode,
                sdc_node,
                [("dwi_file", "in_file"), ("dwi_pe_dir", "pe_dir")],
            ),
            (sdc_node, outputnode, SDC_TO_OUTPUT_EDGES),
            (
                sdc_node,
                extract_bzero_after_wf,
                [("out_file", "extract_b0.in_file")],
            ),
            (inputnode, eddy_report, [("mean_bzero", "before")]),
            (
                extract_bzero_after_wf,
                eddy_report,
                [("outputnode.mean_bzero", "after")],
            ),
        ]
    )
    return wf
