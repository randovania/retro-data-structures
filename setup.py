import os
import subprocess
import sys
from pathlib import Path

from setuptools import setup
from setuptools.command.egg_info import egg_info


def generate_property_templates():
    subprocess.run([
        sys.executable,
        os.fspath(Path(__file__).parent.joinpath("parse_pwe_templates.py"))
    ], check=True)


class GenerateTemplateCommand(egg_info):
    """
    Generate script templates code before building the package.
    """

    def run(self):
        if Path(__file__).parent.joinpath("PrimeWorldEditor").is_dir():
            generate_property_templates()
        return egg_info.run(self)


setup(
    cmdclass={
        'egg_info': GenerateTemplateCommand,
    },
)
