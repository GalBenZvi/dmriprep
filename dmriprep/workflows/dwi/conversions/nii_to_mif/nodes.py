import nipype.pipeline.engine as pe
from dmriprep.workflows.dwi.conversions.nii_to_mif.configurations import (
    INPUT_NODE_FIELDS,
    LOCATE_ASSOCIATED_KWARGS,
    OUTPUT_NODE_FIELDS,
)
from dmriprep.workflows.dwi.conversions.nii_to_mif.utils import (
    locate_associated_files,
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
LOCATE_ASSOCIATED_DWI_NODE = pe.Node(
    niu.Function(**LOCATE_ASSOCIATED_KWARGS, function=locate_associated_files),
    name="locate_associated_dwi",
)
LOCATE_ASSOCIATED_FMAP_NODE = pe.Node(
    niu.Function(**LOCATE_ASSOCIATED_KWARGS, function=locate_associated_files),
    name="locate_associated_fmap",
)
DWI_CONVERSION_NODE = pe.Node(mrt.MRConvert(), name="dwi_conversion")
FMAP_CONVERSION_NODE = pe.Node(mrt.MRConvert(), name="fmap_conversion")
