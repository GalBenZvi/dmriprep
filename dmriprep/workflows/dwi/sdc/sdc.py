import nipype.pipeline.engine as pe
from dmriprep.workflows.dwi.sdc.configurations import (
    INPUT_NODE_FIELDS,
    MRCAT_KWARGS,
    OUTPUT_NODE_FIELDS,
    SDC_KWARGS,
    SDC_NO_DWI_KWARGS,
)
from dmriprep.workflows.dwi.sdc.edges import (  # INPUT_TO_SDC_EDGES,
    INPUT_TO_MERGE_EDGES,
    MERGE_TO_MRCAT_EDGES,
    MRCAT_TO_SDC_EDGES,
    SDC_TO_OUTPUT_EDGES,
)
from nipype.interfaces import mrtrix3 as mrt
from nipype.interfaces import utility as niu
from niworkflows.engine.workflows import LiterateWorkflow as Workflow


def init_sdc_wf(name="sdc_wf") -> Workflow:
    """
    Workflow for Susceptibility Distortion Correction.

    Parameters
    ----------
    name : str, optional
        Name of workflow. Defaults to "sdc_wf".

    Returns
    -------
    Workflow
        Workflow for Susceptibility Distortion Correction.
    """
    #: i/o
    INPUT_NODE = pe.Node(
        niu.IdentityInterface(fields=INPUT_NODE_FIELDS), name="inputnode"
    )
    OUTPUT_NODE = pe.Node(
        niu.IdentityInterface(fields=OUTPUT_NODE_FIELDS), name="outputnode"
    )
    MERGE_NODE = pe.Node(niu.Merge(2), name="merge_dwi_series")
    MRCAT_NODE = pe.Node(mrt.MRCat(**MRCAT_KWARGS), name="concat_dwi_series")
    wf = Workflow(name=name)
    # if fieldmap_is_dwi:
    #: Building blocks
    SDC_NODE = pe.Node(mrt.DWIPreproc(**SDC_KWARGS), name="sdc")
    SDC_WF = [
        (INPUT_NODE, MERGE_NODE, INPUT_TO_MERGE_EDGES),
        (MERGE_NODE, MRCAT_NODE, MERGE_TO_MRCAT_EDGES),
        (MRCAT_NODE, SDC_NODE, MRCAT_TO_SDC_EDGES),
        # (INPUT_NODE, SDC_NODE, INPUT_TO_SDC_EDGES),
    ]
    wf.connect(SDC_WF)
    # else:
    #     #: Building blocks
    #     SDC_NODE = pe.Node(mrt.DWIPreproc(**SDC_NO_DWI_KWARGS), name="sdc")
    #     wf.connect(
    #         [
    #             (
    #                 INPUT_NODE,
    #                 MERGE_NODE,
    #                 [("mean_bzero", "in1"), ("fmap_file", "in2")],
    #             ),
    #             (MERGE_NODE, MRCAT_NODE, [("out", "in_files")]),
    #             (MRCAT_NODE, SDC_NODE, [("out_file", "in_epi")]),
    #             (
    #                 INPUT_NODE,
    #                 SDC_NODE,
    #                 [("dwi_file", "in_file"), ("dwi_pe_dir", "pe_dir")],
    #             ),
    #         ]
    #     )

    wf.connect([(SDC_NODE, OUTPUT_NODE, SDC_TO_OUTPUT_EDGES)])
    return wf
