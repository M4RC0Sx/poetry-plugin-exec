from __future__ import annotations

from typing import TYPE_CHECKING

from poetry.plugins.application_plugin import ApplicationPlugin

from poetry_plugin_exec.command import ExecCommand


if TYPE_CHECKING:
    from poetry.console.commands.command import Command


class ExecApplicationPlugin(ApplicationPlugin):
    @property
    def commands(self) -> list[type[Command]]:
        return [ExecCommand]
