
# # # Crop Yield Prediction
# import pandas as pd
# import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import pickle as pk
# import time
# import warnings
# warnings.filterwarnings('ignore')

# data = pd.read_csv('crop_yield.csv')

# ## only for encoding purpose
# data_new = data.copy(deep = True)

# # Apply transformation to string values in the 'Crop', 'Season', and 'State' columns
# columns_to_transform = ['Crop', 'Season', 'State']

# for column in columns_to_transform:
#     data_new[column] = data_new[column].apply(
#         lambda x: x.lower().replace(" ", "").replace("/", "").replace("(", "").replace(")", "") if isinstance(x, str) else x)

# columns = ['Crop', 'Season', 'State']
# from sklearn.preprocessing import LabelEncoder
# encoder = LabelEncoder()
# for col in columns:
#     data[col] = encoder.fit_transform(data[col])

# data.drop(columns = ["Crop_Year"], inplace = True)

# # X = data.iloc[:,:-1]
# # y = data.iloc[:,-1]

# # from sklearn.model_selection import train_test_split
# # X_train, X_test, y_train, y_test = train_test_split(X, y, random_state= 42, test_size= 0.2)

# # from sklearn.ensemble import ExtraTreesRegressor
# # from sklearn.metrics import r2_score
# # # Create ExtraTreesRegressor with custom parameters
# # model = ExtraTreesRegressor(
# #     n_estimators=100,
# #     criterion='squared_error',  # Use 'squared_error' for Mean Squared Error
# #     max_depth=None,
# #     min_samples_split=2,
# #     min_samples_leaf=1,
# #     max_features=5,
# #     random_state=1000
# # )

# # model.fit(X_train, y_train)

# # predictions = model.predict(X_test)

# def encoding(input_data):
#     try:
#         input_data[0] = (data[data_new.Crop == input_data[0].lower().replace(" ", "").replace(" ", "").replace(" ", "").replace("/", "").replace("(", "").replace(")", "")]["Crop"]).to_list()[0]
#         input_data[1] = (data[data_new.Season== input_data[1].lower().replace(" ", "").replace(" ", "").replace(" ", "").replace("/", "").replace("/", "").replace("(", "").replace(")", "")]["Season"]).to_list()[0]
#         input_data[2] = (data[data_new.State== input_data[2].lower().replace(" ", "").replace(" ", "").replace(" ", "").replace("/", "").replace("(", "").replace(")", "")]["State"]).to_list()[0]
#         return input_data
#     except:
#         return None



#     # if (input_data[0] not in data["Crop"]) or (input_data[1] not in data["Season"]) or (input_data[2] not in data["State"]):
#     #     input_data=0
#     #     return input_data
#     # else :
#     #     return input_data
        
        

# # crop yield prediction Block
# crop_yield_model = pk.load(open('crop_yield_model.pkl','rb'))

# def crop_yield_prediction(input_data):
#     input_data_asarray = np.asarray(input_data)
#     input_data_reshaped = input_data_asarray.reshape(1,-1)
#     prediction = crop_yield_model.predict(input_data_reshaped)
#     return prediction

# # images links:
# # https://scx2.b-cdn.net/gfx/news/hires/2019/8-crops.jpg
# # https://us.123rf.com/450wm/vittuperkele/vittuperkele1804/vittuperkele180400186/100517230-growing-green-crop-fields-at-late-evening-blue-sky-with-clouds-in-countryside-fresh-air-clean.jpg?ver=6


# def Crop_yield():
#     st.title('Crop Yield Prediction')
#     background_image = ' https://us.123rf.com/450wm/vittuperkele/vittuperkele1804/vittuperkele180400186/100517230-growing-green-crop-fields-at-late-evening-blue-sky-with-clouds-in-countryside-fresh-air-clean.jpg?ver=6'
#     html_code = f"""
#         <style>
#             body {{
#                 background-image: url('{background_image}');
#                 background-size: cover;
#                 background-position: center;
#                 background-repeat: no-repeat;
#                 height: 100vh;  /* Set the height of the background to fill the viewport */
#                 margin: 0;  /* Remove default body margin */
#                 display: flex;
#                 flex-direction: column;
#                 justify-content: center;
#                 align-items: center;
#             }}
#             .stApp {{
#                 background: none;  /* Remove Streamlit app background */
#             }}
#         </style>
#     """
#     st.markdown(html_code, unsafe_allow_html=True)
    
#     col1, col2 = st.columns(2)
#     # c1,c2,c3 = st.columns([3,0.5,0.5])
#     crop = col1.selectbox(':black[Enter crop type]',('Arecanut', 'Arhar/Tur', 'Castor seed', 'Coconut ', 'Cotton(lint)',
#        'Dry chillies', 'Gram', 'Jute', 'Linseed', 'Maize', 'Mesta',
#        'Niger seed', 'Onion', 'Other  Rabi pulses', 'Potato',
#        'Rapeseed &Mustard', 'Rice', 'Sesamum', 'Small millets',
#        'Sugarcane', 'Sweet potato', 'Tapioca', 'Tobacco', 'Turmeric',
#        'Wheat', 'Bajra', 'Black pepper', 'Cardamom', 'Coriander',
#        'Garlic', 'Ginger', 'Groundnut', 'Horse-gram', 'Jowar', 'Ragi',
#        'Cashewnut', 'Banana', 'Soyabean', 'Barley', 'Khesari', 'Masoor',
#        'Moong(Green Gram)', 'Other Kharif pulses', 'Safflower',
#        'Sannhamp', 'Sunflower', 'Urad', 'Peas & beans (Pulses)',
#        'other oilseeds', 'Other Cereals', 'Cowpea(Lobia)',
#        'Oilseeds total', 'Guar seed', 'Other Summer Pulses', 'Moth'))
#     season = col2.text_input('Enter season',"Whole Year")
#     state = col1.selectbox('Enter state',('Assam', 'Karnataka', 'Kerala', 'Meghalaya', 'West Bengal',
#        'Puducherry', 'Goa', 'Andhra Pradesh', 'Tamil Nadu', 'Odisha',
#        'Bihar', 'Gujarat', 'Madhya Pradesh', 'Maharashtra', 'Mizoram',
#        'Punjab', 'Uttar Pradesh', 'Haryana', 'Himachal Pradesh',
#        'Tripura', 'Nagaland', 'Chhattisgarh', 'Uttarakhand', 'Jharkhand',
#        'Delhi', 'Manipur', 'Jammu and Kashmir', 'Telangana',
#        'Arunachal Pradesh', 'Sikkim'))
#     area = col2.number_input("Enter area (e.g., in ha)", min_value=1.0, max_value=10000000.0, value=6637.0, step=1.0, format="%f", help="Enter the area in Hacter")
#     production = col1.number_input('Enter production (e.g., in kg)',value=4680,min_value=100,max_value=10000000,step=10)
#     annual_rainfall = col2.number_input('Enter annual rainfall (e.g., in mm)',value=2051.4,min_value=100.0,max_value=10000000.0,step=100.0)
#     fertilizer = col1.number_input('Enter fertilizer (e.g., in kg)',value=631643.29,min_value=1.0,max_value=10000000.0,step=10.0)
#     pesticide = col2.number_input('Enter pesticide (e.g., in kg)',value=2057.47,min_value=1.0,max_value=10000000.0,step=10.0)
    
#     prediction = ''
    
#     if st.button('Submit'):
#         encode = encoding([crop, season, state, area, production, annual_rainfall, fertilizer, pesticide])
#         try:
#             prediction = crop_yield_prediction(list(encode))
#             progress = st.progress(0)
#             for i in range(100):
#                 time.sleep(0.005)
#                 progress.progress(i+1)
#             st.subheader(f"Crop Yied: {round(prediction[0],3)} kg/ha")
#         except:
#             st.error("Invalid Inputs")


# # Crop Yield Prediction
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle as pk
import time
import warnings
import dash as dsh
import requests
from PIL import Image, ImageDraw, ImageFont
warnings.filterwarnings('ignore')

data = pd.read_csv('crop_yield.csv')

## only for encoding purpose
data_new = data.copy(deep = True)

# Apply transformation to string values in the 'Crop', 'Season', and 'State' columns
columns_to_transform = ['Crop', 'Season', 'State']

for column in columns_to_transform:
    data_new[column] = data_new[column].apply(
        lambda x: x.lower().replace(" ", "").replace("/", "").replace("(", "").replace(")", "") if isinstance(x, str) else x)

columns = ['Crop', 'Season', 'State']
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
for col in columns:
    data[col] = encoder.fit_transform(data[col])

data.drop(columns = ["Crop_Year"], inplace = True)

def get_location():
    # Using the IPinfo API to get location based on IP address
    ipinfo_api_key = "a0b55644-ffe1-4c78-bf83-3ae35b2b72b9"
    ipinfo_url = f"http://ipinfo.io?token={ipinfo_api_key}"
    
    # response = requests.get(ipinfo_url)
    # data = response.json()
    
    # state = data.get("region")
    return "Karnataka"

def get_weather(city):
    # Using the OpenWeatherMap API to get weather information based on city name
    openweathermap_api_key = "d73ec4f18aca81c32b1836a8ac2506e0"
    openweathermap_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweathermap_api_key}"
    
    response = requests.get(openweathermap_url)
    data = response.json()
    
    return data.get("weather")[0].get("main")

# X = data.iloc[:,:-1]
# y = data.iloc[:,-1]

# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state= 42, test_size= 0.2)

# from sklearn.ensemble import ExtraTreesRegressor
# from sklearn.metrics import r2_score
# # Create ExtraTreesRegressor with custom parameters
# model = ExtraTreesRegressor(
#     n_estimators=100,
#     criterion='squared_error',  # Use 'squared_error' for Mean Squared Error
#     max_depth=None,
#     min_samples_split=2,
#     min_samples_leaf=1,
#     max_features=5,
#     random_state=1000
# )

# model.fit(X_train, y_train)

# predictions = model.predict(X_test)

from datetime import datetime

from datetime import datetime

def get_season(month):
    # Mapping of months to seasons
    month_to_season = {
        1: 'Winter', 2: 'Winter', 3: 'Spring',
        4: 'Spring', 5: 'Spring', 6: 'Summer',
        7: 'Summer', 8: 'Summer', 9: 'Autumn',
        10: 'Autumn', 11: 'Autumn', 12: 'Winter'
    }

    # Get the season based on the month
    season = month_to_season.get(month, 'Invalid Month')
    
    return season

# Example: Get the season for a specific month
current_month = datetime.now().month
current_season = get_season(current_month)
current_state = get_location()




def encoding(input_data):
    try:
        input_data[0] = (data[data_new.Crop == input_data[0].lower().replace(" ", "").replace(" ", "").replace(" ", "").replace("/", "").replace("(", "").replace(")", "")]["Crop"]).to_list()[0]
        input_data[1] = (data[data_new.Season== input_data[1].lower().replace(" ", "").replace(" ", "").replace(" ", "").replace("/", "").replace("/", "").replace("(", "").replace(")", "")]["Season"]).to_list()[0]
        input_data[2] = (data[data_new.State== input_data[2].lower().replace(" ", "").replace(" ", "").replace(" ", "").replace("/", "").replace("(", "").replace(")", "")]["State"]).to_list()[0]
        return input_data
    except:
        return None



    # if (input_data[0] not in data["Crop"]) or (input_data[1] not in data["Season"]) or (input_data[2] not in data["State"]):
    #     input_data=0
    #     return input_data
    # else :
    #     return input_data
        
        

# crop yield prediction Block
crop_yield_model = pk.load(open('crop_yield_model.pkl','rb'))

def crop_yield_prediction(input_data):
    input_data_asarray = np.asarray(input_data)
    input_data_reshaped = input_data_asarray.reshape(1,-1)
    prediction = crop_yield_model.predict(input_data_reshaped)
    return prediction

# images links:
# https://scx2.b-cdn.net/gfx/news/hires/2019/8-crops.jpg
# https://us.123rf.com/450wm/vittuperkele/vittuperkele1804/vittuperkele180400186/100517230-growing-green-crop-fields-at-late-evening-blue-sky-with-clouds-in-countryside-fresh-air-clean.jpg?ver=6


def Crop_yield():
    tab1, tab2 = st.tabs(["Crop Labels", "Crop Yield"])
    with tab1:
        def display_images_in_columns(dictionary, num_columns=2):
            num_images = len(dictionary)
            num_rows = -(-num_images // num_columns)  # Ceiling division to calculate rows

            for i in range(num_rows):
                cols = st.columns(num_columns)
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

                            'Barley': 'https://www.poshtik.in/cdn/shop/products/com1807851487263barley_Poshtik_c1712f8e-6b63-4231-9596-a49ce84f26ba.png?v=1626004318',
                            'Gram (Chickpea)': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHtf9ivxD23Bp_-VOY4H2tCRMC0_znhzyAEt2jfzvUlskEZcv0',
                            'Tur (Pigeonpea)': 'https://rukminim2.flixcart.com/image/850/1000/xif0q/plant-seed/f/l/n/25-pigeon-pea-for-planting-home-garden-farming-vegetable-kitchen-original-imaghphgmepkjqfz.jpeg?q=90',
                            'Moong (Green Gram)': 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTyIa1Wq11MaHZ_cIdArPjZSR8cnr85STU83QsjKvkI9xNdVDjJ',
                            'Urad (Black gram)': 'https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcRl-eFmBSLAHxB7U_b_SQNptQoQpi585JWgpqU0LH0jmvmrp9mESzQrL3ieox6ICl_-v7rzl38Pi7faf-4',
                            'Masoor (Red lentil)': 'https://www.vegrecipesofindia.com/wp-content/uploads/2022/11/masoor-dal-red-lentils.jpg',
                            'Groundnut (Peanut)': 'https://www.netmeds.com/images/cms/wysiwyg/blog/2019/10/Groundnut_big_2.jpg',
                            'Sesamum (Sesame)': 'https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcThAjpal-k0urS19A2NEoVW35yqF9ljlvx1d-amDokoIiHZ9-RGyUsDaiVcr7SdfwsFjP-I6U1_VYeiEc0',
                            'Castor seed': 'https://5.imimg.com/data5/QV/VN/MY-3966004/caster-seeds.jpg',
                            'Sunflower': 'https://t0.gstatic.com/licensed-image?q=tbn:ANd9GcRuCcoGrqSVqOzxFU9rHPsWKxaHpm7i_srXQPMHaVfrrDmz4eXc5PGWpQFfpAr8qaH2',
                            'Safflower': 'https://upload.wikimedia.org/wikipedia/commons/7/7f/Safflower.jpg',
                            'Sugarcane': 'https://www.saveur.com/uploads/2022/03/05/sugarcane-linda-xiao.jpg?auto=webp',
                            'Cotton (lint)': 'https://img2.tradewheel.com/uploads/images/products/6/0/0048590001615360690-cotton-lint.jpeg.webp',
                            'Jute': 'https://rukminim2.flixcart.com/image/850/1000/kuk4u4w0/rope/d/k/f/2-jute-cord-for-craft-project-natural-jute-rope-jute-thread-original-imag7nrjbkrmgbpm.jpeg?q=20',
                            'Potato': 'https://cdn.mos.cms.futurecdn.net/iC7HBvohbJqExqvbKcV3pP.jpg',
                            'Onion': 'https://familyneeds.co.in/cdn/shop/products/2_445fc9bd-1bab-4bfb-8d5d-70b692745567_600x600.jpg?v=1600812246',
                            'Tomato': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Tomato_je.jpg/1200px-Tomato_je.jpg',
                            'Banana': 'https://fruitboxco.com/cdn/shop/products/asset_2_grande.jpg?v=1571839043',
                            'Coconut': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_rZgOJry6Twt8urk4C1FTo6d6tEDyiIw39w&usqp=CAU'}


        display_images_in_columns(image_dictionary)
    with tab2:
        st.title('Crop Yield Prediction')
        background_image = ' https://us.123rf.com/450wm/vittuperkele/vittuperkele1804/vittuperkele180400186/100517230-growing-green-crop-fields-at-late-evening-blue-sky-with-clouds-in-countryside-fresh-air-clean.jpg?ver=6'
        html_code = f"""
            <style>
                body {{
                    background-image: url('{background_image}');
                    background-size: cover;
                    background-position: center;
                    background-repeat: no-repeat;
                    height: 100vh;  /* Set the height of the background to fill the viewport */
                    margin: 0;  /* Remove default body margin */
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                }}
                .stApp {{
                    background: none;  /* Remove Streamlit app background */
                }}
            </style>
        """
        st.markdown(html_code, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        # c1,c2,c3 = st.columns([3,0.5,0.5])
        crop = col1.selectbox(':black[Enter crop type]',('Arecanut', 'Arhar/Tur', 'Castor seed', 'Coconut ', 'Cotton(lint)',
        'Dry chillies', 'Gram', 'Jute', 'Linseed', 'Maize', 'Mesta',
        'Niger seed', 'Onion', 'Other  Rabi pulses', 'Potato',
        'Rapeseed &Mustard', 'Rice', 'Sesamum', 'Small millets',
        'Sugarcane', 'Sweet potato', 'Tapioca', 'Tobacco', 'Turmeric',
        'Wheat', 'Bajra', 'Black pepper', 'Cardamom', 'Coriander',
        'Garlic', 'Ginger', 'Groundnut', 'Horse-gram', 'Jowar', 'Ragi',
        'Cashewnut', 'Banana', 'Soyabean', 'Barley', 'Khesari', 'Masoor',
        'Moong(Green Gram)', 'Other Kharif pulses', 'Safflower',
        'Sannhamp', 'Sunflower', 'Urad', 'Peas & beans (Pulses)',
        'other oilseeds', 'Other Cereals', 'Cowpea(Lobia)',
        'Oilseeds total', 'Guar seed', 'Other Summer Pulses', 'Moth'))
        season = current_season
        state = get_location()
        area = col2.number_input("Enter area (e.g., in ha)", min_value=1.0, max_value=10000000.0, value=6637.0, step=1.0, format="%f", help="Enter the area in Hacter")
        production = col1.number_input('Enter production (e.g., in kg)',value=area*0.03,min_value=100.0,max_value=area*1.5,step=10.0)
        annual_rainfall = col2.number_input('Enter annual rainfall (e.g., in mm)',value=2051.4,min_value=100.0,max_value=2000.0,step=100.0)
        fertilizer = col1.number_input('Enter fertilizer (e.g., in g)',value=631643.29,min_value=1.0,max_value=10000000.0,step=10.0)
        pesticide = col2.number_input('Enter pesticide (e.g., in g)',value=2057.47,min_value=1.0,max_value=10000000.0,step=10.0)
        
        prediction = ''
        
        if st.button('Submit'):
            encode = encoding([crop, season, state, area, production, annual_rainfall, fertilizer, pesticide])
            try:
                prediction = crop_yield_prediction(list(encode))
                progress = st.progress(0)
                for i in range(100):
                    time.sleep(0.005)
                    progress.progress(i+1)
                st.subheader(f"Crop Yied: {round(prediction[0],3)} kg/ha")
            except:
                st.error("Invalid Inputs")



if __name__ == '__main__':
    Crop_yield()
