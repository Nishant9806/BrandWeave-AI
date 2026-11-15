
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.health import router as health_router
from app.api.routes.content import router as content_router
from app.api.routes.review import router as review_router
from app.api.routes.approval import router as approval_router

app = FastAPI(
    title="BrandWeave AI",
    description="AI-powered brand governance platform",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router, prefix="/api")
app.include_router(content_router, prefix="/api")
app.include_router(review_router, prefix="/api")
app.include_router(approval_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Welcome to BrandWeave AI API"}
