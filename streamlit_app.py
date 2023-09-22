import streamlit

streamlit.title("My Paraents New Healthy Dinner")

streamlit.header("Breakfast Menu")
streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Eggs")
streamlit.text("🥑🍞Avocado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd
myfile = "https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt"
myfruit_df = pd.read_csv(myfile)
# print(mymyfruit_df.head(3))

# Let's put a pick list here so they can pick the fruit they want to include 
myfruit_df.set_index("Fruit")
streamlit.multiselect("Pick some fruits:", list(myfruit_df.index))

# Display the table on the page.
streamlit.dataframe(myfruit_df)

