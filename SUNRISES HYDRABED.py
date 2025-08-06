import seaborn as sns
import  matplotlib.pyplot as plt
from streamlit import columns
import streamlit as st
from PIL import Image
import pandas as pd

st.markdown("<h2 style='color:orange ;'>SUNRISES HYDRABED</h2>", unsafe_allow_html=True)

img9 =Image.open("C:/Users/Nadish/Downloads/srh.png").resize((300,300))
st.image(img9, caption="SUNRISES HYDRABED")
st.write("Sunrisers Hyderabad (SRH) is a franchise cricket team based in Hyderabad, playing in the Indian Premier League (IPL).Founded: 2012 (replacing Deccan Chargers)Owner: SUN GroupHome Ground: Rajiv Gandhi International Stadium, HyderabadTeam Colors: Orange and BlackCaptain (2024): Pat CumminsCoach: Daniel VettoriIPL Title: 🏆 2016 Champions (under David Warner)")

st.title("CAPTAIN")
img=Image.open("C:/Users/Nadish/Downloads/pc.jpg").resize((300, 300))
st.image(img, caption="Pat Cummins")
st.write("Pat Cummins is an Australian fast bowler and the captain of Sunrisers Hyderabad (SRH) in IPL 2024. Known for his pace, accuracy, and leadership, Cummins is one of the world’s top bowlers and a proven performer in all formats.Full Name: Patrick James CumminsBorn: May 8, 1993 (New South Wales, Australia)Role: Right-arm fast bowler, Lower-order batsmanIPL Team: Sunrisers Hyderabad (2024), previously KKR and DCCaptain of SRH: 2024 seasonIPL 2024: Led SRH to the finals with smart tactics and calm leadershipFamous For: Winning the 2023 WTC and 2023 ODI World Cup as Australia’s captain")
st.title("MEMORABLE PLAYERS LIST")
srh_memorable_players = pd.DataFrame({
    "Player Name": [
        "David Warner",
        "Kane Williamson",
        "Bhuvneshwar Kumar",
        "Rashid Khan",
        "Shikhar Dhawan",
        "Jonny Bairstow",
        "Pat Cummins",
        "T. Natarajan",
        "Abhishek Sharma",
        "Heinrich Klaasen"
    ],
    "Notable Contributions": [
        "SRH captain & 2016 title winner, 3x Orange Cap winner",
        "Calm leader, key contributor in batting & captaincy (2018 Finalist)",
        "Top wicket-taker for SRH, reliable swing bowler",
        "Match-winner with his economical leg-spin (2017–2021)",
        "Consistent run-scorer in early SRH years",
        "Explosive opener, iconic partnerships with Warner",
        "Led SRH to 2024 Final as captain",
        "Death-over specialist, impactful in 2020–2022",
        "Emerging all-rounder, consistent IPL 2023–2024",
        "Power-hitter, standout performer in IPL 2023–2024"
    ]
})
st.dataframe(srh_memorable_players)

st.title("ALL RECORDS OF SRH")

srh_records = pd.DataFrame({
    "Record Type": [
        "Most Runs",
        "Most Wickets",
        "Highest Individual Score",
        "Best Bowling Figures",
        "Highest Team Total",
        "Lowest Team Total",
        "Most Catches",
        "Most Sixes",
        "Most Matches Played",
        "Highest Partnership",
        "Best Season Finish",
        "IPL Title Win"
    ],
    "Record Holder / Details": [
        "David Warner – 4014 runs",
        "Bhuvneshwar Kumar – 142 wickets",
        "Jonny Bairstow – 114 vs RCB (2019)",
        "Bhuvneshwar Kumar – 5/19 vs KXIP (2017)",
        "231/2 vs RCB (2019)",
        "96 all out vs MI (2019)",
        "David Warner – 47 catches",
        "David Warner – 143 sixes",
        "Bhuvneshwar Kumar – 121 matches",
        "Bairstow & Warner – 185 runs vs RCB (2019)",
        "Champions in 2016, Runners-up in 2018 & 2024",
        "Won in 2016 (under David Warner)"
    ]
})
st.dataframe(srh_records)