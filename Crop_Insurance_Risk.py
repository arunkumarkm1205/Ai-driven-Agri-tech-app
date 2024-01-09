import streamlit as st
import pandas as pd
import pydeck as pdk
import pickle
import time
import sum_insurance as insu
import gross_premimum as gross
import numpy as np

def sum_insurance_prediction(input_data,crop_insurance_sum_Raghu):
    input_data_asarray = np.asarray(input_data)
    input_data_reshaped = input_data_asarray.reshape(1,-1)
    prediction = crop_insurance_sum_Raghu.predict(input_data_reshaped)
    return prediction

def crop_grosspremimum_pred(input_data,crop_insurance_sum_Raghu):
    input_data_asarray = np.asarray(input_data)
    input_data_reshaped = input_data_asarray.reshape(1,-1)
    prediction = crop_insurance_sum_Raghu.predict(input_data_reshaped)
    return prediction

def insurance_app():
    tab1, tab2 = st.tabs(["Maximum amount an insurance pay for a covered loss.","Total Amount insurance Paid by company in given period."]) 
    with tab1:    
        st.title('Predict Insurance Payout on loss')
        background_image = 'https://img.freepik.com/premium-photo/photo-coins-plant-black-background-with-empty-space-text-design-elements_176841-5042.jpg'
        html_code =  f"""
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

# season,scheme,state_name,district_name,area_insured,sum_insured,farmer_share,goi_share,state_share,iu_count
# kharif,PMFBY,Andhra Pradesh,Anantapur,17.44,9493.41,453.87,285.46,285.46,85
        
        crop_insurance_sum_Raghu = pickle.load(open('crop_insurance_sum_Raghu.pkl','rb'))
        # st.subheader('Enter Input Values')
        col1,col2 = st.columns([1,1])
        with col1:
            season1 = st.text_input('Season', 'kharif',key=1)
        with col1:
            scheme1 = st.text_input('Scheme', 'PMFBY',key=2)
        with col1:
            state_name1 = st.selectbox('State Name',('Assam' ,'Chhattisgarh', 'Goa' ,'Haryana',
                                                        'Himachal Pradesh', 'Karnataka', 'Kerala' ,'Madhya Pradesh' ,'Maharashtra',
                                                        'Meghalaya', 'Odisha', 'Puducherry', 'Rajasthan', 'Sikkim', 'Tamil Nadu',
                                                        'Tripura', 'Uttar Pradesh', 'Uttarakhand'),key=3)
        with col1:
            district_name1 = st.text_input('District Name', "Mandya",key=4)
        with col2:
            area_insured1 = st.number_input('Total Area Covered for Insurence', value=17.44,min_value=1.0,max_value=3777.0,step=1.0,key=5)
        with col2:
            farmer_share1 = st.number_input('Premium Paid by Individual', value=453.87,min_value=1.0,max_value=8600.32,step=10.0,key=6)
        with col2:
            goi_share1 = st.number_input('Premium Paid by GOI', value=285.46,min_value=1.0,max_value=33292.16,step=10.0,key=7)
        with col2:
            state_share1 = st.number_input('Premium Paid by Govt', value=285.46,min_value=1.0,max_value=40723.02,step=10.0,key=8)
        with col1:
            iu_count1 = st.number_input('Count of Insurence Units', value=85.0,min_value=1.0,max_value=2492.00,step=5.0,key=9)

        
        prediction1 = ''
        input_data = [season1,scheme1,state_name1,district_name1,area_insured1,farmer_share1,goi_share1,state_share1,iu_count1]
        if st.button('Predict'):
            encode = insu.encoding(input_data)
            try:
                prediction1 = sum_insurance_prediction(encode,crop_insurance_sum_Raghu)
                progress = st.progress(0)
                for i in range(100):
                    time.sleep(0.005)
                    progress.progress(i+1)
                st.subheader(f"Sum Insured: {round(prediction1[0],3)} Rupees")
            except:
                st.error("Invalid Inputs")




    with tab2:
        st.title('Gross Premium')
        # background_image = 'https://img.freepik.com/premium-photo/photo-coins-plant-black-background-with-empty-space-text-design-elements_176841-5042.jpg'
        # html_code =  f"""
        #     <style>
        #         body {{
        #             background-image: url('{background_image}');
        #             background-size: cover;
        #             background-position: center;
        #             background-repeat: no-repeat;
        #             height: 100vh;  /* Set the height of the background to fill the viewport */
        #             margin: 0;  /* Remove default body margin */
        #             display: flex;
        #             flex-direction: column;
        #             justify-content: center;
        #             align-items: center;
        #         }}
        #         .stApp {{
        #             background: none;  /* Remove Streamlit app background */
        #         }}
        #     </style>
        # """
        # st.markdown(html_code, unsafe_allow_html=True)

# season,scheme,state_name,district_name,area_insured,sum_insured,farmer_share,goi_share,state_share,iu_count,gross_premium
# kharif,PMFBY,Andhra Pradesh,Anantapur,17.44,9493.41,453.87,285.46,285.46,85,1024.79
        
        crop_grosspremimum = pickle.load(open('crop_grosspremimum_Jp.pkl','rb'))
        # st.subheader('Enter Input Values')
        col1,col2 = st.columns([1,1])
        with col1:
            season = st.text_input('Season', 'kharif')
        with col1:
            scheme = st.text_input('Scheme', 'PMFBY')
        with col1:
            state_name = st.selectbox('State Name',('Assam' ,'Chhattisgarh', 'Goa' ,'Haryana',
                                                        'Himachal Pradesh', 'Karnataka', 'Kerala' ,'Madhya Pradesh' ,'Maharashtra',
                                                        'Meghalaya', 'Odisha', 'Puducherry', 'Rajasthan', 'Sikkim', 'Tamil Nadu',
                                                        'Tripura', 'Uttar Pradesh', 'Uttarakhand'))
        with col1:
            district_name = st.text_input('District Name', "Mandya")
        with col2:
            area_insured = st.number_input('Total Area Covered for Insurence', value=17.44,min_value=1.0,max_value=3777.0,step=1.0)
        with col2:
            farmer_share = st.number_input('Premium Paid by Individual', value=453.87,min_value=1.0,max_value=8600.32,step=10.0)
        with col2:
            goi_share = st.number_input('Premium Paid by GOI', value=285.46,min_value=1.0,max_value=33292.15,step=10.0)
        with col2:
            state_share = st.number_input('Premium Paid by Govt', value=285.46,min_value=1.0,max_value=40723.02,step=10.0)
        with col1:
            iu_count = st.number_input('Count of Insurence Units', value=85.0,min_value=1.0,max_value=2492.00,step=5.0)
        with col2:
            sum_insured = st.number_input('YOur Sum Insured For The Crop', value=9493.41,min_value=1.0,max_value=535572.47,step=50.0)        
        
        prediction = ''
        input_data = [season,scheme,state_name,district_name,area_insured,sum_insured,farmer_share,goi_share,state_share,iu_count]
        if st.button('Predict',key=10):
            encode = gross.encoding(input_data)
            try:
                prediction = crop_grosspremimum_pred(encode,crop_grosspremimum)
                progress = st.progress(0)
                for i in range(100):
                    time.sleep(0.005)
                    progress.progress(i+1)
                st.subheader(f"gross premium: {round(prediction[0],3)} Rupees ")
            except:
                st.error("Invalid Inputs") 

if __name__=='__main__':
    insurance_app()