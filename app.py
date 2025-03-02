import streamlit as st

# Set up the page
st.set_page_config(page_title="Unit Converter", page_icon="🔄")

# Design App Layout
st.title("🔄 Unit Converter")
st.write("Convert units with ease!")

# Add Unit Conversion Options
st.sidebar.header("Select a Category")
option = st.sidebar.radio("Choose a conversion type:", ["Length", "Weight", "Temperature"])

# Add Unit Conversion Logic
if option == "Length":
    st.subheader("📏 Length Converter")
    length_option = st.radio("Select conversion:", ["Meter to Centimeter", "Centimeter to Meter"])
    
    col1, col2 = st.columns(2)

    if length_option == "Meter to Centimeter":
        with col1:
            meter = st.number_input("Enter meter value", min_value=0.0, format="%.2f")
        with col2:
            if meter > 0:
                centimeter = meter * 100
                st.success(f"✅ {meter} meters = {centimeter} centimeters")
    elif length_option == "Centimeter to Meter":
        with col1:
            centimeter = st.number_input("Enter centimeter value", min_value=0.0, format="%.2f")
        with col2:
            if centimeter > 0:
                meter = centimeter / 100
                st.success(f"✅ {centimeter} centimeters = {meter} meters")

elif option == "Weight":
    st.subheader("⚖️ Weight Converter")
    weight_option = st.radio("Select conversion:", ["Kilogram to Gram", "Gram to Kilogram"])
    
    col1, col2 = st.columns(2)

    if weight_option == "Kilogram to Gram":
        with col1:
            kilogram = st.number_input("Enter kilogram value", min_value=0.0, format="%.2f")
        with col2:
            if kilogram > 0:
                gram = kilogram * 1000
                st.success(f"✅ {kilogram} kilograms = {gram} grams")
    elif weight_option == "Gram to Kilogram":
        with col1:
            gram = st.number_input("Enter gram value", min_value=0.0, format="%.2f")
        with col2:
            if gram > 0:
                kilogram = gram / 1000
                st.success(f"✅ {gram} grams = {kilogram} kilograms")

elif option == "Temperature":
    st.subheader("🌡️ Temperature Converter")
    temperature_option = st.radio("Select conversion:", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
    
    col1, col2 = st.columns(2)

    if temperature_option == "Celsius to Fahrenheit":
        with col1:
            celsius = st.number_input("Enter Celsius value", format="%.2f")
        with col2:
            fahrenheit = (celsius * 9/5) + 32
            st.success(f"✅ {celsius}°C = {fahrenheit}°F")
    elif temperature_option == "Fahrenheit to Celsius":
        with col1:
            fahrenheit = st.number_input("Enter Fahrenheit value", format="%.2f")
        with col2:
            celsius = (fahrenheit - 32) * 5/9
            st.success(f"✅ {fahrenheit}°F = {celsius}°C")

# Footer
st.markdown("---")
st.markdown("📌 **Pro Tip:** Use the sidebar to switch between different conversion types!")
