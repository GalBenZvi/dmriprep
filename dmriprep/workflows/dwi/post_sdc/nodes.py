import nipype.pipeline.engine as pe
from dmriprep.workflows.dwi.post_sdc.configurations import (
    INPUT_NODE_FIELDS,
    OUTPUT_NODE_FIELDS,
)
from nipype.interfaces import utility as niu


def init_inputnode(
    name: str = "inputnode", fields: list = INPUT_NODE_FIELDS
) -> pe.Node:
    """
    Input node

    Parameters
    ----------
    name : str, optional

    Returns
    -------
    inputnode : nipype.pipeline.engine.Node
        Input node.
    """
    return pe.Node(niu.IdentityInterface(fields=fields), name=name)
