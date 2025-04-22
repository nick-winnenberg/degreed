import pandas as pd
pd.options.display.max_rows = 200
import streamlit as st
import altair as alt

st.header("Degree Requirements and Average Annualized Compensations")
st.write("Maintained by Nick Winnenberg: Nick@Winnenberg.Org.")

df= pd.read_csv("Occupation Data.csv")
df = df.sort_values(by="Average",ascending=False)

st.scatter_chart(data=df,x="Low",y="High", color="Degreed",size="Occupation",x_label="Entry Level Compensation ($)",y_label="Peak Compensation ($)",)

c = (
    alt.Chart(df)
    .mark_circle()
    .encode(
        x="Low",
        y="High",
        color ="Degreed",
        tooltip="Occupation"
    )
)

st.altair_chart(c)

st.dataframe(df)


