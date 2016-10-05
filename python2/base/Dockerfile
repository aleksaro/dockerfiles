#
# python2-base: Sets up a boilerplate Docker environment for NVIDIA CUDA with
# Python 2 and OpenBLAS. The main use of this Dockerfile is as an intermediate
# step for setting up scientific frameworks with Python.
#

# Base image is cuda-base
FROM aleksaro/cuda-base:7.5-cudnn5


MAINTAINER Aleksander Rognhaugen


# Install basic packages and miscellaneous dependencies
RUN apt-get update && apt-get install -y \
    liblapack-dev \
    libopenblas-dev \
    libzmq3-dev \
    python \
    python-dev \
    python-pip \
    python-setuptools \
    python-tk


# Install Pillow (PIL) dependencies
RUN apt-get update && apt-get install -y \
    libfreetype6-dev \
    libjpeg8-dev \
    liblcms2-dev \
    libopenjpeg2 \
    libpng12-dev \
    libtiff5-dev \
    libwebp-dev \
    zlib1g-dev


# Cleanup apt-get
RUN apt-get clean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*


# Upgrade pip and setuptools
RUN pip install --upgrade \
    setuptools \
    pip


# Install basic Python packages (some of these may already be installed)
RUN pip install \
    wheel \
    six \
    ipython \
    jupyter \
    ipdb \
    numpy \
    Pillow \
    scipy \
    matplotlib


# Prepare matplotlib font cache
RUN python -c "import matplotlib.pyplot"


# Set default working directory and image startup command
WORKDIR "/root"
CMD ["/bin/bash"]
