import nipype.pipeline.engine as pe
from dmriprep.workflows.dwi.utils.extract_bzero.edges import (
    CONVERSION_TO_OUTPUT_EDGES,
    EXTRACT_TO_MEAN_EDGES,
    EXTRACT_TO_OUTPUT_EDGES,
    MEAN_TO_CONVERSION_EDGES,
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
    from dmriprep.workflows.dwi.conversions.mif_to_nii.nodes import (
        init_conversion_node,
    )
    from dmriprep.workflows.dwi.utils.extract_bzero.nodes import (
        init_extract_node,
        init_mean_b0_node,
        init_outputnode,
    )

    wf = pe.Workflow(name=name)
    outputnode = init_outputnode()
    extract_bzero = init_extract_node()
    mean_bzero = init_mean_b0_node()
    conversion = init_conversion_node(is_dwi=False)
    wf.connect(
        [
            (extract_bzero, mean_bzero, EXTRACT_TO_MEAN_EDGES),
            (extract_bzero, outputnode, EXTRACT_TO_OUTPUT_EDGES),
            (mean_bzero, conversion, MEAN_TO_CONVERSION_EDGES),
            (conversion, outputnode, CONVERSION_TO_OUTPUT_EDGES),
        ]
    )
    return wf
