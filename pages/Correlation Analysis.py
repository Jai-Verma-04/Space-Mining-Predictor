import streamlit as st
import seaborn as sns
from app import isro

st.write("Correlation Analysis of the isro data")
# st.write(isro.head(4))
corr_matrix = isro.corr(numeric_only=True)

opts =  st.sidebar.multiselect("Select what you want to display -", ('Heatmap', 'Correlation Matrix'))

@st.cache_data
def plot(opts):
    if len(opts)==1:
        if opts[0] == 'Heatmap':
            fig = sns.heatmap(corr_matrix)
            st.pyplot(fig.get_figure())

        elif opts[0] == 'Correlation Matrix':
            st.write(corr_matrix)
    else:
        st.write(corr_matrix)
        fig = sns.heatmap(corr_matrix)
        st.pyplot(fig.get_figure())

plot(opts)