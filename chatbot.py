import os

USER_FILE = "users.txt"


responses = {
    "hello": "Hi there! 👋",
    "hi": "Hello! 😊",
    "how are you": "I'm doing great!",
    "what is your name": "I'm a Python chatbot.",
    "who created you": "I was created using Python.",
    "what is python": "Python is a programming language.",
    "what is java": "Java is an object-oriented programming language.",
    "what is html": "HTML is used to structure web pages.",
    "what is css": "CSS is used to style web pages.",
    "what is javascript": "JavaScript makes web pages interactive.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is machine learning": "Machine learning is a subset of AI.",
    "what is data science": "Data science analyzes data for insights.",
    "what is github": "GitHub is a platform for version control.",
    "what is sql": "SQL is used to manage databases.",
    "what is dbms": "DBMS manages databases efficiently.",
    "what is oop": "OOP stands for Object-Oriented Programming.",
    "what is loop": "A loop repeats a block of code.",
    "what is function": "A function is reusable block of code.",
    "what is variable": "A variable stores data.",
    "what is list": "A list stores multiple values.",
    "what is dictionary": "A dictionary stores key-value pairs.",
    "what is tuple": "A tuple is immutable collection.",
    "what is set": "A set stores unique values.",
    "what is file handling": "File handling reads/writes files.",
    "what is automation": "Automation performs tasks automatically.",
    "what is chatbot": "A chatbot interacts with users automatically.",
    "what is api": "API allows communication between software.",
    "what is cloud": "Cloud provides online computing services.",
    "what is cybersecurity": "Cybersecurity protects systems from attacks.",
    "what is internet": "Internet connects computers globally.",
    "what is computer": "A computer processes data.",
    "what is software": "Software is a program.",
    "what is hardware": "Hardware is physical parts of computer.",
    "what is operating system": "OS manages computer resources.",
    "what is windows": "Windows is an operating system.",
    "what is linux": "Linux is an open-source OS.",
    "what is mac": "MacOS is Apple's OS.",
    "what is coding": "Coding means writing instructions for computer.",
    "what is debugging": "Debugging fixes errors in code.",
    "what is error": "An error is a mistake in program.",
    "what is compiler": "Compiler converts code to machine language.",
    "what is interpreter": "Interpreter executes code line by line.",
    "what is frontend": "Frontend is user interface.",
    "what is backend": "Backend handles server logic.",
    "what is full stack": "Full stack includes frontend and backend.",
    "what is react": "React is a JavaScript library.",
    "what is node": "Node.js runs JavaScript on server.",
    "what is django": "Django is Python web framework.",
    "what is flask": "Flask is lightweight Python framework.",
    "what is bootstrap": "Bootstrap is CSS framework.",
    "what is api testing": "API testing checks APIs.",
    "what is json": "JSON stores data format.",
    "what is xml": "XML stores structured data.",
    "what is firebase": "Firebase is backend service.",
    "what is mongodb": "MongoDB is NoSQL database.",
    "what is mysql": "MySQL is relational database.",
    "what is postman": "Postman tests APIs.",
    "what is vscode": "VS Code is code editor.",
    "what is git": "Git is version control system.",
    "what is agile": "Agile is development methodology.",
    "what is scrum": "Scrum is agile framework.",
    "what is testing": "Testing checks program correctness.",
    "what is unit testing": "Unit testing tests small parts.",
    "what is integration testing": "Integration testing tests modules together.",
    "what is devops": "DevOps combines development and operations.",
    "what is docker": "Docker containerizes applications.",
    "what is virtualization": "Virtualization creates virtual machines.",
    "what is networking": "Networking connects devices.",
    "what is ip address": "IP identifies device on network.",
    "what is http": "HTTP transfers web data.",
    "what is https": "HTTPS is secure HTTP.",
    "what is domain": "Domain is website name.",
    "what is hosting": "Hosting stores website online.",
    "what is seo": "SEO improves website ranking.",
    "what is encryption": "Encryption secures data.",
    "what is decryption": "Decryption unlocks data.",
    "what is algorithm": "Algorithm solves problem step-by-step.",
    "what is recursion": "Recursion is function calling itself.",
    "what is stack": "Stack is LIFO structure.",
    "what is queue": "Queue is FIFO structure.",
    "what is array": "Array stores similar elements.",
    "what is binary tree": "Binary tree has two children nodes.",
    "what is graph": "Graph connects nodes.",
    "what is blockchain": "Blockchain is distributed ledger.",
    "what is iot": "IoT connects smart devices.",
    "what is big data": "Big data handles huge datasets.",
    "what is ar": "AR means Augmented Reality.",
    "what is vr": "VR means Virtual Reality.",
    "what is raspberry pi": "Raspberry Pi is mini computer.",
    "what is microcontroller": "Microcontroller controls hardware.",
    "what is android": "Android is mobile OS.",
    "what is ios": "iOS is Apple's mobile OS.",
    "bye": "Goodbye! 👋"
}
# -----------------------------
# Utility Functions
# -----------------------------

def register():
    print("\n📝 --- User Registration ---")
    username = input("Enter new username: ")
    password = input("Enter new password: ")

    with open(USER_FILE, "a") as file:
        file.write(username + "," + password + "\n")

    print("✅ Registration successful! You can now login.\n")


def login():
    print("\n🔐 --- User Login ---")

    if not os.path.exists(USER_FILE):
        print("❌ No users registered yet. Please register first.\n")
        return None

    attempts = 3

    while attempts > 0:
        username = input("Username: ")
        password = input("Password: ")

        with open(USER_FILE, "r") as file:
            users = file.readlines()

        for user in users:
            stored_username, stored_password = user.strip().split(",")

            if username == stored_username and password == stored_password:
                print("✅ Login successful!\n")
                return username

        attempts -= 1
        print(f"❌ Invalid credentials! Attempts left: {attempts}")

    print("🚫 Too many failed attempts.\n")
    return None


# -----------------------------
# Chatbot Logic
# -----------------------------

def get_response(user_input):
    if user_input in ["hello", "hi"]:
        return "Hi there! 👋"
    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking 😊"
    elif "your name" in user_input:
        return "I'm your secure Python chatbot."
    elif user_input == "bye":
        return "Goodbye! Logging you out..."
    else:
        return "Sorry, I don't understand that."

def chatbot():
    print("🤖 Chatbot Ready! Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input in responses:
            print("Bot:", responses[user_input])
        else:
            print("Bot: Sorry, I don't know that yet.")

        if user_input == "bye":
            break

# -----------------------------
# Main Program
# -----------------------------

def main():
    while True:
        print("===== Chatbot System =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            register()

        elif choice == "2":
            user = login()
            if user:
                chatbot(user)

        elif choice == "3":
            print("👋 Exiting program...")
            break

        else:
            print("❌ Invalid choice!\n")


chatbot()
