#: i/o
INPUT_NODE_FIELDS = ["in_file"]
OUTPUT_NODE_FIELDS = ["bzero", "mean_bzero"]


EXTRACT_KWARGS = dict(out_file="bzero.mif", bzero=True)
MEAN_B0_KWARGS = dict(out_file="mean_bzero.mif", operation="mean", axis=3)
