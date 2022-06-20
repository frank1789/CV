#!/bin/bash

# deploy to github tagged releases
if [ -n "$TRAVIS_TAG" ]; then
    echo "==> Tag $TRAVIS_TAG exists"
else
    echo "==> No current tag"
    echo "==> Make a tag"
    git config --local user.name 'travis'
    git config --local user.email 'travis'
    git tag -a $(date +"%Y-%m-%d")-${TRAVIS_BUILD_NUMBER} -m "Travis build $TRAVIS_BUILD_NUMBER pushed a tag"
    echo "==> Done."
fi
