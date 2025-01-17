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
EXTRACT_NODE = pe.Node(mrt.DWIExtract(**EXTRACT_KWARGS), name="extract_b0")
MEAN_B0_NODE = pe.Node(mrt.MRMath(**MEAN_B0_KWARGS), name="mean_b0")
