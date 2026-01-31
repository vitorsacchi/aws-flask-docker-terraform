from flask import Flask, jsonify, render_template
from models import Item
from database import db
import psutil  # Para logs de CPU/memória

app = Flask(__name__)

# Rota principal - renderiza front-end
@app.route("/")
def home():
    return render_template("index.html")

# Rota de API simples
@app.route("/api")
def api():
    return jsonify({"message": "API Flask rodando!"})

# Rota de tarefas
@app.route("/api/tasks")
def tasks():
    data = [
        {"id": 1, "title": "Aprender Flask", "done": True},
        {"id": 2, "title": "Deploy na AWS", "done": True},
        {"id": 3, "title": "Docker + Front-end", "done":True},
    ]
    return jsonify(data)

# Rota de logs do sistema (CPU/memória)
@app.route("/api/logs")
def logs():
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory()
    return jsonify({
        "cpu_percent": cpu,
        "mem_total_gb": round(mem.total / (1024**3), 2),
        "mem_used_gb": round(mem.used / (1024**3), 2),
        "mem_percent": mem.percent
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

