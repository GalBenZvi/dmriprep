import nipype.pipeline.engine as pe
from dmriprep.workflows.dwi.pre_sdc.configurations import (
    DEGIBBS_KWARGS,
    DENOISE_KWARGS,
    EXTRACT_KWARGS,
    INPUT_NODE_FIELDS,
    MEAN_B0_KWARGS,
    OUTPUT_NODE_FIELDS,
)
from nipype.interfaces import mrtrix3 as mrt
from nipype.interfaces import utility as niu


def init_inputnode(
    name: str = "inputnode", fields=INPUT_NODE_FIELDS
) -> pe.Node:
    """
    Initialize the input node for the pre_sdc workflow.

    Parameters
    ----------
    name : str, optional
        Name of node. Defaults to "inputnode".
    fields : list, optional
        Fields of node. Defaults to INPUT_NODE_FIELDS.

    Returns
    -------
    Node
        Input node for the pre_sdc workflow.
    """
    return pe.Node(niu.IdentityInterface(fields=fields), name=name)


def init_outputnode(
    name: str = "outputnode", fields=OUTPUT_NODE_FIELDS
) -> pe.Node:
    """
    Initialize the output node for the pre_sdc workflow.

    Parameters
    ----------
    name : str, optional
        Name of node. Defaults to "outputnode".
    fields : list, optional
        Fields of node. Defaults to OUTPUT_NODE_FIELDS.

    Returns
    -------
    Node
        Output node for the pre_sdc workflow.
    """
    return pe.Node(niu.IdentityInterface(fields=fields), name=name)


def init_denoise_node(
    name: str = "denoise",
    kwargs: dict = DENOISE_KWARGS,
) -> pe.Node:
    """
    Initialize the denoise node for the pre_sdc workflow.

    Parameters
    ----------
    name : str, optional
        Name of node. Defaults to "denoise".
    kwargs : dict, optional
        Keyword arguments for the denoise node. Defaults to DENOISE_KWARGS.

    Returns
    -------
    Node
        Denoise node for the pre_sdc workflow.
    """
    return pe.Node(mrt.DWIDenoise(**kwargs), name=name)


def init_degibbss_node(
    name: str = "degibbs",
    kwargs: dict = DEGIBBS_KWARGS,
) -> pe.Node:
    """
    Initialize the degibss node for the pre_sdc workflow.

    Parameters
    ----------
    name : str, optional
        Name of node. Defaults to "degibbs".
    kwargs : dict, optional
        Keyword arguments for the degibss node. Defaults to DEGIBBS_KWARGS.

    Returns
    -------
    Node
        Degibss node for the pre_sdc workflow.
    """
    return pe.Node(mrt.MRDeGibbs(**kwargs), name=name)
