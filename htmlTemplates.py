css = '''
<style>
    /* Общий фон страницы */
    .stApp {
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
    }

    /* Заголовок */
    h1, h2, h3 {
        color: #f1f5f9 !important;
    }

    /* Контейнер под поле ввода вопроса */
    .stTextInput > div > div > input {
        background-color: #1e293b;
        color: #f1f5f9;
        border: 1px solid #334155;
        border-radius: 10px;
    }

    /* Сайдбар */
    section[data-testid="stSidebar"] {
        background-color: #0f172a;
        border-right: 1px solid #334155;
    }

    /* Блок одного сообщения в диалоге */
    .chat-message {
        display: flex;
        align-items: flex-start;
        padding: 1rem 1.25rem;
        border-radius: 14px;
        margin-bottom: 0.9rem;
        gap: 0.9rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.25);
    }

    .chat-message.user {
        background: #2563eb;
        flex-direction: row-reverse;
        text-align: right;
    }

    .chat-message.bot {
        background: #1e293b;
        border: 1px solid #334155;
    }

    .chat-message .avatar {
        flex-shrink: 0;
        width: 42px;
        height: 42px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.3rem;
        background: rgba(255, 255, 255, 0.15);
    }

    .chat-message .message {
        color: #f1f5f9;
        font-size: 0.98rem;
        line-height: 1.5;
        white-space: pre-wrap;
        word-wrap: break-word;
    }
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">🤖</div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">🧑</div>
    <div class="message">{{MSG}}</div>
</div>
'''
