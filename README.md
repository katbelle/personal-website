# [Kat Belle Hartling's personal website](http://www.katbellehartling.com)

# About

katbelle.com

My personal website is a one-page app that allows users to explore information about me and my coding life.  The site has not yet been deployed.

# Preview

![Preview](/static/gif/kats_website.gif)

# Tech Stack

* Python
* Flask
* Javascript
* jQuery
* Jinja
* HTML
* CSS
* Bootstrap

# Deployment
Until a code deployment manager is added, here are the manual steps:

## 1. ssh into production server
```
sshpersonalwebsite
```

## 2. pull latest
```
cd personal-website
git pull
```

## 3. if new dependencies, install them:
```
source env/bin/activate
pip3 install -r requirements.txt
```

## 4. restart service
```
sudo systemctl restart flask
```
