# 🎓 Alumnet – AI-Powered Alumni-Company Networking Platform

## 🧠 Project Overview

Alumnet bridges the gap between alumni and companies by providing an intelligent, searchable platform for Training & Placement (TNP) purposes.  
Use cases include identifying company connections via alumni, retrieving HR contacts, and automating outreach via WhatsApp and email.  
The system supports natural language queries and delivers relevant responses using graph and vector databases.

---

## 🚀 Features

- Neo4j graph database for alumni-company-employment relationship modeling  
- Semantic search with Pinecone & FAISS for context-aware alumni retrieval  
- Natural language query classification using LangChain & Google GenAI Gemini  
- Real-time messaging via WhatsApp (pywhatkit) and email (SMTP)  
- FastAPI-powered backend with scalable REST endpoints  

---

## 🛠️ Technologies Used

- **Backend**: Python, FastAPI, LangChain  
- **Databases**: Neo4j (Graph), Pinecone (Vector), FAISS  
- **AI/LLM**: Google GenAI Gemini API  
- **Messaging**: pywhatkit (WhatsApp), smtplib (Email)  
- **Frontend** (Optional): React/Next.js  
- **Deployment**: AWS / GCP  

---

## 📋 Prerequisites

- Python: `>=3.10`  
- Node.js: `>=18.x` (for frontend or plugin interface)  
- Neo4j: `>=5.x`  
- Chrome browser (for pywhatkit)  
- Gemini and Pinecone API keys  
- Git  

---
## ⚙️ Backend Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/alumnet.git
cd alumnet/backend
```

# Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

# Install dependencies
```bash
pip install -r requirements.txt
```

# Create .env file and set the following environment variables
# Example .env content:
```bash
# GEMINI_API_KEY=your_gemini_api_key
# PINECONE_API_KEY=your_pinecone_api_key
# PINECONE_ENV=your_pinecone_env
# PINECONE_INDEX=your_index
# NEO4J_URI=bolt://localhost:7687
# NEO4J_USER=neo4j
# NEO4J_PASSWORD=your_password
```

# Run the FastAPI server
```bash
uvicorn main:app --reload --port 8000
```

Backend runs at: http://localhost:8000

## 🌐 Frontend Setup
```bash
cd frontend

# Install frontend dependencies
npm install

# Start the development server
npm run dev
```

Frontend runs at: http://localhost:3000

## 📞 Communication Services
- WhatsApp: Automated message delivery using pywhatkit. Make sure Chrome is set as default and logged into WhatsApp Web.

- Email: Automated emails sent to HRs via Python's built-in smtplib.
