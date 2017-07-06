#!/usr/bin/env python
import os
import sys
# 1.0导入pymysql包
import pymysql
pymysql.install_as_MySQLdb()


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DailyFresh.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
