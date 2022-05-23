@Echo off
title Multi TRX Attacker [MMDRZA.CoM]
Pushd "%~dp0"
:loop
python AttackxTRX_V3.py
goto loop