from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension

ext_modules = [
    Pybind11Extension(
        "_electrons",
        ["./src/cppscripts/electric.cpp"],
        extra_compile_args=["-std=c++11"]
    ),
]