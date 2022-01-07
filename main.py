import torch
import os
import numpy as np
import torchvision.utils as vutils

from PIL import Image
import torchvision.transforms as transforms
from torch.autograd import Variable

from network.Transformer import Transformer
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input_dir", default="test_img")
parser.add_argument("--load_size", default=1280)
parser.add_argument("--model_path", default="./pretrained_model")
parser.add_argument("--style", default="Shinkai")
parser.add_argument("--output_dir", default="test_output")
parser.add_argument("--gpu", type=int, default=0)

opt = parser.parse_args()

valid_ext = [".jpg", ".png"]

# setup
if not os.path.exists(opt.input_dir):
    os.makedirs(opt.input_dir)
if not os.path.exists(opt.output_dir):
    os.makedirs(opt.output_dir)

# load pretrained model
model = Transformer()
model.load_state_dict(
    torch.load(os.path.join(opt.model_path, opt.style + "_net_G_float.pth"))
)
model.eval()

disable_gpu = opt.gpu == -1 or not torch.cuda.is_available()

if disable_gpu:
    print("CPU mode")
    model.float()
else:
    print("GPU mode")
    model.cuda()

for files in os.listdir(opt.input_dir):
    ext = os.path.splitext(files)[1]
    if ext not in valid_ext:
        continue
    # load image
    input_image = Image.open(os.path.join(opt.input_dir, files)).convert("RGB")
    input_image = np.asarray(input_image)
    # RGB -> BGR
    input_image = input_image[:, :, [2, 1, 0]]
    input_image = transforms.ToTensor()(input_image).unsqueeze(0)
    # preprocess, (-1, 1)
    input_image = -1 + 2 * input_image
    if disable_gpu:
        input_image = Variable(input_image).float()
    else:
        input_image = Variable(input_image).cuda()

    # forward
    output_image = model(input_image)
    output_image = output_image[0]
    # BGR -> RGB
    output_image = output_image[[2, 1, 0], :, :]
    output_image = output_image.data.cpu().float() * 0.5 + 0.5
    # save
    vutils.save_image(
        output_image,
        os.path.join(opt.output_dir, files[:-4] + "_" + opt.style + ".jpg"),
    )

print("Done!")
