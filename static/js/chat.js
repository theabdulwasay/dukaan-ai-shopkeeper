let currentMode = 'qa';

const modeLabels = {
  qa: 'Your question',
  description: 'Product name + details (e.g. "Chai patti, 500g, imported")',
  reply: "Paste the customer's message here",
};
const modePlaceholders = {
  qa: 'e.g. Kya sugar ka stock kam hai?',
  description: 'e.g. Chai patti, 500 gram pack, imported, strong flavour, Rs. 350',
  reply: 'e.g. Kya aapke pass 10kg atta available hai? Price kya hai?',
};

function setMode(mode) {
  currentMode = mode;
  document.querySelectorAll('.mode-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.mode === mode);
  });
  document.getElementById('inputLabel').textContent = modeLabels[mode];
  document.getElementById('chatInput').placeholder = modePlaceholders[mode];
}

function appendMessage(text, cls) {
  const win = document.getElementById('chatWindow');
  const div = document.createElement('div');
  div.className = 'msg ' + cls;
  div.textContent = text;
  win.appendChild(div);
  win.scrollTop = win.scrollHeight;
  return div;
}

document.getElementById('chatForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const input = document.getElementById('chatInput');
  const question = input.value.trim();
  if (!question) return;

  appendMessage(question, 'user');
  input.value = '';

  const sendBtn = document.getElementById('sendBtn');
  sendBtn.disabled = true;
  const thinkingMsg = appendMessage('Thinking...', 'ai');

  try {
    const response = await fetch('/assistant/ask', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        question,
        mode: currentMode,
        language: document.getElementById('langSelect').value,
      }),
    });
    const data = await response.json();
    thinkingMsg.remove();
    if (data.error) {
      appendMessage(data.error, 'error');
    } else {
      appendMessage(data.answer, 'ai');
    }
  } catch (err) {
    thinkingMsg.remove();
    appendMessage('Network error — please try again.', 'error');
  } finally {
    sendBtn.disabled = false;
  }
});
