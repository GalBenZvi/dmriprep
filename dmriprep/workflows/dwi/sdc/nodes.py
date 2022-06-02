import nipype.pipeline.engine as pe
from dmriprep.workflows.dwi.sdc.configurations import (
    INPUT_NODE_FIELDS,
    MRCAT_KWARGS,
    OUTPUT_NODE_FIELDS,
    SDC_KWARGS,
)
from nipype.interfaces import mrtrix3 as mrt
from nipype.interfaces import utility as niu


#: i/o
def init_inputnode(name="inputnode", fields=INPUT_NODE_FIELDS) -> pe.Node:
    """
    Initialize input node for Susceptibility Distortion Correction.

    Parameters
    ----------
    name : str, optional
        Name of node. Defaults to "inputnode".
    fields : list, optional
        Fields of node. Defaults to INPUT_NODE_FIELDS.

    Returns
    -------
    Node
        Input node for Susceptibility Distortion Correction.
    """
    return pe.Node(niu.IdentityInterface(fields=fields), name=name)


def init_outputnode(name="outputnode", fields=OUTPUT_NODE_FIELDS) -> pe.Node:
    """
    Initialize output node for Susceptibility Distortion Correction.

    Parameters
    ----------
    name : str, optional
        Name of node. Defaults to "outputnode".
    fields : list, optional
        Fields of node. Defaults to OUTPUT_NODE_FIELDS.

    Returns
    -------
    Node
        Output node for Susceptibility Distortion Correction.
    """
    return pe.Node(niu.IdentityInterface(fields=fields), name=name)


def init_merge_node(name="merge_dwi_series") -> pe.Node:
    """
    Initialize merge node for Susceptibility Distortion Correction.

    Parameters
    ----------
    name : str, optional
        Name of node. Defaults to "merge_dwi_series".

    Returns
    -------
    Node
        Merge node for Susceptibility Distortion Correction.
    """
    return pe.Node(niu.Merge(2), name=name)


def init_mrcat_node(name="concat_dwi_series", kwargs=MRCAT_KWARGS) -> pe.Node:
    """
    Initialize MRCat node for Susceptibility Distortion Correction.

    Parameters
    ----------
    name : str, optional
        Name of node. Defaults to "concat_dwi_series".
    kwargs : dict, optional
        Keyword arguments for MRCat. Defaults to MRCAT_KWARGS.

    Returns
    -------
    Node
        MRCat node for Susceptibility Distortion Correction.
    """
    return pe.Node(mrt.MRCat(**kwargs), name=name)


def init_sdc_node(name="sdc", kwargs=SDC_KWARGS) -> pe.Node:
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
    return pe.Node(mrt.DWIPreproc(**kwargs), name=name)


# ds_report_eddy = pe.Node(
#     DerivativesDataSink(
#         base_directory=str(config.execution.output_dir),
#         desc="eddy",
#         datatype="figures",
#     ),
#     name="ds_report_eddy",
#     run_without_submitting=True,
# )

# eddy_report = pe.Node(
#     SimpleBeforeAfter(
#         before_label="Distorted",
#         after_label="Eddy Corrected",
#     ),
#     name="eddy_report",
#     mem_gb=0.1,
# )
