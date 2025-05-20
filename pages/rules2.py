from datetime import date

import streamlit as st
from sqlalchemy.orm import Session
from models import engine, RulesRead

st.markdown("**1. :exclamation: General rules**")
st.markdown('''
    1.1 - Everybody needs to be in secret society and on [GT](https://www.gettertools.com/com3.kingdoms.com.17/Truppentool/Join/mLN7TChe). Discord is optional.     
    1.2 - There is troop requirement 100% troops to population for romans 60%.  
    1.3 - Play fair. Bots and any scripts are disallowed.  
'''
)

st.markdown("**2. :house_buildings: Settling During the Game**")
st.markdown('''
    2.1 - **Governors need to settle new villages inside the kingdom borders**.
          The only exception are capitols - croppers (9c and 15c or 7cc/6cc with great oasis crop bonus).
          Borders ar marked with blue spots. You can settle on them.  
    2.2 - Reserving a new settling location can only be done when **settlers have been trained and you have enough CP**.  
    2.3 - Governors must not settle on locations reserved for robber camps or treasuries, which will be marked
          on the map :red[RED]. Settling on one of these tiles will result in the village being zeroed.  
    2.4 - Player that dont have crop has priority to get one.  
    2.5 - There is possibility to reserve village to chief. Inactive players and non kingdom members allowed.    
''')

st.markdown("**3. :pirate_flag: Robber Camps**")
st.markdown('''
    3.1 - **Each player can attack up to 2 robber camps.**       
    3.2 - Two hours after the spawning of camps, you are allow to 2 more camps if any are still there.  
    3.3 - The last player to send to a camp must mark it as 'Full' on the map for the rest of the kingdom to see.
    3.4 - Player that sent attack on camp should wrote on camps thread. Kingdom attacks are not visible on phone.    
    3.5 - Only normal attacks are allowed. 
'''
)

st.markdown("**4. :desert_island: Oasis Rules**")
st.markdown('''
    1.1 - **The max number of units in oasis is 250**. Only Cropper Capitals and Treasuries can be excluded from this 
    rule.  
    1.2 -  Generally, priority is given to those that benefit the most from the Oasis. As an example, here is a typical 
    priority list on oasis priorities:  
    15c Capital Treasury > 15c Capital > 9c Capital Treasury > 9c Capital > 7c Capital Treasury > 7c Capital > 6c Capital  
'''
)

username = st.text_input(
    "Enter your travian nick and click Submit to confirm that you read rules",
    "nick",
    key="username",
)
if st.button("Submit"):
    with Session(engine) as session:
        new_entry = RulesRead(username=username, date=str(date.today()))
        rule_object = session.query(RulesRead).where(RulesRead.username == new_entry.username)
        if rule_object.first() is None:
            session.add(new_entry)
        else:
            rule_object.update(new_entry)
        session.commit()

st.text(','.join([f'{it.username} - {it.date}' for it in session.query(RulesRead).all()]))

st.subheader("FAQ", divider=True)
with st.expander("What if I break a rule?"):
    st.write('''
        Depends what you will do. We all do mistakes. First time you will get warning or penalty.
        If you will repeat there might be kick. 
        Rules serves everyone. To win game and spent nice time we need to respect them
    ''')
with st.expander("Are there any exceptions to rules?"):
    st.write('''
        When player come to leadership with good reason to make exception for him we can bend some of rules a bit. 
        For example if there is red spot for robbers and it would be good for player we could try to move it if possible.
        Better ask first before breaking a rule.
    ''')
with st.expander("Where I can find GT url?"):
    st.write('''
        Join link is attached to rules. Click GT in first rule. The same for discord.
    ''')
with st.expander("Why do i need so many troops?"):
    st.write('''
        Travian is war game, to win and protect each other we need strong army. Population do not win wars.
    ''')

