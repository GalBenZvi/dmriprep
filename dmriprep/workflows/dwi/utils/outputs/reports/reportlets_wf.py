from dmriprep.workflows.dwi.utils.outputs.reports.nodes import (
    init_eddy_report_node,
    init_inputnode,
)
from niworkflows.engine.workflows import LiterateWorkflow as Workflow


def init_reportlets_wf(name="reportlets_wf") -> Workflow:
    """
    Workflow for generating reportlets.

    Parameters
    ----------
    name : str, optional
        Name of workflow. Defaults to "reportlets_wf".

    Returns
    -------
    Workflow
        Workflow for generating reportlets.
    """
    wf = Workflow(name=name)
    inputnode, eddy_report = init_inputnode(), init_eddy_report_node()
    
