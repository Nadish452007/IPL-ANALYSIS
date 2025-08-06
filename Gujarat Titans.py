import pandas as pd
import  streamlit as st
from PIL import Image
import seaborn as sns
import  matplotlib.pyplot as plt
from streamlit import columns

st.markdown("<h2 style='color:lavender;'>Gujarat Titans</h2>", unsafe_allow_html=True)

img9 =Image.open("C:/Users/Nadish/Downloads/gt.jpg").resize((300,300))
st.image(img9, caption="Gujarat Titans ")

st.write("Gujarat Titans (GT) is a professional cricket team based in Ahmedabad, Gujarat, that plays in the Indian Premier League (IPL). The franchise was introduced in 2022 and is owned by CVC Capital Partners.Home ground: Narendra Modi Stadium, AhmedabadCaptain (2024): Shubman Gill (earlier Hardik Pandya in 2022–2023)Coach: Ashish NehraIPL Titles: 🏆 Champions in 2022 (debut season)Team Colors: Dark blue and gold")
st.title("CAPTAIN")
img=Image.open("C:/Users/Nadish/Downloads/sh.jpg").resize((300, 300))
st.image(img, caption="Shubman Gill ")

st.write(
     "Shubman Gill is a young and talented Indian cricketer known for his elegant batting style and strongtemperament.Born: September1999(Punjab,IndiaBatting Style: RighthandedRole: Top-order Batsmanteams: India, Gujarat Titans (IPL), Punjab (domestic)IPL Captain: Appointed captain of Gujarat Titans in 2024Debut for India: 2019 (ODI), 2020 (Test), 2023 ")

st.title("MEMORABLE PLAYERS LIST")

gt_players = pd.DataFrame({
    "Player": [
        "Hardik Pandya", "Shubman Gill", "Rashid Khan",
        "Mohammed Shami", "David Miller", "Sai Sudharsan",
        "Rahul Tewatia", "Wriddhiman Saha", "Vijay Shankar"
    ],
    "Role": [
        "All-rounder", "Batsman", "Bowler",
        "Bowler", "Batsman", "Batsman",
        "All-rounder", "Wicketkeeper-Batsman", "All-rounder"
    ],
    "Memorable Highlights": [
        "Captain & MVP in IPL 2022",
        "Orange Cap in IPL 2023",
        "Consistent wicket-taker & match-winner",
        "Purple Cap in IPL 2023",
        "Key finisher in 2022",
        "94 in IPL 2023 Final",
        "Finishing matches under pressure",
        "Reliable opener",
        "Key middle-order contributions"
    ]
})
st.dataframe(gt_players)
