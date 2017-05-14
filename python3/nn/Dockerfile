#
# python3-nn: Sets up a Docker environment with a slew of artificial neural
# network libraries with NVIDIA CUDA and Python 3: Theano and TensorFlow.
#

# Base image is python-ml
FROM aleksaro/python3-ml:8.0-cudnn5-ubuntu16.04


LABEL maintainer "Aleksander Rognhaugen"


# Install TensorFlow
RUN pip3 install --upgrade tensorflow-gpu


# Install Cython
RUN pip3 install --upgrade Cython


# Download and compile libgpuarray
RUN cd /root && \
    git clone https://github.com/Theano/libgpuarray.git && cd ./libgpuarray && \
    mkdir ./build && cd build && \
    cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr && \
    make -j"$(nproc)" && make install


# Install pygpu
RUN cd /root/libgpuarray && \
    python3 setup.py build_ext -L /usr/lib -I /usr/include && \
    python3 setup.py install


# libgpuarray cleanup
RUN rm -rf /root/libgpuarray


# Install Theano
RUN pip3 install \
    git+git://github.com/Theano/Theano.git@master


# Set up .theanorc configuration file
RUN echo "[global]\ndevice=cuda0\nfloatX=float32\noptimizer_including=cudnn \
          \n\n[dnn.conv]\nalgo_fwd=time_once\nalgo_bwd_data=time_once\nalgo_bwd_filter=time_once \
          \n\n[lib]\ncnmem=0.1" \
    > /root/.theanorc


# Set default working directory and image startup command
WORKDIR "/root"
CMD ["/bin/bash"]
