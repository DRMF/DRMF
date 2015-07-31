# Uploading and Connecting Guide
######This guide contains a brief set of instructions for only certain problems. For a more in depth guide, in which you can learn more about what you are actually doing, visit ["How to become a MediaWiki hacker"](https://www.mediawiki.org/wiki/How_to_become_a_MediaWiki_hacker)

## SSH
	This part of the guide contains information on connecting to you instance
[Connecting to an Instance](https://github.com/DRMF/DRMF/blob/master/doc/The%20SSH%20Guide.MD#connecting-to-your-instance)

## Git, Gerrit, and GitHub
	Blah, Blah, Blah
[Initial Setup for Git](https://github.com/DRMF/DRMF/blob/master/doc/Git%2C%20Gerrit%2C%20GitHub.MD#initial-setup-for-git)

[Keeping your local repository updated](https://github.com/DRMF/DRMF/blob/master/doc/Git%2C%20Gerrit%2C%20GitHub.MD#keeping-your-local-repository-updated)

[Committing to Gerrit](https://github.com/DRMF/DRMF/blob/master/doc/Git%2C%20Gerrit%2C%20GitHub.MD#committing-to-gerrit)

[Check changes on gerrit](https://github.com/DRMF/DRMF/blob/master/doc/Git%2C%20Gerrit%2C%20GitHub.MD#check-changes-on-gerrit)

[Squashing commits](https://github.com/DRMF/DRMF/blob/master/doc/Git%2C%20Gerrit%2C%20GitHub.MD#squashing-commits)

[Commiting to GitHub](https://github.com/DRMF/DRMF/blob/master/doc/Git%2C%20Gerrit%2C%20GitHub.MD#commiting-to-github)


## DRMF-Specfic Information
	 Blah, blah, blah
[Cloning Wikimedia](https://github.com/DRMF/DRMF/blob/master/doc/DRMF-Specific%20Information.MD#cloning-wikimedia)

[Retrieving the formula page indexes](https://github.com/DRMF/DRMF/blob/master/doc/DRMF-Specific%20Information.MD#retrieving-the-formula-page-indexes)

[Installing, Configuring, and Running MathWeb Search](https://github.com/DRMF/DRMF/blob/master/doc/DRMF-Specific%20Information.MD#installing-configuring-and-running-mathweb-search)

[Installing and Running BaseX Search](https://github.com/DRMF/DRMF/blob/master/doc/DRMF-Specific%20Information.MD#installing-and-running-basex-search)

[How to import the DRMF database to your DRMF instance](https://github.com/DRMF/DRMF/blob/master/doc/DRMF-Specific%20Information.MD#how-to-import-the-drmf-database-to-your-drmf-instance)


## PHPStorm
	Blah, blah, blah
[]()

[]()

[]()

[]()



## Tips on How to avoid accidently `sudo`ing on your local machine
###If you are working at NIST or for any other high security facility, chances are, you are not allowed to run commands as root via `sudo`
However, a lot of the setting up and uploading and connecting in this guide requires you to `sudo` inside of ** your** instance. **NOT THE LOCAL MACHINE!**
> I repeat, using `sudo` on a NIST computer can and will get you in a lot of trouble (I know from experience) so you cannot use it. 

One way to avoid accidently `sudo`ing in your machine when you meant to do it on your instance is to create an alias on your instance so that everytime you type in that alias the `sudo` command is actually being implement.

In my case, I made the alias for `sudo` be `doit`
Follow [this](http://stefaanlippens.net/my_bashrc_aliases_profile_and_other_stuff) to make an alias **on your instance** that way you never have to type `sudo` both on your instance and your local machine but typing `doit` will act as a `sudo` alias only when you type it into your instance. 
Therefore if you accidently `doit` on your machine nothing will happen because no alias for `doit` exist. 
