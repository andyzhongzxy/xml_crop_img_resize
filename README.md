# xml_crop_img_resize

**这是一个根据xml文件内记录的名字，坐标，批量对原图片进行裁剪和分类的一个小工具**

在进行python的深度学习之前，一般会用LabelImg先对图片上的需要识别的物体进行标记，此时会生成一个xml文件，里面记录着标记的坐标，标记的名称，和图片的文件名。由于一张图片原本的大小不适于进行训练，而且图片的数量往往非常多，所以此时就需要一个程序，可以将需要用于训练的部分裁剪下来，并按照名字进行分类

- anatation文件夹放置xml文件
- 
- img文件夹放置需要处理的图片
- 
- crop_img和resize分别储存程序裁剪下来的图片，和将裁剪下来的图片进行拉伸，使处理后的图片大小相同