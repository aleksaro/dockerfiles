# python2-base

This Dockerfile uses the following base image ``aleksaro/cuda-base:7.5-cudnn4``.

Below is a listing of the programs, libraries, and compilers are included in this Dockerfile:

| Content                                                       | Description                                       |
|---------------------------------------------------------------|---------------------------------------------------|
| [liblapack-dev](http://www.netlib.org/lapack/)                | Library of linear algebra routines (LAPACK)       |
| [libopenblas-dev](http://www.openblas.net/)                   | OpenBLAS development files                        |
| [libzmq3-dev](http://zeromq.org/)                             | Development files for ØMQ (messaging kernel)      |
| [python](https://www.python.org/)                             | The Python 2 programming language                 |
| python-dev                                                    | Header files and a static library for Python 2    |
| [python-pip](http://www.pip-installer.org/)                   | Python package installer for Python 2             |
| [python-setuptools](https://pypi.python.org/pypi/setuptools)  | Extension to the python-distutils                 |
|                                                               |                                                   |
| [libfreetype6-dev](https://www.freetype.org/)                 | FreeType 2 font engine                            |
| libjpeg8-dev                                                  | Independent JPEG Group's JPEG runtime library     |
| liblcms2-dev                                                  | A colour management library                       |
| libopenjpeg2                                                  | JPEG 2000 image compression/decompression library |
| libpng12-dev                                                  | Portable Network Graphics (PNG) library           |
| libtiff5-dev                                                  | Tag Image File Format (TIFF) library              |
| libwebp-dev                                                   | WebP format library (based on the VP8 codec)      |
| zlib1g-dev                                                    | Compression library for gzip and PKZIP            |
|                                                               |                                                   |
| [wheel](http://pythonwheels.com/)                             | A built-package format for Python                 |
| [six](https://pypi.python.org/pypi/six)                       | Python 2 and 3 compatibility utilities            |
| [ipython](https://ipython.org/)                               | Interactive Python shell                          |
| [jupyter](http://jupyter.org/)                                | Jupyter notebooks                                 |
| [ipdb](https://github.com/gotcha/ipdb)                        | Python debugger for IPython                       |
| [numpy](http://www.numpy.org/)                                | Library for n-dimensional array processing        |
| [Pillow](https://python-pillow.org/)                          | Python Imaging Library (PIL) fork                 |
| [scipy](https://www.scipy.org/)                               | Scientific tools for Python                       |
| [matplotlib](http://matplotlib.org/)                          | Python plotting package                           |

Keep in mind that some of these packages may already be installed by a parent container.
