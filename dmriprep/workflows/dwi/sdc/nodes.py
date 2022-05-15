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
INPUT_NODE = pe.Node(
    niu.IdentityInterface(fields=INPUT_NODE_FIELDS), name="inputnode"
)
OUTPUT_NODE = pe.Node(
    niu.IdentityInterface(fields=OUTPUT_NODE_FIELDS), name="outputnode"
)

#: Building blocks
MERGE_NODE = pe.Node(niu.Merge(2), name="merge_dwi_series")
MRCAT_NODE = pe.Node(mrt.MRCat(**MRCAT_KWARGS), name="concat_dwi_series")
SDC_NODE = pe.Node(mrt.DWIPreproc(**SDC_KWARGS), name="sdc")
