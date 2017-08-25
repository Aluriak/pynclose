#!/usr/bin/env python
import os
import glob
from distutils.core import setup, Extension
# from pynclose import gen_finclose, gen_inclose
from inclose_package import gen_inclose

# module_finclose = os.path.join('build', 'finclose-binding.c')
# with open(module_finclose, 'wt') as file_:
    # print('Generating file {}'.format(module_finclose))
    # gen_finclose.generate(file_)
module_inclose = 'build/inclose-binding.cpp'
with open(module_inclose, 'w') as file_:
    print('Generating file {}'.format(module_inclose))
    gen_inclose.generate(file_)

# finclose = Extension('finclose',
                     # sources = [module_finclose, 'build/my-module.c'],
                     # include_dirs=['pynclose/finclose', 'build'])

inclose = Extension('inclose',
                    # sources=[module_inclose],
                    sources=[module_inclose, *glob.glob('inclose_package/*.cpp')],
                    include_dirs=['inclose_package/'],
                    extra_compile_args=['-fopenmp', '-O2'],
                    extra_link_args=['-fopenmp', '-O2', '-Wl,-z,defs', '-flto'],
                    language='c++')

setup(name='pynclose',
      version='0.0.1',
      description='',
      author='lucas bourneuf',
      author_email='lucas.bourneuf@laposte.net',
      ext_modules=[inclose],
      packages=['pynclose'],
     )

