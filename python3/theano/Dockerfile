#
# python3-theano: Sets up a Docker environment for Theano with NVIDIA CUDA and
# Python 3.
#

# Base image is python-ml
FROM aleksaro/python3-ml:7.5-cudnn5


MAINTAINER Aleksander Rognhaugen


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
