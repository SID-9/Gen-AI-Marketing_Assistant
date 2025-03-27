import faiss
import pickle
import pandas as pd
from sentence_transformers import SentenceTransformer
import ollama
import gradio as gr

# load the faiss index
index = faiss.read_index("marketing_faiss.index")

# load the stored dataset  (.pkl format)
ds = pd.read_pickle("marketing_texts.pkl")

# load the embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# load llama2 model 
#llama2 = pipeline("text-generation", model="meta-llama/Llama-2-7b-chat-hf",device=0 if torch.cuda.is_available() else -1)


def search_marketing_text(query,text_type, top_k=1):
    """
    Searches for the most relevant marketing text from FAISS based on user choice.

    Args:
        query (str): User input text
        text_type (str): "script" or "caption"
        top_k (int): Number of results to return

    Returns:
        List of matching texts
    """
    
    # convert query to embedding with explicit type
    query_embedding = model.encode([f"{text_type}: {query}"], normalize_embeddings=True)
    
    # search faiss for the closest match
    _, indices = index.search(query_embedding, top_k)
    
    # retrieve matched text from dataframe
    results = ds.iloc[indices[0]]
    return results["text"].tolist()

def generate_marketing_text(prompt, brand_name, text_type):
    """
    Generates marketing text using LLaMA2 based on user input and retrieved samples.

    Args:
        prompt (str): The user-provided prompt
        brand_name (str): The name of the brand
        text_type (str): "script" or "caption"

    Returns:
        str: AI-generated marketing text
    """
    retrieved_samples = search_marketing_text(prompt, text_type, top_k=3)
    
    # construct a detailed prompt for llama2
    formatted_prompt = f"""
    You are a marketing expert. Generate a {text_type} for a product based on the following details:
    
    Brand Name: {brand_name}
    User Request: {prompt}
    Sample Marketing {text_type}s for reference:
    1. {retrieved_samples[0]}
    2. {retrieved_samples[1]}
    3. {retrieved_samples[2]}

    Now generate a fresh, engaging, and creative {text_type} in the same style but tailored for {brand_name}.
    """
    
    #response = llama2(formatted_prompt, max_length=200, do_sample=True,temerature=0.7)
    #return response[0]["generated_text"]
    response = ollama.chat(model="llama2", messages=[{'role': 'user', 'content': formatted_prompt}])
    return response['message']['content']
    
    

# Gradio  UI

def marketing_ui(prompt, brand_name , text_type):
    return generate_marketing_text(prompt, brand_name, text_type)
    
iface = gr.Interface(
    fn=marketing_ui,
    inputs=[
        gr.Textbox(label="Enter your marketing prompt : "),
        gr.Textbox(label="Enter your brand name : "),
        gr.Radio(["script","caption"],label="Choose the type of marketing text you want ? ")
        
    ],
    outputs = gr.Textbox(label="Generated Marketing Text : "),
    title = "AI Marketing Assistant",
    description = "Generate AI-powered marketing scripts and captions customized for your brand using LLaMA2. "
    
)

if __name__ == "__main__":
    iface.launch()
    
    
    
    
    

'''
# choose the interaction type from user
def get_user_choice():
    
    print("Choose the type of marketing text you want:")
    print("1. Script")
    print("2. Caption")
    
    while True:
        choice = input("Enter 1 or 2: ")
        if choice == "1":
            return "script"
        elif choice == "2":
            return "caption"
        else:
            print("Invalid input. Please enter 1 or 2.")
        
# Example usage
if __name__ == "__main__":
    user_query = input("Enter your marketing prompt: ")
    text_type = get_user_choice()
    
    result = search_marketing_text(user_query, text_type)
    print(f"\nGenerated {text_type.capitalize()}:\n{result[0]}")
'''