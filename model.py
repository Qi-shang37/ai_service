import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
from transformers import pipeline

# 首次运行会自动下载模型（约300MB）
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text: str):
    result = sentiment_analyzer(text)[0]
    return result['label'], result['score']