from student_clean import clean_data
from EDA_visual import run_visuals

# Step 1: Clean data
df = clean_data()

# Step 2: Run visualizations
run_visuals(df)

# Step 3: Print summary
print(df.head())
print(df.info())

# Step 4: Save cleaned dataset (optional)
df.to_csv("Student_cleaned.csv", index=False)