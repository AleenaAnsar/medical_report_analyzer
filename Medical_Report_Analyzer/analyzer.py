from groq import Groq

# Replace with your Groq API key
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def analyze_report(report_text):

    prompt = f"""
You are a medical report assistant.

Analyze the medical report and provide:

1. Summary
2. Important Findings
3. Abnormal Values
4. General Educational Explanation

Important:
- Do NOT provide a medical diagnosis.
- Do NOT prescribe medicines.
- Clearly state that this is not medical advice.

Medical Report:
{report_text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content