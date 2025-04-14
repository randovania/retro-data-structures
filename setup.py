from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

from setuptools import Command, setup
from setuptools.command.build import build


def generate_property_templates():
    subprocess.run([sys.executable, os.fspath(Path(__file__).parent.joinpath("parse_pwe_templates.py"))], check=True)


class CreateTemplatesCommand(Command):
    """Custom build command."""

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        generate_property_templates()


class CustomBuild(build):
    sub_commands = [
        ("create_templates", None),
        *build.sub_commands,
    ]


setup(
    cmdclass={
        "create_templates": CreateTemplatesCommand,
        "build": CustomBuild,
    },
)
