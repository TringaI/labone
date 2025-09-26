import streamlit as st
import random

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

/* your other CSS here */
</style>
""", unsafe_allow_html=True)


st.markdown("<h1>Web Development Lab01</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)  

st.markdown("<h2>CS 1301</h2>", unsafe_allow_html=True)
st.markdown("<h3>Web Development - Section A</h3>", unsafe_allow_html=True)
st.markdown("<h3>Tringa Ibrahimi</h3>", unsafe_allow_html=True)

st.markdown("<p>Welcome to my Streamlit Web Development Lab01 app!<br>"
            "You can navigate between the pages using the sidebar to the left.<br>"
            "The following pages are:</p>", unsafe_allow_html=True)

st.markdown("""
<p>1. <b>Portfolio Page</b>: This page showcases my portfolio, including projects and experience.<br>
2. <b>PhaseII</b>: This page contains a mini quiz for Kosovo.</p>
""", unsafe_allow_html=True)



st.markdown("<p>After you explore my project come and play a quick game!</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)  

st.markdown("<h2> Guess the Number Game</h2>", unsafe_allow_html=True)
st.markdown("<p>Try to guess the number I'm thinking of between 1 and 20!</p>", unsafe_allow_html=True)

if "number_to_guess" not in st.session_state:
    st.session_state.number_to_guess = random.randint(1, 20)
    st.session_state.guess_result = ""
    st.session_state.attempts = 0

user_guess = st.number_input("Your guess:", min_value=1, max_value=20, step=1)

if st.button("Submit Guess"):
    st.session_state.attempts += 1
    if user_guess < st.session_state.number_to_guess:
        st.session_state.guess_result = "Too low! Try a higher number."
    elif user_guess > st.session_state.number_to_guess:
        st.session_state.guess_result = "Too high! Try a lower number."
    else:
        st.session_state.guess_result = f"Correct! You guessed it in {st.session_state.attempts} attempts."
        st.session_state.number_to_guess = random.randint(1, 20)  
        st.session_state.attempts = 0

st.markdown(f"<p>{st.session_state.guess_result}</p>", unsafe_allow_html=True)
