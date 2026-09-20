import streamlit as st

st.title("📚 Smart Attendance Predictor")
st.subheader("Student Details")

name = st.text_input("Student Name")

roll = st.text_input("Roll Number")

branch = st.text_input("Branch")
total = st.number_input("Total Classes", min_value=1)

attended = st.number_input("Attended Classes", min_value=0)

if attended <= total:

    percentage = (attended / total) * 100

    st.write(f"Attendance Percentage: {percentage:.2f}%")

    if percentage >= 75:
        st.success("✅ Attendance is Safe")
    else:
        st.error("⚠️ Attendance Below 75%")

    missed = st.number_input(
        "Future Classes You Want To Miss",
        min_value=0
    )

    future_percentage = (
        attended / (total + missed)
    ) * 100

    st.write(
        f"Predicted Attendance: {future_percentage:.2f}%"
    )

else:
    st.error(
        "Attended classes cannot exceed total classes"
    )
    # Add creator credit at the bottom
st.markdown("---")
st.markdown("### 🛠️ Created by Charan Singh")
