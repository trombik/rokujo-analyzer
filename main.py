from fastapi import FastAPI
from pydantic import BaseModel
import spacy

# https://github.com/WorksApplications/Sudachi#the-modes-of-splitting
config = {"nlp": {"tokenizer": {"split_mode": "B"}}}

nlp = spacy.load("ja_ginza", config=config)
app = FastAPI()


class TextData(BaseModel):
    text: str


@app.post("/analyze_tokens")
def analyze(data: TextData):
    doc = nlp(data.text)
    tokens = []
    for token in doc:
        tokens.append({
            "i": token.i,
            "text": token.text,
            "lemma": token.lemma_,
            "pos": token.pos_,
            "tag": token.tag_,
            "dep": token.dep_,
            "head": token.head.i,
            "morph": str(token.morph),
            "idx": token.idx
        })
    return {"tokens": tokens}
