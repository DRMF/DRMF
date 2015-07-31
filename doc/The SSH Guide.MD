## Connecting to your instance
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
