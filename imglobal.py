from __future__ import division
import os
from PIL import Image
from PIL import ImageFile
import xml.dom.minidom
import numpy as np
ImageFile.LOAD_TRUNCATED_IMAGES = True
ImgPath = r'./img/'                              #待处理图片
AnnoPath = r'./anatation/'                       #xml保存
ProcessedPath = r'./crop_img/'                   #截取的图片
resizePath = r'./resize/'                        #拉伸后的图片

imagelist = os.listdir(ImgPath)

for image in imagelist:
  image_pre, ext = os.path.splitext(image)
  imgfile = ImgPath + image
  print(imgfile)
  if not os.path.exists(AnnoPath + image_pre + '.xml' ):
    continue
  xmlfile = AnnoPath + image_pre + '.xml'
  DomTree = xml.dom.minidom.parse(xmlfile)
  annotation = DomTree.documentElement
  filenamelist = annotation.getElementsByTagName('filename')
  filename = filenamelist[0].childNodes[0].data
  objectlist = annotation.getElementsByTagName('object')
  i = 1
  for objects in objectlist:
    namelist = objects.getElementsByTagName('name')
    objectname = namelist[0].childNodes[0].data
    savepath = ProcessedPath + objectname
    if not os.path.exists(savepath):
      os.makedirs(savepath)
    resizesPath = resizePath + objectname
    if not os.path.exists(resizesPath):
      os.makedirs(resizesPath)
    bndbox = objects.getElementsByTagName('bndbox')
    cropboxes = []
    for box in bndbox:
      x1_list = box.getElementsByTagName('xmin')
      x1 = int(x1_list[0].childNodes[0].data)
      y1_list = box.getElementsByTagName('ymin')
      y1 = int(y1_list[0].childNodes[0].data)
      x2_list = box.getElementsByTagName('xmax')
      x2 = int(x2_list[0].childNodes[0].data)
      y2_list = box.getElementsByTagName('ymax')
      y2 = int(y2_list[0].childNodes[0].data)
      w = x2 - x1
      h = y2 - y1
      obj = np.array([x1,y1,x2,y2])
      shift = np.array([[1,1,1,1]])
      XYmatrix = np.tile(obj,(1,1))
      cropboxes = XYmatrix * shift
      img = Image.open(imgfile)
      for cropbox in cropboxes:
        cropedimg = img.crop(cropbox)
        cropedimg.save(savepath + '/' + image_pre + '_' + str(i) + '.jpg')
        for img in filename:
          img = Image.open(savepath + '/' + image_pre + '_' + str(i) + '.jpg')
          resize_img = img.resize((64, 64), Image.ANTIALIAS)
          resize_img.save(resizesPath + '/' + image_pre + '_' + str(i) + '.jpg')
        i += 1
