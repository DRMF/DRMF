# Uploading and Connecting Guide

## Connecting to an instance
	An SSH key allows you to connect and communicate with a trusted server (e.g. drmf-ecf) without repeatedly re-entering passwords or other sensitive data.

1. Create an SSH key: `ssh-keygen -t rsa -C 'your_email@youremail.com'` (-C means comment; put useful info here)
2. It will then prompt you for the save location, which you want to keep as default, so just hit enter
3. It will then ask for a password. Enter a password if you want one, otherwise just hit enter
4. Run `ssh-add ~/.ssh/id_rsa` to add the key
5. Make an account (if you don't already have one) on [wikimedia](https://wikitech.wikimedia.org/wiki/Special:UserLogin/signup), and add your **PUBLIC** ssh key (**NOT PRIVATE**) on to [wikimedia](https://wikitech.wikimedia.org/wiki/Special:Preferences#mw-prefsection-openstack)
6. Sign in on [gerrit](https://gerrit.wikimedia.org/r/#/) using the same credentials as you used in wikimedia, and upload your **PUBLIC** ssh key there also
7. Now you must gain access to the wikimedia bastion. You can do this in two ways: 
 - requesting access directly through [wikimedia](https://wikitech.wikimedia.org/wiki/Special:FormEdit/Shell_Access_Request)
 - or asking our friends over at the wikimedia labs [IRC](http://webchat.freenode.net/?channels=#wikimedia-labs)
8. Once you gain access you should get a notification over on wikimedia saying something along the lines of your user rights have changed, this means you now have access to the bastion
9. Next ask whoever owns the instance you are looking to join for access to the instance. (In this case it would be [Moritz](https://github.com/physikerwelt) or [Dr.Cohl](https://github.com/HowardCohl))
10. Once you gain access you should get a notification over on wikimedia saying something along the lines of you have been added to a new group, this means you now have access to the instance
11. Add the code below the config file in the .ssh/ folder (this configures the SSH key to connect to drmf-ecf via localhosts):
```
Host bastion1.eqiad.wmflabs
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

Host INSTANCENAME
    HostName INSTANCENAME.eqiad.wmflabs
    ProxyCommand ssh -a -W %h:%p bastion2.eqiad.wmflabs
    User GERRITUSERNAME
    LocalForward 2222 localhost:22
    LocalForward 8080 localhost:80
```
*(From now on all you have to do to connect to the instance is*`ssh INSTANCENAME`*)*

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

## Committing to Gerrit:
	Gerrit is a cooperative platform which allows other users to review your code. You have locally stored commits, files you want to be reviewed, which can be pushed for review on Gerrit.

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

## Cloning Wikimedia
	 To do this you make a copy of the mediawiki vagrant, mediawiki, and the mediawiki extension you are currently working on, on your local system.

1. Run `git clone https://gerrit.wikimedia.org/r/mediawiki/vagrant` in the folder you want to make the copy
2. Run `cd vagrant` to get into the vagrant directory
3. Run `git clone https://gerrit.wikimedia.org/r/mediawiki/core` to get a copy of mediawiki itself (this may take a while, be patient, and let it finish)
4. Run `mv core mediawiki` to change the name of the the core folder to mediawiki. This is to stay in sync with the instances files
5. Run `cd mediawiki`
6. Run `cd extensions`
7. Run `git clone https://gerrit.wikimedia.org/r/mediawiki/extensions/EXTENSIONNAME` to get a copy of the extension you will be working on

## Installing PHPStorm
	PHPStorm is an integrated development environment for PHP, HTML, and other forms of web development. It makes life much easier. Use it to store, edit, review, and upload files.

1. Download the [PHPStorm file](https://www.jetbrains.com/phpstorm/download/)
2. In terminal, navigate to the directory which contains the downloaded file using the cd command (usually your downloads folder)
3. Use `tar -xvf PhpStorm-*.tar.gz` to unpack it
4. Use `cd PhpStorm-*`, and then "cd bin" to get to directory with the install file which is named PhpStorm.sh
5. Use `./phpstorm.sh` to start the install (make sure a JDK is nstalled in order to complete this task)
6. Go through the installation process, and enter your license key when prompted for it (free license keys are given for MediaWiki development)

## Configuring PHPStorm
	Configuring PHPStorm will allow to modify and upload files directly to the instance with minimal use of the terminal. It also gives a gui for git commands. You can use it to store, edit, review, and upload files. Also this will help you install the latest version of PHP.

1. [Extremly useful link](https://www.mediawiki.org/wiki/PhpStorm) which contains screenshots of each individual step
2. Make sure you have modified the config file as shown above before starting with PHPStorm
3. Also make sure you have a clone of mediawiki on your local machine (follow Cloning Mediawiki as shown above)
4. Go to File-->Settings-->Build, Execution, Deployment-->Deployment
5. Click [+] and create a new Server with a meaningful name and type SFTP
6. Put the following information in the correct places:
 - SFTP host:         localhost (or 127.0.0.1, they are equivalent. whatever floats your boat)
 - Port:              2222
 - Root Path:         /
 - Username:          SHELLNAME
 - Auth type:         Key pair
 - PRIVATE Key file:  link is by default in /home/USERNAME/.ssh/id_rsa
 - Passphrase:        your ssh key password you created when generating your ssh key
7. Press test SFTP connection to make sure it successfully connects to localhost, if it doesn't, refer to [In case PHPStorm is dysfunctional](https://github.com/DRMF/DRMF/blob/master/doc/upload_and_connect.MD#in-case-phpstorm-is-dysfunctional)
8. Go to the mappings tab
 - Local path:                                  navigate to where your local copy vagrant is on your computer
 - Deployment path on server 'meaningful name': navigate to where your instance has a copy of the vagrant

## Installing PHP
1. Download the PHP source code from [here](http://php.net/distributions/php-5.6.10.tar.gz)
2. Run `tar -xvf php-5.6.10.tar.gz` to unpack the PHP source code
3. Run `cd php-5.6.10` to get into the correct directory
4. Run `./configure && make && make install` to completely install PHP
5. In PHPStorm, go to File-->Settings-->Languages & Frameworks-->PHP, and click the `...` next to Interpreter
6. Click the [+]:
 - Name:           something meaningful like, for example, php-installation-5.6.10
 - PHP executable: link to the PHP executable which should be located in WHEREYOUINSTALLEDPHP/sapi/cli/php
7. Click Apply then OK
8. Put this information in the correct places:
 - PHP language level: 5.6
 - Interpreter:        whatever you named it (for example, php-installation-5.6.10)

## Using PHPStorm to create a local server to test PHP files
1. Hit Shift+Alt+F10 and click on Edit Configurations
2. Click [+]:
 - Name: Something meaningful, for example, Web server
 - Host: localhost (or 127.0.0.1, they are equivalent. Whatever floats your ship)
 - Port: 1234 (technically any port should work, just make sure the port isn't being used by anything else)
 - Document Root: link to wherever you want to run your files from
3. Click Apply and close the window
4. Hit Shift+Alt+F10 again, except this time hit on whatever you named it (for example, Web server)
5. You should now be able to go to your browser and go to localhost:1234/example.php

## In case PHPStorm is dysfunctional
- If when trying to test SFTP server, it says 'Algorithm negotiation fail' you need to replace the jsch-0.1.50.jar file in the PHPStorm installation
 - Download [jsch.jar](http://www.svrnm.de/files/jsch.jar)
 - Navigate to your PHPStorm installation, and go into the lib directory
 - Look for the jsch-*.jar and rename the downloaded file to match the name of that file
 - Delete the old version of jsch-*.jar and put in the new downloaded file
 - Check if the 'Algorithm negotiation fail' problem persists. If it does google your woes
 
- If it says that your git version is outdated, simply just update git, [help guide](http://stackoverflow.com/questions/4039416/installing-git-with-non-root-user-account)
 - Clone the source code by running `git clone https://github.com/git/git`
 - Then run `make configure && ./configure --prefix=/home/user/myroot && make && make install` to completely install git (`&&` links together commands)
 - In PHPStorm, go to Settings-->Version Control-->Git, and link to the execuatble git file located in the place you have installed git

- Google your woes -- could potentially be a bug in the software (for instance, a fault in the /lib/jsch-0.1-50.jar file: [Link](http://www.svrnm.de/blog/fixed-netbeans-phpstorm-algorithm-negotiation-fail/))

 
