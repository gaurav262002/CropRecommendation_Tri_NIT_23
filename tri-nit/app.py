import streamlit as st
import pandas as pd
import numpy as np

st.title('Crop Recommendation')

state = st.multiselect(
    'State',
    ['Andaman and Nicobar', 'Assam', 'Gujarat', 'Haryana',
       'Himachal pradesh', 'Karnataka', 'Kerala', 'Madhya pradesh',
       'Maharashtra', 'Manipur', 'Meghalaya', 'Odisha', 'Punjab',
       'Rajasthan', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar pradesh',
       'Uttrakhand', 'West Bengal'],max_selections=1)

season = st.multiselect('Season',["Kharif","Rabi","Zaid"],max_selections=1)
price = st.slider('Price per quintal/100kg', 4000, 11000,4000)

state_dict = {'Andaman and Nicobar': 0,
 'Assam': 1,
 'Gujarat': 2,
 'Haryana': 3,
 'Himachal Pradesh': 4,
 'Karnataka': 5,
 'Kerala': 6,
 'Madhya Pradesh': 7,
 'Maharashtra': 8,
 'Manipur': 9,
 'Meghalaya': 10,
 'Odisha': 11,
 'Punjab': 12,
 'Rajasthan': 13,
 'Tamil Nadu': 14,
 'Telangana': 15,
 'Tripura': 16,
 'Uttar Pradesh': 17,
 'Uttrakhand': 18,
 'West Bengal': 19}

if st.button('Recommend'):
    st.write('The Recommended crop is', state_dict[state[0]] )  

result =0

feature = [st]