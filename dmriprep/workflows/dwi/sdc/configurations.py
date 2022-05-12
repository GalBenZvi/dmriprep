"""
Configuration file for the dwi_sdc workflow.
"""
#: i/o
INPUT_NODE_FIELDS = ["dwi_file", "fmap_file", "dwi_pe_dir", "mean_bzero"]
OUTPUT_NODE_FIELDS = ["dwi_preproc"]

#: Keyword arguments
MRCAT_KWARGS = dict(axis=3, out_file="phasediff.mif")
SDC_KWARGS = dict(
    eddy_options="--slm=linear --repol",
    rpe_options="header",
    out_file="preproc_dwi.mif",
    eddyqc_all="qddyqc",
)
SDC_NO_DWI_KWARGS = dict(
    eddy_options="--slm=linear --repol",
    rpe_options="pair",
    align_seepi=True,
    out_file="preproc_dwi.mif",
    eddyqc_all="qddyqc",
)
