"""
Nodes' configurations for *epi_eg* pipelines.
"""
import nipype.pipeline.engine as pe
from dmriprep.workflows.dwi.post_sdc.epi_reg.configurations import (
    APPLY_XFM_MASK_KWARGS,
    CONVERTXFM_KWARGS,
    DWI_APPLY_XFM_KWARGS,
    EPIREG_KWARGS,
    INPUT_NODE_FIELDS,
    OUTPUT_NODE_FIELDS,
    RESAMPLE_MASK_KWARGS,
    TRANSFORM_AFF_KWARGS,
)
from nipype.interfaces import ants, fsl
from nipype.interfaces import mrtrix3 as mrt
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


def init_fsl_to_mrtrix_xfm_node(
    name="fsl_to_mrtrix_xfm", kwargs: dict = TRANSFORM_AFF_KWARGS
) -> pe.Node:
    """
    Initialize the *fsl_to_mrtrix_xfm* node for the *epi_reg* workflow.

    Parameters
    ----------
    name : str, optional
        Name of the node, by default "fsl_to_mrtrix_xfm"
    kwargs : dict, optional
        Keyword arguments for the node, by default CONVERTXFM_KWARGS

    Returns
    -------
    pe.Node
        *fsl_to_mrtrix_xfm* node.
    """
    return pe.Node(mrt.TransformFSLConvert(**kwargs), name=name)


def init_apply_xfm_node(
    name="apply_xfm", kwargs: dict = DWI_APPLY_XFM_KWARGS
) -> pe.Node:
    """
    Initialize the *apply_xfm* node for the *epi_reg* workflow.

    Parameters
    ----------
    name : str, optional
        Name of the node, by default "apply_xfm"
    kwargs : dict, optional
        Keyword arguments for the node, by default DWI_APPLY_XFM_KWARGS

    Returns
    -------
    pe.Node
        *apply_xfm* node.
    """
    return pe.Node(mrt.MRTransform(**kwargs), name=name)


def init_resample_mask_node(
    name="resample_mask", kwargs: dict = RESAMPLE_MASK_KWARGS
) -> pe.Node:
    """
    Initialize the *resample_mask* node for the *epi_reg* workflow.

    Parameters
    ----------
    name : str, optional
        Name of the node, by default "resample_mask"
    kwargs : dict, optional
        Keyword arguments for the node, by default RESAMPLE_MASK_KWARGS

    Returns
    -------
    pe.Node
        *resample_mask* node.
    """
    return pe.Node(ants.ApplyTransforms(**kwargs), name=name)


def init_apply_xfm_mask_node(
    name="apply_xfm_mask", kwargs: dict = APPLY_XFM_MASK_KWARGS
) -> pe.Node:
    """
    Initialize the *apply_xfm_mask* node for the *epi_reg* workflow.

    Parameters
    ----------
    name : str, optional
        Name of the node, by default "apply_xfm_mask"
    kwargs : dict, optional
        Keyword arguments for the node, by default DWI_APPLY_XFM_KWARGS

    Returns
    -------
    pe.Node
        *apply_xfm_mask* node.
    """
    return pe.Node(fsl.ApplyXFM(**kwargs), name=name)
