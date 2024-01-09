#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

def display_images_in_columns(dictionary, num_columns=2):
    num_images = len(dictionary)
    num_rows = -(-num_images // num_columns)  # Ceiling division to calculate rows

    for i in range(num_rows):
        cols = st.beta_columns(num_columns)
        for j in range(num_columns):
            index = i * num_columns + j
            if index < num_images:
                label, url = list(dictionary.items())[index]
                cols[j].image(url, caption=label, use_column_width=True)

# Example dictionary (replace this with your actual dictionary)
image_dictionary = {'Wheat': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIp7ucodsB63giF1CvVjBtbHf14Px83ck2hcZRUJlMxA&s',
                'Rice': 'https://media.istockphoto.com/id/153737841/photo/rice.webp?b=1&s=170667a&w=0&k=20&c=SF6Ks-8AYpbPTnZlGwNCbCFUh-0m3R5sM2hl-C5r_Xc=',
                'Maize (Corn)': 'https://plus.unsplash.com/premium_photo-1667047165840-803e47970128?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8bWFpemV8ZW58MHx8MHx8fDA%3D',
                'Bajra (Pearl millet)': 'https://media.istockphoto.com/id/1400438871/photo/pear-millet-background.jpg?s=612x612&w=0&k=20&c=0GlBeceuX9Q_AZ0-CH57_A5s7_tD769N2f_jrbNcbrw=',
                'Jowar (Sorghum)': 'https://media.istockphoto.com/id/1262684430/photo/closeup-view-of-a-white-millet-jowar.jpg?s=612x612&w=0&k=20&c=HLyBy06EjbABKybUy1nIQTfxMLV1-s4xofGigOdd6dU=',

                'Barley': 'https://www.shutterstock.com/image-photo/barley-grain-on-wooden-background-2160377105',
                'Gram (Chickpea)': 'https://www.shutterstock.com/image-photo/raw-chickpeas-bowl-nutritious-food-healthy-1731073426',
                'Tur (Pigeonpea)': 'https://www.shutterstock.com/image-photo/fresh-green-pigeon-pea-other-names-2408559687',
                'Moong (Green Gram)': 'https://www.shutterstock.com/image-photo/dry-organic-split-half-moong-mung-1720137034',
                'Urad (Black gram)': 'https://www.shutterstock.com/image-photo/urad-gota-whole-table-top-shot-2345049023',
                'Masoor (Red lentil)': 'https://www.shutterstock.com/image-photo/close-organic-masoor-dal-lens-culinaris-1936459225',
                'Groundnut (Peanut)': 'https://www.shutterstock.com/image-photo/bunch-ecological-peanuts-on-white-2348588173',
                'Sesamum (Sesame)': 'https://www.shutterstock.com/image-photo/wooden-scoop-black-sesame-seeds-close-1976488430',
                'Castor seed': 'https://www.shutterstock.com/image-photo/ricinus-communis-dried-seeds-fruit-castor-2301488541',
                'Sunflower': 'https://www.shutterstock.com/image-photo/sunflower-background-yellow-field-2021151758',
                'Safflower': 'https://www.shutterstock.com/image-photo/colorful-beautiful-safflowers-flowers-summer-374093320',
                'Sugarcane': 'https://www.shutterstock.com/image-photo/sugar-cane-stalks-plantation-background-2214494057',
                'Cotton (lint)': 'https://www.pexels.com/photo/cotton-plant-with-dried-leaves-6168150/',
                'Jute': 'https://www.pexels.com/photo/a-man-with-jute-17778573/',
                'Potato': 'https://images.pexels.com/photos/2286776/pexels-photo-2286776.jpeg?auto=compress&cs=tinysrgb&w=400',
                'Onion': 'https://www.pexels.com/photo/raw-yellow-onions-in-square-plate-on-white-background-4197441/',
                'Tomato': 'https://www.pexels.com/photo/close-up-photo-of-unripe-tomatoes-5503107/',
                'Banana': 'https://www.pexels.com/photo/banana-tree-2168838/',
                'Coconut': 'https://www.pexels.com/photo/photo-of-coconut-tree-on-seashore-1576955/'}
    
    

