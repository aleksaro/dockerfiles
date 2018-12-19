#
# data-science-c9: Dockerfile for data science with Cloud9
# (https://github.com/c9/core).
#

# Base image is `data-science`
FROM aleksaro/data-science:latest


LABEL maintainer "Aleksander Rognhaugen and Igor Barros Barbosa"


# Install Python 2.7 and Node.js
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
        python2.7 \
        nodejs


# Cleanup apt-get
RUN apt-get clean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*


# Install Cloud9
RUN git clone https://github.com/c9/core.git c9
RUN c9/scripts/install-sdk.sh


# Add Cloud9 shortcut
RUN echo 'alias runc9="nodejs c9/server.js --port 8080 --listen 0.0.0.0 "' \
    >> /root/.bash_aliases


# Set default working directory and image startup command
WORKDIR "/root"
CMD ["/bin/bash"]
