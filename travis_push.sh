#!/usr/bin/env sh
# Credit: https://gist.github.com/willprice/e07efd73fb7f13f917ea

setup_git() {
   git config --local user.name 'travis'
   git config --local user.email 'travis'
}

commit_pdf_files() {
  git checkout master
  # Current month and year, e.g: Apr 2018
  DATE=$(date +"%Y%m%d")
  # Stage the modified files in dist/output
  git add -f FrancescoArgentieri-Resume.pdf
  # Create a new commit with a custom build message
  # with "[skip ci]" to avoid a build loop
  # and Travis build number for reference
  git commit -m "CV Release: $DATE (Build $TRAVIS_BUILD_NUMBER)" -m "[skip ci]"
}

upload_files() {
  # Remove existing "origin"
  git remote rm origin
  # Add new "origin" with access token in the git URL for authentication
  git remote add origin https://frank1789:${pushongit}@github.com/frank1789/CV.git > /dev/null 2>&1
  git push origin master --quiet
}

setup_git
commit_pdf_files

# Attempt to commit to git only if "git commit" succeeded
if [ $? -eq 0 ]; then
  echo "A new commit with changed pdf. Uploading to GitHub"
  upload_files
else
  echo "No changes in pdf files. Nothing to do"
fi