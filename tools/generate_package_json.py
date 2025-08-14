import json
import pathlib
from typing import Final

_PACKAGE_JSON_FILEPATH: Final = pathlib.Path("../package.json")
_UNITS_DIRECTORY: Final = pathlib.Path("../units/")

_GITHUB_REPO_STEM: Final = "github:WoolleySheep/micropython-units/"


def _create_package_filepath(file: pathlib.Path) -> str:
    """Create a package filepath for a given file."""
    return str(file)[3:].replace("\\", "/")


def _create_package_info() -> dict[str, str | list[list[str]]]:
    urls = list[list[str]]()
    for file in _UNITS_DIRECTORY.rglob("*"):
        if file.is_dir() or file.suffix != ".py":
            continue
        package_filepath = _create_package_filepath(file)
        package_url = _GITHUB_REPO_STEM + package_filepath
        urls.append([package_filepath, package_url])

    return {
        "urls": sorted(urls),
        "deps": [["github:Josverl/micropython-stubs/mip/typing.py", "main"]],
        "version": "0.1",
    }


def _write_package_json(package_info: dict[str, str | list[list[str]]]) -> None:
    with _PACKAGE_JSON_FILEPATH.open(mode="w") as f:
        json.dump(package_info, fp=f, indent=4)


def _main() -> None:
    _write_package_json(_create_package_info())


if __name__ == "__main__":
    _main()
