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
    from pathlib import Path

    from nipype.interfaces.base import traits

    in_file = Path(in_file)
    associated_extenstions = ["json", "bvec", "bval"]
    output = {}
    for key in associated_extenstions:
        val = in_file.parent / f"{in_file.name.split('.')[0]}.{key}"
        if val.exists():
            output[key] = str(val)
        else:
            output[key] = traits.Undefined
    return [output.get(key) for key in associated_extenstions]
