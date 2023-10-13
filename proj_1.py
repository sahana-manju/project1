import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import hiplot as hip
from PIL import Image
from streamlit import runtime
runtime.exists()


st.set_page_config(page_title="Air Quality Analysis", layout="wide")
#st.title('Air Quality Analysis')
st.markdown(f'<h1 style="color:#336BFF;font-size:34px;">{"BreezoScan"}</h1>', unsafe_allow_html=True)
st.markdown('Check the air quality around you to combat air pollutaion and lead healthier lives')
st.divider()

df_air=pd.read_csv('/Users/sahanamanjunath/Downloads/AQI and Lat Long of Countries.csv')
countries=list(df_air['Country'].unique())

selection = st.sidebar.selectbox("Choose the operation", ["Check Global Statistics", "Check Air Quality for a region","Upload data","Predict Air Quality"])

if selection=='Check Air Quality for a region':
    
    column1 = st.selectbox("Choose Country", countries)
    df_city=df_air[(df_air['Country']==column1)]
    cities=list(df_city['City'])
    column2 = st.selectbox("Choose City", cities)
    df_aqi=df_air[(df_air['Country']==column1)& (df_air['City']==column2)]
    quality=list(df_aqi['AQI Category'])
    #st.markdown(f'<h1 style="color:#336BFF;font-size:34px;">{"Your Air Quality is : "}</h1>', unsafe_allow_html=True)
    class meter():
        def draw_meter(self,a,b):
            data_per = [50,50,50,50,50,50]
            #explode = (0, 0, 0.3, 0, 0, 0)
            categories=['Good(0-50)','Moderate(51-99)','Unhealthy for SG(100-149)','Unhealthy(150-200)','Very Unhealthy(200-300)','Hazardous(>300)']
            plt.pie(data_per,  labels = categories,colors=['green','yellow','orange','red','purple','brown'])
            circle = plt.Circle( (0,0), 0.7, color='white')
            arrow=plt.arrow(0, -0.05, a, b, 
                    head_width = 0.2, 
                    width = 0.1,color='black')
            p=plt.gcf()
            p.gca().add_artist(circle)
            p.gca().add_artist(arrow)
            return p
    meter_placeholder = st
    if quality[0]=='Good':
        st.markdown(f'<h1 style="color:#336BFF;font-size:34px;">{"Good"}</h1>', unsafe_allow_html=True)
        m=meter()
        meter_placeholder.pyplot(m.draw_meter(0.35,0.23))


    elif quality[0]=='Moderate':
        st.markdown(f'<h1 style="color:#336BFF;font-size:34px;">{"Air Quality is : Moderate"}</h1>', unsafe_allow_html=True)
        m=meter()
        meter_placeholder.pyplot(m.draw_meter(0,0.5))

    elif quality[0]=='Unhealthy for sensitive groups':
        st.markdown(f'<h1 style="color:#336BFF;font-size:34px;">{"Unhealthy for sensitive groups"}</h1>', unsafe_allow_html=True)
        m=meter()
        meter_placeholder.pyplot(m.draw_meter(-0.35,0.23))

    elif quality[0]=='Unhealthy':
        st.markdown(f'<h1 style="color:#336BFF;font-size:34px;">{"Unhealthy"}</h1>', unsafe_allow_html=True)
        m=meter()
        meter_placeholder.pyplot(m.draw_meter(-0.37,-0.14))

    elif quality[0]=='Very Unhealthy':
        st.markdown(f'<h1 style="color:#336BFF;font-size:34px;">{"Very Unhealthy"}</h1>', unsafe_allow_html=True)
        m=meter()
        meter_placeholder.pyplot(m.draw_meter(0,-0.39))

    elif quality[0]=='Hazardous':
        st.markdown(f'<h1 style="color:#336BFF;font-size:34px;">{"Hazardous"}</h1>', unsafe_allow_html=True)
        m=meter()
        meter_placeholder.pyplot(m.draw_meter(0.35,-0.19))


if selection=='Check Global Statistics':
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("### Countries with Worst air quality")
        df_air1=df_air[['Country','City','AQI Value','AQI Category']]
        df_bad_aqi = df_air[df_air['AQI Category'] == 'Hazardous']
        hazardous = df_bad_aqi.groupby('Country',as_index=False)['AQI Value'].mean().sort_values(by='AQI Value',ascending=False)
        plt.figure(figsize=(10,6))
        st.pyplot(sns.barplot(x='AQI Value', y='Country',data=hazardous).figure)

    with col2:
        st.markdown("### Countries with Best air quality")
        df_air1=df_air[['Country','City','AQI Value','AQI Category']]
        df_good_aqi = df_air[df_air['AQI Category'] == 'Good']
        good = df_good_aqi.groupby('Country',as_index=False)['AQI Value'].mean().sort_values(by='AQI Value',ascending=False).head(10)
        plt.figure(figsize=(10,6))
        st.pyplot(sns.barplot(x='AQI Value', y='Country',data=good).figure)


    plt.figure(figsize=(10,6))
    sns.barplot(x='AQI Value', y='Country',data=good)
    
    #Pie Chart 
    #with col1:
    st.markdown("### Percent of AQI in each country")
    column1 = st.selectbox("Choose Country", countries)
    df_country=df_air[df_air['Country']==column1]
    plt.figure(figsize=(20,10))
    fig=px.pie(values=df_country['AQI Value'], names=df_country['AQI Category'])
    st.plotly_chart(fig, theme="streamlit")

    #Air Quality Spread across the globes
    plt.figure(figsize=(16, 8))
    st.markdown("### Map Distribution")
    pollutants=['Air Quality','Carbon Monoxide','Nitrogen dioxide','Ozone','Dust Particles']
    column1 = st.selectbox("Choose Pollutant", pollutants)
    pollutant_name='AQI Category'
    if column1=='Carbon Monoxide':
        pollutant_name='CO AQI Category'
    elif column1=='Nitrogen dioxide':
        pollutant_name='NO2 AQI Category'
    elif column1=='Ozone':
        pollutant_name='Ozone AQI Category'
    elif column1=='Dust Particles':
        pollutant_name='PM2.5 AQI Category'
    st.pyplot(sns.scatterplot(data=df_air,x=df_air['lng'],y= df_air['lat'], hue=df_air[pollutant_name]).figure)


    #with col2:
    st.markdown("### Relationship between pollutants and air quality")
    pollutants=['Carbon Monoxide','Nitrogen dioxide','Ozone','Dust Particles']
    column1 = st.selectbox("Choose Pollutant", pollutants)
    pollutant_name='CO AQI Value'
    if column1=='Carbon Monoxide':
        pollutant_name='CO AQI Value'
    elif column1=='Nitrogen dioxide':
        pollutant_name='NO2 AQI Value'
    elif column1=='Ozone':
        pollutant_name='Ozone AQI Value'
    elif column1=='Dust Particles':
        pollutant_name='PM2.5 AQI Value'
    fig=px.scatter(df_air,x=df_air[pollutant_name],
                y= df_air['AQI Value'], 
                size=df_air['AQI Value'],color=df_air['AQI Category'],
                hover_data=['AQI Value'])
    st.plotly_chart(fig, theme="streamlit")

    st.markdown("### In depth relationship between pollutants and Air Quality Index")
    import hiplot as hip
    print(f"HiPlot=={hip.__version__}")
    df_air_new=df_air[['PM2.5 AQI Value','NO2 AQI Value','CO AQI Value','Ozone AQI Value','AQI Value','AQI Category']]
    exp=hip.Experiment.from_dataframe(df_air_new)
    exp_html=exp.to_html()
    st.components.v1.html(exp_html,height=1400)
    












