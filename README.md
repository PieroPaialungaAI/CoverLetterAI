# 📄 AI Cover Letter Generator

🚀 **Automatically generate professional cover letters using AI!**  
This project allows users to upload their resume, provide a job description, and receive an AI-generated cover letter tailored to the job.

---

## 📂 Repository Structure
```
├── constants.py         # Stores global constants (e.g., API keys, file paths)
├── file_loader.py       # Handles file operations (reading resumes, saving outputs)
├── cover_letter.py      # Core AI logic for parsing resumes and generating cover letters
├── main.py              # Streamlit app for the user interface
└── README.md            # Documentation
```

---

## 🚀 Features
✅ Upload a **PDF** or **DOCX** resume  
✅ AI extracts key information from the resume  
✅ Paste a job description to tailor the cover letter  
✅ AI generates a personalized **cover letter**  
✅ Clean **Streamlit UI**  

---

## 🛠 Installation

### Clone the Repository
```bash
git clone https://github.com/yourusername/AI-Cover-Letter-Generator.git
cd AI-Cover-Letter-Generator
```

---

## ▶️ Running the Application
```bash
streamlit run main.py
```
Then, open **http://localhost:8501** in your browser.

---

## 🔑 API Key Setup
This app requires an API key to process resumes and generate cover letters. I used Llama API as a API provider. Feel free to use whatever you like and change the code accordingly. 
👉 **Get Llama API key [here](https://www.llama-api.com/)**  

When running the app, **enter your API key** in the designated field. If you are using the code locally, you can add the key in the `constants.py` file and use it from default.

---

## 📜 Usage
1️⃣ **Upload your resume** (PDF/DOCX)  
2️⃣ **Paste the job description**  
3️⃣ **Click "Generate Cover Letter"**  
4️⃣ **Copy and use your AI-generated cover letter!**  

---

## 👨‍💻 How It Works
1️⃣ **`file_loader.py`** reads and extracts text from resumes.  
2️⃣ **`cover_letter.py`** uses AI to analyze resumes and generate a structured profile.  
3️⃣ **`constants.py`** stores API keys & other configs.  
4️⃣ **`main.py`** is the **Streamlit UI** that interacts with the user.

---

## 📌 Notes
- **Keep your API key private** (do not hardcode it in the scripts unless you are using it locally).  
- Ensure **your resume is well-structured** for better AI parsing.  
- The AI-generated cover letter may need **minor adjustments** and it can be slow.

---

## 👨‍🚀 Author
Made with ❤️ by Piero Paialunga. This is **[my portfolio](https://piero-paialunga.medium.com/)**  
Feel free to reach out for questions or collaborations!

---

## 📜 License
This project is **open-source** under the **MIT License**.
