import pandas as pd
import  streamlit as st
from PIL import Image
import seaborn as sns
import  matplotlib.pyplot as plt
from streamlit import columns

st.markdown("<h2 style='color: purple;'>KOLKATA KNIGHT RIDERS</h2>", unsafe_allow_html=True)

img9 =Image.open("C:/Users/Nadish/Downloads/kkr.jpg").resize((300,300))
st.image(img9, caption="KOLKATA KNIGHT RIDERS")

st.write("Kolkata Knight Riders (KKR) is a popular franchise cricket team in the Indian Premier League (IPL), based in Kolkata, West Bengal. The team is known for its strong fan base and stylish branding.Founded: 2008Owners: Red Chillies Entertainment (Shah Rukh Khan), Juhi Chawla, Jay MehtaHome Ground: Eden Gardens, Kolkatacaptain (2024): Shreyas IyerCoach: Chandrakant PanditIPL Titles: 🏆 2-time champions (2012, 2014)Team Colors: Purple and Gold")
st.title("CAPTAIN")

img=Image.open("C:/Users/Nadish/Downloads/ar.jpg").resize((300, 300))
st.image(img, caption="Ajinkya Rahane")

st.write("Ajinkya Rahane is an experienced Indian cricketer known for his calm temperament, solid technique, and dependability in the middle order.Born: June 6, 1988 (Maharashtra, India)Batting Style: Right-handedRole: BatsmanTeams: India, Chennai Super Kings (CSK), formerly RR, DC, and KKR,India Debut: 2011 (ODI), 2013 (Test)")


df=pd.DataFrame({
    "TITLE HOLD YEAR":[2012, 2014,2024]

})
plt.style.use("dark_background")
fig, ax=plt.subplots()
plt.plot(df["TITLE HOLD YEAR"],marker="o")
st.pyplot(fig)

st.title("MEMORABLE PLAYERS LIST")
kkr_players = pd.DataFrame({
    "Player": [
        "Gautam Gambhir", "Andre Russell", "Sunil Narine",
        "Yusuf Pathan", "Dinesh Karthik", "Shubman Gill",
        "Brendon McCullum", "Nitish Rana", "Robin Uthappa"
    ],
    "Role": [
        "Batsman (Captain)", "All-rounder", "All-rounder (Spinner)",
        "All-rounder", "Wicketkeeper-Batsman", "Batsman",
        "Batsman", "Batsman", "Wicketkeeper-Batsman"
    ],
    "Memorable Highlights": [
        "Led KKR to 2 IPL titles (2012, 2014)",
        "Explosive match-winner with bat and ball",
        "Mysterious spinner, key in KKR's success",
        "Big hitter, turned games single-handedly",
        "Reliable finisher and former captain",
        "Top run-scorer during rebuilding years",
        "Scored 158* in IPL’s first-ever match",
        "Consistent top-order batter",
        "Orange Cap winner in 2014 title win"
    ]
})
st.dataframe(kkr_players)

st.title("ALL RECORDS OF KKR")

kkr_records = pd.DataFrame({
    "Record": [
        "IPL Titles Won",
        "Final Appearances",
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
        "Most Hundreds",
        "Most Matches Played"
    ],
    "Player/Team": [
        "KKR",
        "KKR",
        "Champions (2012, 2014)",
        "Gautam Gambhir",
        "Gautam Gambhir",
        "Brendon McCullum – 158* (2008)",
        "Sunil Narine",
        "Sunil Narine – 5/19 (2012)",
        "245/6 vs Punjab (2018)",
        "67 all out vs Mumbai Indians (2008)",
        "Andre Russell",
        "Gautam Gambhir",
        "Brendon McCullum – 1",
        "Sunil Narine"
    ],
    "Value": [
        2,          
        4,         
        "1st Place",
        122,       
        3035,       
        158,         
        "170+",      
        "5/19",    
        "245/6",    
        "67",      
        "190+",       
        "30+",        
        1,           
        "160+"      
    ]
})
st.dataframe(kkr_records)