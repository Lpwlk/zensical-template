#!/usr/bin/env python3

import argparse
from core import log, run_process, check_pkg_version


def create_parser():

    parser = argparse.ArgumentParser(
        prog="cli.py",
        description="Dev tools CLI app",
    )

    # ----- GLOBAL OPTIONS (AVANT les sous-commandes) -----
    parser.add_argument(
        "-u",
        "--update-pip",
        action="store_true",
        help="Check pip version and update if needed.",
    )

    parser.add_argument(
        "-z",
        "--update-zensical",
        action="store_true",
        help="Check zensical version and update if needed.",
    )

    parser.add_argument(
        "--skip-pip-check",
        action="store_true",
        help="Skip pip version checking (used in update).",
    )

    # ----- SUBCOMMANDS -----
    sub = parser.add_subparsers(dest="command", required=True)

    # serve
    serve_cmd = sub.add_parser("serve", help="Start Zensical dev server")
    serve_cmd.add_argument(
        "-p",
        "--port",
        type=int,
        default=3000,
        help="Port for `zensical serve` (default: 3000)",
    )

    # build
    sub.add_parser("build", help="Build zensical project")

    # update
    update_cmd = sub.add_parser("update", help="Update pip & pip packages")
    update_cmd.add_argument(
        "-s", "--skip-pip-check",
        action="store_true",
        help="Skip the pip update check.",
    )

    return parser

def handle_global_updates(args):

    if args.update_pip and not args.skip_pip_check:
        check_pkg_version("pip")

    if args.update_zensical:
        check_pkg_version("zensical")


def handle_serve(args):
    log.info(f"Starting dev server on localhost:{args.port}")
    run_process(
        ["zensical", "serve", "-a", f"localhost:{args.port}"],
        verbose=True,
        echo_output=False,
        server_mode=True,
    )


def handle_build(args):
    log.info("Building project ...")
    run_process(["zensical", "build"], verbose=True)


def handle_update(args):

    if not args.skip_pip_check:
        check_pkg_version("pip")

    check_pkg_version("zensical")


# --------------------------------------------------------------------
# MAIN DISPATCHER
# --------------------------------------------------------------------


def main():
    parser = create_parser()
    args = parser.parse_args()

    # global flags always run
    handle_global_updates(args)

    match args.command:
        case "serve":
            handle_serve(args)
        case "build":
            handle_build(args)
        case "update":
            handle_update(args)


if __name__ == "__main__":
    main()
