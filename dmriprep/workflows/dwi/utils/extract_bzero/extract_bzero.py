import nipype.pipeline.engine as pe
from dmriprep.workflows.dwi.utils.extract_bzero.edges import (
    EXTRACT_TO_MEAN_EDGES,
    EXTRACT_TO_OUTPUT_EDGES,
    INPUT_TO_EXTRACT_EDGES,
    MEAN_TO_OUTPUT_EDGES,
)
from dmriprep.workflows.dwi.utils.extract_bzero.nodes import (
    init_extract_node,
    init_inputnode,
    init_mean_b0_node,
    init_outputnode,
)


def init_extract_bzero_wf(name: str = "extract_bzero") -> pe.Workflow:
    """
    Initialize the extract_bzero workflow.

    Parameters
    ----------
    name : str, optional
        Name of the workflow. Defaults to "extract_bzero".

    Returns
    -------
    wf : nipype.pipeline.engine.Workflow
        Extract_bzero workflow.
    """
    wf = pe.Workflow(name=name)
    inputnode, outputnode, extract_bzero, mean_bzero = [
        func()
        for func in [
            init_inputnode,
            init_outputnode,
            init_extract_node,
            init_mean_b0_node,
        ]
    ]
    wf.connect(
        [
            (inputnode, extract_bzero, INPUT_TO_EXTRACT_EDGES),
            (extract_bzero, mean_bzero, EXTRACT_TO_MEAN_EDGES),
            (extract_bzero, outputnode, EXTRACT_TO_OUTPUT_EDGES),
            (mean_bzero, outputnode, MEAN_TO_OUTPUT_EDGES),
        ]
    )
    return wf
