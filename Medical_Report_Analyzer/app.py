import streamlit as st

from pdf_reader import extract_text
from analyzer import analyze_report

st.title("Medical Report Analyzer")

uploaded_file = st.file_uploader(
    "Upload Medical Report",
    type=["pdf"]
)

if uploaded_file:

    with st.spinner("Reading report..."):
        report_text = extract_text(uploaded_file)

    st.subheader("Extracted Report")

    st.text_area(
        "Report Text",
        report_text,
        height=250
    )

    if st.button("Analyze Report"):

        with st.spinner("Analyzing..."):

            result = analyze_report(report_text)

        st.subheader("Analysis")

        st.write(result)

        st.warning(
            "This tool is for educational purposes only and not a medical diagnosis."
        )