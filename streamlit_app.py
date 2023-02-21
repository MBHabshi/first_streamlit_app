
import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")




streamlit.title('My Parents new healthy diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 1-Porridge')
streamlit.text('🍞2-French toast')
streamlit.text('3-Coffee')

streamlit.multiselect("Pick some fruits:", list(my_fruits_list.index))

streamlit.dataframe(my_fruit_list)
