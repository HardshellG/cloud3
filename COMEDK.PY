import streamlit as st
import pandas as pd

def app(): 

    st.title("COMEDK") 
    st.write(" COMEDK is a popular engineering entrance exam conducted in Karnataka. It offers admission to a wide range of colleges, including some of the best in the state. The exam is relatively affordable and easy to register for. To prepare for the exam, start early and create a study plan, focus on understanding the concepts covered in the syllabus, practice solving previous year's question papers and mock tests, take breaks and avoid overworking yourself, and stay calm and focused on the day of the exam")
    dg=pd.read_csv("COD.csv")
    st.write(dg)
    st.line_chart(dg,x="Percentile", y=["Top 10 Colleges","Branches"] )