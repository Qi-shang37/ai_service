from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import redis
import json
from model import analyze_sentiment
from database import log_inference

redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

app = FastAPI(title="AI推理服务")

class TextRequest(BaseModel):
    text: str

@app.post("/predict")
async def predict(request: TextRequest):
    input_text = request.text.strip()
    if not input_text:
        raise HTTPException(status_code=400, detail="文本不能为空")

    # 查缓存
    cached = redis_client.get(input_text)
    if cached:
        label, score = json.loads(cached)
        log_inference(input_text, label, score)
        return {"sentiment": label, "confidence": score}

    # 调模型
    label, score = analyze_sentiment(input_text)

    # 存缓存（1小时）
    redis_client.setex(input_text, 3600, json.dumps([label, score]))

    # 存数据库
    log_inference(input_text, label, score)

    return {"sentiment": label, "confidence": score}

@app.get("/")
def root():
    return {"message": "服务已启动，访问 /docs 查看接口文档"}