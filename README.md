## Natural Scenes Image Classifier

### Introduction
This is Natural Scenes Image Classifier project. Model trained with 224x224 image of natural scenes and the model classifies the image of six classes which includes buildings, forest, glacier, mountain, sea and street gives as a output.

### Required python libraries
- Numpy
- Tensorflow 2.0
- Matplotlib
- Glob
- Math

### Model built with
- Python 3.0
- Tensorflow 2.0
- Keras
- VGG16 convolution neural network architecture

### Dataset
Intel Image Classification Dataset from Kaggle.
[Download](https://www.kaggle.com/puneet6060/intel-image-classification) from here.

### Description
I found dataset for this project on kaggle. I used transfer learning technique for build model. VGG16 gives more accuracy than Resnet50 that's why i decided to use VGG16 architecture for this project. I used weights as imagenet in VGG16. VGG16 has 1 InputLayer, 1 OutputLayer, 13 Conv2D, 5 MaxPooling2D and 1 Flatten Layer. Total parameters 14,865,222 with 150,534 trainable parameters and 14,714,688 Non-trainable parameters. Model compiled with 'categorical_crossentropy' loss and 'adam' optimizer parameters.  I select batch_size as 32 and 50 epochs for trainig Neural Network.

### VGG16 Architecture
![VGG16](https://neurohive.io/wp-content/uploads/2018/11/vgg16-1-e1542731207177.png)

![Tensorflow-Keras](https://res.cloudinary.com/practicaldev/image/fetch/s---CuIRi0J--/c_imagga_scale,f_auto,fl_progressive,h_900,q_auto,w_1600/https://thepracticaldev.s3.amazonaws.com/i/mf5cfpdcw33dyvih6jut.png)
