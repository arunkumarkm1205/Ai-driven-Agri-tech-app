# import streamlit as st
# import pandas as pd
# import pydeck as pdk
# import pickle
# import time

# def insurance_app():
#     tab1, tab2 = st.tabs(["Know the risk","Contribute to the dataset"]) 
#     with tab1:    
#         st.title('Predict Paid Claims - (Rs. in crore)')
#         background_image = 'https://img.freepik.com/premium-photo/photo-coins-plant-black-background-with-empty-space-text-design-elements_176841-5042.jpg'
#         html_code =  f"""
#             <style>
#                 body {{
#                     background-image: url('{background_image}');
#                     background-size: cover;
#                     background-position: center;
#                     background-repeat: no-repeat;
#                     height: 100vh;  /* Set the height of the background to fill the viewport */
#                     margin: 0;  /* Remove default body margin */
#                     display: flex;
#                     flex-direction: column;
#                     justify-content: center;
#                     align-items: center;
#                 }}
#                 .stApp {{
#                     background: none;  /* Remove Streamlit app background */
#                 }}
#             </style>
#         """
#         st.markdown(html_code, unsafe_allow_html=True)

#         lasso_model = pickle.load(open('Lasso Regression.pkl','rb'))
#         # st.subheader('Enter Input Values')
#         col1,col2,col3 = st.columns([1,1,1])
#         with col1:
#             reported_claims = st.number_input('Reported Claims (Rs. in crore)', value=531.4,min_value=1.0,max_value=1000.0,step=0.1)
#         with col1:
#             approved_claims = st.number_input('Approved Claims (Rs. in crore)', value=502.0,min_value=1.0,max_value = reported_claims,step=0.1)
#         with col1:
#             claims_outstanding = st.number_input('Claims Outstanding (Rs. in crore)', value=16.05,min_value=1.0,max_value=1000.0,step=0.1)
#         with col2:
#             farmer_applications = st.number_input('Farmer Applications(In Lakh)', value=6.4,min_value=1.0,max_value=100.0,step=0.1)
#         with col2:
#             state_ut_name = st.selectbox('State/UT Name',('Andaman and Nicobar Islands' ,'Assam' ,'Chhattisgarh', 'Goa' ,'Haryana',
#                                                         'Himachal Pradesh', 'Karnataka', 'Kerala' ,'Madhya Pradesh' ,'Maharashtra',
#                                                         'Meghalaya', 'Odisha', 'Puducherry', 'Rajasthan', 'Sikkim', 'Tamil Nadu',
#                                                         'Tripura', 'Uttar Pradesh', 'Uttarakhand'),key="unique_key_2")

#         input_data = pd.DataFrame({
#             'State/UT Name': [state_ut_name],
#             'Reported Claims - (Rs. in crore)': [reported_claims],
#             'Approved Claims - (Rs. in crore)': [approved_claims],
#             'Claims Outstanding as per Reported Claims - (Rs. in crore)': [claims_outstanding],
#             'Farmer Applications Benefitted (In Lakh)': [farmer_applications]
#         })
        

#         if st.button('Predict'):
#             try:
#                 prediction = lasso_model.predict(input_data)[0]
#                 progress = st.progress(0)
#                 for i in range(100):
#                     time.sleep(0.005)
#                     progress.progress(i+1)            
#                 st.subheader('Predicted Paid Claims - (Rs. in crore)')
#                 st.header(prediction.round(3))
#                 # htmlsd = '<h4 style="color: red;">' + str(prediction.round(3)) + '</h4>'
#                 # st.markdown(htmlsd, unsafe_allow_html=True)
#             except:
#                 st.error("Invalid Input")

#     with tab2:
#         df = pd.read_csv('insurance.csv')
#         st.title('Contribute to dataset')
#         col1,col2,col3 = st.columns(3)
#         with col1:
#             state_ut_name = st.selectbox('State/UT Name',('Andaman and Nicobar Islands' ,'Assam' ,'Chhattisgarh', 'Goa' ,'Haryana',
#                                                         'Himachal Pradesh', 'Karnataka', 'Kerala' ,'Madhya Pradesh' ,'Maharashtra',
#                                                         'Meghalaya', 'Odisha', 'Puducherry', 'Rajasthan', 'Sikkim', 'Tamil Nadu',
#                                                         'Tripura', 'Uttar Pradesh', 'Uttarakhand'),key="unique_key_1")
#         with col2:
#             reported_claims = st.number_input('Reported Claims (Rs. in crore)', value=531.4,min_value=1.0,max_value=1000.0,step=0.1,key=2)
#         with col1:
#             approved_claims = st.number_input('Approved Claims (Rs. in crore)', value=502.0,min_value=1.0,max_value = reported_claims,step=0.1,key=3)
#         with col1:
#             claims_outstanding = st.number_input('Claims Outstanding (Rs. in crore)', value=16.05,min_value=1.0,max_value=1000.0,step=0.1,key=4)
#         with col2:
#             farmer_applications = st.number_input('Farmer Applications (in Lacks)', value=6.4,min_value=1.0,max_value=100.0,step=0.1,key=5)
#         new_data = {'State/UT Name': state_ut_name,
#                     'Reported Claims - (Rs. in crore)': reported_claims,
#                     'Approved Claims - (Rs. in crore)': approved_claims,
#                     'Claims Outstanding as per Reported Claims - (Rs. in crore)': claims_outstanding,
#                     'Farmer Applications Benefitted (In Lakh)': farmer_applications}
        
#         if st.button('Contribute'):
#             new_df = pd.DataFrame(new_data, index=[0]) 
#             combined_df = pd.concat([df, new_df], ignore_index=True)
#             combined_df.to_csv('insurance.csv', index=False)
#             st.success('Thank You for your contribution')

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle as pk
import time 
import base64
import Agri_chatbot as ag
import Crop_yield as cy
import Weather_app
import Rain_Forecast as rf
import Crop_Recommendation as cr
import Crop_disease_prediction as disease
import streamlit_option_menu as option_menu
import feedbacko as feed
from Insurance_risk import insurance_app
from Mail import send_confirmation_email
from auth_module import account_creation, login

# 📊🌦️🌾🌱🛡️🦠

# streamlit_app.py
class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            'title': title,
            'function': function
        })

    def run(self):
        with st.sidebar:
            st.markdown(
                """
                <style>
                    .sidebar-container {
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                        text-align: center;
                    }
                    .round-image-container {
                        width: 150px;
                        height: 150px;
                        overflow: hidden;
                        border-radius: 50%;
                        border: 5px solid white;  /* Optional: Add a border */
                    }
                    .round-image {
                        width: 100%;
                        height: 100%;
                        object-fit: cover;
                    }
                </style>
                """,
                unsafe_allow_html=True,
            )
            # Create a container div for the sidebar
            st.sidebar.markdown(
                """
                <div class="sidebar-container">
                    <div class="round-image-container">
                        <img class="round-image" src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQaOVenJRaGjCo3YJo_BokKwl76iwwW30omaw&usqp=CAU'>
                    </div>
                    <br>
                </div>
                """,
                unsafe_allow_html=True,
            )
            selected_app = option_menu.option_menu(
                menu_title='AgriTech Service',
                options=["Weather Forecast", "Crop Recommendation", "Crop Disease", "Crop Yield",  "Insurance Risk","Feedback"],
                default_index=0,
                styles={
                    'container': {'padding': '5!important', 'background-color': 'black'},
                    'nav-link': {'color': 'white', 'font-size': '20px', 'text-align': 'left', 'margin': '0px',
                                '--hover-color': 'blue'},
                    'nav-link-selected': {'background-color': '#02ab21'}
                }
            )

        for app in self.apps:
            if selected_app == app['title']:
                app['function']()

def main():
    # st.title("AgriTech Dashboard")
    authenticated = is_user_authenticated()
    if not authenticated:
        authentication_section()
    else:
        app_interface()

def authentication_section():
    st.title("AgriTech")
    choice = st.sidebar.selectbox("Login/Create Account", ['Login','Create Account'])
    if choice == "Login":
        login_section()
    elif choice == "Create Account":
        create_account_section()

def login_section():
    st.header("Login")
    username_or_email = st.text_input("Username or Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        result = login(username_or_email, password)
        if result == "Login successful":
            progress = st.progress(0)
            for i in range(100):
                time.sleep(0.005)
                progress.progress(i+1)

            st.success("Login successful")
            st.experimental_set_query_params(logged_in=True)
            st.experimental_rerun()
        else:
            st.warning(result)

def create_account_section():
    st.header("Create Account")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Create Account"):
        try:
            send_confirmation_email(email, username)
            progress = st.progress(0)
            for i in range(100):
                time.sleep(0.005)
                progress.progress(i+1)            
            result = account_creation(username, email, password)
            if result == "Account created successfully":
                st.success(result)
            else:
                st.warning(result)
        except:
            st.error("Invalid Email")
            
def app_interface():
    multi_app = MultiApp()
    # multi_app.add_app("Agri ChatBot", ag.chatbot)
    multi_app.add_app("Weather Forecast", Weather_app.weather_forecast_app)
    multi_app.add_app("Crop Yield", cy.Crop_yield)
    multi_app.add_app("Crop Recommendation", cr.run_crop_recommendation)
    multi_app.add_app("Crop Disease",disease.disease_app)
    # multi_app.add_app("Insurance Risk",insurance_app)
    # multi_app.add_app("Feedback",feed.run_feedback)
    multi_app.run()

# Add the following code at the end of the file to handle the redirection
def is_user_authenticated():
    return "logged_in" in st.experimental_get_query_params()

if __name__ == "__main__":
    main()


