from dmriprep.workflows.dwi.post_sdc.epi_reg.edges import (
    CONVERTXFM_TO_OUTPUT_EDGES,
    EPIREG_TO_CONVERTXFM_EDGES,
    EPIREG_TO_OUTPUT_EDGES,
    INPUT_TO_EPIREG_EDGES,
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

    inputnode, epireg_node, convertxfm_node, outputnode = (
        init_inputnode(),
        init_epireg_node(),
        init_invert_xfm_node(),
        init_outputnode(),
    )

    wf.connect(
        [
            (inputnode, epireg_node, INPUT_TO_EPIREG_EDGES),
            (epireg_node, convertxfm_node, EPIREG_TO_CONVERTXFM_EDGES),
            (convertxfm_node, outputnode, CONVERTXFM_TO_OUTPUT_EDGES),
            (epireg_node, outputnode, EPIREG_TO_OUTPUT_EDGES),
        ]
    )
    return wf
