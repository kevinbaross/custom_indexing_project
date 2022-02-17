# including this file for reference,  we can delete this after completing the entire  code
# Prerequisites
# To install/update streamlit
# pip install streamlit
# or
# pip install --upgrade streamlit

#  import the streamlit library
import streamlit as st # for webapp
import pandas as pd # for data manipulation
import numpy as np # for random gen


st.title("Custom Index Tool")
st.write("This is  my new app")

#Buttons
button1 = st.button("Click Me")
if  button1: 
    st.write("This  is button text")

# Checkbox Section

st.header("Start of the Checkbox Section")

like = st.checkbox("Do  you like this app")
button2 =  st.button("Submit")
if  button2:
    if like:
        st.write("Thanks. I  like  it  too")
    else:
        st.write("I'm sorry. You have a bad taste")


# Radio Button Section
st.header("Start of the Radio Section")
animal1 = st.radio("What  animal is your favorite?",("Lions", "Tigers", "Bears"))

button3 = st.button("Submit Animal 1")
if button3:
    st.write(animal1)
    if animal1 == "Lions":
         st.write ("ROAR!")


# Select Box Section
st.header("Start of the Selectbox Section")
animal2 = st.selectbox("What  animal is your favorite?",("Lions", "Tigers", "Bears"))

button4 = st.button("Submit Animal 2")
if button4:
    st.write(animal2)
    if animal2 == "Lions":
         st.write ("ROAR!")



# Muti Select Box Section
st.header("Start of the Multi Selectbox Section")
options = st.multiselect("What animlas do you like?",  ["Lions", "Tigers", "Bears"])

button5 = st.button("Print Animals")
if button5:
    st.write(options)


# Slider Section
st.header("Start of the Slider Section")
epochs_num = st.slider("How many epochs?", 1,100, 10)
button6 = st.button("Slider Button")
if button6:
    st.write(epochs_num)


# Start of the Text Input Section
st.header("Start of the Text Input Section")
user_text = st.text_input("What is your fav movie?", "Start Wars  Ep. IV")
if st.button("Text Button"):
    st.write(user_text)

user_num = st.number_input("What is your fav number?")
if st.button("Number Button"):
    st.write(user_num)


# Layouts and Images
# Side Bar

st.sidebar.title("Layouts and Images")
st.sidebar.image("https://pixabay.com/get/gd9e3436a3e9550124f18b596ded24a79e35f3cf82215c93fae739894663a4c4f2869cfe5f57927694b61bf553a130160b12f95317a5ac119beb95ade4ab7fb6cabe18c6838967818ae073aece31acbb5_640.jpg", width=100)

st.sidebar.header("Options")

text = st.sidebar.text_area("Paste Text Here")
button6 = st.sidebar.button("Clean Text")
if button6:
# Sub Columns + Expander wrapper only for one column   
    col1, col2 = st.columns(2)
    col1_expander = col1.expander("Expand Original")
    with col1_expander:    
        col1_expander.header("Original Text")
        col1_expander.write(text)

    col2.header("Clean Text")
    col2.write("Bye")


# Using Forms
st.sidebar.header("Forms with the Multi Selectbox Section")
form1 = st.sidebar.form(key="Options1")
form1.header("Params1")
ent_types = form1.multiselect("Sllelect the  entities  you want to extract", ["1", "2", "3"])
if form1.form_submit_button("click me"):
    text = form1.text_area("You Chose", ent_types)
    form1.write(text)

# Using Cache
# @st.cache(alllow_output_mutation=True)

# Session State and container

main_container = st.container()

if 'counter' not in  st.session_state:
    st.session_state.counter  = 0
    main_container.write(st.session_state.counter)
if st.button("up"):
    st.session_state.counter +=1
    main_container.write(st.session_state.counter)
if st.button("down"):
    st.session_state.counter -=1
    main_container.write(st.session_state.counter)
if st.button("reset"):
    st.session_state.counter = 0
    main_container.write(st.session_state.counter)


st.markdown('## Key Metrics')

kpi1, kpi2 = st.columns(2)
# increase number is green by default
kpi1.metric(label = "$S&P", value = "$ %.2f"%200.22, delta = -1.4)
# reduced number is green  using inverse delta color
value1 = 33.33333
kpi2.metric(label = "Bounce Rate", value = "%.2f"%value1, delta = -5, delta_color = 'inverse')

st.markdown("### Important Charts")

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a', 'b', 'c'])

st.bar_chart(chart_data)
st.line_chart(chart_data)

chart1, chart2 = st.columns(2)

chart1.bar_chart(chart_data)
chart2.line_chart(chart_data)

st.dataframe(chart_data)



