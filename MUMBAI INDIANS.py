import pandas as pd
import  streamlit as st
from PIL import Image
import seaborn as sns
import  matplotlib.pyplot as plt
from streamlit import columns

st.markdown("<h2 style='color:blue ;'>MUMBAI INDIANS</h2>", unsafe_allow_html=True)

img9 =Image.open("C:/Users/Nadish/Downloads/mi.png").resize((300,300))
st.image(img9, caption="MUMBAI INDIANS")

st.write("Mumbai Indians (MI) is the most successful franchise in the history of the Indian Premier League (IPL).Founded: 2008Owner: Reliance Industries (via Indiawin Sports)Home Ground: Wankhede Stadium, MumbaiCaptain (2024): Hardik Pandya (after Rohit Sharma)Coach: Mark BoucherIPL Titles: 🏆 5-time champions (2013, 2015, 2017, 2019, 2020)Team Colors: Blue and Gold")
st.title("CAPTAIN")
img=Image.open("C:/Users/Nadish/Downloads/hp.jpg").resize((300, 300))
st.image(img, caption="Hardik Pandya")
df=pd.DataFrame({
    "TITLE HOLD YEAR":[2013, 2015, 2017, 2019, 2020]

})
plt.style.use("dark_background")
fig, ax=plt.subplots()
plt.plot(df["TITLE HOLD YEAR"],marker="o")
st.pyplot(fig)

st.title("MEMORABLE PLAYERS LIST")

mi_players = pd.DataFrame({
    "Player": [
        "Rohit Sharma", "Sachin Tendulkar", "Lasith Malinga",
        "Kieron Pollard", "Jasprit Bumrah", "Hardik Pandya",
        "Suryakumar Yadav", "Ambati Rayudu", "Harbhajan Singh"
    ],
    "Role": [
        "Captain & Batsman", "Batsman", "Bowler",
        "All-rounder", "Bowler", "All-rounder",
        "Batsman", "Batsman", "Bowler"
    ],
    "Memorable Highlights": [
        "Led MI to 5 IPL titles (most by any captain)",
        "First MI icon, key batsman from 2008–2013",
        "Highest IPL wicket-taker for years (170+)",
        "Match-winner with bat & ball for over a decade",
        "Spearhead of MI bowling attack, death overs king",
        "Explosive all-rounder, key in 4 title wins",
        "Consistent top-order performer since 2020",
        "Reliable middle-order batter in early years",
        "Spin wizard, played major role in early IPL success"
    ]
})
st.dataframe(mi_players)
st.title("ALL RECORDS OF MI")

mi_records = pd.DataFrame({
    "Record": [
        "IPL Titles Won",
        "Playoff Appearances",
        "Most Matches as Captain",
        "Most Wins by a Team",
        "Most Runs (All-time)",
        "Highest Individual Score",
        "Most Wickets (All-time)",
        "Best Bowling Figures",
        "Highest Team Total",
        "Lowest Team Total",
        "Most Sixes for MI",
        "Most Fifties for MI",
        "Most Hundreds for MI"
    ],
    "Player/Team": [
        "MI",
        "MI",
        "Rohit Sharma",
        "MI",
        "Rohit Sharma",
        "Suryakumar Yadav – 103*",
        "Lasith Malinga",
        "Alzarri Joseph – 6/12 (2019)",
        "235/9 vs SRH (2021)",
        "87 vs SRH (2018)",
        "Kieron Pollard",
        "Rohit Sharma",
        "Sanath Jayasuriya, Suryakumar, Rohit"
    ],
    "Value": [
        5,
        10,
        158,
        "140+",
        "103*",
        170,
        "6/12",
        "235/9",
        "87",
        223,
        "40+",
        "1 each"
    ]
})
st.dataframe(mi_records)
