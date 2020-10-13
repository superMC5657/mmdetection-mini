import importlib
import pkgutil


def load_ext(name, funcs):
    ext = importlib.import_module('mmdet.cv_core.' + name)
    for fun in funcs:
        assert hasattr(ext, fun), f'{fun} miss in module {name}'
    return ext

def check_ops_exist():
    ext_loader = pkgutil.find_loader('mmdet.cv_core._ext')
    return ext_loader is not None
