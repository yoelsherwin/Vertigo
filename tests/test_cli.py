from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from vertigo.cli import main


def test_hello_prints_greeting(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["hello"]) == 0

    captured = capsys.readouterr()
    assert captured.out == "Hello, Vertigo!\n"
    assert captured.err == ""


def test_installed_hello_command_uses_lf_on_every_platform() -> None:
    script = shutil.which("vertigo", path=str(Path(sys.executable).parent))
    assert script is not None

    result = subprocess.run(
        [script, "hello"],
        check=False,
        capture_output=True,
    )

    assert result.returncode == 0
    assert result.stdout == b"Hello, Vertigo!\n"
    assert result.stderr == b""


@pytest.mark.parametrize(
    ("argv", "error_text"),
    [
        ([], "the following arguments are required: command"),
        (["unknown"], "invalid choice: 'unknown'"),
    ],
)
def test_invalid_command_uses_argparse_error(
    argv: list[str],
    error_text: str,
    capsys: pytest.CaptureFixture[str],
) -> None:
    with pytest.raises(SystemExit) as error:
        main(argv)

    assert error.value.code == 2
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err.startswith("usage: vertigo")
    assert error_text in captured.err
