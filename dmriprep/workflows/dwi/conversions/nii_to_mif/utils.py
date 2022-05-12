def locate_associated_files(in_file: str):
    """
    Locates associated json (and possibly bvec & bval) files.

    Parameters
    ----------
    in_file : str
        Input file.

    Returns
    -------
    Tuple[str, str, str]
        Tuple of associated json (and possibly bvec & bval) files.
    """
    from dmriprep.config import config
    from nipype.interfaces.base import traits

    associated_extenstions = ["json", "bvec", "bval"]
    layout = config.execution.layout
    output = {}
    for key in associated_extenstions:
        output[key] = (
            layout.get_nearest(in_file, extension=key) or traits.Undefined
        )
    return [output.get(key) for key in associated_extenstions]
