import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.write("Hello, Welcome to ISRO Space Exploration App")

st.markdown('''
    * **This is the ISRO data**
    * **The original Cleaned Data Source can be found at [Github](https://github.com/Jai-Verma-04/ISRO-Space-Mining)**
''')


isro = pd.read_csv("isro.csv")

isro = isro.rename(columns={
'Celestial Body' : "body",
'Distance from Earth (M km)' : "distance",
'Iron (%)' : "iron",
'Nickel (%)' : "nickel",
'Water Ice (%)' : "water_ice",
'Other Minerals (%)' : "other",
'Estimated Value (B USD)' : "value",
'Sustainability Index' : "sustainability",
'Efficiency Index' : "efficiency",
'Potential Mining Site' : "mining",
'Gravity (m/s²)' : "gravity",
'Surface Temperature (K)' : "temp",
'Orbital Period (days)' : "orbit",
'Rotation Period (hours)' : "rotation",
'Axial Tilt (degrees)' : "tilt"
})

st.sidebar.text("This is a sidebar")

opts = st.sidebar.multiselect("Select the columns you want to see", isro.columns)
st.dataframe(isro[opts].head(5), use_container_width=True)

colnames = ['iron',                     
    'nickel',
    'water_ice',
    'other',
    'distance',
    'gravity',
    'temp',
    'value',
    'tilt',
    'rotation',
    'orbit',
    'efficiency'
    ]

def plot_hist(field):
    fig, ax = plt.subplots(1,1)
    ax.hist(isro[field])
    ax.set_title(f"Histogram of {field}")
    st.pyplot(fig)

corr_matrix = isro.corr(numeric_only=True)

def plot_heatmap(corr_matrix):
    sns.heatmap(corr_matrix)

field = st.sidebar.selectbox("Select which histogram you want to see", options=colnames)

st.sidebar.write("selected field is: ", field)

plot_hist(field)

st.sidebar.divider()