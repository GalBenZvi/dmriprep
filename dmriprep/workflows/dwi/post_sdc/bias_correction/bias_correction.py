import nipype.pipeline.engine as pe
from dmriprep.workflows.dwi.post_sdc.bias_correction.configurations import (
    BIASCORRECT_KWARGS,
)
from nipype.interfaces import mrtrix3 as mrt


def init_bias_correction_node(
    name="bias_correction", kwargs: dict = BIASCORRECT_KWARGS
) -> pe.Node:
    """
    Bias correction node

    Parameters
    ----------
    name : str, optional
        Name of workflow. Defaults to "bias_correction".
    kwargs : dict, optional
        Keyword arguments to be passed to the bias correction node.

    Returns
    -------
    bias_correction : nipype.pipeline.engine.Node
        Bias correction node.
    """

    return pe.Node(
        mrt.DWIBiasCorrect(**kwargs),
        name=name,
    )
