import nipype.pipeline.engine as pe

# from dwiprep.interfaces.dds import DerivativesDataSink
from dmriprep.interfaces import DerivativesDataSink
from dmriprep.workflows.dwi.utils.outputs.derivatives.configurations import (
    INPUT_NODE_FIELDS,
)
from nipype.interfaces import utility as niu


def init_inputnode(name: str = "inputnode", fields: list = INPUT_NODE_FIELDS):
    """
    Initialize input node for the reportlets workflow.

    Parameters
    ----------
    name : str, optional
        Name of workflow. Defaults to "inputnode".
    fields : list, optional
        List of fields to include in the input node. Defaults to
        INPUT_NODE_FIELDS.
    """
    return pe.Node(niu.IdentityInterface(fields=fields), name=name)


def init_dwi_list_node(name: str) -> pe.Node:
    """
    Initialize the list node for the native DWI inputs.

    Parameters
    ----------
    name : str, optional
        Name of node.

    Returns
    -------
    Node
        List node for the native DWI inputs.
    """
    return pe.Node(niu.Merge(numinputs=5), name=name)


def init_dwi_dds_node(name: str, kwargs: dict) -> pe.MapNode:
    """
    Initialize the native DWI DDS node.

    Parameters
    ----------
    name : str, optional
        Name of node.
    kwargs : dict, optional
        Keyword arguments for DDS.

    Returns
    -------
    Node
        Native DWI DDS node.
    """
    return pe.MapNode(
        DerivativesDataSink(**kwargs), iterfield=["in_file"], name=name
    )


def init_dwiref_list_node(name: str) -> pe.Node:
    """
    Initialize the list node for the native DWI reference inputs.

    Parameters
    ----------
    name : str, optional
        Name of node.

    Returns
    -------
    Node
        List node for the native DWI inputs.
    """
    return pe.Node(niu.Merge(numinputs=2), name=name)


def init_dwiref_dds_node(name: str, kwargs: dict) -> pe.Node:
    """
    Initialize a general DDS node.

    Parameters
    ----------
    name : str
        Name of node.
    kwargs : dict
        Keyword arguments for DDS.

    Returns
    -------
    Node
        General DDS node.
    """
    return pe.Node(DerivativesDataSink(**kwargs), name=name)
