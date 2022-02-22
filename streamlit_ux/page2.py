# This is code  specific to Page2 - This page should show the Key ESG Metrics
# for S&P500 on the top and plot the S&P500 and Custom Index Future Performance based on Montecarlo Analysis 
# charts and data summary at bottom of the page
# This is an optional section in case we are able to achive montecarlo simulation for this data

# -----------------Import all dependent libraries and python modules
import streamlit as st # for webapp
import pandas as pd # for data manipulation
import numpy as np # for random gen



# -----------------App function for Page2 - Monte Carlo Analysis-----------------

def app(e_options, s_options, g_options):

    # -----------------Page2 Title-----------------

    st.title('Page2 - Monte Carlo Analysis')



    # -----------------Key Metrics Section-----------------
    st.markdown('## Key Metrics')


    # Create three columns, one for each key metric to be displayed
    new_snp_e, new_snp_s, new_snp_g = st.columns(3)


    # Variables for temp values for custom index
    ### To Do: Kevin/Haoyu: Please update the values to match the actuals or point it to live data source)    
    new_e_value = 3.33333
    new_s_value = 7.33333
    new_g_value = 9.33333

    new_snp_e.metric(label = "S&P Environmental Score", value = "%.2f"%new_e_value) #, delta = -1.4)

    new_snp_s.metric(label = "S&P Environmental Score", value = "%.2f"%new_s_value) #, delta = -1.4)

    new_snp_g.metric(label = "S&P Environmental Score", value = "%.2f"%new_g_value) #, delta = -1.4)


    ### To Do: Kevin/Haoyu: May have to provide the input fields for duration criteria for Monte Corlo Analysis
    ### To Do: Kevin/Haoyu: May have to import custom_index_tool.ipyb for running the monte corlo simulation 



    # ------Delete this code once actual data is available-------
    st.markdown("### Important Charts")

    # temp  dataframe  for chart input
    chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a', 'b', 'c'])

    st.bar_chart(chart_data)
    st.line_chart(chart_data)


    st.markdown("### Summary Stats")
    st.dataframe(chart_data)

    # ------Delete this code once actual data is available-------
