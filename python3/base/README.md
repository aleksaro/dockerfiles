# python3-base

This Dockerfile uses the following base image ``aleksaro/cuda-base:8.0-cudnn6-ubuntu16.04``.

Below is a listing of the programs, libraries, and compilers are included in this Dockerfile:

| Content                                                       | Description                                         |
|---------------------------------------------------------------|-----------------------------------------------------|
| [liblapack-dev](http://www.netlib.org/lapack/)                | Library of linear algebra routines (LAPACK)         |
| [libopenblas-dev](http://www.openblas.net/)                   | OpenBLAS development files                          |
| [libzmq3-dev](http://zeromq.org/)                             | Development files for ØMQ (messaging kernel)        |
| [python3](https://www.python.org/)                            | The Python 3 programming language                   |
| python3-dev                                                   | Header files and a static library for Python 3      |
| [python3-pip](http://www.pip-installer.org/)                  | Python package installer for Python 3               |
| [python3-setuptools](https://pypi.python.org/pypi/setuptools) | Extension to the python-distutils                   |
| [python3-tk](https://wiki.python.org/moin/TkInter)            | Graphical User Interface toolkit for Python         |
|                                                               |                                                     |
| [libfreetype6-dev](https://www.freetype.org/)                 | FreeType 2 font engine                              |
| libjpeg-dev                                                   | Independent JPEG Group's JPEG runtime library       |
| liblcms2-dev                                                  | A colour management library                         |
| libopenjpeg-dev                                               | JPEG 2000 image compression/decompression library   |
| libpng12-dev                                                  | Portable Network Graphics (PNG) library             |
| libtiff5-dev                                                  | Tag Image File Format (TIFF) library                |
| libwebp-dev                                                   | WebP format library (based on the VP8 codec)        |
| zlib1g-dev                                                    | Compression library for gzip and PKZIP              |
|                                                               |                                                     |
| [wheel](http://pythonwheels.com/)                             | A built-package format for Python                   |
| [six](https://pypi.python.org/pypi/six)                       | Python 2 and 3 compatibility utilities              |
| [Cython](http://cython.org/)                                  | C-Extensions for Python                             |
| [nose](https://nose.readthedocs.io/en/latest/)                | An extension of unittest to make testing easier     |
| [ipython](https://ipython.org/)                               | Interactive Python shell                            |
| [jupyter](http://jupyter.org/)                                | Jupyter notebooks                                   |
| [ipdb](https://github.com/gotcha/ipdb)                        | Python debugger for IPython                         |
| [numpy](http://www.numpy.org/)                                | Library for n-dimensional array processing          |
| [Pillow](https://python-pillow.org/)                          | Python Imaging Library (PIL) fork                   |
| [imageio](https://imageio.github.io/)                         | A Python library for reading and writing image data |
| [scipy](https://www.scipy.org/)                               | Scientific tools for Python                         |
| [matplotlib](http://matplotlib.org/)                          | Python plotting package                             |

Keep in mind that some of these packages may already be installed by a parent container.
