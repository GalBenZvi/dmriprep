from audioop import bias

BIASCORRECT_KWARGS = dict(
    use_ants=True, out_file="preproc_biascorr_dwi.mif", bias="bias.nii.gz"
)