import nipype.pipeline.engine as pe
from dmriprep.workflows.dwi.pre_sdc.nodes import (
    init_degibbss_node,
    init_denoise_node,
    init_inputnode,
    init_outputnode,
)
from nipype.interfaces import mrtrix3 as mrt
from nipype.interfaces import utility as niu

# from dmriprep.workflows.dwi.pre_sdc.edges
from niworkflows.engine.workflows import LiterateWorkflow as Workflow


def init_pre_sdc_wf(name="pre_sdc_wf"):
    """
    Workflow to denoise and extract b0 from DWI.

    Parameters
    ----------
    name : str, optional
        Name of workflow. Defaults to "pre_sdc_wf".
    """
    from dmriprep.config import config
    from dmriprep.workflows.dwi.utils.extract_bzero import (
        init_extract_bzero_wf,
    )

    #: i/o
    inputnode, outputnode, denoise_node, degibbs_node = (
        init_inputnode(),
        init_outputnode(),
        init_denoise_node(),
        init_degibbss_node(),
    )
    dwiextract_wf = init_extract_bzero_wf()
    wf = Workflow(name=name)
    if "denoise" not in config.workflow.ignore:
        wf.connect(
            [
                (inputnode, denoise_node, [("dwi_file", "in_file")]),
                (denoise_node, outputnode, [("out_file", "noise")]),
            ]
        )
        if "degibbs" not in config.workflow.ignore:
            wf.connect(
                [
                    (denoise_node, degibbs_node, [("out_file", "in_file")]),
                    (
                        degibbs_node,
                        dwiextract_wf,
                        [("out_file", "extract_b0.in_file")],
                    ),
                    (degibbs_node, outputnode, [("out_file", "dwi_pre_sdc")]),
                ]
            )
        else:
            wf.connect(
                [
                    (
                        denoise_node,
                        dwiextract_wf,
                        [("out_file", "extract_b0.in_file")],
                    ),
                    (denoise_node, outputnode, [("out_file", "dwi_pre_sdc")]),
                ]
            )
    else:
        if "degibbs" not in config.workflow.ignore:
            wf.connect(
                [
                    (inputnode, degibbs_node, [("dwi_file", "in_file")]),
                    (
                        degibbs_node,
                        dwiextract_wf,
                        [("out_file", "extract_b0.in_file")],
                    ),
                    (degibbs_node, outputnode, [("out_file", "dwi_pre_sdc")]),
                ]
            )
        else:
            wf.connect(
                [
                    (
                        inputnode,
                        dwiextract_wf,
                        [("dwi_file", "extract_b0.in_file")],
                    ),
                    (inputnode, outputnode, [("dwi_file", "dwi_pre_sdc")]),
                ]
            )
    wf.connect(
        [
            (
                dwiextract_wf,
                outputnode,
                [
                    ("outputnode.bzero", "bzero"),
                    ("outputnode.mean_bzero", "mean_bzero"),
                ],
            ),
        ]
    )
    return wf
