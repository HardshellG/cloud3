import streamlit as st
import pandas as pd

def app():
df=pd.read_csv("after12th.csv")
   st.write(df)

 


