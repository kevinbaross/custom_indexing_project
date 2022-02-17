# Prerequisites
# To install/update streamlit
# pip install streamlit
# or
# pip install --upgrade streamlit

#  import the streamlit library
import streamlit as st # for webapp
from multiapp import MultiApp #Multiapp code
import page1, page2 # import app modules for each page

# Common to all pages

# main page title
st.title("Custom Index Tool")

# image in the sidebar
st.sidebar.image("https://pixabay.com/get/gd9e3436a3e9550124f18b596ded24a79e35f3cf82215c93fae739894663a4c4f2869cfe5f57927694b61bf553a130160b12f95317a5ac119beb95ade4ab7fb6cabe18c6838967818ae073aece31acbb5_640.jpg", width=200)

# Using Forms for containing the filters selection
st.sidebar.header("Forms with the Multi Selectbox Section")
form1 = st.sidebar.form(key="Industry_Options")
form2 = st.sidebar.form(key="ESG_Options")

# Filters
form1.header("Filters")

form1.title("Industry Filters")

# Multiselect Filters for Industries
industry_options = form1.multiselect("Please select the industry of choice(s)", ["1", "2", "3"])

# if form1.form_submit_button("Apply Industry Criteria"):
#    industry_text = form1.text_area("You chose the following Industry choice(s)", industry_options)
#    form1.write(industry_text)


form1.title("ESG Criteria")

# Slider Selection for ESG Criteria
e_options = form1.slider("Choose Environmental Risk Score?", 0,10, 5)
s_options = form1.slider("Social Risk Factor?", 0,10, 5)
g_options = form1.slider("Governance Risk Factor?", 0,10, 5)

if form1.form_submit_button("Apply Criteria"):
    industry_text = form1.text_area("You chose the following Industry choice(s)", industry_options)
#    form1.write(industry_text)
    e_text = form1.text_area("Environmental Risk Factor", e_options)
    s_text = form1.text_area("Social Risk Factor", s_options)
    g_text = form1.text_area("Governance Risk Factor", g_options)


#form2.title("ESG Criteria")

# Slider Selection for ESG Criteria
#e_options = form2.slider("Choose Environmental Risk Score?", 0,10, 5)
#s_options = form2.slider("Social Risk Factor?", 0,10, 5)
#g_options = form2.slider("Governance Risk Factor?", 0,10, 5)


# if form2.form_submit_button("Apply ESG"):
#    e_text = form2.text_area("Environmental Risk Factor", e_options)
#    s_text = form2.text_area("Social Risk Factor", s_options)
#    g_text = form2.text_area("Governance Risk Factor", g_options)
  

# st.write("This is the section common to both pages of the App")


app = MultiApp()


# Add all your application here
app.add_app("Page1 - Custom Index", page1.app)
app.add_app("Page2 - Monte Carlo Analysis", page2.app)

# The main app
app.run()

