from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

from setuptools import Command, setup
from setuptools.command.build import build


def generate_property_templates():
    subprocess.run([sys.executable, os.fspath(Path(__file__).parent.joinpath("parse_pwe_templates.py"))], check=True)


class GenerateTemplateCommand(Command):
    """
    Generate script templates code before building the package.
    """

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        if Path(__file__).parent.joinpath("retro-script-object-templates").is_dir():
            generate_property_templates()
        else:
            print("### Not generating templates")


class CustomBuild(build):
    sub_commands = [
        ("generate_template", None),
        *build.sub_commands,
    ]


setup(
    cmdclass={
        "generate_template": GenerateTemplateCommand,
        "build": CustomBuild,
    },
)
