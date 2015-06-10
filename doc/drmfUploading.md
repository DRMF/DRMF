-------Terminal commands are in double quotes ("")------

4/20/2015
----------------------Connecting to an instance:--------------------
	--An SSH key allows you to connect and communicate with a trusted server (e.g. drmf-ecf) without repeatedly re-entering passwords or other sensitive data.--
-Create an SSH key: "$ ssh-keygen -t rsa -C 'your_email@youremail.com'"
-Modify the config file in the .ssh/ folder (this configures the SSH key to connect to drmf-ecf via localhosts):

"Host bastion1.eqiad.wmflabs
    Hostname bastion.wmflabs.org
    ProxyCommand none

Host bastion2.eqiad.wmflabs
    Hostname bastion2.wmflabs.org
    ProxyCommand none

Host bastion3.eqiad.wmflabs
    Hostname bastion3.wmflabs.org
    ProxyCommand none

Host *.eqiad.wmflabs
    ProxyCommand ssh -a -W %h:%p bastion1.eqiad.wmflabs

Host *.wmflabs
    User GERRITUSERNAME

Host ecf
    HostName drmf-ecf.eqiad.wmflabs
    ProxyCommand ssh -a -W %h:%p bastion2.eqiad.wmflabs
    User GERRITUSERNAME
    LocalForward 2222 localhost:22
    LocalForward 8080 localhost:80"

-"ssh INSTANCENAME" to connect to the instance each time afterwards (current instance name is 'ecf')

4/13/2015
----------------------------Committing to Gerrit:--------------------------
	--Gerrit is a cooperative platform which allows other users to review your code. You have locally stored commits - files you want to be reviewed - which can be pushed for review on Gerrit.--

-Save the id_rsa content under your account WikiMedia-->Settings-->SSH Public Keys
-cd into folder of commitment (~/MathSearch)
-"git status" to check modified files
-"git add ~insert file name~" for commitment
-"git commit" to update the local commit files
-Add project description/title to file
-"git commit --amend --author='name <email>'" to change author info
-"git remote -v"
-"git push origin HEAD:refs/for/master" to push for review on gerrit
-"scp -p -P 29418 sharmaans@gerrit.wikimedia.org:hooks/commit-msg .git/hooks/" to commit
-------------------------Check changes/commitment:-----------------------
-Log onto WikiMedia
-Check Changes under personal settings
-------------------------Squashing commits:-------------------------------
	--Multiple commits can be squashed into a single upload on a branch with multiple patches.--

-cd into folder of commitment (~/MathSearch)
-"git rebase -i HEAD~1"
-replace "pick" in commit message with "squash"
-"git push origin HEAD:refs/for/master" to push for review on gerrit

4/20/2015
----------------------------Configuring PHPStorm:--------------------------
	--PHPStorm is an integrated development environment for PHP, HTML, and other forms of web development. It makes life much easier. Use it to store, edit, review, and upload files.--

-Download PHPStorm and enter licence key
-Tools-->Deployment-->Configuration
-Enter local host and port number (localhost, 2222 respectively for this config file)
-Enter GERRITUSERNAME
-Link to id_rsa file (should be in .ssh folder at Home) under Private key file
-Should be finished now

6/8/2015
----------------------In case PHPStorm is dysfunctional:-----------------------
-cd into directory of PhpStorm project
-scp to create upload file to instance ("scp filename sharmaans@drmf-ecf.eqiad.wmflabs:~")
-log onto instance to verify uplaod ("drmf-ecf" or "ssh INSTANCENAME")
