#!/usr/bin/env zsh

source $ZSH_CFG/cfg/sourcing.zsh >/dev/null

log INFO "Checking for pip updates ..." -fn -f ${0:h}/v

py -m pip install --upgrade pip > ${0:h}/logs/zsh-scripts.log 2>&1

log INFO "Checking for zensical updates ..." -fn -f ${0:h}/../logs/zsh-scripts.log

pip install --upgrade --force-reinstall zensical > /dev/null 2>&1