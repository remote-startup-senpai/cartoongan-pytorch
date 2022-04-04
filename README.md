# CartoonGAN (PyTorch)

This is a modified version of [Yijunmaverick's implementation](https://github.com/Yijunmaverick/CartoonGAN-Test-Pytorch-Torch) of [CartoonGAN](http://openaccess.thecvf.com/content_cvpr_2018/CameraReady/2205.pdf) `[Chen et al., CVPR18]`. This repo was created due to lack of activity in original repo.

This model is normally used for poster POCs and Blender3D->2D background tests and pre-processing, more like a Photoshop filter for visualising characters with the background before post-processing with light rays, additional shadows, among others.

### Hugging Face Spaces Demo

You can check out the demo here:
[![Demo in Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/akiyamasho/AnimeBackgroundGAN)

Contribute to the demo repository here:
https://github.com/venture-anime/anime-background-gan-hf-space

### Requirements

- Unix-based OS
- `python 3.9.9` (other 3.x versions may work as well)
  - NOTE: This also works with M1 Macbooks
- `wget` (`brew install wget`) (if you don't have it)
- (optional, will default to CPU if no GPU/CUDA detected) NVIDIA GPU

### Setup

1. `pip install -r requirements.txt`
1. Download the pretrained models with `sh pretrained_model/download_pth.sh`

### Running

```
python main.py --input_dir test_img --style Hosoda
```

# Contributing

Create a pull request with your changes and assign it to [Sho](https://github.com/akiyamasho). Make sure to tag your commits using the [numpy commit guidelines](https://numpy.org/doc/1.16/dev/gitwash/development_workflow.html#writing-the-commit-message) for easier review.
