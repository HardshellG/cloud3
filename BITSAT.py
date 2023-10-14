import streamlit as st
import pandas as pd

def app(): 

    st.title("BITSAT") 
    st.write("BITSAT, a computer-based online test for admission to engineering programs at the Birla Institute of Technology and Science (BITS) campuses in Pilani, Goa, and Hyderabad, is one of the most popular engineering entrance exams in India. It is known for its high difficulty level, covering a wide range of topics in Physics, Chemistry, Mathematics, and English Proficiency. BITSAT is highly competitive, with cutoff ranks for admission to BITS Pilani among the highest in India.")         
    st.write("**HERE are top 10 colleges according to percentile for BITSAT**")
    dg=pd.read_csv("bit.csv")
    st.write(dg)
    st.line_chart(dg,x="Percentile", y=["Top 10 Colleges","Branches"] )
