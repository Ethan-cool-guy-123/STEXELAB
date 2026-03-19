import streamlit as st
from streamlit_drawable_canvas import st_canvas
import pandas as pd
import numpy as np
from streamlit import sidebar
from PIL import Image
from datetime import datetime
import random
import time
import matplotlib.pyplot as plt
import urllib.parse
from streamlit_ace import st_ace

from datetime import date

current_hour = datetime.now().hour

st.markdown("""
<style>
@keyframes slideBounceRotate {
    0% {
        transform: translateX(-400px) rotate(-360deg);
        opacity: 0;
    }
    50% {
        transform: translateX(30px) rotate(15deg);
        opacity: 1;
    }
    70% {
        transform: translateX(-15px) rotate(-8deg);
    }
    85% {
        transform: translateX(8px) rotate(4deg);
    }
    100% {
        transform: translateX(0px) rotate(0deg);
    }
}

.title {
    font-size: 50px;
    font-weight: bold;
    text-align: center;
    margin-top: 20px;
    animation: slideBounceRotate 1.2s ease-out;
}
</style>

<div class="title">StExLab V1 </div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; animation: fadeIn 2s ease-in;">
     A streamlit code playground
</div>
""", unsafe_allow_html=True)

if "running" not in st.session_state:
    st.session_state.running = False

if "error_msg" not in st.session_state:
    st.session_state.error_msg = ""

if "code" not in st.session_state:
    st.session_state.code = 'st.write("Hello World!")'

st.write(f"Coding challenge: {"https://www.google.com/search?q=python+coding+challenges+for+streamlit"}")

mode = st.selectbox(
    "Editor Style",
    ["Classic", "Dark", "Bright", "Blue Night"]
)

themes = {
    "Classic": "github",
    "Dark": "monokai",
    "Bright": "tomorrow_night_bright",
    "Blue Night": "tomorrow_night_blue"
}

st.session_state.code = st_ace(
    value=st.session_state.code,
    language="python",
    theme=themes[mode],
    height=450
)

ai_code = st.text_area("Ask ChatGPT for code:")

encoded = urllib.parse.quote(ai_code)

chatgpt_link = f"https://chat.openai.com/?q={"Can you make me a code for: " + encoded + " in Python using Streamlit?" + " Code (ignore if it isnt significant like a write statement): " + st.session_state.code}"

st.link_button("Ask for code from ChatGPT", chatgpt_link)

characters = len(st.session_state.code)
lines = st.session_state.code.count("\n") + 1
words = len(st.session_state.code.split())
st.caption(f"Characters: {characters}")
st.caption(f"Lines: {lines}")
st.caption(f"Words: {words}")

if st.button("Run code?"):
    if st.session_state.running:
        st.session_state.running = False
    else:
        st.session_state.running = True

if st.session_state.running:
    try:
        exec(st.session_state.code)

    except Exception as er:
        st.session_state.error_msg = str(er)
        st.error(f"Error -> {er}")

        question = f"""
How do I fix this error in Streamlit?

Error:
{st.session_state.error_msg}

Code:
{st.session_state.code}
"""

        encoded = urllib.parse.quote(question)

        chatgpt_link = f"https://chat.openai.com/?q={encoded}"

        st.link_button("Get help from ChatGPT", chatgpt_link)

current_hour = datetime.now().hour

night = current_hour >= 19 or current_hour < 6

day_bg = "#ffffff"
day_text = "#000000"
night_bg = "#1e1e1e"
night_text = "#ffffff"

if night:
    st.markdown(f"""
    <style>
    textarea {{
        background-color: {night_bg} !important;
        color: {night_text} !important;
        transition: background-color 2s ease, color 2s ease;
    }}
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"""
    <style>
    textarea {{
        background-color: {day_bg} !important;
        color: {day_text} !important;
        transition: background-color 2s ease, color 2s ease;
    }}
    </style>
    """, unsafe_allow_html=True)