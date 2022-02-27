# This file is for applying the filters as per the user input(from streamlit_ux.py) to the datasources(from jupyternotebook)



# -----------------Data Gathering and Cleanup -----------------
### import custom_index_tool.ipynb (not sure if we need to convert this to .py to be able to use here)


# -----------------Apply Filter Criteria-----------------
###  Use the filter variables from streamlit_ux.py and apply the filters to the data sources
###     1. Use the "industry_options" variable as input 
###     2. Use the ESG factor (e_options,s_options, g_options) variables as input to create final filter criteria
### Hint: You can play with the multi-filters and sliders, click the 'Apply Criteria' button to see the output based on user input  

# Next:
### Present the filtered dataframes/series to the Charts in page1 and page2


import pandas as pd
from pathlib import Path
import matplotlib as plt
import numpy as np
import sqlalchemy
import yfinance as yf
import yahoo_fin.stock_info as si
import os
import streamlit as st         # import the streamlit library for webapp
#from streamlit_ux import form1



################################################################################################################
# Function for  applying filters to the data and visualization


def apply_filters_fn_1(e_options, s_options, g_options, esg_options):
    

    ############################################################################################################
    # Datasets:
    # 1. "sp500_sustainability_scores.csv" file: List of SP500 tickers with ESG Scores, Categories, Industries
    # 2.  yahoo finance data download of all S&P500 tickers - daily close and volume betweek date range


    ############################################################################################################
    # Data Gathering:
    # 1. "sp500_sustainability_scores.csv" 
        # a. read csv into dataframe
        # b. create in memory SQLite Database table

    # Using Pandas read_csv funcion and the Path module, 
    # read "sp500_sustainability_scores.csv" file into a Pandas DataFrame
    esg_df = pd.read_csv(Path("../sp500_sustainability_scores.csv"))


    # Create the connection string for your SQLite database
    database_connection_string = 'sqlite:///'

    # Pass the connection string to the SQLAlchemy create_engine function
    engine = sqlalchemy.create_engine(database_connection_string)

    # Removing unnecessary columns from the Dataframe
    #esg_df_1 = esg_df[['company_ticker', 'environmentScore', 'socialScore', 'governanceScore']]

    # Create New Table(esg_score_info) in the database 
    esg_df.to_sql(
        'esg_score_info', #New table name
        engine, 
        index=False, 
        if_exists='replace'
    )

    ################################################################################################################
    # Query for Filter Range Max Values - environmental score
    query_max_e_score_in_table = """
    SELECT environmentScore
    FROM esg_score_info
    ORDER By environmentScore DESC
    LIMIT  1
    """ 
    query_max_e_score_in_table_data = pd.read_sql_query(query_max_e_score_in_table, con=engine)
    max_e_score=query_max_e_score_in_table_data.iat[0,0]

    # Query for Filter Range Max Values - social score
    query_max_s_score_in_table = """
    SELECT socialScore
    FROM esg_score_info
    ORDER By socialScore DESC
    LIMIT  1
    """ 
    query_max_s_score_in_table_data = pd.read_sql_query(query_max_s_score_in_table, con=engine)
    max_s_score=query_max_s_score_in_table_data.iat[0,0]
    
    
    # Query for Filter Range Max Values - social score
    query_max_g_score_in_table = """
    SELECT governanceScore
    FROM esg_score_info
    ORDER By governanceScore DESC
    LIMIT  1
    """ 
    query_max_g_score_in_table_data = pd.read_sql_query(query_max_g_score_in_table, con=engine)
    max_g_score=query_max_g_score_in_table_data.iat[0,0]


    ################################################################################################################
    # Data Processing
        #  a. Get S&P 500 Ticker List from Table using SQL query
        #  b. Apply ESG Filters to the SQL Table to get Filtered Ticker List SQL query



    #####  a. Get S&P 500 Ticker List from Table using SQL query
    # Fetch the data for ALL S&P 500 as an index for comparison
    # Create and execute a query to return the list of tickers for S&P 500
    query_all_sp500 = """
    SELECT *
    FROM esg_score_info
    """

    # read in your SQL query results into Dataframe using pandas
    all_sp500_df = pd.read_sql(query_all_sp500, con=engine)
    all_sp500_ticker_list = all_sp500_df['company_ticker']


    #####  b. Apply ESG Filters to the SQL Table to get Filtered Ticker List SQL query
    # ESG Input Filtering Variables from streamlit_ux.py - from ESG sliders in side bar
    e_score = e_options
    s_score = s_options 
    g_score = g_options

    # Create and execute a query to return esg data for tickers that match the chosen criteria.
    # query1 ="""
    # SELECT company_ticker, environmentScore, socialScore, governanceScore
    # FROM esg_score_info
    # WHERE environmentScore >= """+str(e_score)+""" AND socialScore >= """+str(s_score)+""" AND governanceScore >= """+str(g_score)+""";
    # """
    print(esg_options[0])
    indexes = []
    ticker_list = []
    company_ticker_list = ["adult","alcoholic", "animalTesting", "catholic", "coal", "controversialWeapons", "furLeather", "gambling", "gmo", "militaryContract",
    "nuclear", "palmOil", "pesticides", "smallArms", "tobacco", "company_ticker"]

    filtered_df = all_sp500_df[company_ticker_list]

    for i in range(len(esg_options)):
        if esg_options[i] == True:
            indexes.append(i)  

    for item in indexes:
        for row in filtered_df.iterrows():
            ind = item
            if row[1][ind] == True:
                ticker_list.append(row[1][15])

    
    query1 ="""
    SELECT *
    FROM esg_score_info
    WHERE environmentScore >= """+str(e_score)+""" 
    AND socialScore >= """+str(s_score)+""" 
    AND governanceScore >= """+str(g_score)+""" 
    """
    # read in your SQL query results using pandas with Tickers that march ESG filters
    esg_df = pd.read_sql(query1, con=engine)
    esg_tickers = esg_df["company_ticker"]
    # ESG Ticker list
    ticker_list = np.array(ticker_list)
    ticker_array = np.setdiff1d(all_sp500_df["company_ticker"], ticker_list)
    esg_ticker = np.intersect1d(esg_tickers, ticker_array)

    return (all_sp500_ticker_list, esg_ticker)


    ################################################################################################################

        





    ################################################################################################################
    #  Execute below  code only after Apply Criteria is clicked
    #if form1.form_submit_button("Apply Criteria"):


def apply_filters_fn_2(all_sp500_ticker_list, esg_ticker):
    ################################################################################################################
    # Data Gathering:
    # 2.  yahoo finance data download of all S&P500 tickers - daily close and volume betweek date range
        # a. download into dataframe for all Tickers in S&P500
        # b. create another dataframe for only ESG tickers in S&P500
    
    # Date range variables for downloading S&P500 Ticker historing data
    start_date_range = "2020-01-01"
    end_date_range = "2020-04-30"

    # a. Download historical data for S&0 500 using the filter list generated above
    all_sp500_hist_data_df = yf.download(list(all_sp500_ticker_list), start=start_date_range, end=end_date_range)
    all_sp500_hist_data_df = all_sp500_hist_data_df[['Adj Close']]

    # b. create another dataframe for only ESG tickers in S&P500
    custom_sp500_hist_data_df =  all_sp500_hist_data_df.droplevel(0,axis=1)
    custom_sp500_hist_data_df = custom_sp500_hist_data_df[list(esg_ticker)]


    ################################################################################################################
    # Add Mean of all tickers for the S&P500 and Custom Index Dataframes for each date in the range

    #Create the "adj_close_daily_average" column to calculate the average price of all the filtered stock
    all_sp500_hist_data_df['sp500_index_adj_close_daily_average'] = all_sp500_hist_data_df.mean(axis=1)
    # Now create Dataframe dropping all columns except adj close daily average column
    sp500_index_adj_close_daily_average_df = all_sp500_hist_data_df['sp500_index_adj_close_daily_average']


    #Create the "Custom_Index" column to calculate the average price of all the filtered stock
    custom_sp500_hist_data_df['custom_indexsp_adj_close_daily_average'] = custom_sp500_hist_data_df.mean(axis=1)
    # Now create Dataframe dropping all columns except adj close daily average column
    custom_indexsp_adj_close_daily_average_df = custom_sp500_hist_data_df['custom_indexsp_adj_close_daily_average']



    ################################################################################################################
    # Calculate Daily Returns
    # Create Dataframes with percentage change on daily average for S&P500 for daily returns
    sp500_index_adj_close_percent_change_df = sp500_index_adj_close_daily_average_df.pct_change().dropna()

    # Create Dataframes with percentage change on daily average for Custom Index for daily returns
    custom_indexsp_adj_close_percent_change_df = custom_indexsp_adj_close_daily_average_df.pct_change().dropna()

    #### Combine the two dataframes for plotting purpose 
    daily_returns_df = pd.concat([sp500_index_adj_close_percent_change_df,custom_indexsp_adj_close_percent_change_df], axis=1)



    ################################################################################################################
    #### Calculate Cumulative Returns for plotting purpose
    cumulative_returns_df = (1 + daily_returns_df).cumprod()



    ################################################################################################################
    #### Plot the charts


    # Title for Charts Section
    st.markdown("### The Daily Returns of Custom ESG based Index vs S&P500 Index Chart")
    
    # Plot the daily returns for S&P500 Index and Custom Index
    st.line_chart(daily_returns_df)


    # Title for Charts Section
    st.markdown("### The Cumulative Returns of Custom ESG based Index vs S&P500 Index Chart")
    
    # Plot the cumulative returns for S&P500 Index and Custom Index
    st.line_chart(cumulative_returns_df)
    st.write("Based on your selection, below is the list of Tickers you may consider trading as part of the customer index")
    st.dataframe(esg_ticker)
    # chart_1.sp500_hist_data_closing_only.plot(
    #      title="The Price Index of Stock Filtered", 
    #      xlabel="Date", 
    #      ylabel="Price Index", 
    #      figsize=(10,7),
    #      legend="top",
    #      label="Filtered Result",
    #      linewidth=3
    # )

    #Plot the "ALL" S&P500 index data frame
    # chart_2.all_sp500_hist_data_closing_only.plot(
    #      legend="top",
    #      label="All S&P500 Benchmark",
    #      linewidth=3
    # )

