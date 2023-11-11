import streamlit
import pandas

streamlit.title('My Parents New Healthy Dinner')

streamlit.header('Breakfast Menu 🤤')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit') # This sets the fruit name column as the index

#Add a pick list here so they can pick the fruit they want to include
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries']) #This addes the multi select, this also defines where the list is from. Also we add Avocados and Strawberries to be preselected.

#Displace the table on the page
streamlit.dataframe(my_fruit_list)
