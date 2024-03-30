import pickle
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = 'Machine Failure Classifier',
    page_icon = 'page_icon.png',
)

st.title('Maintenance - Failure Prediction')
st.image('maintenance.jpg')
st.write('\n\n')

st.markdown(
    '''
    This app aims to classify failure given by following parameters
    '''
)
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

col1, col2 = st.columns(2)

with col1:
    air = st.number_input(label = 'Air Temperature')
    process = st.number_input(label = 'Process Temperature')
    rpm = st.number_input(label = 'Rotational Speed')

with col2:
    torque = st.number_input(label = 'Torque')
    tool_wear = st.number_input(label = 'Tool Wear')
    type = st.selectbox(label = 'Type', options = ['Low','Medium','High'])

def prediction(air, process, rpm, torque, tool_wear, type):
    df_input = df.DataFrame({
        'Air_temperature': [air],
        'Process_temperature' : [process],
        'Rotational_speed' : [rpm],
        'Torque' : [torque],
        'Tool_wear' : [tool_wear],
        'Type': [type]
    })
    prediction = model.predict(df_input)
    return prediction

if st.button('Predict'):
    predict = prediction(air, process, rpm, torque, tool_wear, type)
    st.success(predict)
