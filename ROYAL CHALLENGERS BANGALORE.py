import seaborn as sns
import  matplotlib.pyplot as plt
from streamlit import columns
import streamlit as st
from PIL import Image
import pandas as pd

st.markdown("<h2 style='color:red ;'>ROYAL CHALLENGERS BANGALORE</h2>", unsafe_allow_html=True)

img9 =Image.open("C:/Users/Nadish/Downloads/RCB.jpg").resize((300,300))
st.image(img9, caption="ROYAL CHALLENGERS BANGALORE")
st.write("RCB is one of the most popular IPL franchises, known for its massive fan base and star-studded lineups. Despite reaching the finals three times (2009, 2011, 2016), they are yet to win an IPL trophy.Founded: 2008Owner: United Spirits (a subsidiary of Diageo)Home Ground: M. Chinnaswamy Stadium, BengaluruCaptain (2024): Faf du PlessisCoach: Andy FlowerTeam Colors: Red and Black")

st.title("CAPTAIN")
img=Image.open("C:/Users/Nadish/Downloads/rpt.png").resize((300, 300))
st.image(img, caption="Rajat Patidar")
st.write("Rajat Patidar is a talented Indian top-order batsman who plays for Royal Challengers Bengaluru (RCB) in the IPL. He made headlines during IPL 2022 when he scored a magnificent unbeaten 112 off 54 balls in the Eliminator match against Lucknow Super Giants (LSG) — becoming the first uncapped player to score a century in IPL playoffs.Full Name: Rajat Manohar PatidarBorn: June 1, 1993 (Madhya Pradesh, India)Batting Style: Right-hand batRole: Top-order BatsmanIPL Team: Royal Challengers Bengaluru (2021–present)Famous For: 112* in IPL 2022 playoffs vs LSGStrengths: Calm temperament, elegant strokeplay, plays spin and pace well")
st.title("MEMORABLE PLAYERS LIST")
rcb_players = pd.DataFrame({
    "Player": [
        "Virat Kohli", "AB de Villiers", "Chris Gayle",
        "Anil Kumble", "Faf du Plessis", "Yuzvendra Chahal",
        "Glenn Maxwell", "Devdutt Padikkal", "Dale Steyn"
    ],
    "Role": [
        "Captain & Batsman", "Batsman", "Batsman",
        "Bowler & Mentor", "Captain & Batsman", "Bowler",
        "All-rounder", "Batsman", "Bowler"
    ],
    "Memorable Highlights": [
        "Most runs in IPL history; led RCB 2013–2021",
        "Iconic finisher; consistent match-winner",
        "Fastest IPL century (30 balls); explosive opener",
        "Led team to 2009 final; respected leader",
        "Current captain; steady top-order batsman",
        "RCB’s highest wicket-taker (2014–2021)",
        "Explosive all-rounder; vital in middle overs",
        "Emerging Player 2020; solid opener",
        "Legendary pacer; key spells for RCB"
    ]
})
st.dataframe(rcb_players)
st.title("ALL RECORDS OF RCB")

rcb_records = pd.DataFrame({
    "Record": [
        "IPL Titles Won",
        "Finals Appearances",
        "Most Matches as Captain",
        "Most Runs (All-time)",
        "Highest Individual Score",
        "Most Wickets (All-time)",
        "Best Bowling Figures",
        "Highest Team Total",
        "Lowest Team Total",
        "Most Sixes for RCB",
        "Most Fifties for RCB",
        "Most Hundreds for RCB"
    ],
    "Player/Team": [
        "RCB",
        "RCB",
        "Virat Kohli",
        "Virat Kohli",
        "Chris Gayle – 175*",
        "Yuzvendra Chahal",
        "Anil Kumble – 5/5 (2009)",
        "263/5 vs Pune Warriors (2013)",
        "49 vs KKR (2017)",
        "Chris Gayle",
        "Virat Kohli",
        "Virat Kohli – 7 hundreds"
    ],
    "Value": [
        0,              
        3,               
        "140+",            
        "7500+",           
        "175*",          
        139,             
        "5/5",           
        "263/5",         
        "49",            
        "240+",            
        "45+",            
        7                
    ]
})
st.dataframe(rcb_players)
