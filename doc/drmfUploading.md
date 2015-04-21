Instructions for uploading 
SSH key generation:

Committing to Gerrit:
To check changes/commitments:
-Log onto WikiMedia
-Check Changes under personal settings

Committing:
-cd into folder of commitment (~/MathSearch)
-"git status" to check modified files
-"git add ~insert file name~" for commitment
-"git commit"
-Add project description/title to file
-"git commit --amend --author='name <email>'" to change author info
-"git remote -v"
-"git push origin HEAD:refs/for/master" to push for review
-"scp -p -P 29418 sharmaans@gerrit.wikimedia.org:hooks/commit-msg .git/hooks/" to commit
-'git commit -a -m "reformatting"' to commit an update of files
-"git pull" to pull most recent version of folders
-"git push" to push most recent version of folders
