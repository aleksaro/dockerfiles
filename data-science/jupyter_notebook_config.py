#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# jupyter_notebook_config.py: Sets up miscellaneous options for Jupyter
# notebooks such as port and a self-signed certificate.
#
#   # Copyright (c) Jupyter Development Team.
#   # Distributed under the terms of the Modified BSD License.
#
import os

from jupyter_core.paths import jupyter_data_dir


# Set PEM_FILE location
PEM_FILE = os.path.join(jupyter_data_dir(), "notebook.pem")


# Get Jupyter config
c = get_config()  # NOQA

# Set miscellaneous notebook options
c.NotebookApp.ip = "0.0.0.0"
c.NotebookApp.port = 8888
c.NotebookApp.open_browser = False

# https://github.com/jupyter/notebook/issues/3130
c.FileContentsManager.delete_to_trash = False

# Set up a self-signed certificate if `USE_HTTPS` is set to any value as an
# environment variable, e.g. docker run ... -e "USE_HTTPS=1" ...
if "USE_HTTPS" in os.environ:
    if not os.path.isfile(PEM_FILE):
        import errno
        import stat
        import subprocess

        # Ensure PEM_FILE directory exists
        dir_name = os.path.dirname(PEM_FILE)
        try:
            os.makedirs(dir_name)
        except OSError as ex:
            if ex.errno == errno.EEXIST and os.path.isdir(dir_name):
                pass
            else:
                raise

        # Generate self-signed certificate
        subprocess.check_call(
            [
                "openssl",
                "req",
                "-new",
                "-newkey",
                "rsa:2048",
                "-days",
                "365",
                "-nodes",
                "-x509",
                "-subj",
                "/C=XX/ST=XX/L=XX/O=generated/CN=generated",
                "-keyout",
                PEM_FILE,
                "-out",
                PEM_FILE,
            ]
        )

        # Restrict access to PEM_FILE
        os.chmod(PEM_FILE, stat.S_IRUSR | stat.S_IWUSR)

    # Specify certfile location for Jupyter notebook
    c.NotebookApp.certfile = PEM_FILE
