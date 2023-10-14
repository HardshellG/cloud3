import streamlit as st
from streamlit_option_menu import option_menu
import after12th, jee.py, MHTCET.py, COMEDK.py,BITSAT.py, WBJEE.py
def app(): 
 class MultiApp:

    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })    

    def run():

        with st.sidebar:
            app = option_menu(
                menu_title='Exams',
                options=['after12th','jee','MHTCET','COMEDK','BITSAT','WBJEE'],
                icons=['house-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )    

        if app== 'after12th':
            after12th.app()
        if app== 'jee':
            jee.app()
        if app== 'MHTCET':
           MHTCET.app()
        if app== 'COMEDK':
           COMEDK.app()   
        if app== 'BITSAT':
           BITSAT.app()
        if app== 'WBJEE':
           WBJEE.app()
             

             



    run()
