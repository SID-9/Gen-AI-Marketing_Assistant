import faiss
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
import pickle

# loading the csv original dataset
ds = pd.read_csv("marketing_dataset.csv")

# loading the embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# convert text data into embeddings
texts = ds.apply(lambda row: f"{row['text_type']}: {row['text']}", axis=1).tolist()
embeddings = model.encode(texts,normalize_embeddings=True)

# store in faiss
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# save faiss index
faiss.write_index(index,"marketing_faiss.index")

# save texts and metadata for retrieval in pickle file bcz loading and working with csv is slowwer than pkl
ds.to_pickle("marketing_texts.pkl") # saving full dataframe for later use