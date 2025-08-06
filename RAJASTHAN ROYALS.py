import seaborn as sns
import  matplotlib.pyplot as plt
from streamlit import columns
import streamlit as st
from PIL import Image
import pandas as pd

st.markdown("<h2 style='color:pink ;'>RAJASTHAN ROYALS</h2>", unsafe_allow_html=True)

img9 =Image.open("C:/Users/Nadish/Downloads/rr.png").resize((300,300))
st.image(img9, caption="RAJASTHAN ROYALS")

st.write("Rajasthan Royals (RR) is a Jaipur-based IPL franchise known for winning the inaugural IPL title in 2008 under Shane Warne’s captaincy.Founded: 2008Owner: Royals Sports GroupHome Ground: Sawai Mansingh Stadium, JaipurCaptain (2024): Sanju SamsonCoach: Kumar Sangakkara (Director of Cricket)IPL Titles: 🏆 1 (2008)Team Colors: Pink and Blue")
st.title("CAPTAIN")
img=Image.open("C:/Users/Nadish/Downloads/ss.png").resize((300, 300))
st.image(img, caption="Sanju Samson")

st.title("MEMORABLE PLAYERS LIST")

rr_players = pd.DataFrame({
    "Player": [
        "Shane Warne", "Sanju Samson", "Jos Buttler",
        "Shane Watson", "Rahul Dravid", "Yashasvi Jaiswal",
        "Sohail Tanvir", "Ajinkya Rahane", "Ravindra Jadeja"
    ],
    "Role": [
        "Captain & Bowler", "Captain & Batsman", "Batsman",
        "All-rounder", "Mentor & Batsman", "Batsman",
        "Bowler", "Batsman", "All-rounder"
    ],
    "Memorable Highlights": [
        "Led RR to 2008 title; legendary spinner & mentor",
        "Consistent run-scorer; current captain",
        "Orange Cap winner (2022); explosive opener",
        "Star performer in 2008; key all-rounder for years",
        "Stabilized team as mentor and captain post-2011",
        "Young talent; scored fastest IPL 50 by uncapped Indian",
        "Purple Cap (2008); deadly swing bowler",
        "Key top-order batsman for many seasons",
        "Discovered by RR in 2008; evolved into world-class all-rounder"
    ]
})
st.dataframe(rr_players)



st.title("ALL RECORDS OF RR")

rr_records = pd.DataFrame({
    "Record": [
        "IPL Titles Won",
        "Playoff Appearances",
        "Most Matches as Captain",
        "Most Runs (All-time)",
        "Highest Individual Score",
        "Most Wickets (All-time)",
        "Best Bowling Figures",
        "Highest Team Total",
        "Lowest Team Total",
        "Most Sixes for RR",
        "Most Fifties for RR",
        "Most Hundreds for RR"
    ],
    "Player/Team": [
        "RR",
        "RR",
        "Shane Warne / Sanju Samson",
        "Sanju Samson",
        "Jos Buttler – 124",
        "Siddharth Trivedi",
        "Sohail Tanvir – 6/14 (2008)",
        "226/6 vs PBKS (2020)",
        "58 vs RCB (2009)",
        "Sanju Samson",
        "Sanju Samson",
        "Jos Buttler – 5 hundreds"
    ],
    "Value": [
        1,
        5,
        "55+ (each)",
        "3888+",
        "124",
        65,
        "6/14",
        "226/6",
        "58",
        "190+",
        "20+",
        5
    ]
})
st.dataframe(rr_records)

