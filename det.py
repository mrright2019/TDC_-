from __future__ import division
from models import *
from utils.utils import *
from utils.datasets import *
from PIL import Image
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
import sys
import time,uuid
import datetime
import argparse
import numpy as np
import torch.nn.functional as F
from PIL import Image
import torchvision.transforms as transforms
import torch
from torch.utils.data import DataLoader
from torchvision import datasets
from torch.autograd import Variable
import cv2


def pad_to_square(img, pad_value):
    c, h, w = img.shape
    dim_diff = np.abs(h - w)
    pad1, pad2 = dim_diff // 2, dim_diff - dim_diff // 2
    pad = (0, 0, pad1, pad2) if h <= w else (pad1, pad2, 0, 0)
    img = F.pad(img, pad, "constant", value=pad_value)

    return img, pad

def resize(image, size):
    image = F.interpolate(image.unsqueeze(0), size=size,
                          mode="nearest").squeeze(0)
    return image


def GetImgMat(img_path):
    img = transforms.ToTensor()(Image.open(img_path))
    img, _ = pad_to_square(img, 0)
    img = resize(img, 416)
    img = img.view(-1,3,416,416)
    return img

from PIL import Image, ImageDraw, ImageFont
def predictImg(model,path):

    Tensor = torch.cuda.FloatTensor if torch.cuda.is_available() else torch.FloatTensor
    img_detections = []
    mat = GetImgMat(path)
    input_imgs = Variable(mat.type(Tensor))
    with torch.no_grad():
        detections = model(input_imgs)
        detections = non_max_suppression(
            detections, 0.75, 0.1)
    return getBeforePosition(path,detections[0])



def getBeforePosition(path,detections):
    if detections is None:
        return
    img = np.array(Image.open(path))
    detections = rescale_boxes(detections, 416, list(img.shape)[:2])
    classname = """yuanzhu
yuanzhui
zhengfangti
yuanti
zhengdui
cedui""".split("\n")
    im = cv2.imread(path)
    global_data = []
    fontStyle = ImageFont.truetype(
        "font/simsun.ttc", 16, encoding="utf-8")
    for x1, y1, x2, y2, conf, cls_conf, cls_pred in detections:
        # if cls_conf.item()<0.7:
        item = {}
        item['name'] = classname[int(cls_pred)]
        item['x1'] = x1.item()
        item['x2'] = x2.item()
        item['y1'] = y1.item()
        item['y2'] = y2.item()
        global_data.append(item)
        cv2.rectangle(im,(int(x1),int(y1)),(int(x2),int(y2)),(0,255,0),2)
        cv2.putText(im, classname[int(cls_pred)], (int(x1),int(y1-6)), cv2.FONT_HERSHEY_COMPLEX_SMALL,0.8, (0, 255, 0) )
    cv2.imwrite('output/{}.jpg'.format(str(uuid.uuid1())),im,[int(cv2.IMWRITE_JPEG_QUALITY),70])
    print("写入完成")
    return global_data




def load_model():
    opt = {
        "model_def":"config/yolov3.cfg",
        "class_path":'classes.names',
        "conf_thres":0.75,
        'n_cpu':0,
        'nms_thres':0.1,
        'weights_path':'model/capture_990.pth',
        "img_size":416
    }
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = Darknet(opt['model_def'], img_size=416).to(device)

    if opt['weights_path'].endswith(".weights"):
        # Load darknet weights
        model.load_darknet_weights(opt['weights_path'])
    else:
        # Load checkpoint weights
        model.load_state_dict(torch.load(opt['weights_path'],map_location=device))
    model.eval()
    classes = load_classes(opt['class_path'])
    return model,classes


global_model,global_data = load_model()

def p(img):
    model,classes = load_model()
    obj = predictImg(global_model,img)
    return obj


# p("t.jpg")