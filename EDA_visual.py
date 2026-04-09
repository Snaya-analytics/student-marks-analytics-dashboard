import seaborn as sns
import matplotlib.pyplot as plt

def run_visuals(df):
    # Histogram
    plt.figure(figsize=(8,5))
    sns.histplot(df['total_score'], bins=20, kde=True, color='blue')
    plt.title("Distribution of Total Scores")
    plt.show()

    # Heatmap
    plt.figure(figsize=(8,6))
    sns.heatmap(df[['math_score','reading_score','writing_score','science_score','total_score']].corr(), annot=True, cmap='Blues')
    plt.title("Correlation Between Subjects")
    plt.show()

    # Gender-wise average
    plt.figure(figsize=(8,5))
    sns.barplot(x='gender', y='total_score', data=df, palette='Set2')
    plt.title("Average Total Score by Gender")
    plt.show()

    # Grade distribution
    plt.figure(figsize=(8,5))
    sns.countplot(x='grade', data=df, palette='coolwarm')
    plt.title("Grade Distribution")
    plt.show()

    # Parental education vs average score
    plt.figure(figsize=(10,6))
    sns.barplot(x='parental_level_of_education', y='total_score', data=df, palette='muted')
    plt.title("Average Score by Parental Education")
    plt.xticks(rotation=45)
    plt.show()

    # Lunch type vs performance
    plt.figure(figsize=(8,5))
    sns.boxplot(x='lunch', y='total_score', data=df, palette='pastel')
    plt.title("Lunch Type vs Total Score")
    plt.show()

    # Test-prep impact
    plt.figure(figsize=(8,5))
    sns.barplot(x='test_preparation_course', y='total_score', data=df, palette='Set1')
    plt.title("Impact of Test Preparation Course")
    plt.show()