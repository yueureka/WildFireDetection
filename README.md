# Wildfire Detection Project
In this project, we created a U-net deep learning model that takes any satellite imagery and detects the wildfire burning scar. <br/>
The model is trained on Databricks, and the application is deployed on Streamlit. <br/>

Check here for the [**Video Demonstration**](https://www.youtube.com/watch?v=gkRaKKU9-Es) and the [**Presentation**](https://github.com/yueureka/WildFireDetection/blob/master/Presentation.pdf).

### Content of this document
  * [Installation](#Installation)
  * [Inspiration](#Inspiration)
  * [What-it-does](#What-it-does)
  * [How-we-built-it](#How-we-built-it)
  * [Prediction-examples](#Prediction-examples)
  * [Licensing](#Licensing)
  * [Contact](#Contact)

### Installation 
Clone this repo and direct to the `./app` folder. <br/>
- **Method 1:** Run with Python IDE<br/>
Go to the folder`/app` and then in your terminal please type the following code: <br/>
`streamlit run app.py` <br/>
Please make sure you have the dependency installed is the same as listed in the "requirement.txt"

- **Method 2:** Run with Docker<br/>
You probably need to download docker before you start running the app. <br/>
Then under the folder `./app` in terminal, please add this command `docker build -f Dockerfile -t app:latest .`. This is going to create the docker image and build the corresponding docker container. <br/>
For your better usage, the trained model has been stored in the docker container. <br/>
Then please use the code `docker run -p 8501:8501 app:latest`, this is going to open the app for you. <br/>
Use your favourite browser, and type `http://localhost:8501/` and you should be able to open our app. <br/>
After you done with the app, please remember to stop the container. <br/>


Here is what the application looks like:<br/>
<p align="center">
  <img width="600" height="600" src="https://github.com/yueureka/WildFireDetection/blob/master/Pictures/App2.png">
</p>

After deployed the model, click "browse file" button to add the image you want to predict (we have provided some test images in the 'test_image' folder for you to test), the image needs to be in `"*.PNG"` format, the app will then automatically draw the raw image, burning scar probability picutre and the predicted burning scar mask. <br/>
You may also change the "type of forest" dropdown menu and "image resoltion" to check the burnt area and CO2 emission.  


### Inspiration 
Wildfire has become one of the most devastating disasters that not only causes huge loss to human lives and properties, but also emits enormous CO2 into the environment. The 2018 California Camp fire alone has caused $16.5billion loss and emitted a year’s worth of power pollution. 

Currently, there’re over a thousand of earth observation(EO) satellites that orbiting us, however, only less than 10 of them can monitor wildfire, such as Sentinel and Landsat. These satellites either only track small portion of the land, or require extensive specialties and dedicated preprocessing skills to process, which greatly limit the capability to real time monitor the wildfire across the globe. Therefore, it's important to find a way that may utilize many more of the EO satellite imagery and imporve the effectiveness of wildfire monitoring.

With the increasing development of deep learning technologies, convolutional neural network (CNN) has become one of the most powerful tool in image processing. In this work, we trained a U-net based CNN deep learning model on Databricks, it takes raw imagery from different satellites as the input, and is able to quickly detect the wildfire and monitor the burning scar. 

### What-it-does
This is a user-friendly application. It takes imagery from different satellites resources as input, and then quickly predicts the forest fire probability and segments the burning scar zones.

In addition, given the image resolution and the forest type, it can calculate the total area of the burnt zone of a wildfire, and estimate the total CO2 emission from this fire.

### How-we-built-it
Here is the workflow:
![Workflow](https://github.com/yueureka/WildFireDetection/blob/master/Pictures/Workflow.PNG)
The steps are:
1.	Download the satellite imagery using Google image API to create the training dataset.  
2. Manually contour the burning scar zones as the label.
3.	Build a training pipeline embedded with U-net model.
4.	Train the model on Databricks with 2-instance CPU, and save the trained model to AWS S3.
5.	Create the application using Streamlit framework, and deploy it as a Docker project.
![](https://github.com/yueureka/WildFireDetection/blob/master/Pictures/Databricks.PNG)

The CO2 emission calculation is based on the following references:
* [California Greenhouse Gas Emission for 2000 to 2017 Trends of Emissions and Other Indicators, 2019](https://ww3.arb.ca.gov/cc/inventory/pubs/reports/2000_2016/ghg_inventory_trends_00-16.pdf)
* [The Fire INventory from NCAR (FINN): a high resolution global model to estimate the emissions from open burning, 2011](https://www.geosci-model-dev.net/4/625/2011/gmd-4-625-2011.pdf)

### Prediction-examples
Here are few samples of the test images of our model. <br/>
The figures from left to right are: 1. Raw image, 2. Burning scar masks manually added by hand, 3. Burning scar probabilitys predicted by the model, 4. Burning scar predicted by the model
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
