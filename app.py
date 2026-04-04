import streamlit as st
from model import DonorModel
from utils import validate_input, blood_groups

st.set_page_config(page_title="Blood Donor Finder", layout="centered")

model = DonorModel("donors.csv")

st.title("🩸 Blood Donor Finder")

menu = st.sidebar.selectbox("Menu", ["Search Donor", "Add Donor"])

# SEARCH DONOR
if menu == "Search Donor":
    st.subheader("🔍 Find a Donor")

    bg = st.selectbox("Select Blood Group", blood_groups())
    city = st.text_input("Enter City")

    if st.button("Search"):
        results = model.search_donor(bg, city)

        if not results.empty:
            st.success("Donors Found!")
            st.dataframe(results)
        else:
            st.warning("No donors found.")

# ADD DONOR
elif menu == "Add Donor":
    st.subheader("➕ Add Donor")

    name = st.text_input("Name")
    bg = st.selectbox("Blood Group", blood_groups())
    city = st.text_input("City")
    contact = st.text_input("Contact Number")

    if st.button("Add"):
        if validate_input(name, contact):
            model.add_donor(name, bg, city, contact)
            st.success("Donor added successfully!")
        else:
            st.error("Invalid input. Check name/contact.")