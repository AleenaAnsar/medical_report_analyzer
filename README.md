# 🩺 Medical Report Analyzer

An AI-powered Medical Report Analyzer built using Python, Streamlit, PyMuPDF, and Groq LLMs. The application allows users to upload medical reports in PDF format, extract text automatically, and generate an AI-based summary with important findings and educational explanations.

## 🚀 Features

* Upload medical reports in PDF format
* Automatic text extraction using PyMuPDF
* AI-powered report analysis using Groq LLM
* Summary of key findings
* Identification of abnormal values and observations
* Educational explanations of medical terms
* Simple and user-friendly Streamlit interface

## 🛠️ Technologies Used

* Python
* Streamlit
* Groq API
* PyMuPDF (fitz)
* Python Dotenv

## 📂 Project Structure

```text
Medical_Report_Analyzer/
│
├── app.py
├── analyzer.py
├── pdf_reader.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/medical-report-analyzer.git
cd medical-report-analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

## ▶️ Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## 📸 Workflow

1. Upload a medical report PDF.
2. Extract text from the document.
3. Send extracted content to the Groq LLM.
4. Generate:

   * Summary
   * Important Findings
   * Abnormal Values
   * Educational Explanation
5. Display results through the Streamlit interface.

## ⚠️ Disclaimer

This project is intended for educational and demonstration purposes only. It does not provide medical diagnosis, treatment recommendations, or professional healthcare advice. Always consult a qualified healthcare professional for medical concerns.

## 📈 Future Improvements

* OCR support for scanned reports
* Blood parameter extraction and analysis
* Health trend visualization with charts
* Downloadable PDF reports
* Multi-report comparison
* Patient history tracking

## 👩‍💻 Author

Aleena Ansar

M.Sc. Student | AI & Machine Learning Enthusiast
