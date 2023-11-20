# pylint: disable=missing-module-docstring

import io
import ast
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
    theme = st.selectbox(
        "How would you like to be review?",
        ["cross_joins", "GroupBy", "window_functions"],
        index=None,
        placeholder="Select a theme...",
    )
    st.write("You selected:", theme)

    exercise = con.execute(f"select * from memory_state where theme = '{theme}'").df()
    st.write(exercise)

st.header("enter your code:")

query = st.text_area(label="votre code SQL ici", key="user_input")
if query:
    result = con.execute(query).df()
    st.dataframe(result)

tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    exercise_tables = ast.literal_eval(exercise.loc[0, "tables"])
    for table in exercise_tables:
        st.write(f"table: {table}")
        df_table = con.execute(f"SELECT * FROM {table}").df()
        st.dataframe(df_table)

with tab3:
    exercise_name = exercise_tables.loc[0,"exercise_name"]
    with open(f"answers/{exercise_name}.sql", "r") as f:
        answer = f.read()
    st.write(answer)




