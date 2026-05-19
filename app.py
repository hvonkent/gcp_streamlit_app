import streamlit as st
import pandas as pd
import os

cwd = os.getcwd()
print(cwd)

page_wd = os.path.join(cwd, 'pages')

page_name = os.path.join(cwd, "main_page.py")
main_page = st.Page(page_name, title="Main Page", icon="🎈")

page_name = os.path.join(cwd, "main_page.py")
page_2 = st.Page(page_name, title="Page 2", icon="❄️")

page_name = os.path.join(cwd, "main_page.py")
page_3 = st.Page(page_name, title="Page 3", icon="🎉")

pg = st.navigation([main_page, page_2, page_3])

st.write("table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

# Run the selected page
#pg.run()
