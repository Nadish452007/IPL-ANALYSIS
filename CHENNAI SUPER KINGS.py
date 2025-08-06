from tkinter import Image
from PIL import Image

import matplotlib.pyplot as plt
import  streamlit as st
from numpy.ma.core import resize
from streamlit import columns, dataframe
import seaborn as sns
import pandas as pd



st.markdown("<h2 style='color:orange;'>CHENNAI SUPER KINGS</h2>", unsafe_allow_html=True)
st.image("C:/Users/Nadish/Downloads/csk.jpg")

st.write("Chennai Super Kings (CSK) is one of the most successful and popular teams in the Indian Premier League (IPL). Led by the legendary MS Dhoni, CSK is known for its consistency, team spirit, and loyal fan base, often called the ""Whistle Podu Army"".Founded in 2008, CSK has won the IPL title five times (2010, 2011, 2018, 2021, and 2023) and reached the playoffs in almost every season they’ve played. With a balanced squad of experienced Indian players and dynamic international stars, CSK combines calm leadership with explosive cricketing talent.")
df=pd.DataFrame({
    "TITLE HOLD YEAR":[2010, 2011, 2018, 2021, 2023]

})
plt.style.use("dark_background")
fig, ax=plt.subplots()
plt.plot(df["TITLE HOLD YEAR"],marker="o")
st.pyplot(fig)

st.title("CAPTAIN")
col4,col5=columns(2)
with col4:
    img1 = Image.open("C:/Users/Nadish/Downloads/msd.jpg").resize((300, 300))
    st.image(img1, caption="Mahendra Singh Dhoni")

with col5:
    st.write(
        "Mahendra Singh Dhoni, fondly known as 'Captain Cool', is one of India's most successful cricket captains. "
        "Known for his calm demeanor, sharp cricketing brain, and exceptional finishing skills, Dhoni led India to "
        "historic victories including the 2007 T20 World Cup, 2011 ODI World Cup, and the 2013 Champions Trophy. "
        "As the captain of Chennai Super Kings (CSK), he has guided the team to multiple IPL titles, becoming a beloved "
        "icon in Indian cricket. Beyond the stats, Dhoni is admired for his humility, leadership, and legendary legacy in world cricket. 🏆💛"
    )

st.title("MEMORABLE PLAYERS LIST")
data = {
    "Player": [
        "MS Dhoni",
        "Suresh Raina",
        "Ravindra Jadeja",
        "Dwayne Bravo",
        "Shane Watson",
        "Ruturaj Gaikwad"
    ],
    "Why Memorable": [
        "Captain Cool – led CSK to multiple IPL titles and known for calm finishing",
        "Mr. IPL – top run-scorer for CSK and consistent performer",
        "All-rounder and key finisher – crucial match-winner and strong fielder",
        "Wicket-taker and death-overs specialist – key to CSK's bowling unit",
        "Finals hero in 2018 – scored century in IPL final",
        "Young star – Orange Cap winner and future of CSK batting"
    ]
}

df = pd.DataFrame(data)
st.dataframe(df)

st.title("ALL RECORDS OF CSK")
data = {
    "CATEGORY": [
        "SEASONS PLAYED",
        "TITLES WON",
        "TOTAL MATCHES",
        "MATCHES WON",
        "MATCHES LOST",
        "WIN % (APPROX)",
        "MOST SUCCESSFUL CAPTAIN",
        "MOST RUNS (PLAYER)",
        "MOST WICKETS (PLAYER)"
    ],
    "STATISTICS": [
        15,
        5,
        225,
        131,
        91,
        "58.2%",
        "MS DHONI",
        "SURESH RAINA (~4687 RUNS)",
        "DWAYNE BRAVO (~154 WICKETS)"
    ]
}

df = pd.DataFrame(data)

st.dataframe(df)
