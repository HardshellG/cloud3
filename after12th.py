import streamlit as st
import pandas as pd

def app():
df=pd.read_csv("after12th.csv")
    st.dataframe(df, column_config={"Website": st.column_config.LinkColumn()})
 


