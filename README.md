MIGRATION ERROR CODE
====================

This code is to reproduce an intermittent migration error we've been getting.

To run it:
- create and activate a virtual environment
- pip install --upgrade pip
- pip install -r requirements.txt
- create a postgresql database and update the settings
- python manage.py test -v 2

We've been getting the following error on the 0008\_auto migration:

django.db.utils.ProgrammingError: constraint "polls\_questioncontribution\_base\_question\_id\_25bfb2a8\_fk" for relation "polls\_questioncontribution" already exists

Note: the error is intermittent - it may work fine sometimes.

Note: I tried it on sqlite, but didn't see it fail there.

The code seems to work fine on Django 3.2 - the migrations complete successfully. I dumped the sqlmigrate output from Django 3.2 and Django 4.0.1 - you can see the output in 0008\_sql\_django32 and 0008\_sql\_django4. It looks like Django 4.0.1 (sometimes) creates duplicate SQL statements.

I ran git bisect on the Django code, and it pointed to https://github.com/django/django/commit/3d9040a50b160f8b4bb580e09f4120d4979fe29e as the commit where the problem first showed up.
