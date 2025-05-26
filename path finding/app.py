from flask import Flask, render_template, request, jsonify
import time
from algorithms import dfs, bfs, dijkstra, a_star, backtracking  # Your implementations

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/solve", methods=["POST"])
def solve():
    data = request.json
    grid = data["grid"]
    start = tuple(data["start"])
    end = tuple(data["end"])

    results = []

    for name, algo in [
        ("DFS", dfs),
        ("BFS", bfs),
        ("Dijkstra", dijkstra),
        ("A*", a_star),
        ("Backtracking", backtracking)
    ]:
        start_time = time.perf_counter()
        path = algo(grid, start, end)
        end_time = time.perf_counter()
        results.append({
            "name": name,
            "path": path,
            "time": round((end_time - start_time) * 1000, 2)
        })

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
