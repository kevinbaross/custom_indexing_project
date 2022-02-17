# This is code  specific to Page1

import streamlit as st # for webapp
import pandas as pd # for data manipulation
import numpy as np # for random gen

def app():
    st.title('Page2 - Monte Carlo Analysis')

    st.markdown('## Key Metrics')

    new_snp_e, new_snp_s, new_snp_g = st.columns(3)

    # temp variables for values
    new_e_value = 3.33333
    new_s_value = 7.33333
    new_g_value = 9.33333

    new_snp_e.metric(label = "S&P Environmental Score", value = "%.2f"%new_e_value) #, delta = -1.4)

    new_snp_s.metric(label = "S&P Environmental Score", value = "%.2f"%new_s_value) #, delta = -1.4)

    new_snp_g.metric(label = "S&P Environmental Score", value = "%.2f"%new_g_value) #, delta = -1.4)


    st.markdown("### Important Charts")

    # temp  dataframe  for chart input
    chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a', 'b', 'c'])

    st.bar_chart(chart_data)
    st.line_chart(chart_data)


    st.markdown("### Summary Stats")
    st.dataframe(chart_data)