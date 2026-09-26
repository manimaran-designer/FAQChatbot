// Configuration
const API_URL = '/chat';

// DOM Elements
const chatMessages = document.getElementById('chatMessages');
const messageInput = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');
const typingIndicator = document.getElementById('typingIndicator');
const clearChatBtn = document.getElementById('clearChat');
const charCount = document.getElementById('charCount');
const quickQuestionBtns = document.querySelectorAll('.quick-question-btn');

// Auto-resize textarea
messageInput.addEventListener('input', function () {
    this.style.height = 'auto';
    this.style.height = (this.scrollHeight) + 'px';

    // Update character count
    charCount.textContent = this.value.length;

    // Enable/disable send button
    sendButton.disabled = this.value.trim().length === 0;
});

// Send message on Enter (Shift+Enter for new line)
messageInput.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});

// Send button click
sendButton.addEventListener('click', sendMessage);

// Clear chat button
clearChatBtn.addEventListener('click', function () {
    if (confirm('Are you sure you want to clear the chat history?')) {
        chatMessages.innerHTML = `
            <div class="welcome-message">
                <div class="welcome-icon">👋</div>
                <h2>Welcome to SBI Health Card Support</h2>
                <p>I'm here to help you with questions about your health card, claims, and network hospitals. Ask me anything!</p>
                <div class="quick-questions">
                    <button class="quick-question-btn" data-question="What is a health card?">What is a health card?</button>
                    <button class="quick-question-btn" data-question="How do I apply for cashless treatment?">How do I apply for cashless treatment?</button>
                    <button class="quick-question-btn" data-question="What if my card is lost?">What if my card is lost?</button>
                </div>
            </div>
        `;
        attachQuickQuestionListeners();
    }
});

// Quick question buttons
function attachQuickQuestionListeners() {
    document.querySelectorAll('.quick-question-btn').forEach(btn => {
        btn.addEventListener('click', function () {
            const question = this.getAttribute('data-question');
            messageInput.value = question;
            messageInput.dispatchEvent(new Event('input'));
            sendMessage();
        });
    });
}

attachQuickQuestionListeners();

// Send message function
async function sendMessage() {
    const message = messageInput.value.trim();

    if (!message) return;

    // Remove welcome message if it exists
    const welcomeMsg = chatMessages.querySelector('.welcome-message');
    if (welcomeMsg) {
        welcomeMsg.remove();
    }

    // Add user message
    addMessage(message, 'user');

    // Clear input
    messageInput.value = '';
    messageInput.style.height = 'auto';
    charCount.textContent = '0';
    sendButton.disabled = true;

    // Show typing indicator
    typingIndicator.style.display = 'flex';
    scrollToBottom();

    try {
        // Send to backend
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        // Hide typing indicator
        typingIndicator.style.display = 'none';

        // Add bot response
        if (data.response) {
            addMessage(data.response, 'bot');
        } else if (data.error) {
            addMessage(`Sorry, I encountered an error: ${data.error}`, 'bot');
        }

    } catch (error) {
        console.error('Error:', error);
        typingIndicator.style.display = 'none';
        addMessage('Sorry, I\'m having trouble connecting to the server. Please make sure the Python backend is running on http://localhost:5000', 'bot');
    }
}

// Add message to chat
function addMessage(text, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}`;

    const avatar = document.createElement('div');
    avatar.className = 'message-avatar';
    avatar.textContent = sender === 'user' ? '👤' : '🤖';

    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';

    const textDiv = document.createElement('div');
    textDiv.className = 'message-text';
    textDiv.textContent = text;

    const timeSpan = document.createElement('span');
    timeSpan.className = 'message-time';
    timeSpan.textContent = getCurrentTime();

    contentDiv.appendChild(textDiv);
    contentDiv.appendChild(timeSpan);

    messageDiv.appendChild(avatar);
    messageDiv.appendChild(contentDiv);

    chatMessages.appendChild(messageDiv);
    scrollToBottom();
}

// Get current time
function getCurrentTime() {
    const now = new Date();
    return now.toLocaleTimeString('en-US', {
        hour: 'numeric',
        minute: '2-digit',
        hour12: true
    });
}

// Scroll to bottom
function scrollToBottom() {
    setTimeout(() => {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }, 100);
}

// Focus input on load
window.addEventListener('load', () => {
    messageInput.focus();
});
