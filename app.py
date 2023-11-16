# pylint: disable=missing-module-docstring

import io

import duckdb as du
import pandas as pd
import streamlit as st

CSV = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""


CSV2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""
beverages = pd.read_csv(io.StringIO(CSV))

food_items = pd.read_csv(io.StringIO(CSV2))

answer_str = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

solution_df = du.sql(answer_str).df()
with st.sidebar:
    option = st.selectbox(
        "How would you like to be review?",
        ["Joins", "GroupBy", "Windows Functions"],
        index=None,
        placeholder="Select a theme...",
    )
    st.write("You selected:", option)


st.header("enter your code:")
query = st.text_area(label="votre code SQL ici", key="user_input")

if query:
    result = du.sql(query).df()
    st.dataframe(result)

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("Some columns are missing")

    n_lines_difference = result.shape[0] - solution_df.shape[0]
    if n_lines_difference != 0:
        st.write(
            f" result has a {n_lines_difference} lines differences with the solution_df"
        )


tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("expected:")
    st.dataframe(solution_df)


with tab3:
    st.write(answer_str)
