from flask import Flask, request, jsonify

from flask_cors import CORS  # 导入 CORS


app = Flask(__name__)
CORS(app)  # 启用跨域资源共享


def add(num1, num2):
    return num1 + num2


@app.route("/api/add", methods=["POST"])
def UsingAddFunction():
    data = request.get_json()
    num1 = data.get("num1")
    print("传入的第一个数字", num1)
    num2 = data.get("num2")
    print("传入的第二个数字", num2)

    if num1 is None or num2 is None:
        return (
            jsonify({"error": "Missing input numbers"}),
            400,
        )  # 如果输入的数字缺失，返回错误信息和状态码 400（请求错误）。

    result = add(num1, num2)
    print("加法结果", result)
    return jsonify(
        {"result": result}
    )  # 这行代码将加法结果 result 以 JSON 格式返回给客户端，客户端会看到 {"result": result}。


if __name__ == "__main__":
    app.run(debug=True)
