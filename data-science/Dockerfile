#
# data-science: Boilerplate Docker environment for data science with Python on
# the GPU with NVIDIA CUDA.
#

# Base image is `cuda-base`
FROM aleksaro/cuda-base:latest


LABEL maintainer "Aleksander Rognhaugen"


ARG PYTHON_VERSION=3.6
ARG CONDA_ENV=py36


# For CUDA profiling, TensorFlow requires CUPTI.
# https://github.com/tensorflow/tensorflow/tree/master/tensorflow/tools/dockerfiles
ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH


# Set correct locale for locale-aware programs or libraries
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8


# Add Miniconda3 to PATH
ENV PATH /opt/conda/bin:$PATH


# Set up byobu prompt
RUN echo "[ -r /root/.byobu/prompt ] && . /root/.byobu/prompt" >> /root/.bashrc


# Set up Python with Miniconda3
RUN curl -o ~/miniconda.sh -O  https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh  && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda update --yes conda && \
    /opt/conda/bin/conda update --yes --all && \
    /opt/conda/bin/conda clean -tipsy && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh


# Create default conda environment
RUN conda create --no-default-packages --yes \
    -n ${CONDA_ENV} python=${PYTHON_VERSION} && \
    conda clean -tipsy && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> /root/.bashrc && \
    echo "conda activate ${CONDA_ENV}" >> /root/.bashrc


# Dummy activation
ENV PATH /opt/conda/envs/${CONDA_ENV}/bin:$PATH


# Install basic Python packages
RUN pip install --upgrade --no-cache-dir \
    six \
    Cython \
    nose \
    ipython \
    jupyter \
    ipdb \
    numpy \
    Pillow \
    imageio \
    scipy \
    matplotlib


# Install general-purpose libraries useful for machine learning in Python
RUN pip install --upgrade --no-cache-dir \
    h5py \
    git+git://github.com/vicolab/ml-pyxis.git@$master \
    PyYAML \
    pandas \
    scikit-learn \
    scikit-image


# Install Keras, PyTorch, and TensorFlow
RUN pip install --upgrade --no-cache-dir \
    Keras \
    tf-nightly-gpu \
    torch \
    torchvision


# Prepare matplotlib font cache
RUN python -c "import matplotlib.pyplot"


# Set up `runjupyter` shortcut and Jupyter configuration
RUN echo 'alias runjupyter="jupyter notebook --ip 0.0.0.0 --no-browser --allow-root"' \
    >> /root/.bash_aliases
RUN mkdir /root/.jupyter
COPY jupyter_notebook_config.py /root/.jupyter/


# Set up directory for shared volumes
RUN mkdir /root/shared


# Set default working directory and image startup command
WORKDIR "/root"
CMD ["/bin/bash"]
