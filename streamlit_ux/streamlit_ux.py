# This is the main code for the Streamlit Customer Indexing App
# This file has code for the common sections for all pages, the sidebar - filter section for user input


### To Do: Kevin/Haoyu: Please look for To Do comments in each file listed below and help complete the steps 
### To Do: Review the code in streamlit_ux.py, page1.py, page2.py, apply_filters.py
### To Do: Please clean the comments to ensure all the To Dos are cleared and comments are understandable for everyone.

# Dependency files:
# streamlit_ux.py, multiapp.py, page1.py, page2.py, apply_filters.py



# Prerequisites:
# To install/update streamlit, run below in gitbash after activating conda environment
#   <pip install streamlit>
#           or
#   <pip install --upgrade streamlit>
# To run this file, type the following in gitbash
#   <streamlit run streamlit_ux.py>
# ensure you have all the dependency files as per the git folder structure



# -----------------Import all dependent libraries and python modules
 
import streamlit as st         # import the streamlit library for webapp
from multiapp import MultiApp  # import Multiapp code for accessing multipage functions
import page1, page2            # import app modules for each page
import apply_filters           # import filters module where output of the filters was applied to generate the data for each page



# ------------------Common to all pages------------------

# ---Main page title---
st.title("Custom Index Tool")


# ---Sidebar----
# To show the image in the sidebar
st.sidebar.image("https://pixabay.com/get/gd9e3436a3e9550124f18b596ded24a79e35f3cf82215c93fae739894663a4c4f2869cfe5f57927694b61bf553a130160b12f95317a5ac119beb95ade4ab7fb6cabe18c6838967818ae073aece31acbb5_640.jpg", width=200)

# ---Sidebar Header---
st.sidebar.header("Select filtering criteria using Multi-Selectbox & Sliders")


# Using Forms for containing the filters selection - so the streamlit code waits for each filtering choice to be selected
form1 = st.sidebar.form(key="Industry_Options")
form2 = st.sidebar.form(key="ESG_Options")


# Title for Filters in the Sidebar
form1.title("Industry Filters")

# Multiselect Filters for Industries
industry_options = form1.multiselect("Please select the industry of choice(s)", ["1", "2", "3"])
### To DO: Kevin/Haoyu: Replace ["1", "2", "3"] with a list variable that cointains the list of all industries


# if form1.form_submit_button("Apply Industry Criteria"):
#    industry_text = form1.text_area("You chose the following Industry choice(s)", industry_options)
#    form1.write(industry_text)


form1.title("ESG Criteria")

# Slider Selection for ESG Criteria
e_options = form1.slider("Choose Environmental Risk Score?", 0,10, 5)
s_options = form1.slider("Choose Social Risk Factor?", 0,10, 5)
g_options = form1.slider("Choose Governance Risk Factor?", 0,10, 5)

if form1.form_submit_button("Apply Criteria"):

##### To Decide: ---we may need to modify the below four lines of code to show or not show the output
##### To Decide: ---of the filter choices, I included this only for understaind what will be the output
##### To Decide: ---if we do not want to show the text boxes, just directly assign the options to the text variables below to run after button is clicked    
    industry_text = form1.text_area("You chose the following Industry choice(s)", industry_options)
    e_text = form1.text_area("Environmental Risk Factor", e_options)
    s_text = form1.text_area("Social Risk Factor", s_options)
    g_text = form1.text_area("Governance Risk Factor", g_options)
### To Do: Kevin/Haoyu: Use the "industry_options" variable as input 
### To Do: Kevin/Haoyu: And Use the ESG factor (e_options,s_options, g_options) variables as input to create final filtered dataset
### To Do: Kevin/Haoyu: Use the  apply_filters.py file to apply the filtering criteria to the data that is being collated by Chris and Hugo



# Access the MultiApp function from multiapp.py
app = MultiApp()

# Add all the sub-pages here, provide the Page Title/name and the python page specific function.
app.add_app("Page1 - Custom Index", page1.app)
app.add_app("Page2 - Monte Carlo Analysis", page2.app)

# The main app for multipage
app.run()

