import streamlit as st
import pandas as pd

def app(): 

    st.title("MHTCET") 
    st.write(" The Maharashtra Common Entrance Test MHT CET is a state-level entrance exam conducted for admission to undergraduate engineering, pharmacy and agriculture courses in Maharashtra. The exam is conducted in online mode and consists of three papers: Mathematics, Physics and Chemistry, and Zoology and Botany. Each paper has 100 objective type questions and there is no negative marking. The selection of candidates is based on their MHT CET scores and the merit list is prepared based on the total marks obtained in all three papers. The counselling process for admission to colleges is conducted by the Directorate of Technical Education (DTE), Maharashtra.")         
    st.write("**HERE are top 10 colleges according to percentile for MHTCET**")
    dg=pd.read_csv("mh.csv")
    st.write(dg)
    st.line_chart(dg,x="Percentile", y=["Top 10 Colleges","Branches"] )
