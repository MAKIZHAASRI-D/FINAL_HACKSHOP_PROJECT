import streamlit as st
from streamlit_option_menu import option_menu
from  streamlit_lottie import st_lottie
import requests
import random
from streamlit.components.v1 import html

def game():
    if st.button("Check"):
        st.session_state.attempted += 1
        if guessing_number ==  st.session_state.random_number:
            st.write(f"the number that should be guessed is { st.session_state.random_number}")
            st.success("You have won!")
        else:
            remaining_attempts = no_of_attempts - st.session_state.attempted
            if remaining_attempts > 0:
                if guessing_number>st.session_state.random_number:
                    st.warning(f"Wrong guess! You have {remaining_attempts} attempts left.")
                    st.write("your guess is too high!")
                if guessing_number<st.session_state.random_number:
                    st.warning(f"Wrong guess! You have {remaining_attempts} attempts left.")
                    st.write("your guess is too low!")
            else:
                st.error(f"You've used all your attempts! The correct number was {st.session_state.random_number}.")
                st.session_state.attempted = 0
                st.write("Game over! Please refresh to play again.")

st.title("GUESSING GAME")
st.write("---")

with st.container():
    selected=option_menu(
        menu_title=None,
        options=['INTIUITION ZONE(USER GUESSING)','CYBERNECTIC REIGN(COMPUTER GUESSING)'],
        icons=['code-slash','person'],
        orientation='horizontal',
    )


if selected=="INTIUITION ZONE(USER GUESSING)":
    with st.container():
        selected=option_menu(
        menu_title=None,
        options=['instructions','user details','game'],
        icons=['code-slash','person','game'],
        orientation='horizontal',
    )
    if selected=="instructions":
        with st.container():
            col1,col2=st.columns(2)
            with col1:
                st.header(""" INSTRUCTIONS""")
                st.write("##")
                st.subheader("""to be continued""")
            with col2:
                def load_lottieurl(url):
                    r = requests.get(url)
                    if r.status_code != 200:
                        return None
                    return r.content
                lottie_brain=load_lottieurl("https://lottie.host/9f06bd72-c811-4056-8f2a-a20f12213bb4/wTE3OoVPJE.lottie")
    

    if selected=="user details":
        with st.container():
            col1,col2=st.columns(2)
            with col1:
                st.header("USER DETAILS")
                name=st.text_input("YOUR NAME:",key="name")
                email=st.text_input("YOUR EMAIL:",key="email")  
                submit_button=st.button("submit")
                if submit_button:
                    if not name and not email:
                        st.error("INVALID NAME OR EMAIL")
                    else:
                        st.success(f"YOU ARE LOGGED IN SUCCESSFULLY")
                        
            with col2:
                
                def load_lottieurl(url:str):
                    r=requests.get(url)
                    if r.status_code !=200:
                        return None
                    return r.json
                lottie_brain=load_lottieurl("https://lottie.host/2d617fa0-bee0-4843-87cb-03952fa706e1/gMncSEUZB6.json")
    
    
    if selected=="game":
        st.title("INTUITION ZONE GAME" )
        st.write("##")
        st.header("THE ACTUAL GAME BEGINS HERE........")
        
        with st.container():
                    st.write("RANGE SETUP")
                    st.write("##")
                    min_range = st.number_input("Enter the minimum range:", key="min_range", step=1)
                    max_range = st.number_input("Enter the maximum range:", key="max_range", step=1)
                    if min_range >= max_range:
                        st.error("Minimum range must be less than maximum range.")
                    else:
                        if 'random_number' not in st.session_state:
                            st.session_state.random_number = random.randint(min_range, max_range)




                    st.write("---")
                    st.write("LIVES")
                    st.write("##")
                    no_of_attempts = st.number_input("Enter the number of attempts you want:", step=1,value=0)
            
            
                    st.write("---")
                    st.write("GUESS THE NUMBER")
                    st.write("##")
                    if 'attempted' not in st.session_state:
                        st.session_state.attempted = 0
                    if st.session_state.attempted < no_of_attempts:
                        guessing_number = st.number_input(f"Enter your guess between {min_range} and {max_range}:", key="guess_input", value=0)
                        if guessing_number<=max_range and guessing_number>=min_range:
                            game()
                    else:
                            st.warning(f"enter the number which is within the range {min_range} and {max_range}") 

           



if selected=="CYBERNECTIC REIGN(COMPUTER GUESSING)":
    with st.container():
        selected=option_menu(
        menu_title=None,
        options=['instructions','user details','game'],
        icons=['code-slash','person','game'],
        orientation='horizontal',
    )
    if selected=="instructions":
        with st.container():
            col1,col2=st.columns(2)
            with col1:
                st.header(""" INSTRUCTIONS""")
                st.write("##")
                st.subheader("""to be continued""")
            with col2:
                def load_lottieurl(url:str):
                    r=requests.get(url)
                    if r.status_code !=200:
                        return None
                    return r.json
                lottie_brain=load_lottieurl("https://lottie.host/embed/71ea6e35-e13c-4827-8e90-b8c1d17c49fc/OAelvNDW5s.json")
    

    if selected=="user details":
        with st.container():
            col1,col2=st.columns(2)
            with col1:
                st.header("USER DETAILS")
                name=st.text_input("YOUR NAME:",key="name2")
                email=st.text_input("YOUR EMAIL:",key="email2")  

                submit_button=st.button("submit")
                if submit_button:
                    if not name and email:
                        st.error("INVALID NAME OR EMAIL")
                    else:
                        st.success(f"YOU ARE LOGGED IN SUCCESSFULLY")
                        
            with col2:
                
                def load_lottieurl(url:str):
                    r=requests.get(url)
                    if r.status_code !=200:
                        return None
                    return r.json
                lottie_brain=load_lottieurl("https://lottie.host/embed/b7a72d78-162a-4ee2-ab17-f47cc368eab7/ZbFXr6cuPR.json")
    
    
    if selected=="game":
        st.title("CYBERNETIC REIGN GAME" )
        st.write("##")
        st.header("THE ACTUAL GAME BEGINS HERE........")
        st.write("#")
        with st.container():
                    min_range = st.number_input("Enter the minimum number:",step=1, value=1)
                    max_range = st.number_input("Enter the maximum number:",step=1, value=100)
                    max_attempts = st.number_input("Enter the maximum attempts:", step=1, value=5)
                    COMPUTER_GAME = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Binary Search Game</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 20px;
        }}
        .button{{
            padding: 10px 20px;
            font-size: 16px;
            margin: 5px;
            cursor: pointer;
            border: none;
            background-color:blue;
            color: white;
            border-radius: 5px;
        }}
        
        .button:hover {{
            background-color:red;}}
        .disabled {{
            background-color:black;
            cursor: not-allowed;
        }}
    </style>
</head>
<body>

    <div id="guessing-area">
        <p>My guess is: <span id="guess">N/A</span></p>
        <p>Attempts used: <span id="attempt_used">0</span></p>
        <span id="result"></span>
        <span id="new_game"></span>
    </div>

      
    <div id="buttons">
        <button id="button1" class="button" onclick="tooLow()" >Too Low</button>
        <button id="button2" class="button" onclick="correctGuess()">Correct</button>
        <button id="button3" class="button" onclick="tooHigh()">Too High</button>
    </div>
    <script>
       let minRange = {min_range};
        let maxRange = {max_range};
        let attempts = 1;
        const maxAttempts = {max_attempts};
        let guess = Math.floor((minRange + maxRange) / 2);

        function updateDisplay() {{
            document.getElementById('guess').innerText = guess;
            document.getElementById('attempt_used').innerText = attempts;
        }}

        function disableButtons() {{
            document.getElementById('button1').disabled = true;
            document.getElementById('button2').disabled = true;
            document.getElementById('button3').disabled = true;
            document.getElementById('button1').classList.add("disabled");
            document.getElementById('button2').classList.add("disabled");
            document.getElementById('button3').classList.add("disabled");
        }}

        function tooLow() {{
            if (attempts >= maxAttempts) {{
                document.getElementById('result').innerText = "Game Over! You've used all your attempts.";
                document.getElementById('new_game').innerText ='PLEASE REFRESH TO CONTINUE PLAYING';
                disableButton();
                return;
            }}
            minRange = guess + 1;
            guess = Math.floor((minRange + maxRange) / 2);
            attempts++;
            updateDisplay();
            checkGameOver();
        }}

        function tooHigh() {{
            if (attempts >=maxAttempts) {{
                document.getElementById('result').innerText = "Game Over! You've used all your attempts.";
                document.getElementById('new_game').innerText ='PLEASE REFRESH TO CONTINUE PLAYING';
                disableButtons();
                return;
            }}
            maxRange = guess - 1;
            guess = Math.floor((minRange + maxRange) / 2);
            attempts++;
            updateDisplay();
            checkGameOver();
        }}

         function correctGuess() {{
            document.getElementById('result').innerText = 'I won! I guessed your number!';
            document.getElementById('new_game').innerText ='GAME OVER !PLEASE REFRESH TO CONTINUE PLAYING';
            disableButtons();
           }}

           updateDisplay();
        
    </script>
</body></html>"""

                    if st.button("Start Game"):
                        html(COMPUTER_GAME,height=1000)
