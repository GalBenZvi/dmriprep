"""
Nodes' configurations for *epi_eg* pipelines.
"""
import nipype.pipeline.engine as pe
from dmriprep.workflows.dwi.post_sdc.epi_reg.configurations import (
    CONVERTXFM_KWARGS,
    EPIREG_KWARGS,
    INPUT_NODE_FIELDS,
    OUTPUT_NODE_FIELDS,
)
from nipype.interfaces import fsl
from nipype.interfaces import utility as niu


#: i/o
def init_inputnode(
    name: str = "inputnode", fields: list = INPUT_NODE_FIELDS
) -> pe.Node:
    """
    Initialize the input node for the *epi_reg* workflow.

    Parameters
    ----------
    name : str, optional
        Name of the node, by default "inputnode"
    fields : list, optional
        Fields of the node, by default INPUT_NODE_FIELDS

    Returns
    -------
    pe.Node
        Input node.
    """
    return pe.Node(niu.IdentityInterface(fields=fields), name=name)


def init_outputnode(
    name: str = "outputnode", fields: list = OUTPUT_NODE_FIELDS
) -> pe.Node:
    """
    Initialize the output node for the *epi_reg* workflow.

    Parameters
    ----------
    name : str, optional
        Name of the node, by default "outputnode"
    fields : list, optional
        Fields of the node, by default OUTPUT_NODE_FIELDS

    Returns
    -------
    pe.Node
        Output node.
    """
    return pe.Node(niu.IdentityInterface(fields=fields), name=name)


def init_epireg_node(name="epireg", kwargs: dict = EPIREG_KWARGS) -> pe.Node:
    """
    Initialize the *epi_reg* node for the *epi_reg* workflow.

    Parameters
    ----------
    name : str, optional
        Name of the node, by default "epireg"
    kwargs : dict, optional
        Keyword arguments for the node, by default EPIREG_KWARGS

    Returns
    -------
    pe.Node
        *epi_reg* node.
    """
    return pe.Node(fsl.EpiReg(**kwargs), name=name)


def init_invert_xfm_node(
    name="invert_xfm", kwargs: dict = CONVERTXFM_KWARGS
) -> pe.Node:
    """
    Initialize the *invert_xfm* node for the *epi_reg* workflow.

    Parameters
    ----------
    name : str, optional
        Name of the node, by default "invert_xfm"
    kwargs : dict, optional
        Keyword arguments for the node, by default CONVERTXFM_KWARGS

    Returns
    -------
    pe.Node
        *invert_xfm* node.
    """
    return pe.Node(fsl.ConvertXFM(**kwargs), name=name)
