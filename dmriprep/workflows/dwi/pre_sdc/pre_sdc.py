import nipype.pipeline.engine as pe
from dmriprep.workflows.dwi.pre_sdc.configurations import (
    DEGIBBS_KWARGS,
    DENOISE_KWARGS,
    EXTRACT_KWARGS,
    INPUT_NODE_FIELDS,
    MEAN_B0_KWARGS,
    OUTPUT_NODE_FIELDS,
)
from dmriprep.workflows.dwi.utils.extract_bzero import init_extract_bzero_wf
from nipype.interfaces import mrtrix3 as mrt
from nipype.interfaces import utility as niu

# from dmriprep.workflows.dwi.pre_sdc.edges
from niworkflows.engine.workflows import LiterateWorkflow as Workflow


def init_pre_sdc_wf(ignore: list, name="pre_sdc_wf"):
    """
    Workflow to denoise and extract b0 from DWI.

    Parameters
    ----------
    ignore : list
        List of processes to ignore.
    name : str, optional
        Name of workflow. Defaults to "pre_sdc_wf".
    """
    from dmriprep.config import config

    #: i/o
    INPUT_NODE = pe.Node(
        niu.IdentityInterface(fields=INPUT_NODE_FIELDS), name="inputnode"
    )
    OUTPUT_NODE = pe.Node(
        niu.IdentityInterface(fields=OUTPUT_NODE_FIELDS), name="outputnode"
    )

    #: Building blocks
    DENOISE_NODE = pe.Node(mrt.DWIDenoise(**DENOISE_KWARGS), name="denoise")
    DEGIBBS_NODE = pe.Node(mrt.MRDeGibbs(**DEGIBBS_KWARGS), name="degibbs")
    EXTRACT_WF = init_extract_bzero_wf()
    # EXTRACT_NODE = pe.Node(mrt.DWIExtract(**EXTRACT_KWARGS), name="extract_b0")
    # MEAN_B0_NODE = pe.Node(mrt.MRMath(**MEAN_B0_KWARGS), name="mean_b0")
    wf = Workflow(name=name)
    if "denoise" not in config.workflow.ignore:
        wf.connect(
            [
                (INPUT_NODE, DENOISE_NODE, [("dwi_file", "in_file")]),
                (DENOISE_NODE, OUTPUT_NODE, [("out_file", "noise")]),
            ]
        )
        if "degibbs" not in config.workflow.ignore:
            wf.connect(
                [
                    (DENOISE_NODE, DEGIBBS_NODE, [("out_file", "in_file")]),
                    (
                        DEGIBBS_NODE,
                        EXTRACT_WF,
                        [("out_file", "inputnode.in_file")],
                    ),
                    (DEGIBBS_NODE, OUTPUT_NODE, [("out_file", "dwi_pre_sdc")]),
                ]
            )
        else:
            wf.connect(
                [
                    (
                        DENOISE_NODE,
                        EXTRACT_WF,
                        [("out_file", "inputnode.in_file")],
                    ),
                    (DENOISE_NODE, OUTPUT_NODE, [("out_file", "dwi_pre_sdc")]),
                ]
            )
    else:
        if "degibbs" not in config.workflow.ignore:
            wf.connect(
                [
                    (INPUT_NODE, DEGIBBS_NODE, [("dwi_file", "in_file")]),
                    (
                        DEGIBBS_NODE,
                        EXTRACT_WF,
                        [("out_file", "inputnode.in_file")],
                    ),
                    (DEGIBBS_NODE, OUTPUT_NODE, [("out_file", "dwi_pre_sdc")]),
                ]
            )
        else:
            wf.connect(
                [
                    (
                        INPUT_NODE,
                        EXTRACT_WF,
                        [("dwi_file", "inputnode.in_file")],
                    ),
                    (INPUT_NODE, OUTPUT_NODE, [("dwi_file", "dwi_pre_sdc")]),
                ]
            )
    wf.connect(
        [
            (
                EXTRACT_WF,
                OUTPUT_NODE,
                [
                    ("outputnode.bzero", "bzero"),
                    ("outputnode.mean_bzero", "mean_bzero"),
                ],
            ),
        ]
    )
    return wf
