import importlib
import sys

try:
  st = importlib.import_module("streamlit")
except ImportError:
  sys.stderr.write("Streamlit is not installed. Please install it with `pip install streamlit`.\n")
  sys.exit(1)

st.set_page_config(page_title="My First Streamlit App")

# Set page title
st.title("My First Streamlit App")

# Add header
st.header("Welcome to the dashboard")

# Add text
st.write("This is a simple demonstration of Streamlit capabilities")

## Creating a Simple Streamlit Chatbot
def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def main():
    st.title("Simple Chatbot")
    
    initialize_session_state()

    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Chat input
    if prompt := st.chat_input("What's on your mind?"):
        # Display user message
        with st.chat_message("user"):
            st.write(prompt)
        
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Add simple bot response
        response = f"You said: {prompt}"
        
        # Display bot message
        with st.chat_message("assistant"):
            st.write(response)
        
        # Add bot message to history
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import random
import threading
import time

try:
    notification = importlib.import_module("plyer.notification")
except ImportError:
    notification = None

# =========================
# LOAD & SAVE ASSIGNMENTS
# =========================

FILE_NAME = "assignments.json"

def load_assignments():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

def save_assignments():
    with open(FILE_NAME, "w") as file:
        json.dump(assignments, file)

assignments = load_assignments()

# =========================
# QUIZ QUESTIONS
# =========================

quiz_questions = [
    {
        "question": "What is 5 + 3?",
        "answer": "8"
    },
    {
        "question": "What color is the sky?",
        "answer": "blue"
    },
    {
        "question": "What is Python mainly used for?",
        "answer": "programming"
    }
]

# =========================
# MAIN WINDOW
# =========================

root = tk.Tk()
root.title("🎓 Smart Assignment Reminder")
root.geometry("500x500")
root.config(bg="#1e1e2f")

title = tk.Label(
    root,
    text="📚 Assignment Reminder App",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#1e1e2f"
)
title.pack(pady=10)

# =========================
# LISTBOX
# =========================

listbox = tk.Listbox(
    root,
    width=50,
    height=10,
    font=("Arial", 12),
    bg="#2d2d44",
    fg="white",
    selectbackground="#ff66c4"
)
listbox.pack(pady=20)

# =========================
# FUNCTIONS
# =========================

def refresh_list():
    listbox.delete(0, tk.END)
    for task in assignments:
        listbox.insert(tk.END, "📝 " + task)

def add_assignment():
    task = simpledialog.askstring(
        "New Assignment",
        "Enter assignment:"
    )

    if task:
        assignments.append(task)
        save_assignments()
        refresh_list()

def complete_assignment():
    selected = listbox.curselection()

    if selected:
        index = selected[0]
        assignments.pop(index)
        save_assignments()
        refresh_list()

# =========================
# QUIZ PUNISHMENT
# =========================

def punishment_quiz():
    q = random.choice(quiz_questions)

    answer = simpledialog.askstring(
        "🧠 Punishment Quiz",
        q["question"]
    )

    if answer and answer.lower() == q["answer"]:
        messagebox.showinfo(
            "Correct!",
            "You may snooze the reminder 😎"
        )
        return True
    else:
        messagebox.showerror(
            "Wrong!",
            "No snooze for you 😈"
        )
        return False

# =========================
# REMINDER POPUP
# =========================

def show_reminder():
    if assignments:

        notification.notify(
            title="📌 Unfinished Assignments!",
            message=f"You still have {len(assignments)} unfinished tasks!",
            timeout=5
        )

        popup = tk.Toplevel(root)
        popup.title("⚠ Reminder")
        popup.geometry("350x250")
        popup.config(bg="#29293d")

        label = tk.Label(
            popup,
            text="🔥 Finish your assignments!",
            font=("Arial", 16, "bold"),
            fg="white",
            bg="#29293d"
        )
        label.pack(pady=20)

        task_label = tk.Label(
            popup,
            text="\n".join(assignments[:3]),
            fg="yellow",
            bg="#29293d",
            font=("Arial", 12)
        )
        task_label.pack()

        def remind_later():
            passed = punishment_quiz()

            if passed:
                popup.destroy()

        remind_btn = tk.Button(
            popup,
            text="⏰ Remind Me Later",
            command=remind_later,
            bg="#ff4d6d",
            fg="white",
            font=("Arial", 12, "bold")
        )
        remind_btn.pack(pady=10)

        done_btn = tk.Button(
            popup,
            text="✅ I'll Do It Now",
            command=popup.destroy,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12, "bold")
        )
        done_btn.pack()

# =========================
# AUTO REMINDER THREAD
# =========================

def reminder_loop():
    while True:
        time.sleep(30)  # reminder every 30 sec
        root.after(0, show_reminder)

threading.Thread(target=reminder_loop, daemon=True).start()

# =========================
# BUTTONS
# =========================

add_btn = tk.Button(
    root,
    text="➕ Add Assignment",
    command=add_assignment,
    bg="#6a5acd",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20
)
add_btn.pack(pady=5)

complete_btn = tk.Button(
    root,
    text="✅ Complete Assignment",
    command=complete_assignment,
    bg="#20b2aa",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20
)
complete_btn.pack(pady=5)

# Decorations
footer = tk.Label(
    root,
    text="✨ Stay productive and beat procrastination! ✨",
    fg="#ffcc00",
    bg="#1e1e2f",
    font=("Comic Sans MS", 10, "bold")
)
footer.pack(side="bottom", pady=15)

refresh_list()

root.mainloop()

# Sample DataFrame
df = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'January'],
    'Price': [1000, 1500, 2000, 1200]
})

# Add sidebar
st.sidebar.header("Filters")

# Add dropdown
selected_month = st.sidebar.selectbox(
    "Select Month",
    options=df['Month'].unique()
)

# Add slider
price_range = st.sidebar.slider(
    "Select Price Range",
    min_value=0,
    max_value=3000,
    value=(0, 3000)
)