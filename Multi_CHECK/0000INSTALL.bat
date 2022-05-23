@Echo off
title Multi TRX Attacker [MMDRZA.CoM]
Pushd "%~dp0"
pip install rich
pip install tropapi
pip install colorama
:loop
python AttackxTRX_V3.py
goto loop