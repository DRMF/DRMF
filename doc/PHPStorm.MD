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
