# YouVa-Chat 🚀

An all-in-one AI-powered platform built with Streamlit that combines intelligent chat capabilities with resume analysis features.

## Features

- **AI Chat** 💬 - Interactive chat with multiple AI models (Gemini, OpenAI via OpenRouter)
- **Resume Analyzer** 📄 - Upload and analyze resumes with AI-powered feedback and ratings
- **Chat History** 💾 - Persistent conversation storage using MongoDB
- **Multi-Model Support** 🤖 - Switch between different AI models seamlessly

## Tech Stack

- **Frontend**: Streamlit
- **AI Models**: Google Gemini, OpenAI (via OpenRouter)
- **Database**: MongoDB
- **PDF Processing**: PyMuPDF (fitz), FPDF
- **Environment**: Python 3.11

## Prerequisites

- Python 3.11+
- MongoDB instance (local or cloud)
- API Keys:
  - Google Gemini API Key
  - OpenRouter API Key (for OpenAI models)

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd <your-repo-name>
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:

Create a `.env` file in the root directory with the following:
```env
GEMINI_API_KEY=your_gemini_api_key_here
OPENROUTER_API_KEY=your_openrouter_api_key_here
MONGO_URI=your_mongodb_connection_string_here
```

## Usage

Run the application:
```bash
streamlit run main.py
```

The app will open in your browser at `http://localhost:8501`

### Using the Chat Feature

1. Click "Chat with AI" in the sidebar
2. Select your preferred AI model (Gemini 2.5 Flash)
3. Click "Start Chat"
4. Type your message and interact with the AI

### Using the Resume Analyzer

1. Click "Analyse Resume" in the sidebar
2. Upload a PDF resume
3. Enter your question or instruction (e.g., "Review my resume")
4. Click "Ask AI" to get feedback
5. Download the AI feedback as a PDF

## Project Structure

```
.
├── components/
│   ├── chatAi.py       # AI chat interface and logic
│   ├── mongodb.py      # MongoDB connection and operations
│   ├── resume.py       # Resume analysis functionality
│   └── sidebar.py      # Sidebar navigation component
├── main.py             # Main application entry point
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (not in git)
└── .devcontainer/     # Dev container configuration
```

## Development

### Using Dev Container

This project includes a dev container configuration for easy setup:

1. Open in VS Code with Dev Containers extension
2. Reopen in container when prompted
3. The environment will be automatically configured

### Local Development

The application runs on port 8501 by default. MongoDB connection is configured via the `MONGO_URI` environment variable.

## Features in Detail

### Chat Persistence
- All conversations are saved to MongoDB
- Session-based chat history
- Automatic message retrieval on restart

### Resume Analysis
- PDF text extraction
- AI-powered resume review
- Rating system (out of 10)
- Downloadable feedback reports

### Multi-Model Support
- Gemini 2.5 Flash
- OpenAI models (via OpenRouter)
- Easy model switching
