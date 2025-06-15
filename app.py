from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from sympy import Symbol, laplace_transform, sympify, simplify
from sympy.abc import t, s
import uvicorn

app = FastAPI()

# Permitir acceso desde cualquier frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Laplace API online"}

@app.post("/laplace")
async def compute_laplace(request: Request):
    try:
        data = await request.json()
        expr_str = data.get("expression")
        f = sympify(expr_str)
        F_s = laplace_transform(f, t, s, noconds=True)
        return {"original": str(f), "laplace": str(simplify(F_s))}
    except Exception as e:
        return {"error": str(e)}
