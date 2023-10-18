import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import hiplot as hip
from PIL import Image
from streamlit import runtime
#from streamlit_option_menu import option_menu
runtime.exists()



st.set_page_config(page_title="Air Quality Analysis", layout="wide")

# CSS styles
bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
background-image: url('https://images.unsplash.com/photo-1536514498073-50e69d39c6cf?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxfDB8MXxyYW5kb218MHx8fHx8fHx8MTY4MjQzODAzMA&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=1080');
background-size: cover;
background-repeat: no-repeat;
}
</style>
'''
#https://images.unsplash.com/photo-1528459801416-a9e53bbf4e17
#https://www.gettyimages.ca/detail/photo/splashed-with-fresh-air-royalty-free-image/1127069296?adppopup=true
#WQD6TCLOozg
st.markdown(bg_img, unsafe_allow_html=True)

#selection = option_menu(None, ["Home", "Check Global Statistics", "Check Air Quality for a region"], 
    #icons=['house', 'cloud-upload', "list-task", 'gear'], 
    #menu_icon="cast", 
 #   default_index=0, orientation="horizontal")
#st.title('Air Quality Analysis')
st.markdown(f'<h1 style="color:#336BFF;font-size:45px;">{"BreezoScan"}</h1>', unsafe_allow_html=True)
st.markdown('**Breathing Innovation: Empowering Lives with Precision Air Quality Analysis.**')
#st.markdown('**Breathing Innovation: Empowering Lives with Precision Air Quality Analysis.**')



df_air=pd.read_csv('/Users/sahanamanjunath/Downloads/AQI and Lat Long of Countries.csv')
countries=list(df_air['Country'].unique())

def redirect_to_streamline():
    # Run the other Streamlit script for the streamline page
    import subprocess
    subprocess.run(["streamlit", "run", "index.py"])


if st.sidebar.button("Go back to Home page"):
        # Redirect to the streamline page
    redirect_to_streamline()



selection = st.sidebar.selectbox("Choose your operation", ["Check Global Statistics", "Check Air Quality for desired region","Learn about Air Quality Index(AQI)","Air Quality Prediction"])


#, "Check Air Quality for desired region","Learn about Air Quality Index(AQI)","Air Quality Prediction"))

#radio(

 #   "Choose your operation",

  #  ("About","Check Global Statistics", "Check Air Quality for desired region","Learn about Air Quality Index(AQI)","Air Quality Prediction"))

if selection=='Learn about Air Quality Index(AQI)':
#if st.sidebar.button("About",key="default_button_key"):
    st.markdown('**This page provides information to the user on Air Quality Index (AQI), a significant parameter in measuring the air quality**')
    image = Image.open('/Users/sahanamanjunath/Downloads/girl-transformed.jpg')
    st.image(image, caption='Breathing Innovation: Empowering Lives with Precision Air Quality Analysis.')
    st.markdown("The Air Quality Index (AQI) is a numerical scale used to communicate how polluted the air currently is or how polluted it is forecast to become. It quantifies the concentration of specific air pollutants into a single number, which can help people understand the potential health impacts of breathing the air in a particular area. The pollutants commonly measured to calculate the AQI include:")
    bullet_points = [
    "Ground-level ozone (O3)",
    "Particulate matter (PM2.5 and PM10)",
    "Carbon monoxide (CO)",
    "Nitrogen dioxide (NO2)"
    ]
    bullet_points_formatted = "\n".join([f"- {item}" for item in bullet_points])
    st.markdown(bullet_points_formatted)
    st.markdown("The AQI scale typically ranges from 0 to 500, with lower values indicating better air quality and higher values indicating worse air quality. The scale is divided into different categories, each corresponding to a range of AQI values and indicating a different level of health concern. These categories are:")
    bullet_points2 = [
        "0-50 (Good): Air quality is considered satisfactory, and air pollution poses little or no risk.",
        "51-100 (Moderate): Air quality is acceptable; however, some pollutants may be a concern for a small number of individuals who are sensitive to air pollution.",
        "101-150 (Unhealthy for sensitive groups): Members of sensitive groups may experience health effects, but the general public is less likely to be affected.",
        "151-200 (Unhealthy): Everyone may begin to experience adverse health effects, and members of sensitive groups may experience more serious effects.",
        "201-300 (Very Unhealthy): Health alert! Everyone may experience more serious health effects.",
        "301-500 (Hazardous): Health warnings of emergency conditions; the entire population is more likely to be affected."
    ]
    bullet_points_formatted2 = "\n".join([f"- {item}" for item in bullet_points2])
    st.markdown(bullet_points_formatted2)
    st.markdown("It's important to note that different countries might have their own AQI scales with slight variations in the pollutants measured and the corresponding health categories. The AQI is often reported by weather agencies and environmental organizations and is widely used to inform the public about air quality conditions in their area. People can use this information to make decisions to protect their health, such as reducing outdoor activities on days with poor air quality, especially for individuals with respiratory or heart conditions, children, and the elderly.")

if selection=='Check Global Statistics':
#if st.sidebar.button("Check Global Statistics"): 
    st.markdown("**This page depicts a variety of visualizations to display the Air Quality (Index) distribution across the entire globe. Furthermore, the distribution of airborne pollutants such as Ozone, dust particles, carbon monoxide, and nitrogen dioxide is also shown for the purpose of analyzing air pollution factors.**")
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
    st.markdown("### Proportion of Air Quality spread across each country")
    column1 = st.selectbox("Choose Country", countries)
    df_country=df_air[df_air['Country']==column1]
    plt.figure(figsize=(20,10))
    fig=px.pie(values=df_country['AQI Value'], names=df_country['AQI Category'])
    st.plotly_chart(fig, theme="streamlit")

    #Air Quality Spread across the globes
    plt.figure(figsize=(16, 8))
    st.markdown("### Global distribution of airborne contaminants and the Air Quality Index")
    #pollutants=['Air Quality','Carbon Monoxide','Nitrogen dioxide','Ozone','Dust Particles']
    #column1 = st.selectbox("Choose Pollutant", pollutants)
    column1 = st.radio(

    "Select the distribution of the characteristics that you wish to see worldwide.",

    ('Air Quality Index','Carbon Monoxide','Nitrogen dioxide','Ozone','Dust Particles'))
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
    st.markdown("Hover over each row in the following table to see the relationship between all the pollutants and Air Quality Index")
    print(f"HiPlot=={hip.__version__}")
    df_air_new=df_air[['PM2.5 AQI Value','NO2 AQI Value','CO AQI Value','Ozone AQI Value','AQI Category','AQI Value']]
    exp=hip.Experiment.from_dataframe(df_air_new)
    exp_html=exp.to_html()
    st.components.v1.html(exp_html,height=1400)
    

if selection=='Check Air Quality for desired region':
#if st.sidebar.button("Check Air Quality for desired region"): 
    st.markdown("**This page allows the user to examine the quality of the air in a particular region by selecting the country and city of their choice. To view the safe Air Quality Index (AQI) index levels, please refer to the AQI table below.**")
    image = Image.open('/Users/sahanamanjunath/Downloads/aqi_table2.jpg')
    st.image(image, caption='Breathing Innovation: Empowering Lives with Precision Air Quality Analysis.')
    column1 = st.selectbox("Choose Country", countries)
    df_city=df_air[(df_air['Country']==column1)]
    cities=list(df_city['City'].unique())
    column2 = st.selectbox("Choose City", cities)
    df_aqi=df_air[(df_air['Country']==column1)& (df_air['City']==column2)]
    quality=list(df_aqi['AQI Category'])
    #st.markdown(f'<h1 style="color:#336BFF;font-size:34px;">{"Your Air Quality is : "}</h1>', unsafe_allow_html=True)
    class meter():
        def draw_meter(self,a,b):
            data_per = [50,50,50,50,50,50]
            #explode = (0, 0, 0.3, 0, 0, 0)
            categories=['Good','Moderate','Unhealthy for Sensitive Groups','Unhealthy','Very Unhealthy','Hazardous']
            plt.pie(data_per,  labels = categories,colors=['green','yellow','orange','red','purple','brown'])
            #plt.legend(categories, loc='upper left')
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














