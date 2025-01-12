function sendData() {
    const num1 = document.getElementById("num1").value;
    const num2 = document.getElementById("num2").value;
    if (num1 === "" || num2 === "") {
        alert("请输入两个数字");
        return;
    }
    fetch("http://localhost:5000/add", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            num1: parseInt(num1),
            num2: parseInt(num2)
        })
    })
        .then(response => response.json())
        .then(data => {
            if (data.result !== undefined) {
                document.getElementById('result').textContent = `结果: ${data.result}`;
            } else {
                document.getElementById('result').textContent = '计算出错，请重试。';
            }
        })
        .catch(error => console.error('Error:', error));

}