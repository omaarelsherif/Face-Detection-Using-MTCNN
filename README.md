
<!-- PROJECT TITLE -->
<h1 align="center">Face Detection With MTCNN</h1>

<!-- PROJECT DESCRIPTION -->
## ➲ Project description
Apply face detection using Multi-Task Cascaded Convolutional Neural Network model "MTCNN" algorithm which is based on deep learning where it extract every face bounding box within an image and then we can draw these faces using opencv.

MTCNN Paper : https://arxiv.org/abs/1604.02878

<!-- PREREQUISTIES -->
## ➲ Prerequisites
This is list of required packages and modules for the project to be installed :
* Python 3.x

  <https://www.python.org/downloads>
  
* OpenCv 
  ```sh
  pip install opencv-python
  ```
* mtcnn
  ```sh
  pip install mtcnn
  ```

<!-- INSTALLATION -->
## ➲ Installation
1. Clone the repo
   ```sh
   git clone https://github.com/omaarelsherif/Face-Detection-Using-Deep-Learning.git
   ```
2. Run the code from cmd
   ```sh
   python face_detection.py "IMAGE_PATH"
   ```
   For example:
   ```sh
   python face_detection.py Images/img1.jpg
   ```
   
<!-- OUTPUT -->
## ➲ Output
Here's the project output where the input is an image containing single or multi faces and the output will be the same image with bounding boxs around all faces in the image as follows:
<h3>Single Face Detection Output</h3>

![alt text for screen readers](/Output/output1.jpg "Single Face Detection Output")

<h3>Multi Face Detection Output</h3>

![alt text for screen readers](/Output/output2.jpg "MultiFace Detection Output")

<!-- REFERENCES -->
## ➲ References
These links may help you to better understanding of the project idea and techniques used :
1. Face detection in deep learning : https://bit.ly/3ht8kGY 
2. MTCNN : https://bit.ly/3nshJCJ

<!-- CONTACT -->
## ➲ Contact
- E-mail   : [omaarelsherif@gmail.com](mailto:omaarelsherif@gmail.com)
- LinkedIn : https://www.linkedin.com/in/omaarelsherif/
- Facebook : https://www.facebook.com/omaarelshereif
