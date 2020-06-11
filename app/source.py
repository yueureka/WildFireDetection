
import numpy as np
from tensorflow.keras.models import load_model
from keras import backend as K
from PIL import Image

def add_image_magin(input_image, im_width=720, im_height=480, color=0):
  # padd 
  height, width, vec = input_image.shape
  new_image = np.pad(input_image, ((0, im_height-height), (0, im_width-width), (0, 0)), 'constant', constant_values=color)
  return new_image

# segment the image
def preprocess_input_image(input_image, im_height=480, im_width=720):
  # normalize the pixel value 
  input_image = input_image / np.max(input_image.astype('float'))
  height, width, vec = input_image.shape
  row_num = height//im_height if height%im_height==0 else height//im_height+1
  col_num = width//im_width if width%im_width==0 else width//im_width+1

  new_image_array = np.zeros((row_num*col_num, im_height, im_width, vec))

  for i in range(row_num):
    for j in range(col_num):
      temp_image = input_image[im_height*i:im_height*(i+1), im_width*j:im_width*(j+1), :]
      new_image_array[i*col_num+j] = add_image_magin(temp_image, im_width=im_width, im_height=im_height, color=0)
  return new_image_array, row_num, col_num

# combine all images back to original size 
def combine_image(input_image, row_num, col_num, original_height, original_width, im_height=480, im_width=720, remove_ghost=True):
  num, height, width, vec = input_image.shape
  new_image = np.zeros((height*row_num, width*col_num, vec))
  for i in range(row_num):
    for j in range(col_num):
      # Remove the ghost caused by CNN model prediction boundary artifacts.
      # by padding same 4 pixels on the boundary 
      if remove_ghost:
        # padd all four edges
        input_image[i*col_num+j, :, :, :] = np.pad(input_image[i*col_num+j, 4:height-4, 4:width-4, :], ((4, 4), (4, 4), (0, 0)), 'edge')
          
      new_image[im_height*i:im_height*(i+1), im_width*j:im_width*(j+1), :] = input_image[i*col_num+j, :, :, :]  
  return new_image[:original_height, :original_width, :]

# predict batches of images, and return the probability array
def batch_predict(input_image_array, model):
  num, height, width, vec = input_image_array.shape
  preds_array = np.zeros((num, height, width, 1))
  # to avoid OOM
  for ii in range(input_image_array.shape[0]):
    preds_array[ii] = model.predict(np.expand_dims(input_image_array[ii, :, :, :], axis=0), verbose=1)
  return preds_array
  

def conv_float_int(image):
  # convert arry back to [0, 255] for display
  if not np.any(image): # check if the array is all zero 
    return image.astype(int)
  return ((image-np.min(image))/(np.max(image)-np.min(image))*255).astype(int)


def load_trained_model(model_location):
    loaded_model = load_model(model_location)
    session = K.get_session()
    return loaded_model, session

def burn_area(output_mask, resolution, forest_type):
  # reference: https://www.geosci-model-dev.net/4/625/2011/gmd-4-625-2011.pdf
  # unit in g/m^2
  biomass_type = {'Tropical Forest': 28076,
                   'Temperate Forest':10492,
                   'Boreal Forest': 25000,
                   'Shrublands': 5705,
                   'Grasslands': 976
                  }
  area = np.count_nonzero(output_mask) * resolution**2
  # Ei = A(x,t)×B(x)×FB×efi, 
  # A: area, 
  # B(biomass_type), 
  # FB:Burning fraction, assume 1 here
  # efi: mass of biomass burnt, for CO2, it averages 1624 g/kg. 
  biomass_burnt =  area * biomass_type[forest_type]/1e3 * 1624 #unit in g
  
  # Califorlia annual CO2 emision from power generating, 424 million metric tons of CO2 per year
  # Reference: https://ww3.arb.ca.gov/cc/inventory/pubs/reports/2000_2016/ghg_inventory_trends_00-16.pdf
  ca_co2_daily = 4.24e8 / 365.
  
  equal_days = biomass_burnt /1e6 / ca_co2_daily
  
  print('The total burnt area is:', "{:.4e}".format(area/1e6), 'km^2 \n')
  print('The total CO2 emitted is:', "{:.4e}".format(biomass_burnt/1e6), 'tons \n')
  print("Which equivalent to:", "{:.4e}".format(equal_days), " days of Califorlia's  daily electricity power emission \n")
  return area, biomass_burnt, equal_days