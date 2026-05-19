import streamlit as st
import pandas as pd
import os

cwd = os.getcwd()

# p1= os.path.join(cwd, "main_page.py")
p1 = "main_page.py"
main_page = st.Page(p1, title="Main Page", icon="🎈")

# p2 = os.path.join(cwd, "page_2.py")
p2 = "page_2.py"
page_2 = st.Page(p2, title="Page 2", icon="❄️")

# p3 = os.path.join(cwd, "page_3.py")
p3 = "page_3.py"
page_3 = st.Page(p3, title="Page 3", icon="🎉")

pg = st.navigation([main_page, page_2, page_3])

pg.run()
