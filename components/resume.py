import streamlit as st
import fitz
from io import BytesIO
from fpdf import FPDF
from dotenv import load_dotenv
import os

from google import genai
from google.genai import types


def resume_ui():
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        st.error("Gemini API key missing")
        st.stop()

    client = genai.Client(api_key=api_key)

    st.title("AI Resume Analyser")

    uploaded_file = st.file_uploader(
        "Upload your resume (PDF)", type="pdf"
    )

    if uploaded_file:
        st.success(f"You uploaded: {uploaded_file.name}")

        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")

        full_text = ""
        for page in doc:
            full_text += page.get_text()

        st.subheader("📑 Extracted Resume Text (Preview)")
        st.text_area("Contents", full_text, height=300)

        user_prompt = st.text_input(
            "Enter your question or instruction for the resume"
        )

        if st.button("Ask AI") and user_prompt:
            with st.spinner("Thinking..."):

                # Gemini 3 Flash
                response = client.models.generate_content(
                    model="gemini-3-flash-preview",
                    contents=[
                        f"""
                        {user_prompt}

                        Here is the resume:
                        {full_text}

                        Rate my resume out of 10 and explain briefly.
                        """
                    ],
                    config=types.GenerateContentConfig(
                        temperature=0.3,
                        max_output_tokens=1200,
                    ),
                )

                content = response.text

            st.success("Response received!")
            st.write(content)

            # -------- PDF --------
            def create_pdf_from_text(content):
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)

                content = content.replace("\u2013", "-")
                content = content.encode(
                    "latin-1", "replace"
                ).decode("latin-1")

                for line in content.split("\n"):
                    pdf.multi_cell(0, 10, txt=line)

                buffer = BytesIO()
                buffer.write(pdf.output(dest="S").encode("latin1"))
                buffer.seek(0)
                return buffer

            pdf_file = create_pdf_from_text(content)

            st.download_button(
                "📄 Download Suggestions as PDF",
                pdf_file,
                file_name="ai_resume_feedback.pdf",
            )