import streamlit as st
import pandas as pd
import plotly.express as px

file = pd.read_csv('SleepDisorder.csv')

st.title('Sleep Disorder App')
cols = file.columns.drop(['Person ID','Sleep Disorder','BMI Category','Stress Level'])

#occ_list = []
#for i in file['Occupation'].unique():
 #   occ_list.append(i)

#bmi_list = []
#for i in file['BMI Category'].unique():
 #   bmi_list.append(i)

st.sidebar.title('Specify Your Details')
pp = st.sidebar.selectbox('Primary Parameter',cols)
sp = st.sidebar.selectbox('Secondary Parameter',cols.drop(pp))
graph = st.sidebar.radio('Plot Type',['bar', 'scatter','histogram'])
btn = st.sidebar.button('Possible Sleep Disorders')


if btn:
    if graph == 'bar' :
        st.write('Bar Graph')
        st.write(px.bar(file,x=pp,y=sp,color='Sleep Disorder',hover_name='BMI Category',animation_frame='Stress Level'))
    elif graph == 'scatter':
        st.write('Scatter Plot')
        st.write(px.scatter(file,x=pp,y=sp,color='Sleep Disorder',hover_name='BMI Category',animation_frame='Stress Level'))
    elif graph == 'histogram':
        st.write('Histograms')
        st.write(px.histogram(file,x=pp))
        st.write(px.histogram(file,x=sp))




