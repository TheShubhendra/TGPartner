#!usr/bin/bash
if [ -z "$REPO_BRANCH" ]
then
      REPO_BRANCH = "main"
else
      echo "Fetching from custom branch $REPO_BRANCH"
fi
git fetch origin $REPO_BRANCH
git reset --hard origin/HEAD
python -m tgpartner
