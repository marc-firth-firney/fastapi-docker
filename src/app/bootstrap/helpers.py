from pathlib import Path, PosixPath

'''
| Returns the path to the base directory of the project.
| 
| @return PosixPath
'''
def base_path() -> PosixPath:
    return Path(__file__).resolve().parent.parent


'''
| Returns the path to the seeders directory.
| 
| @return PosixPath
'''
def seeders_path() -> PosixPath:
    return Path(str(base_path()) + "/database/seeders").resolve()
