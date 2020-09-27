# cartoongan-pytorch

This is a modified version of [Yijunmaverick's implementation](https://github.com/Yijunmaverick/CartoonGAN-Test-Pytorch-Torch) of [CartoonGAN](http://openaccess.thecvf.com/content_cvpr_2018/CameraReady/2205.pdf) `[Chen et al., CVPR18]`. This repo was created due to lack of activity in original repo.

This model is normally used for poster POCs and Blender3D->2D background tests and pre-processing, more like a Photoshop filter for visualising characters with the background before post-processing with light rays, additional shadows, among others.

### Requirements

- Unix-based OS
- `python 3.6.11` (other 3.x versions may work as well)
- (optional, will default to CPU if no GPU/CUDA detected) NVIDIA GPU

### Setup

1. `pip install -r requirements.txt`
1. Download the pretrained models with `sh pretrained_model/download_pth.sh`

### Running

```
python main.py --input_dir test_img --style Hosoda
```
