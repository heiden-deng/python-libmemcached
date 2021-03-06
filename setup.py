#!/usr/bin/env python

from setuptools import setup, Extension
from Cython.Distutils import build_ext

setup(
        name = "python-libmemcached",
        version = "1.0",
        description="python memcached client wrapped on libmemcached",
        maintainer="davies",
        maintainer_email="davies.liu@gmail.com",
        install_requires = ['cython'],
        cmdclass = {'build_ext': build_ext},
        ext_modules=[Extension('cmemcached_imp', 
            ['cmemcached_imp.pyx', 'split_mc.c'],
            libraries=['memcached'],
            #extra_link_args=['--no-undefined', '-Wl,-rpath=/usr/local/lib'],
            #include_dirs = ["/usr/local/include"],
            #library_dirs = ["/usr/local/lib"],
        )],

        py_modules=['cmemcached'],
        test_suite="cmemcached_test",
)
