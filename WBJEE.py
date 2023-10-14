import streamlit as st
import pandas as pd

def app(): 

    st.title("WBJEE") 
    st.write("WBJEE, a state-level engineering entrance exam for West Bengal, is one of the most popular and competitive exams in the state. Held every year in May, it covers Physics, Chemistry, and Mathematics. To be eligible, students must have passed the 12th grade with 45% marks in PCM. Admission to top colleges is highly competitive, with cutoff ranks among the highest in India. ")         
    st.write("**HERE are top 10 colleges according to percentile for WBJEE**")
    dg=pd.read_csv("wb.csv")
    st.write(dg)
    st.line_chart(dg,x="Percentile", y=["Top 10 Colleges","Branches"] )
