import pandas as pd
import  streamlit as st
from PIL import Image
import seaborn as sns
import  matplotlib.pyplot as plt
from streamlit import columns

st.markdown("<h2 style='color:skyblue ;'>Lucknow Super Giants</h2>", unsafe_allow_html=True)

img9 =Image.open("C:/Users/Nadish/Downloads/lsg.png").resize((300,300))
st.image(img9, caption="Lucknow Super Giants")

st.write("Lucknow Super Giants (LSG) is a professional IPL franchise based in Lucknow, Uttar Pradesh. The team made its debut in the IPL 2022 season.Owner: RPSG Group (also owned Rising Pune Supergiant earlier)Home Ground: Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, LucknowCaptain (2024): KL RahulCoach: Justin Langer (earlier Andy Flower)Best Performance: Reached playoffs in both 2022 & 2023Team Colors: Sky Blue and Orange")
st.title("CAPTAIN")
img=Image.open("C:/Users/Nadish/Downloads/rp.jpg").resize((300, 300))
st.image(img, caption="Rishabh Pant")
st.write("Rishabh Pant is a dynamic Indian cricketer known for his aggressive batting and wicketkeeping skills.Born: October 4, 1997 (Uttarakhand, India)Role: Wicketkeeper-BatsmanBatting Style: Left-handedTeams: India, Delhi Capitals (IPL – Captain)India Debut: 2017 (T20I), 2018 (Test & ODI)")
st.title("MEMORABLE PLAYERS LIST")
lsg_players = pd.DataFrame({
    "Player": [
        "KL Rahul", "Quinton de Kock", "Marcus Stoinis",
        "Nicholas Pooran", "Ravi Bishnoi", "Mohsin Khan",
        "Krunal Pandya", "Avesh Khan", "Deepak Hooda"
    ],
    "Role": [
        "Captain & Batsman", "Wicketkeeper-Batsman", "All-rounder",
        "Wicketkeeper-Batsman", "Bowler", "Bowler",
        "All-rounder", "Bowler", "All-rounder"
    ],
    "Memorable Highlights": [
        "Multiple IPL centuries & team leader since 2022",
        "140* vs KKR in 2022 — one of the highest IPL scores",
        "Hard-hitting finisher, key in multiple chases",
        "Explosive lower-order batter in 2023–24",
        "Consistent wicket-taker with leg-spin",
        "Defended 10 runs in final over vs MI (2022)",
        "Steady all-rounder & occasional captain",
        "Pace spearhead in 2022",
        "Reliable middle-order contributions"
    ]
})
st.dataframe(lsg_players)

st.title("ALL RECORDS OF LSG")

lsg_records = pd.DataFrame({
    "Record": [
        "IPL Titles Won",
        "Playoff Appearances",
        "Best Season Finish",
        "Most Matches as Captain",
        "Most Runs",
        "Highest Individual Score",
        "Most Wickets",
        "Best Bowling Figures",
        "Highest Team Total",
        "Lowest Team Total",
        "Most Sixes",
        "Most Fifties",
        "Most Hundreds"
    ],
    "Player/Team": [
        "LSG",
        "LSG",
        "4th Place (2022, 2023)",
        "KL Rahul",
        "KL Rahul",
        "Quinton de Kock – 140* (2022)",
        "Ravi Bishnoi",
        "Avesh Khan – 4/24 (2022)",
        "213/9 vs RCB (2023)",
        "108 vs RCB (2023)",
        "Nicholas Pooran",
        "KL Rahul",
        "KL Rahul – 2"
    ],
    "Value": [
        0,
        2,
        "4th Place",
        24,
        1130,
        140,
       "30+",
        "4/24",
        "213/9",
        "108",
        "40+",
        "10+",
        2
    ]
})
st.dataframe(lsg_records)

