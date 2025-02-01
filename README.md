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

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/AI-Cover-Letter-Generator.git
cd AI-Cover-Letter-Generator
```

### 2️⃣ Create a Virtual Environment (Optional, Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application
```bash
streamlit run main.py
```
Then, open **http://localhost:8501** in your browser.

---

## 🔑 API Key Setup
This app requires an API key to process resumes and generate cover letters.  
👉 **Get your API key [here](https://your-api-provider.com)**  

When running the app, **enter your API key** in the designated field.

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
- **Keep your API key private** (do not hardcode it in the scripts).  
- Ensure **your resume is well-structured** for better AI parsing.  
- The AI-generated cover letter may need **minor adjustments**.

---

## 👨‍🚀 Author
Made with ❤️ by **[Piero Paialunga](https://piero-paialunga.medium.com/)**  
Feel free to reach out for questions or collaborations!

---

## 📜 License
This project is **open-source** under the **MIT License**.
