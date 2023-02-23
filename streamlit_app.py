
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')



streamlit.title('My Parents new healthy diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 1-Porridge')
streamlit.text('🍞2-French toast')
streamlit.text('3-Coffee')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit Advice...')

def get_fruityvice_data(this_fruit_choice):
    streamlit.write("in func")
    fruity_endpoint = "https://fruityvice.com/api/fruit/"
    fruityEndpointWithSearch = fruity_endpoint+this_fruit_choice
    streamlit.write(fruityEndpointWithSearch)
    fruityvice_response = requests.get(fruityEndpointWithSearch)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.write('Before Return')
    return fruityvice_normalised
streamlit.write("before try")
try:
  streamlit.write("in try")
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Apple')
  if not fruit_choice:
    streamlit.write("if check")
    streamlit.error("Please select a fruit to get information.")
    
  else:
    streamlit.write("else")
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
    streamlit.write("exception")
    streamlit.error()

streamlit.stop()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
#streamlit.text("Hello from Snowflake:")
fruit_choice_sf = streamlit.text_input('What fruit would you like?','Apple')
streamlit.write('The user entered ', fruit_choice_sf)

streamlit.header("The Fruit load list contains:")
streamlit.dataframe(my_data_row)

streamlit.write("Thanks for adding ",fruit_choice_sf)
my_cur.execute("insert into FRUIT_LOAD_LIST values ('from streamli')")


