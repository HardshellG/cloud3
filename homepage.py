import streamlit as st
from streamlit_option_menu import option_menu

import  Engineering.py, home.py
st.set_page_config(
        page_title="ExamTimeLine",
)

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
                menu_title='ExamTimeLine',
                options=['Engineering','home'],
                icons=[ 'person-circle','house-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )    

        if app == 'Engineering.py':
            Engineering.py.app()
        if app == 'home':
           home.py.app()
          
        

    run()                                         
