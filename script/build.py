#!/usr/bin/env python3

from core import os
from core import log, check_pkg_version, run_process

if __name__ == "__main__":

    log.trace(f"[path]{os.path.basename(__file__)}[/] standalone script")

    run_process(
        command=[
            "zensical",
            "build",
            "--clean",
            "--config-file",
            "zensical.toml",
        ],
        verbose=True,
        echo_output=False,
        server_mode=False,
        extra_msg=None,
    )
