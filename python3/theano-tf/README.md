# python3-theano-tf

This Dockerfile uses the following base image ``aleksaro/python3-ml:7.5-cudnn4``.

| Content                                    | Description                                                                      |
|--------------------------------------------|----------------------------------------------------------------------------------|
| [TensorFlow](https://www.tensorflow.org/)  | Python library for computation using data flow graphs                            |
| [Theano](https://github.com/Theano/Theano) | Python library for defining, optimising, and evaluating mathematical expressions |

The following boilerplate .theanorc is set up inside ``/root``:

```bash
[global]
device=gpu0
floatX=float32

[dnn.conv]
algo_fwd=time_once
algo_bwd_data=time_once
algo_bwd_filter=time_once

[lib]
cnmem=0.1
```
