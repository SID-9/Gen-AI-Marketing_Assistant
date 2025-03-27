# Gen-AI-Marketing_Assistant

🚀 **AI Marketing Assistant** is a **RAG**  web-based application that generates AI-powered marketing scripts and captions for brands using **LLaMA 2**. This project allows users to input a marketing prompt and brand name, select the type of marketing text (script or caption), and receive an AI-generated marketing response.

## 🌟 Features
- Generate **marketing scripts** and **captions** based on user input.
- Utilizes **LLaMA 2** for AI-powered content generation.
- Interactive UI with easy input fields and selection options.
- Supports emoji-rich marketing content for better engagement.
- Simple and intuitive design for seamless user experience.

## 🛠️ Tech Stack
- **Backend:** Python, Ollama (for LLaMA 2 inference)
- **Frontend:** Gradio
- **Deployment:** Local Server

## 📥 Installation & Setup
### Prerequisites
- Python 3.x installed
- [Ollama](https://ollama.ai/) installed for running LLaMA 2 models

## steps to run the project
1. upon installation of faiss and llama2 run these scripts to confirm there proper working:
  -> faiss_verfification.py
  -> ollama_verification.py
2. run the creating_embeddings.py file :
   -> it will generate embeddins from your stored database in marketing_dataset.csv and save it in faiss.index file
   -> it will save the original dataset in .pkl format since it is faster than a .csv format to use it as a reference for the llama2 model.
4. finally run the marketing_assistant.py file to start the web app.

## 🚀 Usage
1. Enter your **marketing prompt** (e.g., "an ad for a personalized shoe").
2. Enter your **brand name** (e.g., "Steam").
3. Select **Script** or **Caption**.
4. Click **Submit** to generate AI-powered marketing content.
5. View and copy the generated response!

## 🖼️ Screenshots
### Marketing Script Example
![image](https://github.com/user-attachments/assets/dd0f898f-f9ca-49fa-86f9-c30f29732a09)


### Marketing Caption Example
![image](https://github.com/user-attachments/assets/4602b9bf-e6a9-42b1-a6ef-eb5051360337)


## 🎯 Future Enhancements
- Add **multi-model support** (Mistral, GPT-4, etc.).
- Implement **API integration** for external access.
- Improve **UI/UX** with better styling and animations.
- Allow **user authentication** for personalized experiences.

## 🤝 Contributing
Want to contribute? Follow these steps:
1. **Fork** the repository.
2. Create a **new branch** (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Added new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a **Pull Request**.

## 📬 Contact
- **Author:** Siddharth Upadhyay
- **GitHub:** https://github.com/SID-9
- **Email:** siddharthup6103@gmail.com

