import typing as t

from pydantic import Field, RootModel
from pydantic_settings import BaseSettings, CliApp, CliSubCommand

from aind_behavior_pirouette import __semver__, regenerate


class VersionCli(RootModel):
    root: t.Any

    def cli_cmd(self) -> None:
        print(__semver__)


class DslRegenerateCli(RootModel):
    root: t.Any

    def cli_cmd(self) -> None:
        regenerate.main()


class PirouetteCli(BaseSettings, cli_prog_name="pirouette", cli_kebab_case=True):
    version: CliSubCommand[VersionCli] = Field(
        description="Print the version of the pirouette package.",
    )
    regenerate: CliSubCommand[DslRegenerateCli] = Field(
        description="Regenerate the pirouette dsl dependencies.",
    )

    def cli_cmd(self):
        return CliApp().run_subcommand(self)


def main():
    CliApp().run(PirouetteCli)


if __name__ == "__main__":
    main()
