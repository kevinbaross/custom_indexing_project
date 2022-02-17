# This is code  specific to Page1

import streamlit as st # for webapp
import pandas as pd # for data manipulation
import numpy as np # for random gen


def app():
    st.title('Page1 - Custom Index')

    st.markdown('## Key Metrics')

    snp_e, snp_s, snp_g = st.columns(3)

    # temp variables for values
    e_value = 3.33333
    s_value = 7.33333
    g_value = 9.33333

    snp_e.metric(label = "S&P Environmental Score", value = "%.2f"%e_value) #, delta = -1.4)

    snp_s.metric(label = "S&P Environmental Score", value = "%.2f"%s_value) #, delta = -1.4)

    snp_g.metric(label = "S&P Environmental Score", value = "%.2f"%g_value) #, delta = -1.4)


    st.markdown("### Important Charts")

    # temp  dataframe  for chart input
    chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a', 'b', 'c'])

    chart1, chart2 = st.columns(2)

    chart1.bar_chart(chart_data)
    chart2.line_chart(chart_data)


    st.markdown("### Summary Stats")

    st.dataframe(chart_data)