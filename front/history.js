async function fetchHistory() {
    try {
        const response = await fetch('http://localhost:5000/api/history');
        const data = await response.json();

        const historyList = document.getElementById('historyList');
        historyList.innerHTML = ''; // 清空现有内容

        data.forEach(record => {
            const recordDiv = document.createElement('div');
            recordDiv.className = 'history-item';
            recordDiv.innerHTML = `
                <div class="calculation">
                    ${record.num1} + ${record.num2} = ${record.result}
                </div>
                <div class="timestamp">
                    ${record.timestamp}
                </div>
            `;
            historyList.appendChild(recordDiv);
        });
    } catch (error) {
        console.error('Error fetching history:', error);
    }
}

// 页面加载时获取历史记录
document.addEventListener('DOMContentLoaded', fetchHistory);