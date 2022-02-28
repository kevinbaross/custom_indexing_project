# This is code  specific to Page2 - This page should show the Key ESG Metrics
# for S&P500 on the top and plot the S&P500 and Custom Index Future Performance based on Montecarlo Analysis 
# charts and data summary at bottom of the page
# This is an optional section in case we are able to achive montecarlo simulation for this data

# -----------------Import all dependent libraries and python modules
import streamlit as st # for webapp
import pandas as pd # for data manipulation
import numpy as np # for random gen
import yfinance as yf



# -----------------App function for Page2 - Monte Carlo Analysis-----------------
def app(e_options, s_options, g_options, esg_options, apply_filters_fn_1, apply_filters_fn_2):

    # -----------------Page2 Title-----------------

    st.title('Page2 - Monte Carlo Analysis')
    #st.title('Page2 - Next Steps (Documentation, Data, Predictive Analysis')


    # -----------------Key Metrics Section-----------------
    st.markdown('## Key Metrics')


    # Create three columns, one for each key metric to be displayed
    new_snp_e, new_snp_s, new_snp_g = st.columns(3)


    # Variables for temp values for S&P index 
    e_value = 5.47           # S&P Environment
    s_value = 9.28           # S&P Social
    g_value = 6.87           # S&P Governance


    
    new_snp_e.metric(label = "S&P Environmental Score", value = "%.2f"%e_value, delta = (5.47-24.61))

    new_snp_s.metric(label = "S&P Social Score", value = "%.2f"%s_value, delta = (9.28 - 21.01))

    new_snp_g.metric(label = "S&P Governance Score", value = "%.2f"%g_value, delta = (6.87 - 15.51))


    #### To Do: May have to provide the input fields for duration criteria for Monte Corlo Analysis
    #### To Do: May have to import custom_index_tool.ipyb for running the monte corlo simulation 



    # ------Delete this code once actual data is available-------
    st.markdown("### Important Charts")

    # temp  dataframe  for chart input
    #chart_data = pd.DataFrame(
    #np.random.randn(20,3),
    #columns=['a', 'b', 'c'])

    #st.bar_chart(chart_data)
    #st.line_chart(chart_data)


    #st.markdown("### Summary Stats")
    #st.dataframe(chart_data)


    # define ticker symbol, to plot S&P timeseries
    ticker_symbol = 'SPY'

    # get the data for this ticker
    ticker_data = yf.Ticker(ticker_symbol)

    # get the historical prices for this ticker
    ticker_df = ticker_data.history(period='1d', start='2012-1-1', end='2022-2-17')
    # Columns within the S&P Dataframe: Open High Low Close Volume Dividends Stock Splits
    
    #chart1, chart2 = st.columns(2)
    st.line_chart(ticker_df.Close)
    st.line_chart(ticker_df.Volume)

    st.markdown("### Summary Stats")

    st.dataframe(ticker_df)
    # ------Delete this code once actual data is available-------
