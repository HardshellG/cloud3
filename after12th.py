import streamlit as st
import pandas as pd

def app():
  st.title("Engineering Exams")



  df=pd.read_csv("after12th.csv")

  st.write(df)

 


