# from flask import Flask, jsonify
# import pandas as pd

# app = Flask(__name__)

# # -------------------------------
# # Load Dataset
# # -------------------------------
# df = pd.read_csv("student_cleaned.csv")   # apna dataset path yahan do

# # Agar total_score column nahi hai to create karo
# if "total_score" not in df.columns:
#     df["total_score"] = df[["math_score","reading_score","writing_score","science_score"]].sum(axis=1)

# # Pass/Fail column add karo (example: >=40 in each subject = Pass)
# if "pass_fail" not in df.columns:
#     df["pass_fail"] = df.apply(lambda row: "Pass" if (
#         row["math_score"]>=40 and 
#         row["reading_score"]>=40 and 
#         row["writing_score"]>=40 and 
#         row["science_score"]>=40) else "Fail", axis=1)

# # -------------------------------
# # Routes
# # -------------------------------

# @app.route('/')
# def home():
#     return "✅ Backend is running! Use /get_data or /get_kpis endpoints."

# @app.route('/get_data')
# def get_data():
#     return jsonify(df.to_dict(orient="records"))

# @app.route('/get_kpis')
# def get_kpis():
#     avg_score = round(df["total_score"].mean(), 2)
#     pass_rate = round((df["pass_fail"].value_counts(normalize=True).get("Pass", 0) * 100), 2)
#     top_score = df["total_score"].max()
#     return jsonify({
#         "average_score": avg_score,
#         "pass_rate": pass_rate,
#         "top_score": top_score
#     })

# # -------------------------------
# # Run Server
# # -------------------------------
# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=5000, debug=True)


from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# -------------------------------
# Load Dataset
# -------------------------------
df = pd.read_csv("student_cleaned.csv")   # apna dataset path yahan do

# -------------------------------
# ✅ DATA CLEANING (ONLY ADDED PART)
# -------------------------------

# Gender → Only Male/Female
if "gender" in df.columns:
    df["gender"] = df["gender"].astype(str).str.strip().str.lower().replace({
        "male": "Male",
        "boy": "Male",
        "female": "Female",
        "girl": "Female"
    })
    df = df[df["gender"].isin(["Male", "Female"])]

# Lunch → Clean format
if "lunch" in df.columns:
    df["lunch"] = df["lunch"].astype(str).str.strip().str.lower().replace({
        "standard": "Standard",
        "free/reduced": "Free/Reduced",
        "0": "Free/Reduced",
        "1": "Standard",
        "0.0": "Free/Reduced",
        "1.0": "Standard"
    })

# Test preparation → Clean format
if "test_preparation_course" in df.columns:
    df["test_preparation_course"] = df["test_preparation_course"].astype(str).str.strip().str.lower().replace({
        "completed": "Complete",
        "complete": "Complete",
        "none": "Not Complete",
        "not completed": "Not Complete",
        "0": "Not Complete",
        "1": "Complete",
        "0.0": "Not Complete",
        "1.0": "Complete"
    })

# -------------------------------
# Agar total_score column nahi hai to create karo
# -------------------------------
if "total_score" not in df.columns:
    df["total_score"] = df[["math_score","reading_score","writing_score","science_score"]].sum(axis=1)

# -------------------------------
# Pass/Fail column add karo
# -------------------------------
if "pass_fail" not in df.columns:
    df["pass_fail"] = df.apply(lambda row: "Pass" if (
        row["math_score"]>=40 and 
        row["reading_score"]>=40 and 
        row["writing_score"]>=40 and 
        row["science_score"]>=40) else "Fail", axis=1)

# -------------------------------
# Routes
# -------------------------------

@app.route('/')
def home():
    return "✅ Backend is running! Use /get_data or /get_kpis endpoints."

@app.route('/get_data')
def get_data():
    return jsonify(df.to_dict(orient="records"))

@app.route('/get_kpis')
def get_kpis():
    avg_score = round(df["total_score"].mean(), 2)
    pass_rate = round((df["pass_fail"].value_counts(normalize=True).get("Pass", 0) * 100), 2)
    top_score = df["total_score"].max()
    return jsonify({
        "average_score": avg_score,
        "pass_rate": pass_rate,
        "top_score": top_score
    })

# -------------------------------
# Run Server
# -------------------------------
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)