import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
from source import preprocess_input_image, batch_predict, conv_float_int, combine_image, load_trained_model, burn_area   
import numpy as np
from keras import backend as K
from tensorflow.python.lib.io import file_io
import boto3
from keras.models import load_model

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


st.title("Wild Fire Detection App")

st.sidebar.markdown("** App Status **")

model, session = load_trained_model("temp_model.h5")
K.set_session(session)


st.sidebar.markdown('Please upload a raw satellite image')
uploaded_file = st.sidebar.file_uploader("Upload png file", type=["png"])


if uploaded_file is not None:
    uploaded_image = Image.open(uploaded_file)
    st.markdown("** Original Raw Image: **")
    st.image(uploaded_image, width = 500)
    
    ### Preprocess the raw image
    #st.sidebar.text("Pre-processing the image...")
    with st.spinner("Pre-processing the image..."):
        input_image_array = np.array(uploaded_image)
        original_width, original_height, pix_num = input_image_array.shape
        new_image_array, row_num, col_num = preprocess_input_image(input_image_array)
        st.sidebar.success("Pre-processing has been done.")


    with st.spinner("Making the prediction..."):
        #### Make Prediction
        preds = batch_predict(new_image_array, model)
        # combine the images, and converted to 0-255 for display 
        output_pred = conv_float_int(combine_image(preds, row_num, col_num, original_width, original_height, remove_ghost=True)[:,:,0])
        st.sidebar.success("Prediction has been done.")
        # add image mask to the probability array
    


    #### Show the picture
    st.markdown("** The Predicted Probability is **: ")
    plt.imshow(output_pred)
    st.pyplot()


    #threshold = st.sidebar.slider("Threshold", 0, 1, 0.25)
    preds_t = (preds > 0.25).astype(np.uint8)
    output_mask = conv_float_int(combine_image(preds_t, row_num, col_num, original_width, original_height, remove_ghost=False)[:,:,0])
    st.markdown("** The Predicted Mask is **: ")
    plt.imshow(output_mask)
    st.pyplot()
    #plt.imshow(output_mask)
   
    st.sidebar.markdown("** CO2 Emission Calculator **")
    forest_type = st.sidebar.selectbox("Please select the type of forest: ", ('Tropical Forest', 'Temperate Forest', 'Boreal Forest', 'Shrublands', 'Grasslands'))
    resolution = st.sidebar.text_input("Please enter the image resolution value: ", '10')
    
    area, biomass_burnt, equal_days = burn_area(output_mask = output_mask, resolution = float(resolution), forest_type = forest_type)
    st.sidebar.markdown('The total burnt area is:')
    st.sidebar.text("{0:.2f}".format(area/1e6) + ' km^2')
    st.sidebar.markdown('The total CO2 emitted is:')
    st.sidebar.text("{0:.2f}".format(biomass_burnt/1e6) + ' tons')
    st.sidebar.markdown("This is equivalent to:")
    st.sidebar.text("{0:.2f}".format(equal_days) + " days of Califorlia's daily electricity power emission")




