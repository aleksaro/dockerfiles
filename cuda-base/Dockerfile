#
# cuda-base: Boilerplate Docker environment for GPU computing with NVIDIA CUDA.
#

# Base image is CUDA from NVIDIA
FROM nvidia/cuda:10.0-base-ubuntu18.04


LABEL maintainer "Aleksander Rognhaugen"


# Install CUDA tools, various dependencies and programs
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        cmake \
        cuda-command-line-tools-10-0 \
        cuda-cublas-10-0 \
        cuda-cufft-10-0 \
        cuda-curand-10-0 \
        cuda-cusolver-10-0 \
        cuda-cusparse-10-0 \
        libcudnn7=7.4.1.5-1+cuda10.0 \
        libfreetype6-dev \
        libhdf5-serial-dev \
        libjpeg-dev \
        liblapack-dev \
        liblcms2-dev \
        libopenblas-dev \
        libpng-dev \
        libtiff-dev \
        libwebp-dev \
        libzmq3-dev \
        locales \
        pkg-config \
        software-properties-common


# Install basic programs
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        byobu \
        curl \
        git \
        htop \
        nano \
        rsync \
        unzip \
        vim \
        wget


# Cleanup apt-get
RUN apt-get clean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*


# Set default working directory and image startup command
WORKDIR "/root"
CMD ["/bin/bash"]
