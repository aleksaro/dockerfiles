.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://github.com/senbon/dockerfiles/blob/master/LICENSE

===========
dockerfiles
===========

A compilation of Dockerfiles for personal use with automated builds enabled on
`Docker Hub`_. Most of the images are made with machine learning on GPUs in
mind. CUDA enabled images use the NVIDIA CUDA base image at `NVIDIA Docker`_.


Notice
======

The Dockerfiles and associated images for ``aleksaro/python2-base``,
``aleksaro/python3-theano``, ``aleksaro/python3-tf``, ``aleksaro/python3-theano-tf``,
and ``aleksaro/python3-nn`` have been deprecated in favour of ``aleksaro/python3-ml``.

Theano is no longer installed by default.


Usage
=====

Before doing anything, make sure that you have `Docker`_ Engine and optionally
`NVIDIA Docker`_ installed. Read more about Docker on the official
`Docker Docs`_.


Automated builds
----------------

With the automated builds enabled the simplest way to make use of these images
is to run either the ``nvidia-docker run`` or ``docker run`` command. It is
recommended to use ``nvidia-docker`` when working with GPUs because it
simplifies the act of adding host GPU devices to the container. Running one of
the images from Docker Hub and opening a terminal can be achieved by performing
the following command:

.. code-block:: bash

  nvidia-docker run -it aleksaro/<image name[:tag]>

When running multiple GPUs it might be useful to isolate the GPUs you want by
using the environment variable ``NV_GPU``, e.g. ``NV_GPU=0 nvidia-docker ...``.
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


What next?
==========

The Dockerfiles in this repository are sparse by design and will most likely
not contain all of the packages a regular user may want. To install any
remaining packages, set up configuration files, expose ports, and so on, we
recommend creating another Dockerfile on top of one of the more general
Dockerfiles. Below is an example of one such user-level Dockerfile containing
`Keras`_:

.. code-block:: bash

  FROM aleksaro/python3-ml:8.0-cudnn6-ubuntu16.04

  # Install Keras
  RUN pip3 install \
      git+git://github.com/fchollet/keras.git@$master

  WORKDIR "/root"
  CMD ["/bin/bash"]

Depending on the situation, it may be appropriate to build these locally.

Take a look at `senbon/user-dockerfiles`_ for more details on how to create
user-level Dockerfiles.


Acknowledgements
================

The main inspiration for these Dockerfiles is `Kaixhin`_. Please have a look at
their GitHub page for a slew of general Dockerfiles.


.. Links

.. _Docker Hub: https://hub.docker.com/u/aleksaro/
.. _NVIDIA Docker: https://github.com/NVIDIA/nvidia-docker
.. _Docker: https://www.docker.com/
.. _Docker Docs: https://docs.docker.com/
.. _NVIDIA Docker wiki: https://github.com/NVIDIA/nvidia-docker/wiki
.. _shared volumes: https://docs.docker.com/engine/tutorials/dockervolumes/
.. _Keras: https://github.com/fchollet/keras
.. _senbon/user-dockerfiles: https://github.com/senbon/user-dockerfiles
.. _Kaixhin: https://github.com/Kaixhin/dockerfiles
