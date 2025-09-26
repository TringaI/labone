import streamlit as st
from PIL import Image
import base64
from io import BytesIO

st.set_page_config(page_title="Kosovo Knowledge Quiz")

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap" rel="stylesheet">

<style>
html, body, [class*="css"], .stText, .stMarkdown, h1, h2, h3, p {
    font-family: 'Montserrat', sans-serif !important;
}
h1 { font-size: 32px !important; font-weight: normal !important; }
h2 { font-size: 28px !important; font-weight: normal !important; }
h3 { font-size: 24px !important; font-weight: normal !important; }
p  { font-size: 18px !important; font-weight: normal !important; margin:0; padding:0; }

/* Radio buttons */
div.stRadio > div[role='radiogroup'] > label > div:first-child {
    background-color: #fff;
    border: 2px solid purple;
    border-radius: 50%;
    width: 18px;
    height: 18px;
    display: inline-block;
    position: relative;
    margin-right: 8px;
}
div.stRadio > div[role='radiogroup'] > label > div:first-child:after {
    content: "";
    position: absolute;
    top: 3px;
    left: 3px;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background-color: purple;
    display: none;
}
div.stRadio > div[role='radiogroup'] > label[data-checked="true"] > div:first-child:after {
    display: block;
}

/* Checkbox + slider + tags */
input[type=checkbox] { accent-color: purple !important; }
div.stSlider [role='slider'] { background-color: purple !important; border: 2px solid white !important; }
div.stSlider > div[data-baseweb="slider"] > div > div > div > div { color: purple !important; font-weight: bold !important; }
div[data-baseweb="tag"] { background-color: purple !important; color: white !important; border-radius: 8px !important; }
</style>
""", unsafe_allow_html=True)


# Convert image to base64
def img_to_base64(path):
    img = Image.open(path)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Title
st.markdown("<h1>Kosovo Knowledge Quiz 🇽🇰</h1>", unsafe_allow_html=True)

# Images
img1 = img_to_base64("images/kosovo/kosovo_flag.png")
img2 = img_to_base64("images/kosovo/kosovo_mountains.avif")
img3 = img_to_base64("images/kosovo/prizren.jpg")

st.markdown(f"""
<div style="display:flex; gap:10px; margin-bottom:30px;">
    <div style="flex:1; height:200px; overflow:hidden;">
        <img src="data:image/png;base64,{img1}" style="width:100%; height:100%; object-fit:cover;">
    </div>
    <div style="flex:1; height:200px; overflow:hidden;">
        <img src="data:image/png;base64,{img2}" style="width:100%; height:100%; object-fit:cover;">
    </div>
    <div style="flex:1; height:200px; overflow:hidden;">
        <img src="data:image/png;base64,{img3}" style="width:100%; height:100%; object-fit:cover;">
    </div>
</div>
""", unsafe_allow_html=True)

# Session state
if "submitted" not in st.session_state:
    st.session_state.submitted = False
    st.session_state.score = 0

# Questions
st.markdown("<p>1. What is the capital of Kosovo?</p>", unsafe_allow_html=True)
q1 = st.radio("", ["Pristina", "Peja", "Gjakova", "Mitrovica"], index=None)

st.markdown("<p>2. Select the traditional Kosovar dishes:</p>", unsafe_allow_html=True)
q2 = st.multiselect("", ["Flija", "Pite", "Pizza", "Burger"])

st.markdown("<p>3. How many municipalities does Kosovo have?</p>", unsafe_allow_html=True)
q3 = st.number_input("", min_value=0, max_value=50, step=1)

st.markdown("<p>4. In what year did Kosovo declare independence? (2000–2020)</p>", unsafe_allow_html=True)
q4 = st.slider("", min_value=2000, max_value=2020, step=1, value=2010)

NB = int((q4 - 2000) / 20 * 100)
st.markdown(f"""
<style>
div.stSlider > div[data-baseweb="slider"] > div > div {{
    background: linear-gradient(to right, purple 0%, purple {NB}%, #d3d3d3 {NB}%, #d3d3d3 100%) !important;
}}
</style>
""", unsafe_allow_html=True)

st.markdown("<p>5. What is the primary official language of Kosovo?</p>", unsafe_allow_html=True)
q5 = st.selectbox("", ["","Albanian", "English", "Turkish", "Bosnian"])

# Scoring
if st.session_state.submitted:
    total = 5
    st.success(f"You scored {st.session_state.score}/{total}!")
    if st.session_state.score == total:
        st.balloons()
        st.write("Amazing! You’re a true Kosovo expert!")
    elif st.session_state.score >= 3:
        st.write("Good job! You know quite a bit about Kosovo.")
    else:
        st.write("Keep learning about Kosovo – you’ll ace it next time!")
    
    if st.button("Try Again"):
        st.session_state.submitted = False
        st.session_state.score = 0
        st.rerun()
else:
    if st.button("Submit Quiz"):
        score = 0
        if q1 == "Pristina":
            score += 1
        if set(q2) == set(["Flija", "Pite"]):
            score += 1
        if q3 == 38:
            score += 1
        if q4 == 2008:
            score += 1
        if q5 == "Albanian":
            score += 1
        st.session_state.score = score
        st.session_state.submitted = True
        st.rerun()
