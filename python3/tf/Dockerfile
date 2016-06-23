#
# python3-tf: Sets up a Docker environment for TensorFlow with NVIDIA CUDA and
# Python 3.
#

# Base image is python-ml
FROM aleksaro/python3-ml:7.5-cudnn4


MAINTAINER Aleksander Rognhaugen


# Specify TensorFlow version
ARG TF_VERSION=0.9.0rc0


# Install TensorFlow
RUN pip3 install --upgrade \
    https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-${TF_VERSION}-cp34-cp34m-linux_x86_64.whl


# At the time when this Dockerfile was made Tensorflow tries to open libcuda.so
# instead of libcuda.so.1 which means we have to set up the following symbolic
# links:
RUN ln -s /usr/local/nvidia/lib64/libcuda.so.1 /usr/lib/x86_64-linux-gnu/libcuda.so
# See: https://github.com/tensorflow/tensorflow/issues/808#issuecomment-180228698


# Set default working directory and image startup command
WORKDIR "/root"
CMD ["/bin/bash"]
