# cuda-base

This Dockerfile uses the following base image by NVIDIA:

```bash
nvidia/cuda:10.0-base-ubuntu18.04
```

Below is a listing of the programs, libraries, and compilers are included in this Dockerfile:

| Content                                                             | Description                                              |
|---------------------------------------------------------------------|----------------------------------------------------------|
| build-essential                                                     | A slew of packages necessary to compile Debian packages  |
| [ca-certificates](https://launchpad.net/ca-certificates)            | PEM files of CA certificates                             |
| [CMake](https://cmake.org/)                                         | Cross-platform make system                               |
| cuda-*                                                              | Various CUDA tools                                       |
| [libcudnn7](https://developer.nvidia.com/cudnn)                     | GPU-accelerated library of primitives for ANNs           |
| [libfreetype6-dev](https://www.freetype.org/)                       | FreeType 2 font engine                                   |
| [libhdf5-serial-dev](https://www.hdfgroup.org/)                     | Hierarchical Data Format 5 (HDF5) development files      |
| libjpeg-dev                                                         | Independent JPEG Group's JPEG runtime library            |
| [liblapack-dev](http://www.netlib.org/lapack/)                      | Library of linear algebra routines (LAPACK)              |
| liblcms2-dev                                                        | A colour management library                              |
| [libopenblas-dev](http://www.openblas.net/)                         | OpenBLAS development files                               |
| libpng-dev                                                          | Portable Network Graphics (PNG) library                  |
| libtiff-dev                                                         | Tag Image File Format (TIFF) library                     |
| libwebp-dev                                                         | WebP format library (based on the VP8 codec)             |
| [libzmq3-dev](http://zeromq.org/)                                   | Development files for ØMQ (messaging kernel)             |
| locales                                                             | Language settings                                        |
| [pkg-config](https://www.freedesktop.org/wiki/Software/pkg-config/) | System for managing library compile and link flags       |
| software-properties-common                                          | Manage the repositories installed from software          |
|                                                                     |                                                          |
| [byobu](http://byobu.co/)                                           | Terminal multiplexer built on top of GNU Screen          |
| [curl](https://curl.haxx.se/)                                       | Tool for transferring data with URL syntax               |
| [git](https://git-scm.com/)                                         | Distributed revision control system                      |
| [htop](https://hisham.hm/htop/)                                     | An interactive process viewer                            |
| [nano](http://www.nano-editor.org/)                                 | Small, simple text editor                                |
| [rsync](https://rsync.samba.org/)                                   | A utility program for fast file transfer                 |
| unzip                                                               | De-archiver for .zip files                               |
| [vim](https://www.vim.org/)                                         | Highly configurable text editor                          |
| [wget](https://www.gnu.org/software/wget/)                          | Network utility for file retrieval over HTTP(S) and FTP  |
