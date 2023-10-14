import streamlit as st
import pandas as pd

def app():
    data = {
        'Exam name': ['JEE Main','MHTCET','VITEEE','BITSAT','SRM','Manipal','KIIT','WBJEE','COMEDK','Symbiosis'],
        'Website': ['https://jeemain.nta.nic.in/','https://cetcell.mahacet.org/CAP_landing_page_2023/','https://vit.ac.in/vellore-institute-technology-engineering-entrance-examination','https://www.bitsadmission.com/bitsatmain.aspx?id=11012016','https://www.srmist.edu.in/admission-india/','https://manipal.edu/mu/admission/indian-students/online-entrance-exam-overview.html'
        'https://kiitee.kiit.ac.in/','https://wbjeeb.nic.in/WBJEECMS/Page/Page?PageId=1&LangId=P','https://www.comedk.org/','https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.set-test.org/&ved=2ahUKEwjIssvZ6tGBAxVjcGwGHcEnDbMQFnoECBEQAQ&usg=AOvVaw24IYpbKSYoZGC0wNE9o7N3']
    } 
    

    df = pd.DataFrame(data)
    st.dataframe(df, column_config={"Website": st.column_config.LinkColumn()})
 


