"""
Configurations for the "fieldmap_query" workflow.
"""
#: Keyword arguments
OPPOSITE_PHASE_QUERY_KWARGS = dict(
    input_names=["dwi_file"],
    output_names=["fmap_file", "fieldmap_is_dwi", "dwi_pe_dir"],
)
