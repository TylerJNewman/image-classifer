#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os


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
    filename_list = os.listdir(image_dir)
    results_dic = {}
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
