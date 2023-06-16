

import os
from glob import glob



def find_path(file_name, path):
    """ Searches [path] for [file_name]

    Args:
        file_name (str): File name with extention
        path (str): Relative/Absolute search dir path

    Returns:
        (str): Absolute filepath for [file_name]
    """
    
    files = []
    for dir,_,_ in os.walk(path):
        files.extend(glob(os.path.join(dir,file_name)))
    
    assert len(files) == 1, f"Multiple files found for {file_name}! {files}"
    
    return files[0]
