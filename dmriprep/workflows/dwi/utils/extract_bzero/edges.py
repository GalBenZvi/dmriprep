INPUT_TO_EXTRACT_EDGES = [("in_file", "in_file")]
EXTRACT_TO_MEAN_EDGES = [("out_file", "in_file")]
EXTRACT_TO_OUTPUT_EDGES = [("out_file", "bzero")]
MEAN_TO_CONVERSION_EDGES = [("out_file", "in_file")]
CONVERSION_TO_OUTPUT_EDGES = [
    ("out_file", "mean_bzero"),
    ("json_export", "bzero_json"),
]
