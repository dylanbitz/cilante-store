document.addEventListener('DOMContentLoaded', () => {
    const input = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-button');
    const chatBox = document.getElementById('chat-box');

    function appendUser(text) {
        const d = document.createElement('div');
        d.className = 'bubble user';
        d.textContent = text;
        chatBox.appendChild(d);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    function appendBot(text) {
        const d = document.createElement('div');
        d.className = 'bubble bot';
        d.textContent = text;
        chatBox.appendChild(d);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    async function sendMessage() {
        const msg = input.value.trim();
        if (!msg) return;
        appendUser(msg);
        input.value = '';
        sendBtn.disabled = true;

        try {
            const res = await fetch(window.location.pathname, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: msg, conversation_id: window.conversation_id || null })
            });
            const data = await res.json();
            if (res.ok) {
                appendBot(data.response || '[sin respuesta]');
                if (data.conversation_id) {
                    window.conversation_id = data.conversation_id;
                }
            } else {
                appendBot(data.error || 'Error del servidor');
            }
        } catch (err) {
            appendBot('Error de conexión');
            console.error(err);
        } finally {
            sendBtn.disabled = false;
        }
    }

    sendBtn.addEventListener('click', sendMessage);
    input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });

    // Restaurar conversación anterior
    const restoreYes = document.getElementById('restore-yes');
    const restoreNo = document.getElementById('restore-no');
    const restorePrompt = document.getElementById('restore-prompt');
    if (restoreYes) {
        restoreYes.addEventListener('click', function() {
            // Recarga la página con el parámetro ?restaurar=1
            window.location.search = '?rstr=1';
        });
    }
    if (restoreNo) {
        restoreNo.addEventListener('click', function() {
            restorePrompt.remove();
        });
    }
});