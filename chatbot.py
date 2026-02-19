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
    

    # History
    "who is the father of the nation of india": "Mahatma Gandhi is known as the Father of the Nation of India.",
    "who was the first prime minister of india": "Jawaharlal Nehru was the first Prime Minister of India.",
    "who was the first president of india": "Dr. Rajendra Prasad was the first President of India.",
    "when did india get independence": "India got independence in 1947.",
    "who discovered america": "Christopher Columbus discovered America in 1492.",
    "who was the first man on the moon": "Neil Armstrong was the first man to walk on the Moon.",

    # Geography
    "what is the capital of india": "The capital of India is New Delhi.",
    "what is the capital of france": "The capital of France is Paris.",
    "what is the largest ocean": "The Pacific Ocean is the largest ocean in the world.",
    "what is the longest river": "The Nile River is the longest river in the world.",
    "which is the largest continent": "Asia is the largest continent.",
    "which is the smallest continent": "Australia is the smallest continent.",

    # Science
    "what is the chemical formula of water": "The chemical formula of water is H2O.",
    "which planet is known as red planet": "Mars is known as the Red Planet.",
    "what gas do humans breathe": "Humans breathe oxygen.",
    "what is the powerhouse of the cell": "Mitochondria is the powerhouse of the cell.",
    "what is the boiling point of water": "The boiling point of water is 100 degrees Celsius.",
    "what is the speed of light": "The speed of light is approximately 299,792 kilometers per second.",

    # India GK
    "what is the national animal of india": "The national animal of India is the Tiger.",
    "what is the national bird of india": "The national bird of India is the Peacock.",
    "what is the national flower of india": "The national flower of India is the Lotus.",
    "what is the national anthem of india": "The national anthem of India is Jana Gana Mana.",
    "what is the national sport of india": "Hockey is considered the national sport of India.",

    # Sports
    "how many players are there in a cricket team": "There are 11 players in a cricket team.",
    "who is known as the god of cricket": "Sachin Tendulkar is known as the God of Cricket.",
    "which country won 2011 cricket world cup": "India won the 2011 Cricket World Cup.",

    # Computer & Technology
    "what does cpu stand for": "CPU stands for Central Processing Unit.",
    "what does ram stand for": "RAM stands for Random Access Memory.",
    "what does www stand for": "WWW stands for World Wide Web.",
    "what does html stand for": "HTML stands for HyperText Markup Language.",
    "what does ai stand for": "AI stands for Artificial Intelligence.",

    # Mixed GK
    "what is the largest animal in the world": "The Blue Whale is the largest animal in the world.",
    "how many continents are there": "There are 7 continents in the world.",
    "how many days are there in leap year": "There are 366 days in a leap year.",
    "what is the currency of japan": "The currency of Japan is Yen.",
    "who wrote ramayana": "The Ramayana was written by Valmiki.",

    # 🌍 Geography
    "what is the capital of india" : "New Delhi",
"what is the capital of france": "Paris",
"what is the capital of japan": "Tokyo",
"what is the largest continent": "Asia",
"which is the longest river in the world": "Nile River",
"which is the highest mountain in the world": "Mount Everest",
"which ocean is the largest": "Pacific Ocean",
"which desert is the largest": "Sahara Desert",
"what is the capital of karnataka": "Bengaluru",
"which country has the largest population": "India",

# 🏛 History
"who is the father of nation india": "Mahatma Gandhi",
"who invented the telephone": "Alexander Graham Bell",
"who discovered india": "Vasco da Gama",
"who was the first prime minister of india": "Jawaharlal Nehru",
"who was the first president of india": "Dr. Rajendra Prasad",
"when did india get independence": "15 August 1947",
"who was the first man on the moon": "Neil Armstrong",
"which war ended in 1945": "World War II",
"who built the taj mahal": "Shah Jahan",
"who was known as iron man of india": "Sardar Vallabhbhai Patel",

# 🔬 Science
"what is h2o": "Water",
"what planet is known as red planet": "Mars",
"which gas do plants absorb": "Carbon Dioxide",
"which organ pumps blood": "Heart",
"what is the boiling point of water": "100 degree Celsius",
"which is the nearest star to earth": "Sun",
"what is the chemical symbol of gold": "Au",
"who discovered gravity": "Isaac Newton",
"which vitamin do we get from sunlight": "Vitamin D",
"what is the hardest natural substance": "Diamond",

# 💻 Computer
"who is father of computer": "Charles Babbage",
"what does cpu stand for": "Central Processing Unit",
"what does ram stand for": "Random Access Memory",
"what is html": "HyperText Markup Language",
"what is css": "Cascading Style Sheets",
"what is python": "A programming language",
"what is the brain of computer": "CPU",
"what does ip stand for": "Internet Protocol",
"what is full form of http": "HyperText Transfer Protocol",
"which key is used to refresh page": "F5",

# 🏏 Sports
"who is known as god of cricket": "Sachin Tendulkar",
"which country won world cup 2011": "India",
"how many players in football team": "11",
"how many players in cricket team": "11",
"which sport uses racket": "Tennis",
"where were olympics 2021 held": "Tokyo",
"which country hosts ipl": "India",
"who is ms dhoni": "Former Indian Cricket Captain",
"which sport is called king of sports": "Football",
"how many rings in olympic flag": "5",

# 📚 Literature
"who wrote ramayana": "Valmiki",
"who wrote mahabharata": "Vyasa",
"who wrote romeo and juliet": "William Shakespeare",
"who wrote harry potter": "J K Rowling",
"who wrote geetanjali": "Rabindranath Tagore",
"which is national song of india": "Vande Mataram",
"which is national anthem of india": "Jana Gana Mana",
"who is known as nightingale of india": "Sarojini Naidu",
"who wrote discovery of india": "Jawaharlal Nehru",
"who wrote wings of fire": "A P J Abdul Kalam",

# 🎬 Entertainment
"who is called king of bollywood": "Shah Rukh Khan",
"who is called megastar of bollywood": "Amitabh Bachchan",
"who directed bahubali": "S S Rajamouli",
"who played iron man": "Robert Downey Jr",
"which movie won oscar in 2023": "Everything Everywhere All at Once",
"who is known as thala": "Ajith Kumar",
"who is known as superstar of kollywood": "Rajinikanth",
"which is highest grossing indian movie": "Dangal",
"who composed national anthem of india": "Rabindranath Tagore",
"who sang kesariya song": "Arijit Singh",

# 🧠 General
"how many states in india": "28",
"how many union territories in india": "8",
"which is smallest state in india": "Goa",
"which is largest state in india": "Rajasthan",
"currency of india": "Indian Rupee",
"currency of usa": "US Dollar",
"which day is celebrated as republic day": "26 January",
"which day is celebrated as independence day": "15 August",
"who is current prime minister of india": "Narendra Modi",
"who is current president of india": "Droupadi Murmu",

# ➕ Extra
"how many bones in human body": "206",
"how many days in a year": "365",
"how many colors in rainbow": "7",
"which animal is known as king of jungle": "Lion",
"which bird is national bird of india": "Peacock",
"which flower is national flower of india": "Lotus",
"which animal is national animal of india": "Tiger",
"which fruit is national fruit of india": "Mango",
"which tree is national tree of india": "Banyan Tree",
"which game is national game of india": "Hockey",
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
