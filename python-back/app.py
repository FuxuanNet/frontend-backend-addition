from flask import Flask, request, jsonify

from flask_cors import CORS  # 导入 CORS

import sqlite3
from datetime import datetime


app = Flask(__name__)
CORS(app)  # 启用跨域资源共享


# 创建数据库和表
def init_db():
    conn = sqlite3.connect("calculations.db")
    c = conn.cursor()
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS calculations
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         num1 REAL NOT NULL,
         num2 REAL NOT NULL,
         result REAL NOT NULL,
         timestamp TEXT NOT NULL)
    """
    )
    conn.commit()
    conn.close()


def add(num1, num2):
    return num1 + num2


@app.route("/api/add", methods=["POST"])
def using_add_function():
    data = request.get_json()
    num1 = data.get("num1")
    num2 = data.get("num2")

    if num1 is None or num2 is None:
        return (
            jsonify({"error": "Missing input numbers"}),
            400,
        )  # 如果输入的数字缺失，返回错误信息和状态码 400（请求错误）。

    result = add(num1, num2)

    # 保存计算记录到数据库
    conn = sqlite3.connect("calculations.db")
    c = conn.cursor()
    c.execute(
        """
        INSERT INTO calculations (num1, num2, result, timestamp)
        VALUES (?, ?, ?, ?)
    """,
        (num1, num2, result, datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
    )
    conn.commit()
    conn.close()

    return jsonify(
        {"result": result}
    )  # 这行代码将加法结果 result 以 JSON 格式返回给客户端，客户端会看到 {"result": result}。


@app.route("/api/history", methods=["GET"])
def get_history():
    conn = sqlite3.connect("calculations.db")
    c = conn.cursor()
    c.execute("SELECT * FROM calculations ORDER BY timestamp DESC")
    rows = c.fetchall()

    history = []
    for row in rows:
        history.append(
            {
                "id": row[0],
                "num1": row[1],
                "num2": row[2],
                "result": row[3],
                "timestamp": row[4],
            }
        )

    conn.close()
    return jsonify(history)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
