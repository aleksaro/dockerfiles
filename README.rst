===========
dockerfiles
===========

A compilation of Dockerfiles for personal use with automated builds enabled on
`Docker Hub`_. Most of the images are made with machine learning on GPUs in
mind. CUDA enabled images use the NVIDIA CUDA base image at `NVIDIA Docker`_.


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
`Keras`_ and `Lasagne`_:

.. code-block:: bash

  FROM aleksaro/python3-theano-tf:7.5-cudnn4

  # Install Keras
  RUN pip3 install \
      git+git://github.com/fchollet/keras.git@$master

  # Install Lasagne
  RUN pip3 install \
      git+git://github.com/Lasagne/Lasagne.git@$master

  WORKDIR "/root"
  CMD ["/bin/bash"]

Depending on the situation, it may be appropriate to build these locally.


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
.. _shared volumes: https://docs.docker.com/engine/userguide/containers/dockervolumes/
.. _Keras: https://github.com/fchollet/keras
.. _Lasagne: https://github.com/Lasagne/Lasagne
.. _Kaixhin: https://github.com/Kaixhin/dockerfiles
