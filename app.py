import pandas as pd
pd.options.display.max_rows = 200
import streamlit as st
import altair as alt

st.header("Degree Requirements and Average Annualized Compensations in the Cincinnati MSA")
st.write("Maintained by Nick Winnenberg: Nick@Winnenberg.Org.")

df= pd.read_csv("Occupation Data.csv")
df = df.sort_values(by="Average",ascending=False)

c = (
    alt.Chart(df)
    .mark_circle()
    .encode(
        x="Low",
        y="High",
        color ="Degreed",
        tooltip="Occupation"
    )
    .resolve_axis(
        x="Test",
        y="test"
    )
)

st.altair_chart(c)

st.dataframe(df)


