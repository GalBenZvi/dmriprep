#: i/o
INPUT_NODE_FIELDS = ["dwi_file", "fmap_file"]
OUTPUT_NODE_FIELDS = ["dwi_preproc", "noise", "bzero", "mean_bzero"]

#: Keyword arguments
DENOISE_KWARGS = dict(noise="noise.nii.gz")
DEGIBBS_KWARGS = dict()
EXTRACT_KWARGS = dict(bzero=True)
MEAN_B0_KWARGS = dict(operation="mean", axis=3)
