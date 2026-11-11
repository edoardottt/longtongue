"""CLI validation tests: explicit zero lengths must be rejected.

`-m/--minlength` and `-M/--maxlength` document that they require an
integer greater than 0. A negative value already exits(1) with that
message, but an explicit zero was silently swallowed (``if
args.minlength:`` is falsy for 0) so the program fell through into the
interactive prompts instead of failing fast.
"""

import sys
from unittest.mock import patch

import pytest

from longtongue import cli


def run_main(argv):
    with patch.object(sys, "argv", argv):
        return cli.main()


def test_minlength_zero_rejected(capsys):
    with patch.object(cli, "input_person", side_effect=AssertionError("must not prompt")):
        with pytest.raises(SystemExit) as exc_info:
            run_main(["longtongue", "-p", "-m", "0"])
    assert exc_info.value.code == 1
    assert "-m requires an integer greater than 0." in capsys.readouterr().out


def test_maxlength_zero_rejected(capsys):
    with patch.object(cli, "input_person", side_effect=AssertionError("must not prompt")):
        with pytest.raises(SystemExit) as exc_info:
            run_main(["longtongue", "-p", "-M", "0"])
    assert exc_info.value.code == 1
    assert "-M/--maxlength requires an integer greater than 0." in capsys.readouterr().out


def test_minlength_negative_rejected(capsys):
    with pytest.raises(SystemExit) as exc_info:
        run_main(["longtongue", "-p", "-m", "-5"])
    assert exc_info.value.code == 1
    assert "-m requires an integer greater than 0." in capsys.readouterr().out


def test_version_still_works():
    with pytest.raises(SystemExit) as exc_info:
        run_main(["longtongue", "-v"])
    assert exc_info.value.code == 0
