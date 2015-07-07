---
layout: page
title: Install
---

# Installing

I highly recommend you create a new virtual environment before proceeding.

If you have virtualenvwrapper installed you can do so like this:
```bash
# Type the following to create a virtual env.
# The example env is called 'dentalenv'.
$ mkvirtualenv dentalenv

# It should activate after creating it.
(dentalenv)$

```

## Install Requirements

You can do so by navigating to the repository root (dentaldev) and typing the following:
```bash
(dentalenv)$ pip install -r requirements.txt
```

## Configuring Settings

### Which Settings Does Django Load?

Because of how the settings are configured, you should let Django know what settings file to load when running. To do so, you must set an environment variable called `DJANGO_SETTINGS_MODULE`.

Below is an example on how to configure the variable if you are using the default `development` settings:
```bash
(dentalenv)$ vi $VIRTUAL_ENV/bin/postactivate
```
Proceed to edit the file using `vi` or your preferred text editor:
```bash
#!/bin/bash
# This hook is sourced after this virtualenv is activated.

export DJANGO_SETTINGS_MODULE='settings.expedientedental.development'
```
You must also `unset` the variable in the `predeactivate` file:
```bash
#!/bin/bash
# This hook is sourced before this virtualenv is deactivated.

unset DJANGO_SETTINGS_MODULE
```
For the changes to take place, run `deactivate` in your terminal, then activate it again by running `workon dentalenv` or `source /path/to/virtual/env/bin/activate`.

### Database and Secret Key

The settings file looks for a file named `cfg.json` in your project root. Below is an example configuration file:

```json
{
    "FILENAME": "cfg.json",
    "SECRET_KEY": "baconislife",
    "DATABASE": {
        "NAME": "dentaldb",
        "USER": "root",
        "PASSWORD": "root",
        "HOST": "localhost"
    }
}
```

### Personal Settings File

But what if you want to have your own settings file and add custom apps or change other configuration? Please don't do any of this in `development.py`! Create your own settings file and **DO NOT** .gitignore it.

```python
# john-dev.py - john's settings file
INSTALLED_APPS += (
    'debug_toolbar',
)
```

To load your settings, configure it in the environment variable:
```bash
#!/bin/bash
# This hook is sourced after this virtualenv is activated.

export DJANGO_SETTINGS_MODULE='settings.expedientedental.john-dev'
```

## Install Fixtures

Fixtures, or 'dummy data' are provided to you in the repository root in a file named `testdata.json`. To install it use Django's `loaddata`.

To run `loaddata` you must be in the project's directory:
```bash
# Go into the project's directory:
(dentalenv)$ cd expedientedental
(dentalenv)$ python manage.py loaddata ../testdata.json
Installed 130 object(s) from 1 fixture(s)
```
**Heads up** - Please note that the number of installed objects may vary.

## Run!

If everything goes as it should, you only need to type this:
```bash
(dentalenv)$ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
July 07, 2015 - 09:01:35
Django version 1.8.2, using settings 'expedientedental.settings.development'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## Common Problems

You should encounter the most problems when installing the requirements and their dependencies. Head over to the [documentation](http://dental.github.io) and read the detailed list of requirements and their dependencies.

For any other kind of problem, feel free to contact me via twitter ([@andiosuna](https://twitter.com/andiosuna)) or open an issue. Please read the [contributing guidelines]({{ site.baseurl }}/contributing) before doing so!
