import streamlit as st
import pandas as pd
import seaborn as sns
df = pd.read_csv('supermarket.csv')
dfsmall = df.nsmallest(10, ['store_sales'])
dflarge = df.nlargest(10, ['store_sales'])
st.write('ten smallest store_sales')
st.dataframe(dfsmall)
st.write('ten largest store_sales')
st.dataframe(dflarge)
st.write('Total sales')
df_sales = df['store_sales'].copy()
st.bar_chart(data = df_sales)