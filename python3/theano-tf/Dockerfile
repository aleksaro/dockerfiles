#
# python3-theano-tf: Sets up a Docker environment for both Theano and
# TensorFlow with NVIDIA CUDA and Python 3.
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


# Install Theano
RUN pip3 install \
    git+git://github.com/Theano/Theano.git@master


# Set up .theanorc configuration file
RUN echo "[global]\ndevice=gpu0\nfloatX=float32 \
          \n\n[dnn.conv]\nalgo_fwd=time_once\nalgo_bwd_data=time_once\nalgo_bwd_filter=time_once \
          \n\n[lib]\ncnmem=0.1" \
    > /root/.theanorc


# Set default working directory and image startup command
WORKDIR "/root"
CMD ["/bin/bash"]
