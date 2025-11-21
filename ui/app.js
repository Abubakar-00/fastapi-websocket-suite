const ws = new WebSocket('ws://localhost:8000/ws');
const statusSpan = document.getElementById('status');
const resultBox = document.getElementById('resultBox');
const computeBtn = document.getElementById('computeBtn');

ws.onopen = () => {
    statusSpan.textContent = 'Connected';
    statusSpan.className = 'text-green-500';
};

ws.onclose = () => {
    statusSpan.textContent = 'Disconnected';
    statusSpan.className = 'text-red-500';
};

ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    if (data.error) {
        resultBox.innerHTML = `<span class="text-red-600">Error: ${data.error}</span>`;
    } else {
        resultBox.innerHTML = `<span class="text-gray-800 font-bold text-xl">${data.result}</span>`;
    }
};

computeBtn.addEventListener('click', () => {
    const operation = document.getElementById('operation').value;
    const a = parseFloat(document.getElementById('a').value);
    const b = parseFloat(document.getElementById('b').value);

    if (isNaN(a) || isNaN(b)) {
        resultBox.innerHTML = '<span class="text-red-600">Please enter valid numbers</span>';
        return;
    }

    const payload = {
        operation: operation,
        a: a,
        b: b
    };

    ws.send(JSON.stringify(payload));
    resultBox.innerHTML = '<span class="text-gray-400">Computing...</span>';
});
