#!/usr/bin/env zsh

source $ZSH_CFG/cfg/sourcing.zsh >/dev/null

log INFO "Starting Zensical build task ..." -fn -f ${0:h}/../logs/zsh-scripts.log

zensical build -f zensical.toml