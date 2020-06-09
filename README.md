# Wildfire Detection Project
In this project, we created a U-net deep learning model that takes any satellite imagery to detect the wildfire and monitor the burning scar in real-time. <br/>
The model is trained on Databricks, and the application is deployed on Streamlit. <br/>

### Content of this document
  * [Installation](#Installation)
  * [Inspiration](#Inspiration)
  * [What-it-does](#What-it-does)
  * [How-we-built-it](#How-we-built-it)
  * [Prediction-examples](#Prediction-examples)
  * [Licensing](#Licensing)

### Installation 
Download the WildfireApp.zip and unzip the file to your local computer.<br/>
Open your Python terminal, cd to the folder/app and then type the following code:<br/>
`streamlit run app.py` <br/>

If there are any dependencies requirements, please download them.

***Dependencies***
- matplotlib==3.2.1<br/>
- numpy==1.18.4<br/>
- streamlit==0.59.0<br/>
- tensorflow==1.14.0<br/>
- Keras==2.0.0<br/>
- Pillow==7.1.2<br/>


### Inspiration 
Wildfire has become one of the most devastating disasters that not only causes huge loss to human lives and properties, but also emits enormous CO2 into the environment. Governments and scientists have built dedicated earth observation satellites and system to monitor the wildfire, such as Sentinel and Landsat, however, these satellites either only track small portion of the land, or require extensive specialties and dedicated preprocessing skills to process, which greatly limit the capability to real time monitor the wildfire across the globe. 

With the increasing development of deep learning technologies, convolutional neural network (CNN) has become one of the most powerful tool in image processing. In this work, we trained a U-net based CNN deep learning model on Databricks, it takes raw imagery from different satellites as the input, and is able to real-time detect the wildfire and monitor the burning scar. 

### What-it-does
1.	A simple to use application that takes imagery from different satellites resources as input, and then quickly predict the forest fire probability and segment the burning scar zones.

2.	The application calculates the total area of the burnt area of a wildfire, and estimates the total CO2 emitted due to this fire. 



### How-we-built-it
Here 's the workflow:
![Workflow](https://github.com/yueureka/WildFireDetection/blob/master/Pictures/Workflow.PNG)
1.	Download the satellite imagery from Google image API, and prepare the training dataset.
2.	Build U-net model with Keras library and Tensorflow.
3.	Train the model on Databricks with CPU, and save the trained model on S3.
4.	Deploy the application on stream.io, it calls model from S3 and satellite imagery, and make the prediction.

### Prediction-examples
![Result1](https://github.com/yueureka/WildFireDetection/blob/master/Pictures/Result1.png)
![Result2](https://github.com/yueureka/WildFireDetection/blob/master/Pictures/Result4.png)
![Result3](https://github.com/yueureka/WildFireDetection/blob/master/Pictures/Result3.png)

### Licensing 
DATA ACCESS AND USE: Creative Commons Attribution-NonCommercial-ShareAlike license.<br/>
Please send email to yueureka@gmail.com before using the code. 
