from __future__ import annotations

import subprocess

from typing import ClassVar

from cleo.helpers import argument
from poetry.console.commands.command import Command


class ExecCommand(Command):
    name = "exec"
    description = (
        "Execute a script defined in pyproject.toml (tool.poetry_plugin_exec.scripts)"
    )
    arguments: ClassVar = [
        argument(
            "script_name",
            description="The name of the script to execute",
            optional=False,
        )
    ]

    def handle(self) -> int:
        script_name = self.argument("script_name")
        poetry = self.poetry
        scripts = (
            poetry.pyproject.data.get("tool", {})
            .get("poetry_plugin_exec", {})
            .get("scripts", None)
        )

        if scripts is None:
            self.line_error(
                "<error>Scripts section missing in pyproject.toml!</error> (tool.poetry_plugin_exec.scripts)"
            )
            return 1

        if script_name not in scripts:
            self.line_error(
                f"<error>Script <question>{script_name}</> does not exist in pyproject.toml!</error> (tool.poetry_plugin_exec.scripts)"
            )
            return 1

        command = scripts[script_name]
        self.line(f"Executing <info>{script_name}</> script...")

        try:
            process = subprocess.run(command, shell=True, check=True)
            return process.returncode
        except subprocess.CalledProcessError as e:
            self.line_error(f"Error executing <comment>{script_name}</> script: {e}")
            return 1
