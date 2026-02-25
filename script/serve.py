#!/usr/bin/env python3

from core import os
from core import log, check_pkg_version, run_process

if __name__ == "__main__":

    log.trace(f"[path]{os.path.basename(__file__)}[/] standalone script")

    run_process(
        command=["zensical", "serve", "-a", "localhost:3000", "-o"],
        verbose=True,
        echo_output=False,
        server_mode=True,
        extra_msg=None,
    )
