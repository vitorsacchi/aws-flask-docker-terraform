async function getMessage() {
    const res = await fetch('/api');
    const data = await res.json();
    document.getElementById('message').innerText = data.message;
}

async function getTasks() {
    const res = await fetch('/api/tasks');
    const tasks = await res.json();
    const ul = document.getElementById('tasks');
    ul.innerHTML = "";
    tasks.forEach(task => {
        const li = document.createElement('li');
        li.innerText = `${task.id}. ${task.title} - ${task.done ? '✅' : '❌'}`;
        ul.appendChild(li);
    });
}

async function getLogs() {
    const res = await fetch('/api/logs');
    const data = await res.json();
    document.getElementById('cpu').innerText = `CPU: ${data.cpu_percent}%`;
    document.getElementById('mem').innerText = `Memória: ${data.mem_percent}% (${data.mem_used_gb}GB de ${data.mem_total_gb}GB)`;
}

