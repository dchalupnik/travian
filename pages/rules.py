import streamlit as st

st.title("Moltress - Rules")


with st.expander("Settling During the Game"):
    st.write('''
        1 - Governors need to settle new villages inside the kingdom borders. The only exception are capitols - croppers (9c and 15c or 7cc/6cc with great oasis crop bonus). 
        2 - Reserving a new settling location can only be done when settlers have been trained and you have enough CP. 
        3 - Governors must not settle on locations reserved for robber camps or treasuries, which will be marked on the map (RED). Settling on one of these tiles will result in the village being zeroed. 
    ''')
    st.image("https://static.streamlit.io/examples/dice.jpg")