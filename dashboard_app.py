# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import requests

# # -------------------------------
# # Page Config
# # -------------------------------
# st.set_page_config(
#     page_title="Student Marks Analysis",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # -------------------------------
# # Custom Styling (Dark Theme + Hover Fix)
# # -------------------------------
# page_style = """
# <style>
# body {
#     background-color: #1e272e;   /* Dark navy background */
#     color: #ecf0f1;
#     margin: 0;
#     padding: 0;
# }
# h1 {
#     color: #f39c12;   /* Golden yellow */
#     text-align: center;
#     font-size: 42px;
#     font-weight: bold;
#     margin-bottom: 25px;   /* Gap below heading */
# }
# h2, h3 {
#     color: #00cec9;   /* Cyan */
#     margin-top: 20px; /* Gap above headings */
#     margin-bottom: 15px;
# }
# div[data-testid="stSidebar"] {
#     background-color: #2f3640;   /* Slightly lighter sidebar */
#     color: #dcdde1;
#     padding: 15px;
# }
# div[data-testid="stSidebar"] h2 {
#     color: #e84393;   /* Pink filter heading */
# }
# div[data-testid="stMarkdownContainer"] div {
#     margin-bottom: 20px; /* Gap between KPI cards and visuals */
# }
# div[data-testid="stMarkdownContainer"] div:hover {
#     box-shadow: 0 0 15px #f1c40f;
#     transform: scale(1.02);
# }
# </style>
# """
# st.markdown(page_style, unsafe_allow_html=True)

# st.markdown("<h1>📊 Student Marks Analysis Dashboard</h1>", unsafe_allow_html=True)

# # -------------------------------
# # Load Data (Backend or Local)
# # -------------------------------
# try:
#     data = requests.get("http://127.0.0.1:5000/get_data").json()
#     df = pd.DataFrame(data)
#     kpi_data = requests.get("http://127.0.0.1:5000/get_kpis").json()
#     avg_score = kpi_data["average_score"]
#     pass_rate = kpi_data["pass_rate"]
#     top_score = kpi_data["top_score"]
# except Exception:
#     df = pd.read_csv("student_cleaned.csv")
#     avg_score = round(df["total_score"].mean(), 2)
#     pass_rate = round((df["pass_fail"].value_counts(normalize=True).get("Pass", 0) * 100), 2)
#     top_score = df["total_score"].max()

# # -------------------------------
# # Sidebar Filters
# # -------------------------------
# st.sidebar.markdown("<h2>🎨 Filters</h2>", unsafe_allow_html=True)

# st.sidebar.markdown("### 👩 Demographics")
# gender_filter = st.sidebar.multiselect("Select Gender", ["All"] + list(df['gender'].unique()))
# race_filter = st.sidebar.multiselect("Race/Ethnicity", ["All"] + list(df['race_ethnicity'].unique()))

# st.sidebar.markdown("### 🎓 Academic")
# education_filter = st.sidebar.multiselect("Parental Education", ["All"] + list(df['parental_level_of_education'].unique()))
# grade_filter = st.sidebar.multiselect("Grade", ["All"] + list(df['grade'].unique()))

# st.sidebar.markdown("### 🍽️ Support")
# lunch_filter = st.sidebar.multiselect("Lunch Type", ["All"] + list(df['lunch'].unique()))
# prep_filter = st.sidebar.multiselect("Test Prep Course", ["All"] + list(df['test_preparation_course'].unique()))

# # Apply filters
# filtered_df = df.copy()
# if "All" not in gender_filter and gender_filter:
#     filtered_df = filtered_df[filtered_df['gender'].isin(gender_filter)]
# if "All" not in race_filter and race_filter:
#     filtered_df = filtered_df[filtered_df['race_ethnicity'].isin(race_filter)]
# if "All" not in education_filter and education_filter:
#     filtered_df = filtered_df[filtered_df['parental_level_of_education'].isin(education_filter)]
# if "All" not in lunch_filter and lunch_filter:
#     filtered_df = filtered_df[filtered_df['lunch'].isin(lunch_filter)]
# if "All" not in prep_filter and prep_filter:
#     filtered_df = filtered_df[filtered_df['test_preparation_course'].isin(prep_filter)]
# if "All" not in grade_filter and grade_filter:
#     filtered_df = filtered_df[filtered_df['grade'].isin(grade_filter)]

# # -------------------------------
# # KPI Section
# # -------------------------------
# st.markdown("## 🌟 Key Performance Indicators")

# col1, col2, col3 = st.columns(3)
# col1.markdown(f"<div style='background-color:#27ae60;padding:20px;border-radius:10px;text-align:center;'><h3>📊 Average Score</h3><h2>{avg_score}</h2></div>", unsafe_allow_html=True)
# col2.markdown(f"<div style='background-color:#2980b9;padding:20px;border-radius:10px;text-align:center;'><h3>✅ Pass Rate (%)</h3><h2>{pass_rate}</h2></div>", unsafe_allow_html=True)
# col3.markdown(f"<div style='background-color:#8e44ad;padding:20px;border-radius:10px;text-align:center;'><h3>🏆 Top Score</h3><h2>{top_score}</h2></div>", unsafe_allow_html=True)

# # -------------------------------
# # Visualizations (2-column layout)
# # -------------------------------

# col1, col2 = st.columns(2)

# with col1:
#     st.markdown("### 🎯 Distribution of Total Scores")
#     fig, ax = plt.subplots()
#     sns.histplot(filtered_df['total_score'], bins=20, kde=True, ax=ax, color="#e74c3c")
#     avg = filtered_df['total_score'].mean()
#     ax.axvline(avg, color='yellow', linestyle='--', label=f'Average: {avg:.2f}')
#     ax.legend()
#     st.pyplot(fig)

# with col2:
#     st.markdown("### 📚 Subject-wise Average Scores")
#     fig, ax = plt.subplots()
#     subject_means = filtered_df[['math_score','reading_score','writing_score','science_score']].mean()
#     sns.barplot(x=subject_means.index, y=subject_means.values, ax=ax, palette="Set2")
#     st.pyplot(fig)

# col3, col4 = st.columns(2)

# with col3:
#     st.markdown("### 👩‍🎓 Gender-wise Total Score")
#     fig, ax = plt.subplots()
#     sns.barplot(x="gender", y="total_score", data=filtered_df, ax=ax, palette="muted")
#     st.pyplot(fig)

# with col4:
#     st.markdown("### 🎓 Impact of Parental Education")
#     fig, ax = plt.subplots()
#     sns.barplot(x="parental_level_of_education", y="total_score", data=filtered_df, ax=ax, palette="Set2")
#     plt.xticks(rotation=45)
#     st.pyplot(fig)

# col5, col6 = st.columns(2)

# with col5:
#     st.markdown("### 🍽️ Lunch Type vs Total Score")
#     fig, ax = plt.subplots()
#     sns.boxplot(x="lunch", y="total_score", data=filtered_df, ax=ax, palette="coolwarm")
#     st.pyplot(fig)

# with col6:
#     st.markdown("### 📖 Test Prep Course Impact")
#     fig, ax = plt.subplots()
#     sns.barplot(x="test_preparation_course", y="total_score", data=filtered_df, ax=ax, palette="Blues")
#     st.pyplot(fig)

# st.markdown("### 🏅 Grade Distribution")
# fig, ax = plt.subplots()
# sns.countplot(x="grade", data=filtered_df, ax=ax, palette="viridis")
# st.pyplot(fig)

# # -------------------------------
# # Extra Visuals
# # -------------------------------
# st.markdown("### 🔥 Correlation Heatmap")
# fig, ax = plt.subplots()
# sns.heatmap(filtered_df[['math_score','reading_score','writing_score','science_score']].corr(),
#             annot=True, cmap="coolwarm", ax=ax)
# st.pyplot(fig)

# # -------------------------------
# # Data Table + Download
# # -------------------------------
# st.markdown("## 📑 Sample Data")
# st.dataframe(filtered_df.head(20))

# st.markdown("### 📥 Download Filtered Data")
# csv = filtered_df.to_csv(index=False).encode('utf-8')
# st.download_button("Download CSV", csv, "filtered_data.csv", "text/csv")


import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Student Marks Analysis",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------
# Custom Styling (Dark Theme + Hover Fix)
# -------------------------------
page_style = """
<style>
body {
    background-color: #1e272e;
    color: #ecf0f1;
    margin: 0;
    padding: 0;
}
h1 {
    color: #f39c12;
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 25px;
}
h2, h3 {
    color: #00cec9;
    margin-top: 20px;
    margin-bottom: 15px;
}
div[data-testid="stSidebar"] {
    background-color: #2f3640;
    color: #dcdde1;
    padding: 15px;
}
div[data-testid="stSidebar"] h2 {
    color: #e84393;
}
div[data-testid="stMarkdownContainer"] div {
    margin-bottom: 20px;
}
div[data-testid="stMarkdownContainer"] div:hover {
    box-shadow: 0 0 15px #f1c40f;
    transform: scale(1.02);
}
</style>
"""
st.markdown(page_style, unsafe_allow_html=True)

st.markdown("<h1>📊 Student Marks Analysis Dashboard</h1>", unsafe_allow_html=True)

# -------------------------------
# Load Data
# -------------------------------
try:
    data = requests.get("http://127.0.0.1:5000/get_data").json()
    df = pd.DataFrame(data)
    kpi_data = requests.get("http://127.0.0.1:5000/get_kpis").json()
    avg_score = kpi_data["average_score"]
    pass_rate = kpi_data["pass_rate"]
    top_score = kpi_data["top_score"]
except Exception:
    df = pd.read_csv("student_cleaned.csv")
    avg_score = round(df["total_score"].mean(), 2)
    pass_rate = round((df["pass_fail"].value_counts(normalize=True).get("Pass", 0) * 100), 2)
    top_score = df["total_score"].max()

# -------------------------------
# 🔥 ONLY CHANGE: DATA TRANSFORMATION
# -------------------------------

# Gender → Male/Female (already ok but standardize)
df["gender"] = df["gender"].replace({
    "male": "Male",
    "female": "Female",
    "M": "Male",
    "F": "Female"
})

# Race/Ethnicity → A B C D E groups
df["race_ethnicity"] = df["race_ethnicity"].replace({
    "group A": "A",
    "group B": "B",
    "group C": "C",
    "group D": "D",
    "group E": "E"
})

# Lunch mapping
df["lunch"] = df["lunch"].replace({
    1.0: "Standard",
    0.0: "Free/Reduced",
    "standard": "Standard",
    "free/reduced": "Free/Reduced",
    "unknown": "Other",
    "unkown": "Other"
})

# Test preparation mapping
df["test_preparation_course"] = df["test_preparation_course"].replace({
    1.0: "Complete",
    0.0: "Not Complete",
    "unknown": "None",
    "unkwnone": "None",
    "none": "None"
})

# -------------------------------
# Sidebar Filters
# -------------------------------
st.sidebar.markdown("<h2>🎨 Filters</h2>", unsafe_allow_html=True)

st.sidebar.markdown("### 👩 Demographics")
gender_filter = st.sidebar.multiselect("Select Gender", ["All"] + list(df['gender'].unique()))
race_filter = st.sidebar.multiselect("Race/Ethnicity", ["All"] + list(df['race_ethnicity'].unique()))

st.sidebar.markdown("### 🎓 Academic")
education_filter = st.sidebar.multiselect("Parental Education", ["All"] + list(df['parental_level_of_education'].unique()))
grade_filter = st.sidebar.multiselect("Grade", ["All"] + list(df['grade'].unique()))

st.sidebar.markdown("### 🍽️ Support")
lunch_filter = st.sidebar.multiselect("Lunch Type", ["All"] + list(df['lunch'].unique()))
prep_filter = st.sidebar.multiselect("Test Prep Course", ["All"] + list(df['test_preparation_course'].unique()))

# Apply filters
filtered_df = df.copy()

if "All" not in gender_filter and gender_filter:
    filtered_df = filtered_df[filtered_df['gender'].isin(gender_filter)]

if "All" not in race_filter and race_filter:
    filtered_df = filtered_df[filtered_df['race_ethnicity'].isin(race_filter)]

if "All" not in education_filter and education_filter:
    filtered_df = filtered_df[filtered_df['parental_level_of_education'].isin(education_filter)]

if "All" not in lunch_filter and lunch_filter:
    filtered_df = filtered_df[filtered_df['lunch'].isin(lunch_filter)]

if "All" not in prep_filter and prep_filter:
    filtered_df = filtered_df[filtered_df['test_preparation_course'].isin(prep_filter)]

if "All" not in grade_filter and grade_filter:
    filtered_df = filtered_df[filtered_df['grade'].isin(grade_filter)]

# -------------------------------
# KPI Section
# -------------------------------
st.markdown("## 🌟 Key Performance Indicators")

col1, col2, col3 = st.columns(3)
col1.markdown(f"<div style='background-color:#27ae60;padding:20px;border-radius:10px;text-align:center;'><h3>📊 Average Score</h3><h2>{avg_score}</h2></div>", unsafe_allow_html=True)
col2.markdown(f"<div style='background-color:#2980b9;padding:20px;border-radius:10px;text-align:center;'><h3>✅ Pass Rate (%)</h3><h2>{pass_rate}</h2></div>", unsafe_allow_html=True)
col3.markdown(f"<div style='background-color:#8e44ad;padding:20px;border-radius:10px;text-align:center;'><h3>🏆 Top Score</h3><h2>{top_score}</h2></div>", unsafe_allow_html=True)

# -------------------------------
# Visualizations (UNCHANGED)
# -------------------------------

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🎯 Distribution of Total Scores")
    fig, ax = plt.subplots()
    sns.histplot(filtered_df['total_score'], bins=20, kde=True, ax=ax, color="#e74c3c")
    avg = filtered_df['total_score'].mean()
    ax.axvline(avg, color='yellow', linestyle='--', label=f'Average: {avg:.2f}')
    ax.legend()
    st.pyplot(fig)

with col2:
    st.markdown("### 📚 Subject-wise Average Scores")
    fig, ax = plt.subplots()
    subject_means = filtered_df[['math_score','reading_score','writing_score','science_score']].mean()
    sns.barplot(x=subject_means.index, y=subject_means.values, ax=ax, palette="Set2")
    st.pyplot(fig)

col3, col4 = st.columns(2)

with col3:
    st.markdown("### 👩‍🎓 Gender-wise Total Score")
    fig, ax = plt.subplots()
    sns.barplot(x="gender", y="total_score", data=filtered_df, ax=ax, palette="muted")
    st.pyplot(fig)

with col4:
    st.markdown("### 🎓 Impact of Parental Education")
    fig, ax = plt.subplots()
    sns.barplot(x="parental_level_of_education", y="total_score", data=filtered_df, ax=ax, palette="Set2")
    plt.xticks(rotation=45)
    st.pyplot(fig)

col5, col6 = st.columns(2)

with col5:
    st.markdown("### 🍽️ Lunch Type vs Total Score")
    fig, ax = plt.subplots()
    sns.boxplot(x="lunch", y="total_score", data=filtered_df, ax=ax, palette="coolwarm")
    st.pyplot(fig)

with col6:
    st.markdown("### 📖 Test Prep Course Impact")
    fig, ax = plt.subplots()
    sns.barplot(x="test_preparation_course", y="total_score", data=filtered_df, ax=ax, palette="Blues")
    st.pyplot(fig)

st.markdown("### 🏅 Grade Distribution")
fig, ax = plt.subplots()
sns.countplot(x="grade", data=filtered_df, ax=ax, palette="viridis")
st.pyplot(fig)

# -------------------------------
# Correlation Heatmap
# -------------------------------
st.markdown("### 🔥 Correlation Heatmap")
fig, ax = plt.subplots()
sns.heatmap(filtered_df[['math_score','reading_score','writing_score','science_score']].corr(),
            annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# -------------------------------
# Data Table + Download
# -------------------------------
st.markdown("## 📑 Sample Data")
st.dataframe(filtered_df.head(20))

st.markdown("### 📥 Download Filtered Data")
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button("Download CSV", csv, "filtered_data.csv", "text/csv")



