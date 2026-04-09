import pandas as pd
import numpy as np
from scipy import stats

def clean_data():
    # Load dataset
    df = pd.read_csv("Student_performance_10k.csv")

    # Convert numeric columns
    numeric_cols = ['math_score','reading_score','writing_score','science_score','total_score']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Fill missing numeric values with mean
    for col in numeric_cols:
        if df[col].isnull().sum() > 0:
            df[col] = df[col].fillna(df[col].mean())

    # Fill missing categorical values with "Unknown"
    cat_cols = ['gender','race_ethnicity','parental_level_of_education','lunch','test_preparation_course']
    for col in cat_cols:
        df[col] = df[col].fillna("Unknown")

    # Recalculate total_score
    df['total_score'] = df[['math_score','reading_score','writing_score','science_score']].sum(axis=1)

    # Outlier handling (Z-score method)
    df = df[(np.abs(stats.zscore(df[numeric_cols])) < 3).all(axis=1)]

    # Feature engineering
    df['percentage'] = df['total_score'] / 400 * 100
    df['pass_fail'] = df['percentage'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')

    # Assign grade
    def grade(x):
        if x >= 350:
            return 'A'
        elif x >= 300:
            return 'B'
        elif x >= 250:
            return 'C'
        else:
            return 'D'
    df['grade'] = df['total_score'].apply(grade)

    return df
 