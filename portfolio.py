import streamlit as st
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html

st.set_page_config(page_title=None,page_icon=None,layout='centered')

with st.container():


        with st.container():
            selected=option_menu(
                menu_title=None,
                options=['ABOUT ME','MY WORK','CONTACT ME'],
                icons=['code-slash','person'],
                orientation='horizontal',
             )
            

        if selected=='ABOUT ME':
            st.title("ABOUT ME")
            about_me = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Binary Search Game</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            padding: 20px;
            line-HEIGHT:50px;
            background-color:lavender;
        }}
       
         p{{
         color:teal;
         
         }}
    </style>
</head>
<body>
<p>MY NAME IS MAKIZHAA SRI DURAIRAJU.</p>
<p> I AM CURRENTLY PURSUING A BACHELOR'S DEGREE IN COMPUTER SCIENCE AND ENGINEERING.</p>
<p>I HAVE COMPLETED A COURSE IN FULL STACK DEVELOPMENT WHICH COVERS THE BASICS .</P>
<p>I AM INTERESTED AT LEARNING NEW THINGS.</p>
<p>I CONSIDER ME AS A PERSON WHO HAS QUALITY OF LEADERSHIP AND ALSO LEVELING MY SKILLS UP.</p>
<p>APART FROM ACADEMICS ,I AM A KABADDI PLAYER AND ALSO HAVE TAKEN CLASSES FOR SILAMBAM.</p>
</body></html>"""
    
            html(about_me,height=500,width=700)
        
        if selected=="MY WORK":
            st.title("MY WORK")
            my_work= f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Binary Search Game</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            padding: 20px;
            line-HEIGHT:50px;
            background-color:lavender;
        }}
       
         p{{
         color:teal;
         
         }}
    </style>
</head>
<body>
<p>MY FIRST WORK ON PROGRAMMING  IS CONSIDERED AS A PROJECT OR ASSIGNMENT .</p>
<p> THAT WAS A QUESTION TO BUILD INTERACTIVE ,DYNAMICALLY GIVING INPUT GUESSING GAME WITH TWO DIFFERENT TYPES OF MODES</p>
<p>THE TECHNOLOGY USED HERE WAS THE COMPLETE CORE OF PYTHON STREAMLIT WITH SOME SUPPORTING HTML AND JAVASCRIPT CODE</p>


</body></html>"""
            html(my_work,height=500,width=700)
            st.write("[view my project on github](https://github.com/MAKIZHAASRI-D/FINAL_HACKSHOP_PROJECT.git)")



        if selected=="CONTACT ME":
            st.title("BE IN TOUCH")
            contact_form="""<form action="https://formsubmit.co/makiduraijmp@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false"><br><br>
            <label id="name" >enter your name:</label><br><br>
            <input type="text" name="name" placeholder="your name"  required><br><br>
            <label id="email" >enter your email:</label><br><br>
            <input type="email" name="email" placeholder="your gmail" required><br><br>
            <textarea name="message" placeholder="email me here" required></textarea><br><br>
            <button type="submit">Send</button><br><br>
            </form>"""
            html(contact_form,height=1000,width=700)