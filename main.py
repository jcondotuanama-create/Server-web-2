from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Servidor Biomédico Profesional")

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head><title>Biomedical Pro</title></head>
        <body style="font-family: Arial; text-align: center; margin-top: 100px;">
            <h1>🧬 Servidor Biomédico Profesional</h1>
            <p>FastAPI está funcionando perfectamente en Windows.</p>
            <a href="/docs">Ver Documentación Automática</a>
        </body>
    </html>
    """
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=21080, reload=True)