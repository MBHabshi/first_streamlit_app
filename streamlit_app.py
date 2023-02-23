
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
    fruity_endpoint = "https://fruityvice.com/api/fruit/"
    fruityEndpointWithSearch = fruity_endpoint+this_fruit_choice
    fruityvice_response = requests.get(fruityEndpointWithSearch)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
    
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
    streamlit.error()
    
streamlit.stop()



#my_cur = my_cnx.cursor()





streamlit.header("The Fruit load list contains:")
#Snowflake related function
def get_fruit_load_list():
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()

# Add buttton to load the fruit
if streamlit.button('Get Fruit Load List'):    
    my_data_row = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)
    




