@Echo off
title Multi TRX Attacker [MMDRZA.CoM]
Pushd "%~dp0"
python -m pip install --upgrade pip
pip install rich
pip install tropapi
pip install colorama
python AttackxTRX_V3.py
