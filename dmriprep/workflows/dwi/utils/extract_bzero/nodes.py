import nipype.pipeline.engine as pe
from dmriprep.workflows.dwi.utils.extract_bzero.configurations import (
    EXTRACT_KWARGS,
    INPUT_NODE_FIELDS,
    MEAN_B0_KWARGS,
    OUTPUT_NODE_FIELDS,
)
from nipype.interfaces import mrtrix3 as mrt
from nipype.interfaces import utility as niu


def init_inputnode(
    name="inputnode", fields: list = INPUT_NODE_FIELDS
) -> pe.Node:
    """
    Define the inputnode for the extract_bzero workflow.

    Parameters
    ----------
    name : str, optional
        Name of the inputnode. Defaults to "inputnode".
    fields : list, optional
        Fields to be passed to the inputnode. Defaults to INPUT_NODE_FIELDS.

    Returns
    -------
    inputnode : nipype.pipeline.engine.Node
        Inputnode for the extract_bzero workflow.
    """
    return pe.Node(niu.IdentityInterface(fields=fields), name=name)


def init_outputnode(
    name="outputnode", fields: list = OUTPUT_NODE_FIELDS
) -> pe.Node:
    """
    Define the outputnode for the extract_bzero workflow.

    Parameters
    ----------
    name : str, optional
        Name of the outputnode. Defaults to "outputnode".
    fields : list, optional
        Fields to be passed to the outputnode. Defaults to OUTPUT_NODE_FIELDS.

    Returns
    -------
    outputnode : nipype.pipeline.engine.Node
        Outputnode for the extract_bzero workflow.
    """
    return pe.Node(niu.IdentityInterface(fields=fields), name=name)


def init_extract_node(
    name="extract_b0", kwargs: dict = EXTRACT_KWARGS
) -> pe.Node:
    """
    Define the extract_bzero node for the extract_bzero workflow.

    Parameters
    ----------
    name : str, optional
        Name of the extract_bzero node. Defaults to "extract_b0".
    kwargs : dict, optional
        Keyword arguments to be passed to the extract_bzero node. Defaults to EXTRACT_KWARGS.

    Returns
    -------
    extract_b0 : nipype.pipeline.engine.Node
        Extract_bzero node for the extract_bzero workflow.
    """
    return pe.Node(mrt.DWIExtract(**kwargs), name=name)


def init_mean_b0_node(
    name="mean_b0", kwargs: dict = MEAN_B0_KWARGS
) -> pe.Node:
    """
    Define the mean_bzero node for the extract_bzero workflow.

    Parameters
    ----------
    name : str, optional
        Name of the mean_bzero node. Defaults to "mean_b0".
    kwargs : dict, optional
        Keyword arguments to be passed to the mean_bzero node. Defaults to MEAN_B0_KWARGS.

    Returns
    -------
    mean_b0 : nipype.pipeline.engine.Node
        Mean_bzero node for the extract_bzero workflow.
    """
    return pe.Node(mrt.MRMath(**kwargs), name=name)
