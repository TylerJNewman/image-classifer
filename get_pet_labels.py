#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
import os

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Retrieve the filenames from folder pet_images/
    filename_list = os.listdir(image_dir)
 
    # Creates empty dictionary for the results (pet labels, etc.)
    results_dic = {}
   
    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label
    for pet_image in filename_list:
       if pet_image[0] != ".":
           # remove extension - "Poodle.jpg" -> "Poodle"
           pet_image = os.path.splitext(pet_image)[0]
        
           # Sets string to lower case letters
           low_pet_image = pet_image.lower()

           # Splits lower case string by _ to break into words 
           pet_labels = low_pet_image.split("_")

           # Create pet_name starting as empty string
           pet_name = ""
        
           # Loops to check if word in pet name is only
           # alphabetic characters - if true append word
           # to pet_name separated by trailing space 
           for word in pet_labels:
            if word.isalpha():
                pet_name += word + " "
           
           # Strip off starting/trailing whitespace characters 
           pet_name = pet_name.strip()
        
           # If filename doesn't already exist in dictionary add it and it's
           # pet label - otherwise print an error message because indicates 
           # duplicate files (filenames)
           if pet_image not in results_dic:
             results_dic[pet_image] = [pet_name]
              
           else:
             print("** Warning: Duplicate files exist in directory:", 
                   file_name)

    return results_dic
