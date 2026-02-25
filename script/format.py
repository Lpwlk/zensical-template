#!/usr/bin/env python3

from core import os
from core import log, check_pkg_version, run_process

if __name__ == "__main__":

    log.trace(f"[path]{os.path.basename(__file__)}[/] standalone script")
    check_pkg_version("black")

    proc = run_process(
        command=["black", "tools", "-l", "90"],
        verbose=True,
        echo_output=True,
        server_mode=False,
        extra_msg=None,
    )
