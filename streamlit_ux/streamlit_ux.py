# This is the main code for the Streamlit Customer Indexing App
# This file has code for the common sections for all pages, the sidebar - filter section for user input


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
from apply_filters import *    # import filters module where output of the filters was applied to generate the data for each page
#import datetime


# ------------------Common to all pages------------------

# ---Main page title---
st.title("Custom Index Tool")


# ---Sidebar----
# To show the image in the sidebar
st.sidebar.image("../images/stocks_image.jpg", width=200)

# ---Sidebar Header---
st.sidebar.header("Select filtering criteria using Multi-Selectbox & Sliders")


# Using Forms for containing the filters selection - so the streamlit code waits for each filtering choice to be selected
form1 = st.sidebar.form(key="Industry_Options")
form2 = st.sidebar.form(key="ESG_Options")


# Title for Filters in the Sidebar
form1.title("Filters")

#  Variable for  Industry List
industry_filter_list = ["Aerospace & Defense", "Auto Components", "Automobiles", "Banks", "Building Products", "Chemicals", "Commercial Services", "Construction & Engineering", "Construction Materials", "Consumer Durables", "Consumer Services", "Containers & Packaging", "Diversified Financials", "Diversified Metals", "Electrical Equipment", "Energy Services", "Food Products", "Food Retailers", "Healthcare", "Homebuilders", "Household Products", "Industrial Conglomerates", "Insurance", "Machinery", "Media", "Oil & Gas Producers", "Paper & Forestry", "Pharmaceuticals", "Precious Metals", "Real Estate", "Refiners & Pipelines", "Retailing", "Semiconductors", "Software & Services", "Steel", "Technology Hardware", "Telecommunication Services", "Textiles & Apparel", "Traders & Distributors", "Transportation", "Utilities"]

esg_fiter_list = ["adult", "alcoholic", "animalTesting", "catholic", "coal", "controversialWeapons", "furLeather", "gambling", "gmo", "militaryContract", "nuclear", "palmOil", "pesticides", "smallArms", "tobacco", "Energy Services"]

col1_expander = form1.expander("Show Filters")
with col1_expander:    
   
    # Multiselect Filters for Industries
    industry_options = col1_expander.multiselect("Please select the industry of your choice(s)", industry_filter_list)
    #esg_options = col1_expander.multiselect("Please select the ESG factor(s) you dislike", esg_fiter_list)
    
    # Checkbox Section
    col1_expander.write("Please select the ESG factor(s) you dislike")
    esg_options = []
    counter = 1
    for each_esg in esg_fiter_list:
        counter = counter +1
        #like = col1_expander.checkbox(each_esg)
        esg_option_v = col1_expander.checkbox(each_esg)
        esg_options.append(esg_option_v)
        # esg_options[counter] = like
    
    #for i in range(esg_fiter_list):
    #    globals()["esg_options_v" + str(i)] = col1_expander.checkbox(esg_fiter_list[i])
    #    esg_options.append(esg_options_v)


    #st.write(esg_options)
    #   if like:
    #         esg_options_false = esg_options.append(each_esg)
    #     else:
    #         esg_options_true = esg_options.append(each_esg)
    # st.write(f"esg_options_false: {esg_options_false}")
    # st.write(f"esg_options_true: {esg_options_true}")


# if form1.form_submit_button("Apply Industry Criteria"):
#    industry_text = form1.text_area("You chose the following Industry choice(s)", industry_options)
#    form1.write(industry_text)

e_options = 24.61           # S&P Environment sider max variable
s_options = 21.01           # S&P Social
g_options = 15.51           # S&P Governance


form1.title("ESG Criteria")



# Slider Selection for ESG Criteria
e_options = form1.slider("Minimum Environmental Score?", 0,25, 24)
s_options = form1.slider("Minimum Social Score?", 0,25, 21)
g_options = form1.slider("Minimum Governance Score?", 0,25, 15)

if form1.form_submit_button("Apply Criteria"):

##pending## To remove: ---we may need to modify the below four lines of code to show or not show the output
##pending## To remove: ---of the filter choices, I included this only for understaind what will be the output
    industry_text = form1.text_area("You chose the following Industry choice(s)", industry_options)
    esg_text = form1.text_area("You do not like the following ESG Factors", esg_options)
         
    #e_text = form1.text_area("Environmental Risk Factor", e_options)
    #s_text = form1.text_area("Social Risk Factor", s_options)
    #g_text = form1.text_area("Governance Risk Factor", g_options)
##pending## To Do: Use the "industry_options" variable as input 
##pending## To Do: Use the ESG factor "esg_options" variable as input 
#done# To Do: And Use the ESG Score (e_options,s_options, g_options) variables as input to create final filtered dataset
#done# To Do: Use the  apply_filters.py file to apply the filtering criteria to the data that is being collated



# Access the MultiApp function from multiapp.py
app = MultiApp()

# Add all the sub-pages here, provide the Page Title/name and the python page specific function.
#app.add_app("Page1 - Custom Index", page1.app, e_options, s_options, g_options, apply_filters_fn_1) #, apply_filters_fn_2 )
#app.add_app("Page2 - Monte Carlo Analysis", page2.app, e_options, s_options, g_options, apply_filters_fn_1) #, apply_filters_fn_2 )
app.add_app("Page1 - Custom Index", page1.app, e_options, s_options, g_options, esg_options, apply_filters_fn_1, apply_filters_fn_2)
app.add_app("Page2 - Monte Carlo Analysis", page2.app, e_options, s_options, g_options, esg_options, apply_filters_fn_1, apply_filters_fn_2)


# The main app for multipage
#app.run(e_options, s_options, g_options, apply_filters_fn_1) #, apply_filters_fn_2)
app.run(e_options, s_options, g_options, esg_options, apply_filters_fn_1, apply_filters_fn_2)

