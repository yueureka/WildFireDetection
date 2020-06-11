# Wildfire Detection Project
In this project, we created a U-net deep learning model that takes any satellite imagery and detects the wildfire burning scar. <br/>
The model is trained on Databricks, and the application is deployed on Streamlit. <br/>
Check here for the [Video Demonstration](https://www.youtube.com/watch?v=gkRaKKU9-Es).

### Content of this document
  * [Installation](#Installation)
  * [Inspiration](#Inspiration)
  * [What-it-does](#What-it-does)
  * [How-we-built-it](#How-we-built-it)
  * [Prediction-examples](#Prediction-examples)
  * [Licensing](#Licensing)
  * [Contact](#Contact)

### Installation 
Clone this repo and direct to the `./app` folder <br/>
You probably need to download docker before you start running the app. <br/>
Then under the folder `./app` in terminal, please add this command `docker build -f Dockerfile -t app:latest .` This is going to create the docker image and build the corresponding docker container. <br/>
For your better usage, the trained model has been stored in the docker container. <br/>
Then please use the code `docker run -p 8501:8501 app:latest`, this is going to open the app for you. <br/>
Use your favourite browser, and type `http://localhost:8501/` and you should be able to open our app. <br/>
After you done with the app, please remember to stop the container. <br/>

***Dependencies***
- matplotlib==3.2.1<br/>
- numpy==1.18.4<br/>
- streamlit==0.59.0<br/>
- tensorflow==1.14.0<br/>
- Keras==2.0.0<br/>
- Pillow==7.1.2<br/>

Here is what the application looks like:<br/>
<p align="center">
  <img width="600" height="600" src="https://github.com/yueureka/WildFireDetection/blob/master/Pictures/App2.png">
</p>

After deployed the model, click "browse file" button to add the image you want to predict (we have provided some test images in the 'Test image' folder for you to test), the app will then automatically draw the raw image, burning scar probability picutre and the predicted burning scar mask. You may also change the "type of forest" dropdown menu and "image resoltion" to check the burnt area and CO2 emission.  


### Inspiration 
Wildfire has become one of the most devastating disasters that not only causes huge loss to human lives and properties, but also emits enormous CO2 into the environment. The 2018 California Camp fire alone has caused $16.5billion loss and emitted a year’s worth of power pollution. 

Currently, there’re over a thousand of earth observation(EO) satellites that orbiting us, however, only less than 10 of them can monitor wildfire, such as Sentinel and Landsat. These satellites either only track small portion of the land, or require extensive specialties and dedicated preprocessing skills to process, which greatly limit the capability to real time monitor the wildfire across the globe. Therefore, it's important to find a way that may utilize many more of the EO satellite imagery and imporve the effectiveness of wildfire monitoring.

With the increasing development of deep learning technologies, convolutional neural network (CNN) has become one of the most powerful tool in image processing. In this work, we trained a U-net based CNN deep learning model on Databricks, it takes raw imagery from different satellites as the input, and is able to quickly detect the wildfire and monitor the burning scar. 

### What-it-does
The simple to use application takes imagery from different satellites resources as input, and then quickly predict the forest fire probability and segment the burning scar zones. 

In addition, with the input of image resolution and forest type, it calculates the total area of the burnt area of a wildfire, and estimates the total CO2 emitted due to this fire. 

### How-we-built-it
Here is the workflow:
![Workflow](https://github.com/yueureka/WildFireDetection/blob/master/Pictures/Workflow.PNG)
The steps are:
1.	Download the satellite imagery from Google image API, and then manually draw the burning scar segmentation on training dataset.
2.	Build U-net model with Keras library and Tensorflow.
3.	Train the model on Databricks with CPU, and save the trained model on S3.
4.	Deploy the application on streamlit.

### Prediction-examples
Here are few samples of the test images of our model. The figures from left to right are: 1. Raw image, 2. Burning scar masks manually added by hand, 3. Burning scar probabilitys predicted by the model, 4. Burning scar predicted by the model
![Result1](https://github.com/yueureka/WildFireDetection/blob/master/Pictures/Result1.png)
![Result2](https://github.com/yueureka/WildFireDetection/blob/master/Pictures/Result4.png)
![Result3](https://github.com/yueureka/WildFireDetection/blob/master/Pictures/Result3.png)

### Licensing 
DATA ACCESS AND USE: Creative Commons Attribution-NonCommercial-ShareAlike license.<br/>
Please send email to either of us before using the code. 

### Contact
Disha An (disha.an.datascience@gmail.com)<br/>
Boran Han (boranhan.dl@gmail.com)<br/>
Zhijuan Zhang (zzhijuan@yahoo.com )<br/>
Yanxiang Yu (yueureka@gmail.com)<br/>
