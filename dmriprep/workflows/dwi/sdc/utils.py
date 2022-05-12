def is_dwi_file(in_file: str) -> bool:
    """
    Check if the input file is a DWI file.

    Parameters
    ----------
    in_file : str
        Input file.

    Returns
    -------
    bool
        True if the input file is a DWI file.
    """
    from subprocess import PIPE, Popen

    cmd = ["mrinfo", "in_file", "-dwgrad"]
    p = Popen(cmd, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()
    if stderr:
        return False
    else:
        return True
