from dmriprep.workflows.dwi.post_sdc.bias_correction.configurations import (
    BIASCORRECT_KWARGS,
)


def init_bias_correction_node(name="bias_correction"):
    """
    Bias correction node

    Parameters
    ----------
    name : str, optional
        Name of workflow. Defaults to "bias_correction".
    """
    import nipype.pipeline.engine as pe
    from nipype.interfaces import mrtrix3 as mrt

    return pe.Node(
        mrt.DWIBiasCorrect(**BIASCORRECT_KWARGS),
        name=name,
    )
