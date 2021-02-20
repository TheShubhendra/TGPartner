#!usr/bin/bash
git fetch origin main
git reset --hard main/HEAD
python -m tgpartner
