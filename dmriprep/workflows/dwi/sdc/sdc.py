from dmriprep.workflows.dwi.sdc.edges import (
    INPUT_TO_MERGE_EDGES,
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


def init_sdc_wf(name="sdc_wf") -> Workflow:
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
        init_sdc_node(),
    )
    eddy_report = init_eddy_report_node()
    extract_bzero_wf = init_extract_bzero_wf()
    wf = Workflow(name=name)
    wf.connect(
        [
            (inputnode, merge_node, INPUT_TO_MERGE_EDGES),
            (merge_node, mrcat_node, MERGE_TO_MRCAT_EDGES),
            (mrcat_node, sdc_node, MRCAT_TO_SDC_EDGES),
            (sdc_node, outputnode, SDC_TO_OUTPUT_EDGES),
            (sdc_node, extract_bzero_wf, [("out_file", "extract_b0.in_file")]),
            (inputnode, eddy_report, [("mean_bzero", "before")]),
            (
                extract_bzero_wf,
                eddy_report,
                [("outputnode.mean_bzero", "after")],
            ),
        ]
    )
    return wf
