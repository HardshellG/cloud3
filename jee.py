import streamlit as st
import pandas as pd

def app():

   st.title("Jee") 
   st.write("**The Joint Entrance Examination (JEE) Main** is a highly competitive entrance exam in India for admission to undergraduate engineering and architecture programs. Conducted by the National Testing Agency (NTA), it serves as the initial screening for entry into prestigious institutions, including the National Institutes of Technology (NITs) and various other engineering colleges.")
   st.write("**Here are the total number of seats vs branches for IIT's and NIT's**")
   df=pd.read_csv("Total Seats.csv")
   st.write(df)

   st.bar_chart(df, x="Branch of Study", y="Total Seats" )
   dg=pd.read_csv("All IIT List of Percentile.csv")
   st.write(dg)
   st.line_chart(dg,x="IIT/Branch", y=["General","SC","ST","OBC"] )

