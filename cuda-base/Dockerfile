#
# cuda-base: Sets up a boilerplate Docker environment for NVIDIA CUDA.
#

# Base image is CUDA + cuDNN from nvidia-docker
FROM nvidia/cuda:7.5-cudnn4-devel


MAINTAINER Aleksander Rognhaugen


# Install basic programs and dependencies
RUN apt-get update && apt-get install -y \
        build-essential \
        byobu \
        cmake \
        curl \
        g++ \
        gcc \
        gfortran \
        git \
        make \
        nano \
        pkg-config \
        rsync \
        unzip \
        wget

# Cleanup apt-get
RUN apt-get clean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*


# Set default working directory and image startup command
WORKDIR "/root"
CMD ["/bin/bash"]
