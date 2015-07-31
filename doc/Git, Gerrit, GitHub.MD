## Initial Setup for Git
	Git is the platform in which developers can work together on a project.
1. If you dont already have a running git repository, run `git init` in the folder in which you want to create your git repository
2. Make sure to set up your git username and email before making any changes:
 - Run `git config --global user.name "YOUR NAME"` to set the author's name
 - Run `git config --global user.email "YOUR_EMAIL@example.com"` to set the authour's email
3. To install the hook on your local machine, run `scp -p -P 29418 <GERRITUSERNAME>@gerrit.wikimedia.org:hooks/commit-msg .git/hooks/` 
4. To check which remote you currently have, run `git remote -v` 
 - If you need to add a new remote to push to run `git remote add NAME LINK_TO_REPO`
5. To learn more about git read [this link](https://try.github.io/levels/1/challenges/1) or [that link](https://www.atlassian.com/git/tutorials/comparing-workflows/)

## Keeping your local repository updated
	Make sure you do this before making any changes as to aviod future complications.
1. Find the project you are working with on [here](https://git.wikimedia.org/). This should contain the most updated version of your project. (Ex: [MathSearch Extension](https://git.wikimedia.org/summary/mediawiki%2Fextensions%2FMathSearch))
2. Using the repository url, from your project, make a new remote called 'upstream' by running `git remote add upstream REPOSITORY_URL` (MathSearch repository url:  https://git.wikimedia.org/git/mediawiki/extensions/MathSearch.git)
3. You also have to make a gerrit remote. First find your project on [here](https://gerrit.wikimedia.org/r/#/admin/projects/). Then log in and click ssh in the top left. This should give you a ssh link which you will use next. Run `git remote add gerrit SSH_LINK` (Ex: (MathSearch Link) ssh://GERRITUSERNAME@gerrit.wikimedia.org:29418/mediawiki/extensions/MathSearch)
4. Run `git fetch upstream` to get the temporarily get access to the most updated version on the project you are working on
5. Run `git diff master..upstream/master` to check the differences between your local repository and the most updated version. If nothing appears, then you have the most updated version on your local machine. Otherwise, continue to step 5
6. There are many ways to approach this problem but the method being shown here will download a new fully updated branch and we will make it your new master branch. (**NOTE: THIS WILL REMOVE ALL THE CHANGES THAT YOU HAVEN'T COMMITTED**)
7. Run `git pull`
8. Redo steps 4 and 5 to see if you have any differences in your code and the most updated code

## Committing to Gerrit:
	Gerrit is a cooperative platform which allows other users to review your code. You have locally stored commits, files you want to be reviewed, which can be pushed for review on Gerrit.

######Before you make any changes you should check to see if you have the most updated version of whatever you will be commiting to visit [Keeping your local repository updated](https://github.com/DRMF/DRMF/blob/master/doc/upload_and_connect.MD#keeping-your-local-repository-updated)
1. Save the id_rsa.pub (**Public**) content under your account WikiMedia-->Settings-->SSH Public Keys
2. You might have to [add a remote](https://github.com/DRMF/DRMF/blob/master/doc/upload_and_connect.MD#initial-setup-for-git) which uses ssh rather than anonymous  https (for example `ssh://USERNAME@gerrit.wikimedia.org:29418/mediawiki/extensions/MathSearch` rather than `https://gerrit.wikimedia.org/r/mediawiki/extensions/MathSearch`)
3. cd into folder of commitment (~/MathSearch)
4. Run `git status` to check modified files
5. Run `git add FILENAME` or `git add -A` if you want to commit everything from `git status`
6. Run `git commit` to update the local commit files
7. Add project description/title to file
8. Run `git review` to push for review on gerrit OR (if "git review" doesn't work) run `git push [remote name] HEAD:refs/for/master` to push your commits anywhere else

## Check changes on gerrit

1. Log on to gerrit
2. In the upper left hand corner go to My-->Changes

## Squashing commits
	Multiple commits can be squashed into a single upload on a branch with multiple patches.

1. cd into folder of commitment (~/MathSearch)
2. `git rebase -i HEAD~1`
3. Replace "pick" in commit message with "squash"
4. `git review` to push for review on gerrit

## Commiting to GitHub
	GitHub allows files and contributions to be collected and stored in a Cloud collective project database.
	
1. Log onto your GitHub account
2. Request to be added to the DRMF directory
3. Navigate to the branch to which you want to contribute
4. Click the [+] next to the directory address to add a new pull request
5. Copy/paste the file and add appropriate name and description
6. Choose the option to "commit directly to the master branch"
7. Commit changes
