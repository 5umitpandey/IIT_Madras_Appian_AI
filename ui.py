import streamlit as st
import asyncio
from app import query_knowledge

st.set_page_config(page_title="Just-in-Time Knowledge Assistant", layout="centered")

st.title("🧠 Just-in-Time Knowledge Assistant")
st.subheader("Context-Aware Policy Retrieval for Case Management")

st.markdown("Enter the case details below:")

# --- Case context inputs ---
claim_type = st.selectbox(
    "Claim Type",
    ["Flood", "Fire", "Accident", "Health", "Other"]
)

location = st.text_input("Location / State", "Florida")

case_category = st.selectbox(
    "Case Category",
    ["Insurance Claim", "Regulatory Case", "Benefits Approval"]
)

if st.button("🔍 Retrieve Relevant Policy Information"):
    with st.spinner("Analyzing case context and retrieving knowledge..."):
        case_context = {
            "claim_type": claim_type,
            "location": location,
            "case_category": case_category,
        }

        answer, sources = asyncio.run(query_knowledge(case_context))

    st.success("Relevant information retrieved")

    st.markdown("### 🧾 Answer")
    st.write(answer)

    st.markdown("### 📎 Sources")
    for src in sources:
        st.write(f"- {src}")
