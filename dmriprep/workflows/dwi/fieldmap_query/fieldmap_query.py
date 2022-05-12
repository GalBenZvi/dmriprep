import nipype.pipeline.engine as pe
from dmriprep.workflows.dwi.fieldmap_query.configurations import (
    OPPOSITE_PHASE_QUERY_KWARGS,
)
from dmriprep.workflows.dwi.fieldmap_query.nodes import locate_opposite_phase
from nipype.interfaces import utility as niu


def init_fieldmap_query(name="fieldmap_query"):
    return pe.Node(
        niu.Function(
            **OPPOSITE_PHASE_QUERY_KWARGS, function=locate_opposite_phase
        ),
        name=name,
    )
