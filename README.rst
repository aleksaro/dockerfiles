.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://github.com/aleksaro/dockerfiles/blob/master/LICENSE

===========
dockerfiles
===========

A compilation of Dockerfiles for personal use with automated builds enabled on
`Docker Hub`_. The images are made with machine learning on GPUs in mind. CUDA
enabled images use the NVIDIA CUDA base image at `NVIDIA Docker`_.


Notice
======

The Dockerfiles and associated images for ``aleksaro/python2-base``,
``aleksaro/python3-theano``, ``aleksaro/python3-tf``,
``aleksaro/python3-theano-tf``, ``aleksaro/python3-nn``,
``aleksaro/python3-ml``, and ``aleksaro/python3-base`` have been deprecated in
favour of ``aleksaro/data-science``.


Usage
=====

Before doing anything, make sure that you have `Docker`_ Engine and
`NVIDIA Docker`_ installed. Read more about Docker on the official
`Docker Docs`_.


Automated builds
----------------

With the automated builds enabled the simplest way to make use of these images
is to run the ``docker run --runtime=nvidia ...`` command. Running one of
the images from Docker Hub and opening a terminal can be achieved by performing
the following command:

.. code-block:: bash

  docker run --runtime=nvidia -it aleksaro/<image name[:tag]>

When running multiple GPUs it might be useful to isolate the GPUs you want by
using the environment variable ``NVIDIA_VISIBLE_DEVICES``. For example:

.. code-block:: bash

  docker run --runtime=nvidia -e NVIDIA_VISIBLE_DEVICES=0 -it aleksaro/<image name[:tag]>

More information about this and more can be found on the `NVIDIA Docker wiki`_.


Local builds
------------

The Dockerfiles can, of course, also be built locally using the ``docker build``
command, e.g.:

.. code-block:: bash

  docker build -t <name[:tag]> -f <Name of Dockerfile> PATH


Shared volumes
--------------

Shared volumes can be used to read and write data from the host machine within
a docker container. For example, three common use cases for machine learning
include reading datasets, reading code, and writing trained model parameters.

Volumes are bound to the docker container using the ``-v`` option when running
a Docker image. Read more about how to use `shared volumes`_ on the Docker Docs.


Acknowledgements
================

The main inspiration for these Dockerfiles is `Kaixhin`_. Please have a look at
their GitHub page for a slew of general Dockerfiles.

Part of the code is borrowed from `Jupyter dockerstacks`_ (see
``/base-notebook``). A copy of the relevant license can be found in the ``/3rd-part-licenses``
directory.


.. Links

.. _Docker Hub: https://hub.docker.com/u/aleksaro/
.. _NVIDIA Docker: https://github.com/NVIDIA/nvidia-docker
.. _Docker: https://www.docker.com/
.. _Docker Docs: https://docs.docker.com/
.. _NVIDIA Docker wiki: https://github.com/NVIDIA/nvidia-docker/wiki
.. _shared volumes: https://docs.docker.com/storage/volumes/
.. _Kaixhin: https://github.com/Kaixhin/dockerfiles
.. _Jupyter dockerstacks: https://github.com/jupyter/docker-stacks
