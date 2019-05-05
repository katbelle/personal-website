# [Kat Belle Hartling's personal website](http://www.katbellehartling.com)

# About

## katbelle.com

My personal website is a one-page app that allows users to explore information about me and my coding life.

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

### 1. ssh into production server
```
sshpersonalwebsite
```

### 2. pull latest
```
cd personal-website
git pull
```

### 3. if new dependencies, install them:
```
pipenv install
```

### 4. restart service
```
sudo systemctl restart flask
```

# Development
This flask server runs on port 8080, make sure that port is not in use.

### 1. install dependencies
```
pipenv install
```

### 2. activate pipenv
```
pipenv shell
```

### 3. run server
```
python server.py
```

