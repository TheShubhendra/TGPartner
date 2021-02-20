#!usr/bin/bash
git fetch upstream main
git reset --hard upstream/HEAD
python -m tgpartner
