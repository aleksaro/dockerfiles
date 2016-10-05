# python3-ml

This Dockerfile uses the following base image ``aleksaro/python3-base:7.5-cudnn5``.

Below is a listing of the libraries included in this Dockerfile:

| Content                                         | Description                                         |
|-------------------------------------------------|-----------------------------------------------------|
| [libhdf5-dev](https://www.hdfgroup.org/)        | Hierarchical Data Format 5 (HDF5) development files |
|                                                 |                                                     |
| [h5py](http://www.h5py.org/)                    | Python interface to HDF5                            |
| [PyYAML](http://pyyaml.org/)                    | YAML implementation for Python                      |
| [pandas](http://pandas.pydata.org/)             | Python data analysis library                        |
| [scikit-learn](http://scikit-learn.org/stable/) | General-purpose machine learning in Python          |

Keep in mind that some of these packages may already be installed by a parent container.
