from bs4 import BeautifulSoup
import requests
import streamlit as st
from PIL import Image

im = Image.open('image/favicon.ico')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

st.set_page_config(page_title='WEATHER FORECASTER',
                   page_icon=im,
                   layout='centered',
                   initial_sidebar_state='auto')

st.image('image/logo.png')
st.title(" 📅 WEATHER FORECASTER 🌥️ ☔ ")

def user_input_features():
    city = st.text_input('   Name of Any City 🌆 ')
    city=city+" weather"
    return city

p = user_input_features()

def weather(city):
    city=city.replace(" ","+")
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')   
    location = soup.select('#wob_loc')[0].getText().strip()  
    time = soup.select('#wob_dts')[0].getText().strip()       
    info = soup.select('#wob_dc')[0].getText().strip() 
    weather = soup.select('#wob_tm')[0].getText().strip()
    st.subheader(location)
    st.write("📅",time)
    st.write("⛅️",info)
    st.write("🌡️ Temperature:",weather+"°C")

if st.button('Prediction'):
    weather(p)
else:
    st.info("Please enter a Valid city name")