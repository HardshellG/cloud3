import streamlit as st
import pandas as pd

def app():
    data = {
        'Exam name': ['JEE Main','MHTCET'],
        'Website': ['https://jeemain.nta.nic.in/','https://cetcell.mahacet.org/CAP_landing_page_2023/']
    }
    
    
    df = pd.DataFrame(data)
    
        st.dataframe(df, column_config={"Website": st.column_config.LinkColumn()})


 


