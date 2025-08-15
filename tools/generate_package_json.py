import json
import pathlib
from os import path
from typing import Final

_PACKAGE_JSON_FILE: Final = pathlib.Path("package.json")
_UNITS_DIRECTORY: Final = pathlib.Path("src", "units")

_GITHUB_REPO_STEM: Final = "github:WoolleySheep/micropython-units"

# [
#     "units/angular_motion.py",
#     "github:WoolleySheep/micropython-units/src/units/angular_motion.py"
# ],


def _create_package_filepath(file: pathlib.Path) -> str:
    """Create a package filepath for a given file."""
    src_directory = pathlib.Path.cwd().parent / "src"
    relative_path = file.relative_to(src_directory)
    return str(relative_path).replace("\\", "/")


def _create_package_info() -> dict[str, str | list[list[str]]]:
    urls = list[list[str]]()
    for file in (pathlib.Path.cwd().parent / _UNITS_DIRECTORY).rglob("*"):
        if file.is_dir() or file.suffix != ".py":
            continue
        package_filepath = _create_package_filepath(file)
        package_url = f"{_GITHUB_REPO_STEM}/src/{package_filepath}"
        urls.append([package_filepath, package_url])

    return {
        "urls": sorted(urls),
        "deps": [["github:Josverl/micropython-stubs/mip/typing.py", "main"]],
        "version": "0.1",
    }


def _write_package_json(package_info: dict[str, str | list[list[str]]]) -> None:
    with (pathlib.Path.cwd().parent / _PACKAGE_JSON_FILE).open(mode="w") as f:
        json.dump(package_info, fp=f, indent=4)


def _main() -> None:
    _write_package_json(_create_package_info())


if __name__ == "__main__":
    _main()
