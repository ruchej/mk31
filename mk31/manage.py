#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import pymysql
pymysql.install_as_MySQLdb()

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mk31.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Не могу импортировать Джанго. Вы уверены, что он установлен и "
                "доступен в переменной окружения PYTHONPATH? Ты "
                "забыл активировать виртуальную среду?"
            )
        raise
    execute_from_command_line(sys.argv)
