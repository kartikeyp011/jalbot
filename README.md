---

## 🧠 JalBot – Water Conservation Chatbot (SDG 6)

**JalBot** is an AI-powered chatbot built with Streamlit and Gemini API to educate communities about water conservation, sanitation, and sustainable water usage. It supports multilingual responses and is designed as a quick and impactful project under **SDG 6 – Clean Water and Sanitation**.

---

### 🌍 UN Sustainable Development Goal 6

> *"Ensure availability and sustainable management of water and sanitation for all."*
> JalBot addresses this goal by spreading awareness and educating users on:

* 💧 Water-saving methods
* 🚿 Sanitation practices
* 🧠 Conservation tips
* 🌱 Sustainable usage habits

---

## 🔧 Features

* ✅ Ask questions about water conservation and cleanliness
* 🌐 Multilingual support (auto-translates Gemini output)
* ⚡ Powered by Gemini 1.5 Flash (free-tier API)
* 📦 Lightweight, fast Streamlit app
* 🔒 Secure API key handling via `.env` file

---

## 🖼️ Demo Preview

![JalBot UI Screenshot](https://via.placeholder.com/800x400?text=JalBot+Demo+Screenshot)
*(Replace with your own screenshot or GIF)*

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/jalbot.git
cd jalbot
```

### 2. Create a virtual environment (Windows CMD)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Get Gemini API Key (Free)

1. Visit: [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Copy your API key

### 5. Set up `.env` file

Create a `.env` file in the root folder:

```env
GEMINI_API_KEY=your_api_key_here
```

### 6. Run the app

```bash
streamlit run app/main.py
```

---

## 📁 Project Structure

```
WaterBot/
│
├── app/
│   ├── main.py               # Streamlit app
│   └── qa_engine.py          # Gemini setup & response function
│
├── .env                      # Gemini API Key
├── requirements.txt
└── README.md
```

---

## 📚 Example Questions

* *What are some simple ways to save water at home?*
* *How can we prevent water pollution in villages?*
* *Give tips to keep drinking water clean.*
* *बच्चों को जल संरक्षण कैसे सिखाएं?*

---

## 🌐 Multilingual Support

Uses the Gemini API to respond in the selected language.
Current supported languages: English, Hindi, Bengali, Gujarati, Tamil, Kannada, etc.
*(More can be added easily using Google Translate API or language dictionaries)*

---

## 💡 Future Improvements

* Chat history & memory
* Text-to-speech answers
* Quiz mode for school students
* Offline support with local QnA dataset

---

## 🧠 Built With

* [Streamlit](https://streamlit.io/)
* [Google Gemini API](https://ai.google.dev/)
* [dotenv](https://pypi.org/project/python-dotenv/)

---

## 🤝 Contributing

PRs welcome! Feel free to fork and enhance JalBot.

---

## 📜 License

MIT License — feel free to use, modify, and share with attribution.

---

## 🙌 Acknowledgements

* Inspired by UN's **Sustainable Development Goals**
* Built with support from [IBM SkillsBuild](https://skillsbuild.org/)
* Gemini API by Google AI

---
