
import streamlit as st
import time
import random
import numpy as np
import pandas as pd
import random
def app():
     st.title("Home")                              
st.write("Welcome to the Exam Timeline website, your one-stop destination for comprehensive and up-to-date information on examination schedules, deadlines, and important dates. Whether you're a student, educator, or professional seeking to stay organized, our platform is designed to help you navigate the world of exams with ease and confidence.")
st.write("## Exam time remaining ##")
progress_text = "Your jee exam is in 15 days."
my_bar = st.progress(0, text=progress_text)
for percent_complete in range(15):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
    




