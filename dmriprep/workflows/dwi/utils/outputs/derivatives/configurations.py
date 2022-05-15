INPUT_NODE_FIELDS = [
    "source_file",
    "base_directory",
    "native_dwi_file",
    "native_dwi_json",
    "native_dwi_bvec",
    "native_dwi_bval",
    "native_dwi_grad",
    "native_dwiref_file",
    "native_dwiref_json",
    "epi_to_t1w_aff",
    "t1w_to_epi_aff",
    "coreg_dwi_file",
    "coreg_dwi_bvec",
    "coreg_dwi_bval",
    "coreg_dwi_json",
    "coreg_dwi_grad",
    "coreg_dwiref_file",
    "coreg_dwiref_json",
    "native_dwi_mask",
    "coreg_dwi_mask",
]

NATIVE_DWI_KWARGS = dict(
    datatype="dwi",
    space="dwi",
    desc="preproc",
    suffix="dwi",
    compress=None,
)
COREG_DWI_KWARGS = dict(
    datatype="dwi",
    space="T1w",
    desc="preproc",
    suffix="dwi",
    compress=None,
)
NATIVE_DWIREF_KWARGS = dict(
    datatype="dwi",
    space="dwi",
    desc="preproc",
    suffix="dwiref",
    compress=None,
)
COREG_DWIREF_KWARGS = dict(
    datatype="dwi",
    space="T1w",
    desc="preproc",
    suffix="dwiref",
    compress=None,
)
EPI_TO_T1_AFF_KWARGS = dict(
    datatype="dwi",
    suffix="xfm",
    extension=".txt",
    to="T1w",
    compress=False,
)
EPI_TO_T1_AFF_KWARGS["from"] = "dwi"

T1_to_EPI_AFF_KWARGS = dict(
    datatype="dwi",
    suffix="xfm",
    extension=".txt",
    to="dwi",
    compress=False,
)
T1_to_EPI_AFF_KWARGS["from"] = "T1w"

NATIVE_DWI_MASK_KWARGS = dict(
    datatype="dwi",
    suffix="mask",
    desc="brain",
    space="dwi",
    compress=None,
    # dismiss_entities=["direction"],
)
COREG_DWI_MASK_KWARGS = dict(
    datatype="dwi",
    suffix="mask",
    desc="brain",
    space="T1w",
    compress=None,
    # dismiss_entities=["direction"],
)
