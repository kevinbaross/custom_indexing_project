# This is code  specific to Page1 - This page should show the Key ESG Metrics
# for ESG of S&P500 on the top and plot the S&P500 and Custom Index Performance 
# charts and data summary at bottom of the page. 
#   This page is considered as the Minimum Viable Product(MVP) with slider based filtering
#   Post MVP, to enable fitering using ESG Factor and Industry filters


### To Do: Once the Data Filters have been applied, the filtered data should be presented as input for charts below for plotting custom index performance against S&P


# -----------------Import all dependent libraries and python modules
import streamlit as st      # for webapp
import pandas as pd         # for data manipulation on dataframes
import numpy as np          # for random geneneration of dataset until actual data available
import yfinance as yf
from zmq import EVENT_CLOSE_FAILED       # for ticker information from yahoo finance - live data
# from streamlit_ux import * #e_options, s_options, g_options #importing ESG filter inputs from user for key metrics section
from apply_filters import *
# -----------------App function for Page1-----------------

#def app(e_options, s_options, g_options, apply_filters_fn_1): #, apply_filters_fn_2):
def app(e_options, s_options, g_options, esg_options, apply_filters_fn_1, apply_filters_fn_2):


    # -----------------Page1 Title-----------------
    st.title('Page1 - Custom Index')




    # -----------------Key Metrics Section-----------------

    st.markdown('## Key Metrics')
    
    
    # Create three columns, one for each key metric to be displayed
    snp_e, snp_s, snp_g = st.columns(3)

    # Variables for temp values 
    ### To Do: Kevin/Haoyu: Please update the values to match the actuals or point it to live data source)
    e_value = 5.47           # S&P Environment
    s_value = 9.28           # S&P Social
    g_value = 6.87           # S&P Governance


    # To display the key metrics of the S&P
    snp_e.metric(label = "S&P Average Environmental Score", value = "%.2f"%e_value)
    snp_s.metric(label = "S&P Average Social Score", value = "%.2f"%s_value)
    snp_g.metric(label = "S&P Average Governance Score", value = "%.2f"%g_value)

    # To display the key metrics of the Custom Index
    snp_e.metric(label = "Custom Index Environmental Min Score", value = "%.2f"%e_options, delta = (e_options-e_value))
    snp_s.metric(label = "Custom Index Social Min Score", value = "%.2f"%s_options, delta = (s_options-s_value))
    snp_g.metric(label = "Custom Index Governance Min Score", value = "%.2f"%g_options, delta = (g_options-g_value))



# -----------------Charts Section-----------------
    st.markdown("### Important Charts")

    # ------Delete this code once actual data is available-------
    # temp  dataframe  for chart input
    ## chart_data = pd.DataFrame(
    ##np.random.randn(20,3),
    ##columns=['a', 'b', 'c'])

    # Create two columns, one for each chart to be displayed on the page
    ##chart1, chart2 = st.columns(2)

    # Plot the charts
    ##chart1.bar_chart(chart_data)
    ##chart2.line_chart(chart_data)
    # ------Delete this code once actual data is available-------
    



    ########################################################################################
    #Apply Filteres Code has been broken to two parts in case we want to delay the initial visualization until user inputs filter choices or separately only run visualization multiple times

    
    #for counter 0 to 1:
    #    counter = counter + 1

    #    if counter = 1:
    
    #Apply Filteres Code - Part1
    all_sp500_ticker_list, esg_ticker = apply_filters_fn_1(e_options, s_options, g_options, esg_options)

    #Apply Filteres Code - Part1
    apply_filters_fn_2(all_sp500_ticker_list, esg_ticker)

    