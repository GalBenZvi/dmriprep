#: i/o
INPUT_NODE_FIELDS = ["dwi_file"]
OUTPUT_NODE_FIELDS = ["dwi_pre_sdc", "noise", "bzero", "mean_bzero"]

#: Keyword arguments
DENOISE_KWARGS = dict(out_file="denoised.mif")
DEGIBBS_KWARGS = dict(out_file="degibbsed.mif")
EXTRACT_KWARGS = dict(out_file="bzero.mif", bzero=True)
MEAN_B0_KWARGS = dict(out_file="mean_bzero.mif", operation="mean", axis=3)
