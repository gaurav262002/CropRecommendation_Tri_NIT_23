
import streamlit as st

import pandas as pd
import numpy as np

import pickle


st.title('Crop Recommendation')

state = st.multiselect(
    'State',
    ['Andaman and Nicobar', 'Assam', 'Gujarat', 'Haryana',
       'Himachal Pradesh', 'Karnataka', 'Kerala', 'Madhya Pradesh',
       'Maharashtra', 'Manipur', 'Meghalaya', 'Odisha', 'Punjab',
       'Rajasthan', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
       'Uttrakhand', 'West Bengal'],max_selections=1)

season = st.multiselect('Season',["Kharif","Rabi","Zaid"],max_selections=1)
price = st.slider('Price per quintal/100kg', 475, 8000,475)

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

season_dict ={'Kharif': 0, 'Zaid': 1, 'Rabi': 2}

result_dict={0: 'Coconut',
 1: 'Rice',
 2: 'Jute',
 3: 'Maize',
 4: 'Cotton',
 5: 'Banana',
 6: 'Grapes',
 7: 'Apple',
 8: 'Orange',
 9: 'Pomegranate',
 10: 'Papaya',
 11: 'Mango'}

v = (price -3326.175159)/1798.630513


print(state)



if st.button('Recommend'):
    loaded_model = pickle.load(open("model.pkl", 'rb'))
    feature = [[state_dict[state[0]],season_dict[season[0]],v ]]
    result=loaded_model.predict(feature)
    
    st.write('The Recommended crop is', result_dict[result[0]] )  



