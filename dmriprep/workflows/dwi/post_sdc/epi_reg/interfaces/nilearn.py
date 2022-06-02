import os.path as op

from nipype.interfaces.base import (
    BaseInterface,
    BaseInterfaceInputSpec,
    File,
    TraitedSpec,
    traits,
)


def resample_to_image(
    source: str, target: str, interpolation: str, out_file: str
) -> str:
    """
    Function to resample *mask* to a target.
    Relies on nilearn's resample_to_image and nibabel.

    Parameters
    ----------
    source : str
        Source file.
    target : str
        Target file.
    interpolation : str
        Interpolation method.

    Returns
    -------
    str
        Resampled mask.
    """
    from nilearn.image import resample_to_img

    img = resample_to_img(source, target, interpolation=interpolation)
    img.to_filename(out_file)
    return out_file


class ResampleToImageInputSpec(BaseInterfaceInputSpec):
    source = File(exists=True, mandatory=True, desc="Image to resample")
    out_file = File(
        mandatory=True,
        desc="the output image",
    )  # Do not set exists=True !!
    target = File(
        exists=True,
        mandatory=True,
        desc="Reference image taken for resampling.",
    )
    interpolation = traits.Str(
        default_value="nearest", usedefault=True, desc="Interpolation method"
    )


class ResampleToImageOutputSpec(TraitedSpec):
    out_file = File(desc="The output, resampled image")


class ResampleToImage(BaseInterface):
    input_spec = ResampleToImageInputSpec
    output_spec = ResampleToImageOutputSpec

    def _run_interface(self, runtime):
        resample_to_image(
            self.inputs.source,
            self.inputs.target,
            self.inputs.interpolation,
            self.inputs.out_file,
        )
        return runtime

    def _list_outputs(self):
        return {"out_file": op.abspath(self.inputs.out_file)}
