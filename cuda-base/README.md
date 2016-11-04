# cuda-base

This Dockerfile uses the following base image by [NVIDIA Docker](https://github.com/NVIDIA/nvidia-docker):

```bash
nvidia/cuda:8.0-cudnn5-devel
```

Below is a listing of the programs, libraries, and compilers are included in this Dockerfile:

| Content                                                             | Description                                              |
|---------------------------------------------------------------------|----------------------------------------------------------|
| build-essential                                                     | A slew of packages necessary to compile Debian packages  |
| [byobu](http://byobu.co/)                                           | Terminal multiplexer built on top of GNU Screen          |
| [CMake](https://cmake.org/)                                         | Cross-platform make system                               |
| [curl](https://curl.haxx.se/)                                       | Tool for transferring data with URL syntax               |
| [g++](https://gcc.gnu.org/)                                         | GNU C++ compiler (GNU Compiler Collection)               |
| [gcc](https://gcc.gnu.org/)                                         | GNU C compiler (GNU Compiler Collection)                 |
| [gfortran](https://gcc.gnu.org/fortran/)                            | GNU Fortran 95 compiler                                  |
| [git](https://git-scm.com/)                                         | Distributed revision control system                      |
| [make](https://www.gnu.org/software/make/)                          | GNU Make is a utility program for generating executables |
| [nano](http://www.nano-editor.org/)                                 | Small, simple text editor                                |
| [pkg-config](https://www.freedesktop.org/wiki/Software/pkg-config/) | System for managing library compile and link flags       |
| [rsync](https://rsync.samba.org/)                                   | A utility program for fast file transfer                 |
| unzip                                                               | De-archiver for .zip files                               |
| [wget](https://www.gnu.org/software/wget/)                          | Network utility for file retrieval over HTTP(S) and FTP  |

Keep in mind that some of these packages may already be installed by a parent container.
