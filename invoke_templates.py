from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

# https://discuss.python.org/t/custom-build-steps-moving-bokeh-off-setup-py/16128/3
from hatchling.builders.hooks.plugin.interface import BuildHookInterface


def generate_property_templates() -> None:
    subprocess.run([sys.executable, os.fspath(Path(__file__).parent.joinpath("parse_pwe_templates.py"))], check=True)


class CustomHook(BuildHookInterface):
    def initialize(self, version, build_data):
        generate_property_templates()
