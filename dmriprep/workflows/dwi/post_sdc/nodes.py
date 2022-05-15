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


def init_outputnode(
    name: str = "outputnode", fields: list = OUTPUT_NODE_FIELDS
) -> pe.Node:
    """
    Output node

    Parameters
    ----------
    name : str, optional

    Returns
    -------
    outputnode : nipype.pipeline.engine.Node
        Output node.
    """
    return pe.Node(niu.IdentityInterface(fields=fields), name=name)
