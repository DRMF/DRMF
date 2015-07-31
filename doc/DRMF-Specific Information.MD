## Cloning Wikimedia
	 To do this you make a copy of the mediawiki vagrant, mediawiki, and the mediawiki extension you are currently working on, on your local system.

1. Run `git clone https://gerrit.wikimedia.org/r/mediawiki/vagrant` in the folder you want to make the copy
2. Run `cd vagrant` to get into the vagrant directory
3. Run `git clone https://gerrit.wikimedia.org/r/mediawiki/core` to get a copy of mediawiki itself (this may take a while, be patient, and let it finish)
4. Run `mv core mediawiki` to change the name of the the core folder to mediawiki. This is to stay in sync with the instances files
5. Run `cd mediawiki`
6. Run `cd extensions`
7. Run `git clone https://gerrit.wikimedia.org/r/mediawiki/extensions/EXTENSIONNAME` to get a copy of the extension you will be working on

## Retrieving the formula page indexes
	For use with either of the search engines (BaseX or MathWeb)
	
1. cd into your MathSearch extension directory
2. Run `mkdir indexes` to make the folder in which you will store the indexs
3. Run `cd maintainence` to get into the maintainence folder
4. Run `php CreateMWSHarvest.php ../indexes/ 1000000000 --mwsns="mws:"` to actaully create the file with the indexes (it is located in .../MathSearch/index/math*.xml)

## Installing, Configuring, and Running MathWeb Search
	Use https://github.com/KWARC/mws for further documentation

1. Run `sudo add-apt-repository ppa:radu-hambasan/math-web-search`
2. Run `sudo apt-get install mws`
3. Run `sudo mws-config create -p 9090 -i /vagrant/mediawiki/extensions/MathSearch/indexes wiki -- -e "xml"` This creates a config 
4. Run `sudo mws-config enable wiki`

## Installing and Running BaseX Search
	Use https://github.com/TU-Berlin/mathosphere/blob/master/README.md and https://github.com/TU-Berlin/mathosphere/blob/master/restd/readme.md

1. Run `git clone https://github.com/TU-Berlin/mathosphere.git` to get the mathosphere backend
2. Run `cd mathoshpere` to get into the correct directory
3. Run `git submodule init && git submodule update`
4. Run `cd /your/path/to/mathosphere/restd`
5. Run `mvn clean install`
6. Run `mvn exec:java -Drestx.http.XForwardedSupport=all -Dpassword=mathosphere -Dpath=/your/path/to/the/index/file` this will launch a BaseX server

## How to import the DRMF database to your DRMF instance

1. ssh into your instance (e.g. `ssh drmf-ecf`)
2. change directories to the where the sql database is located (`cd /data/project/wdump`)
3. Type in `ls` to see the files in the directory. There should be a file that looks like this: YEAR-MONTH-DAY-drmf.sql
    The specific file I had was `2015-07-18.sql` but yours will be a more up to  date version.  
4. Type in `mysql -u root -pvagrant wiki <2015-07-18-drmf.sql`
This will run a mysql command with user root and pass vagrant on the wiki database and put the sql file into it.
5. refresh your website (e.g. drmf-ecf.wmflabs.org)
