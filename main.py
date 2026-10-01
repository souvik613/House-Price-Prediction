
import streamlit as st

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 House Price Prediction")
st.write("Enter the house details below to predict the price.")

st.divider()

# ---------------- INPUTS ----------------

col1, col2, col3 = st.columns(3)

with col1:

    area = st.number_input(
        "Area",
        min_value=0,
        value=1000
    )

    bedrooms = st.number_input(
        "Bedrooms",
        min_value=0,
        value=2
    )

    bathrooms = st.number_input(
        "Bathrooms",
        min_value=0,
        value=2
    )

    stories = st.number_input(
        "Stories",
        min_value=0,
        value=1
    )

    parking = st.number_input(
        "Parking",
        min_value=0,
        value=1
    )


with col2:

    age = st.number_input(
        "Age",
        min_value=0,
        value=5
    )

    city = st.selectbox(
        "City",
        [
            "Pune",
            "Kolkata",
            "Chennai",
            "Delhi",
            "Mumbai",
            "Hyderabad",
            "Bangalore"
        ]
    )

    furnishing = st.selectbox(
        "Furnishing",
        [
            "Semi-Furnished",
            "Unfurnished",
            "Furnished"
        ]
    )

    main_road = st.selectbox(
        "Main Road",
        ["Yes", "No"]
    )

    guest_room = st.selectbox(
        "Guest Room",
        ["Yes", "No"]
    )


with col3:

    basement = st.selectbox(
        "Basement",
        ["Yes", "No"]
    )

    water_supply = st.selectbox(
        "Water Supply",
        [
            "Both",
            "Corporation",
            "Borewell"
        ]
    )

    air_conditioning = st.selectbox(
        "Air Conditioning",
        ["No", "Yes"]
    )

    preferred_tenant = st.selectbox(
        "Preferred Tenant",
        [
            "Company",
            "Bachelor",
            "Family"
        ]
    )

    locality_rating = st.slider(
        "Locality Rating",
        min_value=1,
        max_value=5,
        value=3
    )


st.divider()

# ---------------- PREDICTION ----------------

if st.button("Predict House Price"):

    # Temporary prediction
    predicted_price = 5000000

    st.success("Prediction completed!")

    st.metric(
        "Estimated House Price",
        f"₹{predicted_price:,.0f}"
    )

