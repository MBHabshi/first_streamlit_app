
import streamlit
import pandas
import requests
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
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruity_endpoint = "https://fruityvice.com/api/fruit/"
fruityEndpointWithSearch = fruity_endpoint+fruit_choice


fruityvice_response = requests.get(fruityEndpointWithSearch)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

