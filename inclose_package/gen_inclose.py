from pybindgen import *

def generate(file):
    mod = Module('inclose')
    mod.add_include('"In-Close4.h"')
    mod.add_function('niam', retval('int'), [])
    mod.generate(file)
