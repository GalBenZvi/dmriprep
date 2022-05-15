INPUT_TO_BIASCORRECT_EDGES = [("dwi_file", "in_file")]
BIASCORRECT_TO_NII_EDGES = [("out_file", "in_file")]

INPUT_TO_EXTRACT_EDGES = [("dwi_file", "extract_b0.in_file")]
BIASCORRECT_TO_EXTRACT_EDGES = [("out_file", "extract_b0.in_file")]

EXTRACT_TO_EPIREG_EDGES = [("outputnode.mean_bzero", "inputnode.in_file")]
INPUT_TO_EPIREG_EDGES = [
    ("t1w_head", "inputnode.t1w_head"),
    ("t1w_brain", "inputnode.t1w_brain"),
]
