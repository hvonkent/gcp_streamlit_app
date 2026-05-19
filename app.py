import streamlit as st
import pandas as pd
import os

cwd = os.getcwd()
print(cwd)

p1= os.path.join(cwd, "main_page.py")
main_page = st.Page(p1, title="Main Page", icon="🎈")

p2 = os.path.join(cwd, "page_2.py")
page_2 = st.Page(p2, title="Page 2", icon="❄️")

p3 = os.path.join(cwd, "page_3.py")
page_3 = st.Page(p3, title="Page 3", icon="🎉")

pg = st.navigation([main_page, page_2, page_3])



st.write("table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

pg.run()
