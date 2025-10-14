import streamlit as st

st.title("SNEAKO")
st.write(
    "FRESH GAME FRESH KICKS"
)

pages = {
    "Your Account":[
        st.Page("my_profile.py", title="My Profile")
        st.Page("my_listing.py", title="My Listings")
    ],
    st.Page("browse.py", title="Browse"
    st.Page("discounts.py", title="{}sale.format(type_of_sale)"
            }
pg = st.navigation(pages)
pg.run()
