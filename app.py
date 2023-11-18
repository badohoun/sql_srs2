# pylint: disable=missing-module-docstring

import io

import duckdb as du
import pandas as pd
import streamlit as st


answer_str = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

con = du.connect(database="data/exercises_sql_tables.duckdb", read_only=False)
#solution_df = du.sql(answer_str).df()
with st.sidebar:
    option = st.selectbox(
        "How would you like to be review?",
        ["cross_joins", "GroupBy", "Windows Functions"],
        index=None,
        placeholder="Select a theme...",
    )
    st.write("You selected:", option)

    exercise  = con.execute("select * from memory_state where theme= '{theme}'").df()
    st.write(exercise)


st.header("enter your code:")

query = st.text_area(label="votre code SQL ici", key="user_input")
