

import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
st.markdown("<h1 style='text-align:center;'>IPL ANALYSIS</h1>",unsafe_allow_html=True)
data = {
    'Team': [
        'Mumbai Indians', 'Chennai Super Kings', 'Kolkata Knight Riders',
        'Sunrisers Hyderabad', 'Rajasthan Royals', 'Gujarat Titans',
        'Royal Challengers Bangalore', 'Delhi Capitals', 'Punjab Kings'
    ],
    'Titles Won': [5, 5, 2, 1, 1, 1, 1, 0, 0],
    'Runners Up': [1, 5, 1, 1, 1, 1, 3, 1, 1],
    'Debut Year': [2008, 2008, 2008, 2013, 2008, 2008, 2008, 2008, 2022]
}

df = pd.DataFrame(data)

st.dataframe(df)

st.header("TEMS")


col1, col2, col3 = st.columns(3)


img1 = Image.open("C:/Users/Nadish/Downloads/csk.jpg").resize((300, 200))
img2 = Image.open("C:/Users/Nadish/Downloads/mi.jpg").resize((300, 200))
img3 = Image.open("C:/Users/Nadish/Downloads/RCB.jpg").resize((300, 200))


with col1:
    st.image(img1, caption="CHENNAI SUPER KINGS")
with col2:
    st.image(img2, caption="MUMBAI INDIANS")
with col3:
    st.image(img3, caption="ROYAL CHALLENGERS BANGALORE")


col4, col5, col6= st.columns(3)

img4 =Image.open("C:/Users/Nadish/Downloads/kkr.jpg").resize((300,200))
img5 =Image.open("C:/Users/Nadish/Downloads/dc.png").resize((300,200))
img6 =Image.open("C:/Users/Nadish/Downloads/srh.png").resize((300,200))

with col4:
    st.image(img4,caption="KOLKATA KNIGHT RIDERS")
with col5:
    st.image(img5,caption="DELHI CAPTICALS")
with col6:
    st.image(img6,caption="SUNRISES HYDRABED")

col7, col8, col9= st.columns(3)

img7 =Image.open("C:/Users/Nadish/Downloads/rr.png").resize((300,200))
img8 =Image.open("C:/Users/Nadish/Downloads/lsg.png").resize((300,200))
img9 =Image.open("C:/Users/Nadish/Downloads/gt.jpg").resize((300,200))

with col7:
    st.image(img7,caption="RAJASTHAN ROYALS")

with col8:
    st.image(img8, caption="Lucknow Super Giants ")
with col9:
    st.image(img9, caption="Gujarat Titans ")

st.markdown("<h1 style='text-align:center;'>IPL Teams vs Titles Won</h1>",unsafe_allow_html=True)


df= pd.DataFrame({
    "TOTAL CUP WIN": [5, 5, 1, 3, 1]
})
labels = ["CSK", "MI", "RCB", "KKR", "RR"]
values = df["TOTAL CUP WIN"]
colors=["yellow","blue","red","purple","pink"]

def absolute_value(val):
    total = sum(values)
    count = int(round(val * total / 100))
    return f"{count} "

plt.style.use("dark_background")
fig, ax = plt.subplots()
ax.pie(values, labels=labels,colors=colors, autopct=absolute_value,)
ax.set_title("Total IPL Titles by Team")
st.pyplot(fig)

st.subheader("TOP BATSMAN")


data1 = {
    "Player": [
        "Virat Kohli", "Shikhar Dhawan", "David Warner", "Rohit Sharma",
        "Suresh Raina", "MS Dhoni", "AB de Villiers", "Chris Gayle",
        "Robin Uthappa", "KL Rahul"
    ],
    "Matches": [252, 222, 176, 243, 205, 264, 184, 142, 205, 118],
    "Innings": [244, 218, 176, 238, 200, 226, 170, 141, 197, 114],
    "Runs": [7924, 6769, 6568, 6628, 5528, 5243, 5162, 4965, 4952, 4211],
    "Average": [38.66, 35.18, 41.56, 30.15, 32.52, 39.13, 39.70, 39.72, 27.51, 46.78],
    "Strike Rate": [131.9, 127.1, 139.9, 131.1, 136.7, 135.0, 151.7, 148.9, 130.4, 135.0],
    "100s": [7, 2, 4, 1, 1, 0, 3, 6, 0, 4],
    "50s": [55, 50, 63, 42, 39, 24, 40, 31, 27, 33],
    "Highest Score": [113, 106,126, 109, 100, 84, 133, 175, 87, 132]
}

df_batsmen = pd.DataFrame(data1)
st.dataframe(df_batsmen)



st.subheader("TOP WICKET TAKER")
data2 = {
    "Player": [
        "Yuzvendra Chahal", "Dwayne Bravo", "Piyush Chawla", "Bhuvneshwar Kumar", "Amit Mishra",
        "Ravichandran Ashwin", "Sunil Narine", "Lasith Malinga", "Rashid Khan", "Harbhajan Singh"
    ],
    "Matches": [145, 161, 181, 160, 161, 197, 162, 122, 109, 163],
    "Wickets": [198, 183, 179, 174, 173, 172, 163, 170, 139, 150],
    "Average": [21.49, 23.82, 26.55, 26.44, 23.87, 28.28, 25.78, 19.80, 21.27, 26.86],
    "Economy": [7.67, 8.38, 7.94, 7.43, 7.35, 6.99, 6.73, 7.14, 6.87, 7.07],
    "Strike Rate": [16.80, 17.04, 20.06, 21.34, 19.46, 24.25, 22.96, 16.63, 18.57, 22.79],
    "Best Bowling": ["5/40", "4/22", "4/17", "5/19", "5/17", "4/34", "5/19", "5/13", "4/24", "5/18"],
    "Team(s)": [
        "RR, RCB", "CSK, RCB, MI", "MI, KKR, PBKS", "SRH, PWI", "DC, SRH",
        "CSK, DC, RR, KXIP", "KKR", "MI", "SRH, GT", "MI, CSK, KKR"
    ]
}

df_wickets = pd.DataFrame(data2)
st.dataframe(df_wickets)


st.subheader("TOP SIXERS")
sixer_data = {
    "Player": [
        "Chris Gayle", "Rohit Sharma", "AB de Villiers", "MS Dhoni",
        "Virat Kohli", "Kieron Pollard", "David Warner",
        "Suresh Raina", "Andre Russell", "Shane Watson"
    ],
    "Sixes": [357, 280, 251, 245, 246, 223, 226, 203, 193, 190]
}

df_sixers = pd.DataFrame(sixer_data)
st.dataframe(df_sixers)
plt.style.use('dark_background')
fig, ax = plt.subplots()
sns.barplot(y="Player",x="Sixes",data=df_sixers,ax=ax)
st.pyplot(fig)
st.subheader("TOP FOURS")
top_fours_data = {
        "Player": ["Shikhar Dhawan","Virat Kohli","David Warner","Rohit Sharma","Suresh Raina","Gautam Gambhir","Robin Uthappa","Ajinkya Rahane", "KL Rahul","AB de Villiers"],
        "Fours":[768, 714, 651, 554, 506, 491, 481, 471, 420, 413]
 }

df_fours = pd.DataFrame(top_fours_data)
st.dataframe(df_fours)
plt.style.use('dark_background')
fig2, ax2 = plt.subplots()
sns.barplot(x="Fours",y="Player",data=df_fours,ax=ax2)
st.pyplot(fig2)