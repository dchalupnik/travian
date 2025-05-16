import streamlit as st


st.title('Moltress')

pg = st.navigation(["pages/rules.py", "pages/op.py"])
pg.run()