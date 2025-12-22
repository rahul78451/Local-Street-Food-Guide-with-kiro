import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Delhi Eats – Local Street Food Guide",
    page_icon="🍔",
    layout="wide"
)

# ---------------- CUSTOM CSS (FIXED & STABLE) ----------------
st.markdown("""
<style>

/* GLOBAL */
body {
    background-color: #ffffff;
}

/* HEADER */
.header {
    background: linear-gradient(90deg, #E23744, #F4B400);
    padding: 30px;
    border-radius: 20px;
    color: white;
    margin-bottom: 30px;
}

.header h1 {
    font-size: 48px;
    font-weight: 900;
    margin: 0;
}

.header p {
    font-size: 18px;
    opacity: 0.95;
}

/* FOOD CARD */
.food-card {
    background-color: #ffffff;
    padding: 26px;
    border-radius: 18px;
    box-shadow: 0px 12px 32px rgba(0,0,0,0.15);
    margin-bottom: 24px;
    border-left: 8px solid #E23744;
}

/* TEXT FIX (IMPORTANT) */
.food-name {
    font-size: 28px;
    font-weight: 900;
    color: #111111 !important;
    margin-bottom: 6px;
    user-select: none;
}

.food-name::selection {
    background: transparent;
}

.shop-name {
    font-size: 17px;
    color: #444444 !important;
    margin-bottom: 4px;
}

.price {
    font-size: 18px;
    font-weight: 800;
    color: #0F9D58 !important;
    margin-bottom: 6px;
}

.map a {
    color: #E23744 !important;
    font-weight: 800;
    text-decoration: none;
}

/* BUTTON */
.stButton button {
    background-color: #E23744 !important;
    color: white !important;
    font-size: 18px !important;
    font-weight: 800 !important;
    border-radius: 14px !important;
    padding: 12px 28px !important;
}

/* SIDEBAR */
.sidebar-title {
    font-size: 20px;
    font-weight: 800;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER UI ----------------
st.markdown("""
<div class="header">
    <h1>🍔 Delhi Eats</h1>
    <p>Discover the best street food near you • Powered by Kiro</p>
</div>
""", unsafe_allow_html=True)

# ---------------- DATA ---------------- #
food_data = {
    "Chandni Chowk": [
        {"food": "Chole Bhature", "shop": "Sita Ram Diwan Chand", "price": 120,
         "map": "https://www.google.com/maps?q=Sita+Ram+Diwan+Chand+Delhi"},
        {"food": "Paratha", "shop": "Paranthe Wali Gali", "price": 100,
         "map": "https://www.google.com/maps?q=Paranthe+Wali+Gali+Delhi"},
        {"food": "Jalebi", "shop": "Old Famous Jalebi Wala", "price": 80,
         "map": "https://www.google.com/maps?q=Old+Famous+Jalebi+Wala+Chandni+Chowk"}
    ],

    "Connaught Place": [
        {"food": "Raj Kachori", "shop": "Haldiram's", "price": 160,
         "map": "https://www.google.com/maps?q=Haldirams+Connaught+Place"},
        {"food": "Chole Kulche", "shop": "Kumar Kulche", "price": 120,
         "map": "https://www.google.com/maps?q=Kumar+Kulche+CP"},
        {"food": "Sandwich", "shop": "Wenger's", "price": 180,
         "map": "https://www.google.com/maps?q=Wengers+Connaught+Place"}
    ],

    "Karol Bagh": [
        {"food": "Pav Bhaji", "shop": "Anand Restaurant", "price": 180,
         "map": "https://www.google.com/maps?q=Anand+Restaurant+Karol+Bagh"},
        {"food": "Kulfi Falooda", "shop": "Roshan Di Kulfi", "price": 120,
         "map": "https://www.google.com/maps?q=Roshan+Di+Kulfi+Karol+Bagh"},
        {"food": "Chole Kulche", "shop": "Standard Corner", "price": 140,
         "map": "https://www.google.com/maps?q=Standard+Corner+Karol+Bagh"}
    ],

    "Lajpat Nagar": [
        {"food": "Golgappa", "shop": "Nagpal Chaat", "price": 60,
         "map": "https://www.google.com/maps?q=Nagpal+Chaat+Lajpat+Nagar"},
        {"food": "Aloo Tikki", "shop": "Bittu Tikki Wala", "price": 80,
         "map": "https://www.google.com/maps?q=Bittu+Tikki+Wala+Lajpat+Nagar"},
        {"food": "Chaat Papdi", "shop": "Gupta Chaat", "price": 100,
         "map": "https://www.google.com/maps?q=Gupta+Chaat+Lajpat+Nagar"}
    ],

    "Saket": [
        {"food": "Rolls", "shop": "Kathi Junction", "price": 150,
         "map": "https://www.google.com/maps?q=Kathi+Junction+Saket"},
        {"food": "Momos", "shop": "Wow Momos", "price": 140,
         "map": "https://www.google.com/maps?q=Wow+Momos+Saket"},
        {"food": "Burger", "shop": "Burger Singh", "price": 200,
         "map": "https://www.google.com/maps?q=Burger+Singh+Saket"}
    ],

    "Hauz Khas": [
        {"food": "Street Fries", "shop": "HKV Food Stalls", "price": 200,
         "map": "https://www.google.com/maps?q=Hauz+Khas+Village+Food"},
        {"food": "Momos", "shop": "Yeti Cafe", "price": 180,
         "map": "https://www.google.com/maps?q=Yeti+Hauz+Khas"},
        {"food": "Pasta", "shop": "La Piazza", "price": 250,
         "map": "https://www.google.com/maps?q=La+Piazza+Hauz+Khas"}
    ],

    "Rajouri Garden": [
        {"food": "Shawarma", "shop": "Al Bake", "price": 180,
         "map": "https://www.google.com/maps?q=Al+Bake+Rajouri+Garden"},
        {"food": "Momos", "shop": "Chawla Momos", "price": 140,
         "map": "https://www.google.com/maps?q=Chawla+Momos+Rajouri+Garden"},
        {"food": "Chaat", "shop": "Aggarwal Chaat", "price": 120,
         "map": "https://www.google.com/maps?q=Aggarwal+Chaat+Rajouri+Garden"}
    ],

    "Punjabi Bagh": [
        {"food": "Tandoori Snacks", "shop": "Kake Da Hotel", "price": 220,
         "map": "https://www.google.com/maps?q=Kake+Da+Hotel+Punjabi+Bagh"},
        {"food": "Momos", "shop": "Yo Tibet", "price": 160,
         "map": "https://www.google.com/maps?q=Yo+Tibet+Punjabi+Bagh"},
        {"food": "Chaat", "shop": "Bikanerwala", "price": 140,
         "map": "https://www.google.com/maps?q=Bikanerwala+Punjabi+Bagh"}
    ],

    "Janakpuri": [
        {"food": "Chole Kulche", "shop": "Om Chole Kulche", "price": 120,
         "map": "https://www.google.com/maps?q=Om+Chole+Kulche+Janakpuri"},
        {"food": "Golgappa", "shop": "Local Chaat Stall", "price": 60,
         "map": "https://www.google.com/maps?q=Golgappa+Janakpuri"},
        {"food": "Pav Bhaji", "shop": "Street Junction", "price": 150,
         "map": "https://www.google.com/maps?q=Pav+Bhaji+Janakpuri"}
    ],

    "Dwarka": [
        {"food": "Vada Pav", "shop": "Goli Vada Pav", "price": 60,
         "map": "https://www.google.com/maps?q=Goli+Vada+Pav+Dwarka"},
        {"food": "Rolls", "shop": "Kathi Rolls", "price": 150,
         "map": "https://www.google.com/maps?q=Kathi+Rolls+Dwarka"},
        {"food": "Chaat", "shop": "Bikanerwala", "price": 120,
         "map": "https://www.google.com/maps?q=Bikanerwala+Dwarka"}
    ],

    "Rohini": [
        {"food": "Chole Bhature", "shop": "Om Corner", "price": 140,
         "map": "https://www.google.com/maps?q=Chole+Bhature+Rohini"},
        {"food": "Momos", "shop": "Tandoori Momos Point", "price": 130,
         "map": "https://www.google.com/maps?q=Momos+Rohini"},
        {"food": "Kulfi", "shop": "Kulfi Junction", "price": 70,
         "map": "https://www.google.com/maps?q=Kulfi+Rohini"}
    ],

    "Pitampura": [
        {"food": "Rolls", "shop": "Nazeer Foods", "price": 160,
         "map": "https://www.google.com/maps?q=Nazeer+Foods+Pitampura"},
        {"food": "Chaat", "shop": "Aggarwal Sweets", "price": 120,
         "map": "https://www.google.com/maps?q=Aggarwal+Sweets+Pitampura"},
        {"food": "Burger", "shop": "Burger Singh", "price": 200,
         "map": "https://www.google.com/maps?q=Burger+Singh+Pitampura"}
    ],

    "Laxmi Nagar": [
        {"food": "Momos", "shop": "Delhi Momos", "price": 100,
         "map": "https://www.google.com/maps?q=Momos+Laxmi+Nagar"},
        {"food": "Chaat", "shop": "Shree Ram Chaat", "price": 90,
         "map": "https://www.google.com/maps?q=Chaat+Laxmi+Nagar"},
        {"food": "Pav Bhaji", "shop": "Street Treat", "price": 150,
         "map": "https://www.google.com/maps?q=Pav+Bhaji+Laxmi+Nagar"}
    ],

    "Preet Vihar": [
        {"food": "Golgappa", "shop": "Prince Chaat", "price": 70,
         "map": "https://www.google.com/maps?q=Prince+Chaat+Preet+Vihar"},
        {"food": "Pav Bhaji", "shop": "Anand Pav Bhaji", "price": 160,
         "map": "https://www.google.com/maps?q=Pav+Bhaji+Preet+Vihar"},
        {"food": "Kulfi", "shop": "Kulfi King", "price": 80,
         "map": "https://www.google.com/maps?q=Kulfi+Preet+Vihar"}
    ],

    "Mayur Vihar": [
        {"food": "Momos", "shop": "Yash Momos", "price": 120,
         "map": "https://www.google.com/maps?q=Yash+Momos+Mayur+Vihar"},
        {"food": "Chaat Papdi", "shop": "Local Chaat Point", "price": 100,
         "map": "https://www.google.com/maps?q=Chaat+Mayur+Vihar"},
        {"food": "Dosa", "shop": "South Indian Cafe", "price": 180,
         "map": "https://www.google.com/maps?q=Dosa+Mayur+Vihar"}
    ],

    "Paharganj": [
        {"food": "Thali", "shop": "Krishna Roof Top", "price": 200,
         "map": "https://www.google.com/maps?q=Krishna+Roof+Top+Paharganj"},
        {"food": "Paratha", "shop": "Local Dhaba", "price": 100,
         "map": "https://www.google.com/maps?q=Paratha+Paharganj"},
        {"food": "Chai", "shop": "Tea Stall", "price": 30,
         "map": "https://www.google.com/maps?q=Tea+Paharganj"}
    ],

    "Malviya Nagar": [
        {"food": "Momos", "shop": "Tibetan Hut", "price": 140,
         "map": "https://www.google.com/maps?q=Tibetan+Hut+Malviya+Nagar"},
        {"food": "Rolls", "shop": "Roll Express", "price": 150,
         "map": "https://www.google.com/maps?q=Rolls+Malviya+Nagar"},
        {"food": "Burger", "shop": "Burger Point", "price": 180,
         "map": "https://www.google.com/maps?q=Burger+Malviya+Nagar"}
    ]
}


# ---------------- SIDEBAR ---------------- #
st.sidebar.markdown("<div class='sidebar-title'>🔍 Find Street Food</div>", unsafe_allow_html=True)
location = st.sidebar.selectbox("📍 Area", sorted(food_data.keys()))
budget = st.sidebar.slider("💰 Budget (₹)", 50, 300, 180)
time = st.sidebar.selectbox("⏰ Time", ["Morning", "Afternoon", "Evening"])
st.sidebar.info("🍟 Tip: Street food tastes best in the evening")

# ---------------- ACTION BUTTON ----------------
show = st.button("🍽️ Show Recommendations")

# ---------------- RESULTS ----------------
if show:
    st.subheader(f"🔥 Best Street Food in {location}")

    found = False
    for item in food_data[location]:
        if item["price"] <= budget:
            found = True
            st.markdown(f"""
            <div class="food-card">
                <div class="food-name">🍽 {item['food']}</div>
                <div class="shop-name">🏪 {item['shop']}</div>
                <div class="price">💰 ₹{item['price']}</div>
                <div class="map">📍 
                    <a href="{item['map']}" target="_blank">
                        Open in Google Maps
                    </a>
                </div>
            </div>
            """, unsafe_allow_html=True)

    if not found:
        st.warning("No items found within your budget. Try increasing it.")

    if time != "Evening":
        st.info("ℹ️ Food stalls are most active in the evening.")

# ---------------- FOOTER ----------------
st.write("")
st.caption("© 2025 Delhi Eats • Built with Streamlit & Kiro")