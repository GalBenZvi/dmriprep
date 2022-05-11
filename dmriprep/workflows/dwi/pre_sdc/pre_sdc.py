from dmriprep.workflows.dwi.pre_sdc.nodes import (
    DEGIBBS_NODE,
    DENOISE_NODE,
    EXTRACT_NODE,
    INPUT_NODE,
    MEAN_B0_NODE,
    OUTPUT_NODE,
)

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

    wf = Workflow(name=name)
    if "denoise" not in config.workflows.ignore:
        wf.connect(
            [
                (INPUT_NODE, DENOISE_NODE, [("dwi_file", "in_file")]),
                (DENOISE_NODE, OUTPUT_NODE, [("out_file", "noise")]),
            ]
        )
        if "degibbs" not in config.workflows.ignore:
            wf.connect(
                [
                    (DENOISE_NODE, DEGIBBS_NODE, [("out_file", "in_file")]),
                    (DEGIBBS_NODE, EXTRACT_NODE, [("out_file", "in_file")]),
                    (DEGIBBS_NODE, OUTPUT_NODE, [("out_file", "dwi_preproc")]),
                ]
            )
        else:
            wf.connect(
                [
                    (DENOISE_NODE, EXTRACT_NODE, [("out_file", "in_file")]),
                    (DENOISE_NODE, OUTPUT_NODE, [("out_file", "dwi_preproc")]),
                ]
            )
    else:
        if "degibbs" not in config.workflows.ignore:
            wf.connect(
                [
                    (INPUT_NODE, DEGIBBS_NODE, [("dwi_file", "in_file")]),
                    (DEGIBBS_NODE, EXTRACT_NODE, [("out_file", "in_file")]),
                    (DEGIBBS_NODE, OUTPUT_NODE, [("out_file", "dwi_preproc")]),
                ]
            )
        else:
            wf.connect(
                [
                    (INPUT_NODE, EXTRACT_NODE, [("dwi_file", "in_file")]),
                    (INPUT_NODE, OUTPUT_NODE, [("dwi_file", "dwi_preproc")]),
                ]
            )
    wf.connect(
        [
            (EXTRACT_NODE, MEAN_B0_NODE, [("out_file", "in_file")]),
            (EXTRACT_NODE, OUTPUT_NODE, [("out_file", "bzero")]),
            (MEAN_B0_NODE, OUTPUT_NODE, [("out_file", "mean_bzero")]),
        ]
    )
    return wf
