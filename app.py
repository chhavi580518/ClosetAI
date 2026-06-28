from ai.predict import predict_clothing
import streamlit as st
from PIL import Image

from repository.clothing_repository import (
    save_clothing,
    get_all_clothes,
    search_clothes,
    get_total_clothes,
    get_category_counts,
    get_color_counts,
    delete_clothing,
    get_recommended_outfit,
    get_weather_outfit,
    get_packing_list,
)

from repository.image_repository import save_image

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="ClosetAI",
    page_icon="👔",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------
st.sidebar.title("👔 ClosetAI")
st.sidebar.markdown("---")

menu = [
    "🏠 Home",                           
    "👕 My Wardrobe",
    "📤 Upload Clothes",
    "✨ Outfit Recommender",
    "🌦 Weather Stylist",
    "🧳 Packing Assistant",
    "📊 Statistics",
    "⚙ Settings"
]

choice = st.sidebar.radio("Navigation", menu)

# ===================================================
# HOME
# ===================================================

if choice == "🏠 Home":

    logo = Image.open("assets/logos/logo.png")

    col1, col2 = st.columns([1, 5])

    with col1:
        st.image(logo, width=90)

    with col2:
        st.title("ClosetAI")
        st.subheader("Your AI Personal Stylist")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
### Welcome 👋

ClosetAI helps you:

✅ Organize your wardrobe

✅ Detect clothing automatically

✅ Get outfit recommendations

✅ Plan trip packing

✅ Weather-based styling

✅ AI Fashion Assistant
""")


    st.markdown("---")

    st.success("Project Setup Completed Successfully!")

# ===================================================
# UPLOAD CLOTHES
# ===================================================

elif choice == "📤 Upload Clothes":

    st.title("📤 Upload Clothes")

    uploaded_file = st.file_uploader(
        "Choose a clothing image",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file:

        st.image(uploaded_file, width=250)
        import tempfile

# Save uploaded image temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
            tmp.write(uploaded_file.getbuffer())
            temp_path = tmp.name

# AI Prediction
        prediction, confidence = predict_clothing(temp_path)

        st.success(f"🤖 AI Prediction: {prediction.title()}")
        st.info(f"Confidence: {confidence:.2f}%")

# Use AI prediction
        clothing_type = prediction.title()

        st.subheader("Clothing Details")


        color = st.text_input("Color")

        pattern = st.text_input("Pattern")

        style = st.selectbox(
            "Style",
            [
                "Casual",
                "Formal",
                "Sports",
                "Party"
            ]
        )

        season = st.selectbox(
            "Season",
            [
                "Summer",
                "Winter",
                "Rainy",
                "All Season"
            ]
        )

        if st.button("Save Clothing"):

            path = save_image(
                uploaded_file,
                clothing_type
            )

            save_clothing(
                path,
                clothing_type,
                color,
                pattern,
                style,
                season
            )

            st.success("✅ Clothing Saved Successfully!")

# ===================================================
# MY WARDROBE
# ===================================================

# ===================================================
# MY WARDROBE
# ===================================================

elif choice == "👕 My Wardrobe":

    st.title("👕 My Wardrobe")

    search = st.text_input("🔍 Search Clothing")

    if search:
        clothes = search_clothes(search)
    else:
        clothes = get_all_clothes()

    # Temporary Debug (Remove later)

    if not clothes:

        st.info("No clothes uploaded yet.")

    else:

        cols = st.columns(3)

        for index, cloth in enumerate(clothes):

            with cols[index % 3]:

                # Display Image
                try:
                    st.image(
                        cloth[1],
                        width="stretch"
                    )
                except:
                    st.warning("Image not found.")

                # Display Details
                st.markdown(f"### {cloth[2]}")
                st.write(f"🎨 Color : {cloth[3]}")
                st.write(f"🧵 Pattern : {cloth[4]}")
                st.write(f"👔 Style : {cloth[5]}")
                st.write(f"🌤 Season : {cloth[6]}")

                # Delete Button
                if st.button(
                    "🗑 Delete",
                    key=f"delete_{cloth[0]}"
                ):

                    delete_clothing(
                        cloth[0],
                        cloth[1]
                    )

                    st.success("Deleted Successfully!")

                    st.rerun()

                st.markdown("---")

# ===================================================
# OTHER PAGES
# ===================================================

elif choice == "✨ Outfit Recommender":

    st.title("✨ AI Outfit Recommender")

    occasion = st.selectbox(
        "Select Occasion",
        [
            "Casual",
            "Formal",
            "Party",
            "Sports"
        ]
    )

    if st.button("Recommend Outfit"):

        outfit = get_recommended_outfit(occasion)

        if not outfit:
            st.warning("No outfit found.")

        else:

            st.success(f"Recommended {occasion} Outfit")

            cols = st.columns(len(outfit))

            for i, cloth in enumerate(outfit):

                with cols[i]:

                    st.image(cloth[1], width="stretch")

                    st.markdown(f"### {cloth[2]}")
                    st.write(f"🎨 Color : {cloth[3]}")
                    st.write(f"🧵 Pattern : {cloth[4]}")
                    st.write(f"👔 Style : {cloth[5]}")
                    st.write(f"🌤 Season : {cloth[6]}")
elif choice == "🌦 Weather Stylist":

    st.title("🌦 Weather Stylist")

    st.write("Select today's weather.")

    weather = st.selectbox(
        "Weather",
        [
            "Hot",
            "Cold",
            "Rainy",
            "Normal"
        ]
    )

    if st.button("Get Recommendation"):

        clothes = get_weather_outfit(weather)

        if not clothes:
            st.warning("No suitable clothes found.")

        else:

            st.success(f"Recommended Outfit for {weather} Weather")

            cols = st.columns(len(clothes))

            for i, cloth in enumerate(clothes):

                with cols[i]:

                    st.image(
                        cloth[1],
                        width="stretch"
                    )

                    st.markdown(f"### {cloth[2]}")
                    st.write(f"🎨 Color : {cloth[3]}")
                    st.write(f"🧵 Pattern : {cloth[4]}")
                    st.write(f"👔 Style : {cloth[5]}")
                    st.write(f"🌤 Season : {cloth[6]}")

elif choice == "🧳 Packing Assistant":

    st.title("🧳 Packing Assistant")

    destination = st.text_input("Destination")

    days = st.slider(
        "Trip Duration (Days)",
        1,
        15,
        3
    )

    season = st.selectbox(
        "Season",
        [
            "Summer",
            "Winter",
            "Rainy",
            "All Season"
        ]
    )

    if st.button("Generate Packing List"):

        clothes = get_packing_list(days, season)

        if not clothes:

            st.warning("No suitable clothes found.")

        else:

            st.success(
                f"Packing List for {destination}"
            )

            cols = st.columns(3)

            for i, cloth in enumerate(clothes):

                with cols[i % 3]:

                    st.checkbox(
                        f"Pack {cloth[2]}",
                        key=f"pack_{cloth[0]}"
                    )

                    st.image(
                        cloth[1],
                        width="stretch"
                    )

                    st.write(f"**{cloth[2]}**")
                    st.write(f"🎨 {cloth[3]}")
                    st.write(f"👔 {cloth[5]}")

elif choice == "📊 Statistics":

    st.title("📊 Closet Statistics")

    total = get_total_clothes()

    st.metric("👕 Total Clothes", total)

    st.markdown("---")

    st.subheader("📂 Clothes by Category")

    category_data = get_category_counts()

    for category, count in category_data:
        st.write(f"**{category}** : {count}")

    st.markdown("---")

    st.subheader("🎨 Clothes by Color")

    color_data = get_color_counts()

    for color, count in color_data:
        st.write(f"**{color}** : {count}")
