#!/usr/bin/env python3

from core import os
from core import log, check_pkg_version, run_process

if __name__ == "__main__":

    log.trace(f"[path]{os.path.basename(__file__)}[/] standalone script")

    pip_packages = [
        "pip",
        "black",
        "zensical",
    ]

    for package in pip_packages:
        check_pkg_version(package)
