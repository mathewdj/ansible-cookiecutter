import os
import sys

show_license = {{cookiecutter.show_license}}

if not show_license:
    os.remove('LICENSE')