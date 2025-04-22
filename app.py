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
        x=alt.X("Low", axis=alt.Axis(title="Low/Entry-Level Compensation ($)")),
        y=alt.Y("High", axis= alt.Axis(title="High/Peak Compensation ($)")),
        color ="Degreed",
        tooltip="Occupation"
    )
)

st.altair_chart(c)

st.dataframe(df)


