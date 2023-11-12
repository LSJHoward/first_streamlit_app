import streamlit
import pandas
import requests
import snowflake.connector

streamlit.title('My Parents New Healthy Dinner')

streamlit.header('Breakfast Menu 🤤')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit') # This sets the fruit name column as the index

#Add a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries']) #This addes the multi select, this also defines where the list is from. Also we add Avocados and Strawberries to be preselected.
fruits_to_show = my_fruit_list.loc[fruits_selected] #This calls the fruits_selected variable and convers it into a boolean array.

#Display the table on the page
streamlit.dataframe(fruits_to_show)

#New section to display the fruity vice API response
streamlit.header('Fruityvice Fruit Advice!')

#Fruityvice API response due to the REQUESTS library imported above
fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice) #This calls the api using the input variable from fruit_choice
streamlit.text(fruityvice_response.json()) #This shows it on the screen but it looks like json

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#Now output the normalized data as a table
streamlit.dataframe(fruityvice_normalized)
