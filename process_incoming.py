import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import requests


def create_embedding(text_list):
    if isinstance(text_list, str):
        text_list = [text_list]
    payload = {"model": "bge-m3", "input": text_list}

    try:
        r = requests.post("http://localhost:11434/api/embed", json=payload, timeout=30)
        r.raise_for_status()
    except Exception as e:
        raise RuntimeError(f"Embedding request failed: {e}")

    data = r.json()
    embeddings = data.get("embeddings")
    if embeddings is None:
        raise ValueError(f"Response JSON missing 'embeddings': {data}")
    return embeddings

def inference(prompt):
    payload = {"model": "llama3.2", "prompt": prompt, "stream": False}
    r = requests.post("http://localhost:11434/api/generate", json=payload, timeout=30)

    response=r.json()
    
    print(response)
    return response

df=joblib.load("embeddings.joblib")



incoming_query = input("Ask a question: ").strip()
question_embedding = create_embedding([incoming_query])[0]

emb_matrix = np.vstack(df['embedding'].values).astype(float)

similarities = cosine_similarity(emb_matrix, [question_embedding]).flatten()
#print("Top similarity scores (first 10):", similarities[:10])

top_results = 5
top_idx = similarities.argsort()[::-1][:top_results]
#print("Top indices:", top_idx)

result_df = df.iloc[top_idx].copy()
cols_to_show = [c for c in ('text', 'number', 'title') if c in result_df.columns]
#print(result_df[cols_to_show] if cols_to_show else result_df[['text']])

prompt=f''' Andrew Ng is the course instructor for the Machine Learning Specialization course 1.
Here are video subtitle chunks containing video title, video number, start time in seconds, end time
in seconds, the text at that time :

{result_df[['title', 'number','start', 'end','text']].to_json(orient="records")}
------------------------------
"{incoming_query}"
User asked this question related to the video chunks, you have to answer 
in a human way( don't mention the above format,its just for you) where and how much content is taught
where(in which video and at what timestamp) and guide the user to go to that particular video. If the user asks some
unrelated question, tell him that you can only answer questions related to the 4 videos provided.
'''

with open("prompt.txt", "w") as f:
    f.write(prompt)

response = inference(prompt)["response"]
print(response)

with open("response.txt", "w") as f:
    f.write(response)

#for index, item in result_df.iterrows():
   # print(index, item["title"], item["number"],item["text"],item["start"], item["end"])