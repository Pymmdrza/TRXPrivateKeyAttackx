@Echo off
title Multi TRX Attacker [MMDRZA.CoM]
Pushd "%~dp0"
start X1.cmd
start X2.cmd
start X3.cmd
start X4.cmd
start X5.cmd
start X6.cmd
start X7.cmd
start X8.cmd
start X9.cmd
start X10.cmd
:loop
python AttackxTRX_V3.py
goto loop
