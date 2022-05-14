#: i/o
OUTPUT_NODE_FIELDS = ["bzero", "mean_bzero", "bzero_json"]


EXTRACT_KWARGS = dict(out_file="bzero.mif", bzero=True)
MEAN_B0_KWARGS = dict(out_file="mean_bzero.mif", operation="mean", axis=3)
