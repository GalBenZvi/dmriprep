# from dmriprep.workflows.dwi.conversions.nii_to_mif.edges import (
#     DWI_CONVERSION_TO_OUTPUT_EDGES,
#     FMAP_CONVERSION_TO_OUTPUT_EDGES,
#     INPUT_TO_DWI_CONVERSION_EDGES,
#     INPUT_TO_FMAP_CONVERSION_EDGES,
#     LOCATE_ASSOCIATED_TO_COVERSION_EDGES,
# )
# from dmriprep.workflows.dwi.conversions.nii_to_mif.nodes import (
#     DWI_CONVERSION_NODE,
#     FMAP_CONVERSION_NODE,
#     INPUT_NODE,
#     LOCATE_ASSOCIATED_DWI_NODE,
#     LOCATE_ASSOCIATED_FMAP_NODE,
#     OUTPUT_NODE,
# )

from nipype.interfaces import mrtrix3 as mrt
from nipype.interfaces import utility as niu

# MIF_CONVERSION = [
#     (INPUT_NODE, LOCATE_ASSOCIATED_DWI_NODE, INPUT_TO_DWI_CONVERSION_EDGES),
#     (INPUT_NODE, LOCATE_ASSOCIATED_FMAP_NODE, INPUT_TO_FMAP_CONVERSION_EDGES),
#     (
#         LOCATE_ASSOCIATED_DWI_NODE,
#         DWI_CONVERSION_NODE,
#         LOCATE_ASSOCIATED_TO_COVERSION_EDGES,
#     ),
#     (
#         LOCATE_ASSOCIATED_FMAP_NODE,
#         FMAP_CONVERSION_NODE,
#         LOCATE_ASSOCIATED_TO_COVERSION_EDGES,
#     ),
#     (INPUT_NODE, DWI_CONVERSION_NODE, INPUT_TO_DWI_CONVERSION_EDGES),
#     (INPUT_NODE, FMAP_CONVERSION_NODE, INPUT_TO_FMAP_CONVERSION_EDGES),
#     (DWI_CONVERSION_NODE, OUTPUT_NODE, DWI_CONVERSION_TO_OUTPUT_EDGES),
#     (FMAP_CONVERSION_NODE, OUTPUT_NODE, FMAP_CONVERSION_TO_OUTPUT_EDGES),
# ]
from nipype.pipeline import engine as pe


def init_nii_to_mif_wf(name="nii_to_mif_wf"):
    """
    Workflow to convert NIfTI files to mif files

    Parameters
    ----------
    name : str, optional
        Name of workflow. Defaults to "nii_to_mif_wf".
    """
    from dmriprep.workflows.dwi.conversions.nii_to_mif.configurations import (
        INPUT_NODE_FIELDS,
        LOCATE_ASSOCIATED_KWARGS,
        OUTPUT_NODE_FIELDS,
    )
    from dmriprep.workflows.dwi.conversions.nii_to_mif.edges import (
        DWI_CONVERSION_TO_OUTPUT_EDGES,
        FMAP_CONVERSION_TO_OUTPUT_EDGES,
        INPUT_TO_DWI_CONVERSION_EDGES,
        INPUT_TO_FMAP_CONVERSION_EDGES,
        LOCATE_ASSOCIATED_TO_COVERSION_EDGES,
    )
    from dmriprep.workflows.dwi.conversions.nii_to_mif.utils import (
        locate_associated_files,
    )

    #: i/o
    INPUT_NODE = pe.Node(
        niu.IdentityInterface(fields=INPUT_NODE_FIELDS), name="inputnode"
    )
    OUTPUT_NODE = pe.Node(
        niu.IdentityInterface(fields=OUTPUT_NODE_FIELDS), name="outputnode"
    )

    #: Building blocks
    LOCATE_ASSOCIATED_DWI_NODE = pe.Node(
        niu.Function(
            **LOCATE_ASSOCIATED_KWARGS, function=locate_associated_files
        ),
        name="locate_associated_dwi",
    )
    LOCATE_ASSOCIATED_FMAP_NODE = pe.Node(
        niu.Function(
            **LOCATE_ASSOCIATED_KWARGS, function=locate_associated_files
        ),
        name="locate_associated_fmap",
    )
    DWI_CONVERSION_NODE = pe.Node(mrt.MRConvert(), name="dwi_conversion")
    FMAP_CONVERSION_NODE = pe.Node(mrt.MRConvert(), name="fmap_conversion")
    MIF_CONVERSION = [
        (
            INPUT_NODE,
            LOCATE_ASSOCIATED_DWI_NODE,
            INPUT_TO_DWI_CONVERSION_EDGES,
        ),
        (
            INPUT_NODE,
            LOCATE_ASSOCIATED_FMAP_NODE,
            INPUT_TO_FMAP_CONVERSION_EDGES,
        ),
        (
            LOCATE_ASSOCIATED_DWI_NODE,
            DWI_CONVERSION_NODE,
            LOCATE_ASSOCIATED_TO_COVERSION_EDGES,
        ),
        (
            LOCATE_ASSOCIATED_FMAP_NODE,
            FMAP_CONVERSION_NODE,
            LOCATE_ASSOCIATED_TO_COVERSION_EDGES,
        ),
        (INPUT_NODE, DWI_CONVERSION_NODE, INPUT_TO_DWI_CONVERSION_EDGES),
        (INPUT_NODE, FMAP_CONVERSION_NODE, INPUT_TO_FMAP_CONVERSION_EDGES),
        (DWI_CONVERSION_NODE, OUTPUT_NODE, DWI_CONVERSION_TO_OUTPUT_EDGES),
        (FMAP_CONVERSION_NODE, OUTPUT_NODE, FMAP_CONVERSION_TO_OUTPUT_EDGES),
    ]
    wf = pe.Workflow(name=name)
    wf.connect(MIF_CONVERSION)
    return wf
