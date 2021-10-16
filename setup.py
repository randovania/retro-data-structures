import os
import subprocess
import sys
from pathlib import Path

from setuptools import setup
from setuptools.command.build_py import build_py
from wheel.bdist_wheel import bdist_wheel


def generate_property_templates():
    subprocess.run([
        sys.executable,
        os.fspath(Path(__file__).parent.joinpath("parse_pwe_templates.py"))
    ], check=True)


class BuildPyCommand(build_py):
    """
    Generate script templates code before building the package.
    """

    def run(self):
        generate_property_templates()
        build_py.run(self)


class BDistWheelCommand(bdist_wheel):
    """
    Generate script templates code before building a wheel.
    """

    def run(self):
        generate_property_templates()
        bdist_wheel.run(self)


setup(
    cmdclass={
        'build_py': BuildPyCommand,
        'bdist_wheel': BDistWheelCommand,
    },
)
