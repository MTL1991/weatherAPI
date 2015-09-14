#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    if os.environ.get('HEROKU_ENV'):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weathersite.settings.production")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weathersite.settings.local")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
