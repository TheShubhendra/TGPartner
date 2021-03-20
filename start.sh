#!usr/bin/bash
if [ -z "$DO_NOT_UPDATE_BEFORE_START" ]
then
     python -m tgpartner
     exit
fi
if [ -z "$REPO_BRANCH" ]
then
      REPO_BRANCH = "main"
else
      echo "Fetching from custom branch $REPO_BRANCH"
fi
git fetch origin $REPO_BRANCH
git reset --hard origin/HEAD
python -m tgpartner

