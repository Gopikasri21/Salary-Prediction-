import streamlit as st
import pickle
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Salary Prediction",
    page_icon="💼",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("Final_model_SLR.pkl", "rb"))

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    color: white;
}

.title {
    font-size: 40px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 20px;
}

.card {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
}

.salary-box {
    font-size: 28px;
    font-weight: bold;
    text-align: center;
    background: rgba(0,0,0,0.3);
    padding: 15px;
    border-radius: 10px;
    margin-top: 20px;
}

.sidebar-news {
    font-size: 14px;
    line-height: 1.8;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("📰 Latest Tech News")

news_list = [
    "AI hiring increasing in 2026 📈",
    "Python remains top skill for ML jobs 🐍",
    "Data Science salaries rising globally 💰",
    "Companies investing more in AI automation 🤖",
    "Machine Learning engineers in high demand 🚀"
]

for news in news_list:
    st.sidebar.markdown(f"- {news}")

# ---------------- MAIN PAGE ----------------
st.markdown('<div class="title">💼 Salary Prediction System</div>', unsafe_allow_html=True)

col1, col2 = st.columns([2,1])

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Predict Your Salary")

    years_experience = st.number_input(
        "Enter Years of Experience",
        min_value=0.0,
        max_value=50.0,
        step=0.5
    )

    # Expected salary input
    expected_salary = st.text_input("Enter Expected Salary (Optional)")

    if st.button("Predict Salary"):

        prediction = model.predict([[years_experience]])
        salary = float(prediction.ravel()[0])

        st.markdown(
            f'<div class="salary-box">Predicted Salary: ₹ {salary:,.2f} 🔥</div>',
            unsafe_allow_html=True
        )

        # --------- COMPARISON LOGIC ---------
        if expected_salary:
            try:
                expected_value = float(expected_salary)

                if salary > expected_value:
                    st.success("🔥 Predicted Salary is HIGHER than your Expected Salary!")
                elif salary < expected_value:
                    st.warning("⚠ Predicted Salary is LOWER than your Expected Salary!")
                else:
                    st.info("✅ Predicted Salary is EQUAL to your Expected Salary!")

            except:
                st.error("Please enter a valid number for Expected Salary.")

    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 Career Tips")
    st.write("✔ Learn Python & Machine Learning")
    st.write("✔ Build real-world projects")
    st.write("✔ Improve problem solving")
    st.write("✔ Keep updating skills")
    st.markdown('</div>', unsafe_allow_html=True)