#
# python3-nn: Sets up a Docker environment with a slew of artificial neural
# network libraries with NVIDIA CUDA and Python 3: Theano and TensorFlow.
#

# Base image is python-ml
FROM aleksaro/python3-ml:8.0-cudnn5-ubuntu16.04


LABEL maintainer "Aleksander Rognhaugen"


# Specify TensorFlow version
ARG TF_VERSION=0.12.1


# Install TensorFlow
RUN pip3 install --upgrade \
    https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-${TF_VERSION}-cp35-cp35m-linux_x86_64.whl


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
