import faiss
import numpy as np

# Create a small FAISS index
d = 128  # Vector dimension
index = faiss.IndexFlatL2(d)
print("FAISS is installed and working correctly!")
