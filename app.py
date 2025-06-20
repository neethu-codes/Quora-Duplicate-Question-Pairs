import streamlit as st
import helper
import pickle


st.header('Duplicate Question Pairs')
st.markdown(
    "Enter two questions below to check if they are semantically similar. "
    "This tool uses an ML model trained on the Quora Question Pairs dataset to predict duplication."
)

q1 = st.text_input('🔹 Question 1', placeholder="Type the first question here...")
q2 = st.text_input('🔸 Question 2', placeholder="Type the second question here...")


if st.button('Check Similarity'):
    prob, result = helper.query_point_creator_and_predict(q1,q2)
    st.markdown("---")
    st.subheader("🔍 Prediction Result")
    if result:
        st.success("✅ The questions are **Duplicate**.")
    else:
        st.error("❌ The questions are **Not Duplicate**.")
    # st.subheader(f"Confidence of predicted class: {max(prob)}")

