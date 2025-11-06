# 👵 MediGranny
![MediGranny Banner](assets/MediGrannyESP.jpeg)

**AI-powered chatbot for medication guidance** — Making healthcare information accessible to everyone, especially seniors.

![Status](https://img.shields.io/badge/status-MVP-green)
![Python](https://img.shields.io/badge/python-3.11+-blue)
![License](https://img.shields.io/badge/license-MIT-blue)

---

## 🌟 About

MediGranny is a compassionate AI assistant that translates complex medical information into warm, simple language. As Spain transitions medication leaflets to digital-only formats, millions of seniors risk being excluded. MediGranny bridges this digital divide.

### Key Features

- 💜 **Empathetic tone** — Like talking to a caring grandmother
- 🇪🇸 **Official data** — Powered by Spain's CIMA API (Medicines Agency)
- 🤖 **AI-driven** — OpenAI for natural language understanding
- 🔐 **Responsible AI** — Never diagnoses, always includes disclaimers
- ⚡ **Fast & simple** — Plain language explanations in seconds

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- OpenAI API key ([get one here](https://platform.openai.com/api-keys))

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/YOUR-USERNAME/MediGranny.git
cd MediGranny

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Edit .env and add your OpenAI API key

# 5. Run the backend
python app.py

# 6. Open frontend
# Simply open index.html in your browser
```

---

## 🏗️ Architecture

```
┌─────────────┐
│   User      │
└──────┬──────┘
       │
       ▼
┌─────────────────────────┐
│  Frontend (index.html)  │
│  Simple chat interface  │
└──────┬──────────────────┘
       │ HTTP POST
       ▼
┌─────────────────────────┐
│  Backend (Flask)        │
│  • app.py               │
└──────┬──────────────────┘
       │
   ┌───┴────┐
   ▼        ▼
┌──────┐ ┌────────┐
│ CIMA │ │ OpenAI │
│ API  │ │  API   │
└──────┘ └────────┘
```

---

## 💻 Tech Stack

- **Backend:** Python, Flask, Flask-CORS
- **AI:** OpenAI API (GPT-3.5-turbo)
- **Data:** CIMA REST API (Spanish Medicines Agency)
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Deployment:** Docker-ready (coming soon)

---

## 📊 Example Usage

```
User: "What is paracetamol?"

MediGranny: "Paracetamol is a medicine that helps reduce fever 
and relieve mild to moderate pain, like headaches or body aches. 
It's one of the most commonly used medicines and is generally safe 
when taken as directed. Remember, dear, always check with your 
doctor or pharmacist."
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your-openai-key-here
```

**⚠️ Never commit your `.env` file!** It's already in `.gitignore`.

---

## 🧪 Testing

Try these medications:
- `paracetamol`
- `aspirina`
- `ibuprofeno`

---

## 📈 Roadmap

- [x] MVP: Basic chat functionality
- [x] CIMA API integration
- [x] OpenAI integration
- [ ] Docker containerization
- [ ] Deploy to Render/Railway
- [ ] Voice input support (Web Speech API)
- [ ] Multi-language support
- [ ] Expand to EU medicine databases

---

## 💰 Cost

- **CIMA API:** Free (Spanish government)
- **OpenAI API:** ~$0.002 per conversation
- **Hosting:** Free tier available (Render/Railway)

**Total:** ~$10-30/month for 1,500-4,000 conversations

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📄 License

MIT License - feel free to use this project for learning or personal use.

---

## 🌍 Social Impact

This project addresses digital exclusion in healthcare. As governments transition to digital-first services, we must ensure vulnerable populations aren't left behind.

**Technology should serve everyone, not just the digitally native.**

---

## 👩‍💻 Author

**Sara Triana Merchan**

- LinkedIn: [linkedin.com/in/sara-triana-merchan](https://linkedin.com/in/sara-triana-merchan)
- Email: saratrianamerchan@gmail.com

---

## ⚠️ Disclaimer

MediGranny is not a medical professional. It provides informational summaries based on official medication sources (CIMA/AEMPS). Always consult a qualified healthcare professional before making medical decisions.

---

## 💜 Acknowledgments

Built with empathy for seniors and vulnerable populations experiencing digital exclusion in healthcare services.

---

**⭐ If you find this project helpful, please consider giving it a star!**
