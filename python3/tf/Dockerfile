#
# python3-tf: Sets up a Docker environment for TensorFlow with NVIDIA CUDA and
# Python 3.
#

# Base image is python-ml
FROM aleksaro/python3-ml:8.0-cudnn5


MAINTAINER Aleksander Rognhaugen


# Specify TensorFlow version
ARG TF_VERSION=0.12.1


# Install TensorFlow
RUN pip3 install --upgrade \
    https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-${TF_VERSION}-cp34-cp34m-linux_x86_64.whl


# Set default working directory and image startup command
WORKDIR "/root"
CMD ["/bin/bash"]
