"""
Configuration file for mif_to_nii.py
"""

DWI_CONVERSION_KWARGS = dict(
    out_file="dwi.nii.gz",
    out_bvec="dwi.bvec",
    out_bval="dwi.bval",
    json_export="dwi.json",
    out_grad_mrtrix="grad.b",
)

NON_DWI_CONVERSION_KWARGS = dict(
    out_file="outfile.nii.gz", json_export="outfile.json"
)
