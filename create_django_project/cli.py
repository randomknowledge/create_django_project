#!/usr/bin/env python
# coding: utf-8
import os
import sys


def create_virtualenv(target_directory):
    print("Creating virtualenv...")
    os.chdir(target_directory)
    cmd = "virtualenv{0} virtualenv".format(" --system-site-packages" if os.name == 'nt' else '')
    if os.system(cmd) == 0:
        print("done.")
        sys.exit(0)
    else:
        sys.exit(1)


def usage():
    print "Usage: {0} <project name>".format(os.path.basename(sys.argv[0]).partition('.')[0])
    sys.exit(0)


def main():
    if len(sys.argv) != 2:
        usage()

    cmd = "django-admin.py startproject --template=https://github.com/randomknowledge/"\
          "django_project_template/zipball/master --extension=py,md,gitignore,txt,conf,yml "\
          "{0}".format(sys.argv[1])

    target_directory = os.path.abspath(
        os.path.join(
            os.getcwd(),
            sys.argv[1],
        )
    )

    sys.stdout.write("Creating Project {0}...".format(sys.argv[1]))
    if os.system(cmd) == 0:
        sys.stdout.write(" done.\n")
        create_virtualenv(target_directory)
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()
