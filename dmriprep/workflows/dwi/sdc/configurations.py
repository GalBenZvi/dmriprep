"""
Configuration file for the dwi_sdc workflow.
"""
#: i/o
INPUT_NODE_FIELDS = ["dwi_file", "fmap_file", "dwi_pe_dir"]
OUTPUT_NODE_FIELDS = ["dwi_preproc"]

#: Keyword arguments
MRCAT_KWARGS = dict(axis=3, out_file="phasediff.mif")
SDC_KWARGS = dict(
    eddy_options="--slm=linear --repol",
    rpe_options="header",
    out_file="preproc_dwi.mif",
    export_grad_mrtrix=True,
    eddyqc_all="qddyqc",
)
