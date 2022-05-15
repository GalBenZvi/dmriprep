from dmriprep.workflows.dwi.utils.outputs.reports.configurations import (
    COREG_REPORT_KWARGS,
    DENOISE_REPORT_KWARGS,
    INPUT_NODE_FIELDS,
)
from nipype.interfaces import utility as niu
from nipype.pipeline import engine as pe
from niworkflows.interfaces.reportlets.masks import ROIsPlot, SimpleShowMaskRPT
from niworkflows.interfaces.reportlets.registration import (
    SimpleBeforeAfterRPT as SimpleBeforeAfter,
)


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


def init_eddy_report_node(name="eddy_report") -> pe.Node:
    """
    Initialize SDC node for Susceptibility Distortion Correction.

    Parameters
    ----------
    name : str, optional
        Name of node. Defaults to "sdc".
    kwargs : dict, optional
        Keyword arguments for SDC. Defaults to SDC_KWARGS.

    Returns
    -------
    Node
        SDC node for Susceptibility Distortion Correction.
    """
    return pe.Node(
        SimpleBeforeAfter(
            before_label="Distorted",
            after_label="Eddy Corrected",
        ),
        name=name,
        mem_gb=0.1,
    )


def init_coreg_report(
    name: str = "coreg_report", kwargs: dict = COREG_REPORT_KWARGS
) -> pe.Node:
    """
    Initialize the coreg report node.

    Parameters
    ----------
    name : str, optional
        Name of node. Defaults to "coreg_report".
    kwargs : dict, optional
        Keyword arguments for coreg report. Defaults to COREG_REPORT_KWARGS.
    """
    return pe.Node(SimpleBeforeAfter(**kwargs), name=name)


def init_denoise_report(
    name: str = "denoise_report", kwargs: dict = DENOISE_REPORT_KWARGS
) -> pe.Node:
    """
    Initialize the denoise report node.

    Parameters
    ----------
    name : str, optional
        Name of node. Defaults to "denoise_report".
    kwargs : dict, optional
        Keyword arguments for denoise report. Defaults to DENOISE_REPORT_KWARGS.

    Returns
    -------
    Node
        Denoise report node.
    """
    return pe.Node(ROIsPlot(**kwargs), name=name)


def init_mask_reportlet(name: str = "mask_reportlet") -> pe.Node:
    """
    Initialize the mask reportlet node.

    Parameters
    ----------
    name : str, optional
        Name of node. Defaults to "mask_reportlet".
    """
    return pe.Node(SimpleShowMaskRPT(), name=name)
