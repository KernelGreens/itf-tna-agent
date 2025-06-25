from fastapi import FastAPI
from app.routes.analyze import router as analyze_router

app = FastAPI(title="Agentic TNA Automation")

#routes
app.include_router(analyze_router, prefix="/api/analyze")

#root path for testing
@app.get("/")
def root():
    return {"message": "Agentic TNA API is running"}