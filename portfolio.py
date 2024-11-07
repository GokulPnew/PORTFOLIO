import streamlit as st
import random

st.title("Student Portfolio")
page = st.sidebar.radio("Go to", ["Home", "About Me", "Skills", "Projects", "Contact"])

if page == "Home":
    st.header("Welcome to my portfolio")
    st.write("I am a college student pursuing a degree in Engineering."
             " This is my personal portfolio for showcasing my skills, projects, and contact information.")
elif page == "About Me":
    st.header("About Me")
    st.write("Hello! I am Gokul, currently pursuing my undergraduate degree in Artificial Engineering & Data Science.")
elif page == "Skills":
    st.header("Skills")
    st.write("Here are some of my skills:")
    st.write("Programming languages: Python")
elif page == "Projects":
    st.header("Guessing Game")
    st.write("DO YOU WANT TO PLAY MY GUESSING GAME?")
    if 'target_number' not in st.session_state:
            st.session_state.target_number = random.randint(1, 10)
            st.session_state.new=False
            st.session_state.gameover=False

    
    if st.button("Yes"):
        st.title("Number Guessing Game")
        st.write("Guess a number between 1 to 10")
        st.session_state.new=True
    if  st.session_state.new:
            st.session_state.guess = st.number_input("Enter Your Guess", min_value=1, max_value=10, step=1)
            if st.button("Submit Guess"):
                    if st.session_state.guess == st.session_state.target_number:
                        st.success(f"Congratulations! You guessed the right number. The number was {st.session_state.target_number}.")
                        st.session_state.gameover=True
                        
                    else:
                        st.warning("Oops! Wrong guess. Try again.")
            if st.button("RESET"):
                st.session_state.target_number = random.randint(1, 10)
                st.write("New number generated. Try guessing again!")
                st.session_state.gameover=False
            
elif  page == "Contact":
            st.header("Contact")
            st.write("Mobile No: 6374198723")
            st.write("Email: appu20082006@gmail.com")
