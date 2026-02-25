#!/usr/bin/env zsh

source $ZSH_CFG/cfg/sourcing.zsh >/dev/null

log INFO "Now serving Zensical frontend on http://localhost:3000 ..." -fn -f ${0:h}/../logs/zsh-scripts.log

zensical serve -f zensical.toml -a localhost:3000 > /dev/null 2>&1