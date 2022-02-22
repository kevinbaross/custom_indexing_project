# This is code  specific to Page1 - This page should show the Key ESG Metrics
# for ESG of S&P500 on the top and plot the S&P500 and Custom Index Performance 
# charts and data summary at bottom of the page. This page is considered as the Minimum Viable Product(MVP)


### To Do: Kevin/Haoyu: Once the Data Filters have been applied, the filtered data should be presented as input for charts below for plotting custom index performance against S&P


# -----------------Import all dependent libraries and python modules
import streamlit as st      # for webapp
import pandas as pd         # for data manipulation on dataframes
import numpy as np          # for random geneneration of dataset until actual data available
import yfinance as yf       # for ticker information from yahoo finance - live data
# from streamlit_ux import * #e_options, s_options, g_options #importing ESG filter inputs from user for key metrics section
from apply_filters import *
# -----------------App function for Page1-----------------

def app(e_options, s_options, g_options, apply_filters_fn_1): #, apply_filters_fn_2):



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
    snp_e.metric(label = "S&P Environmental Score", value = "%.2f"%e_value)
    snp_s.metric(label = "S&P Social Score", value = "%.2f"%s_value)
    snp_g.metric(label = "S&P Governance Score", value = "%.2f"%g_value)

    # To display the key metrics of the Custom Index
    snp_e.metric(label = "Custom Index Environmental Score", value = "%.2f"%e_options, delta = (e_options-e_value))
    snp_s.metric(label = "Custom Index Social Score", value = "%.2f"%s_options, delta = (s_options-s_value))
    snp_g.metric(label = "Custome Index Governance Score", value = "%.2f"%g_options, delta = (g_options-g_value))



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
    

    # define ticker symbol, to plot S&P timeseries
    ##ticker_symbol = 'SPY'

    # get the data for this ticker
    ##ticker_data = yf.Ticker(ticker_symbol)

    # get the historical prices for this ticker
    ##ticker_df = ticker_data.history(period='1d', start='2012-1-1', end='2022-2-17')
    # Columns within the S&P Dataframe: Open High Low Close Volume Dividends Stock Splits
    
    # chart1, chart2 = st.columns(2)
    # chart1.line_chart(ticker_df.Close)
    # chart2.line_chart(ticker_df.Volume)

    ##st.markdown("### Summary Stats")

    ##st.dataframe(ticker_df)

    
    apply_filters_fn_1(e_options, s_options, g_options)
    #apply_filters_fn_2(all_sp500_ticker_list, esg_ticker)