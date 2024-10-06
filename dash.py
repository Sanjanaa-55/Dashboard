import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
data = pd.read_csv('large_ocean_depletion_factors.csv')

# Streamlit page layout
st.title('Ocean Depletion Factors Dashboard')

# Dropdown to select region
selected_region = st.selectbox('Select Region', data['Region'].unique())

# Range slider to select CO2 levels
co2_range = st.slider('Select CO2 Level Range', 
                      float(data['CO2_level'].min()), 
                      float(data['CO2_level'].max()), 
                      (float(data['CO2_level'].min()), float(data['CO2_level'].max())))

# Filter data based on user input
filtered_data = data[(data['Region'] == selected_region) & 
                     (data['CO2_level'] >= co2_range[0]) & 
                     (data['CO2_level'] <= co2_range[1])]

# Create a 3D scatter plot with Plotly
fig = px.scatter_3d(filtered_data, 
                    x='Latitude', 
                    y='Longitude', 
                    z='CO2_level', 
                    color='Water_temperature', 
                    size='Chemical_contamination',
                    hover_name='Region', 
                    title=f'Ocean Depletion Factors in {selected_region}')

# Display the plot in Streamlit
st.plotly_chart(fig)
