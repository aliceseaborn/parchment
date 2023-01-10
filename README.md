# Parchment

An internal documentation system, designed and intended for internal project tracking. 


## Table of Contents
- [Background](#background)
- [Usage](#usage)
- [Deployment](#deployment)


## [Background](#table-of-contents)

Parchment is a sphinx documentation project using the PyData template and ReStructuredText files. Additional scripts have been written to automatically format the docs and create the index listings.


## [Usage](#table-of-contents)

1. Navigate to the project directory and build the application.
```BASH
cd project/
make clean && make html
```

2. Navigate to the html source and serve it locally.
```BASH
cd build/html && python3 -m http.server
```

3. Criticize. Backtrack. Change. Rebuild. Repeat.


## [Deployment](#table-of-contents)

Ideally, Parchment is deployed to a server which automatically fetches the latest remote source and rebases the local repository at the top of every hour. The server should then build the html files from scratch and copy them to the server webroot where they can be served for public consumption.

This deployment method requires that the server have unrestricted read access to the remote Parchment repository. When the server attempts to fetch the latest remote source, it must use an ssh key which does not pause to prompt for a password. Since this password-less ssh key presents a security vulnerability, it must be constrained to only the Parchment repo and must be limited to read-only access. This arrangement is achieved through GitHub deploy keys.

On the Parchment server, a new ssh key is created using `ssh-keygen` and a password is not set for the key pair. The public key is then uploaded to GitHub as a [new deploy key](https://github.com/aliceseaborn/parchment/settings/keys) with read-only access. To ensure that git uses this ssh key, create an alias in `~/.ssh/config` for Parchment that selects the private key used for this deployment.
```GITCONFIG
Host parchment
  Hostname github.com
  IdentityFile /home/seaborn/.ssh/id_parchment_git
```

Then reset the origin to point to the alias instead of `github.com` proper. When the origin is set to an alias, the ssh key used for the transaction is provided by the ssh configuration and not the git preferences.
```BASH
$ git remote set-url origin git@parchment:aliceseaborn/parchment.git
$ git remote show origin
* remote origin
  Fetch URL: git@parchment:aliceseaborn/parchment.git
  Push  URL: git@parchment:aliceseaborn/parchment.git
  ...
```

Lastly, the server must be configured to run the `Makefile` every hour. To achieve this task, we set up the following cron job. Note that the `make` command is instructed to change directory to the Parchment repo before commencing its make routine.
```
0 * * * * make -C /opt/medusa/parchment/project/ all
```

The server is now configured for Parchment deployment and will automatically update itself at the top of every hour in perpetuity.


*Written by alice seaborn.*
