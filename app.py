import streamlit as st

# Set up the page
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

# Custom CSS for better UI
st.markdown("""
    <style>
        .stButton>button {
            width: 100%;
            border-radius: 10px;
            background: #007BFF;
            color: white;
            padding: 10px;
            border: none;
            font-size: 16px;
        }
        .stTextInput, .stNumberInput {
            border-radius: 8px;
            padding: 8px;
            border: 1px solid #ddd;
        }
        .stRadio > label {
            font-weight: bold;
        }
        .stSuccess {
            background: #e6ffe6;
            padding: 10px;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.title("🔄 **Unit Converter**")
st.write("Easily convert Length, Weight, and Temperature units!")

# Sidebar for Category Selection
st.sidebar.header("📌 **Select Conversion Type**")
st.sidebar.markdown("---")
option = st.sidebar.radio("Choose a category:", ["📏 Length", "⚖️ Weight", "🌡️ Temperature"])
st.sidebar.markdown("---")
st.sidebar.info("🔹 Use the sidebar to switch between different conversions!")

# Conversion Logic
if option == "📏 Length":
    st.subheader("📏 **Length Converter**")
    
    col1, col2 = st.columns(2)
    with col1:
        meter = st.number_input("📏 **Enter Meters**", format="%.2f", key="meter")
    with col2:
        centimeter = st.number_input("📏 **Enter Centimeters**", format="%.2f", key="centimeter")

    if meter:
        converted_cm = meter * 100
        st.success(f"✅ {meter} meters = {converted_cm:.2f} centimeters")

    if centimeter:
        converted_m = centimeter / 100
        st.success(f"✅ {centimeter} centimeters = {converted_m:.2f} meters")

elif option == "⚖️ Weight":
    st.subheader("⚖️ **Weight Converter**")

    col1, col2 = st.columns(2)
    with col1:
        kilogram = st.number_input("⚖️ **Enter Kilograms**", format="%.2f", key="kilogram")
    with col2:
        gram = st.number_input("⚖️ **Enter Grams**", format="%.2f", key="gram")

    if kilogram:
        converted_g = kilogram * 1000
        st.success(f"✅ {kilogram} kilograms = {converted_g:.2f} grams")

    if gram:
        converted_kg = gram / 1000
        st.success(f"✅ {gram} grams = {converted_kg:.2f} kilograms")

elif option == "🌡️ Temperature":
    st.subheader("🌡️ **Temperature Converter**")

    col1, col2 = st.columns(2)
    with col1:
        celsius = st.number_input("🌡️ **Enter Celsius**", format="%.2f", key="celsius")
    with col2:
        fahrenheit = st.number_input("🔥 **Enter Fahrenheit**", format="%.2f", key="fahrenheit")

    if celsius:
        converted_fahrenheit = (celsius * 9/5) + 32
        st.success(f"✅ {celsius}°C = {converted_fahrenheit:.2f}°F")

    if fahrenheit:
        converted_celsius = (fahrenheit - 32) * 5/9
        st.success(f"✅ {fahrenheit}°F = {converted_celsius:.2f}°C")

# Footer
st.markdown("---")
st.markdown("✨ **Pro Tip:** Bookmark this page for quick conversions!")
