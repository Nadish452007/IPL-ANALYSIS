from tkinter import Image
from PIL import Image
import streamlit as st
from streamlit import columns
import pandas as pd


st.markdown("<h2 style='color:darkblue;'>DELHI CAPTICALS</h2>", unsafe_allow_html=True)

img=Image.open("C:/Users/Nadish/Downloads/dc.png").resize((300,300))
st.image(img,caption="DELHI CAPTICALS")
st.write("Delhi Capitals (DC) is a franchise cricket team based in Delhi that plays in the Indian Premier League (IPL). The team was originally known as Delhi Daredevils before being renamed to Delhi Capitals in 2019. The franchise is jointly owned by the JSW Group and GMR Group.")
st.title("CAPTAIN")

img=Image.open("C:/Users/Nadish/Downloads/ap.jpg").resize((300, 300))
st.image(img, caption="Axar Patel ")

st.write("Axar Patel (full name: Akshar Rajeshbhai Patel) is an Indian international cricketer known for his left-arm orthodox spin bowling and handy batting in the lower order""Born: January 20, 1994, in Gujarat, India","Role: Bowling all-rounder""Batting style: Left-handed""Bowling style: Left-arm orthodox spin""IPL Team: Delhi Capitals""India Debut: 2014 (ODI)")

st.title("MEMORABLE PLAYERS LIST")
data = {
    'Player': ['Rishabh Pant', 'Shikhar Dhawan', 'David Warner', 'Amit Mishra', 'Kagiso Rabada',
               'Prithvi Shaw', 'Axar Patel', 'Virender Sehwag', 'AB de Villiers', 'Andre Russell'],
    'Role': ['Wicketkeeper-Batsman', 'Batsman', 'Batsman', 'Bowler', 'Bowler',
             'Batsman', 'All-rounder', 'Batsman', 'Batsman', 'All-rounder'],
    'Matches': [98, 68, 30, 99, 50, 71, 65, 86, 27, 7],

}

df = pd.DataFrame(data)

st.dataframe(df)


st.title("ALL RECORDS OF DC")

data=pd.DataFrame( {
    'Record': [
        'Most Matches as Captain',
        'Most Runs',
        'Highest Individual Score',
        'Most Wickets',
        'Best Bowling Figures',
        'Highest Team Total',
        'Lowest Team Total',
        'Most Catches',
        'Most Sixes',
        'Most Fifties',
        'Most Hundreds',
        'Most Matches Played'
    ],
    'Player/Team': [
        'Rishabh Pant',
        'Rishabh Pant',
        'Rishabh Pant - 128*',
        'Amit Mishra',
        'Kagiso Rabada - 4/21',
        'Delhi Capitals - 231/4 vs KKR (2020)',
        'Delhi Capitals - 66 all out vs MI (2017)',
        'Shreyas Iyer',
        'Rishabh Pant',
        'Shikhar Dhawan',
        'Shikhar Dhawan - 2',
        'Amit Mishra'
    ],
    'Value': [
        58,
        2844,
        128,
        106,
        '4/21',
        '231/4',
        '66 all out',
        35,
        110,
        20,
        2,
        99
    ]
})

dc_records_df = pd.DataFrame(data)
st.dataframe(dc_records_df)
