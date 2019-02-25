
from . import inclose
from . import export
from . import extract


def concepts(infile:str, min_ext:int, min_int:int) -> [(set, set)]:
    import importlib
    importlib.reload(inclose)
    csv_file = inclose.run_search(infile, min_ext, min_int)
    yield from extract.from_csv_file(csv_file)
