<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
   
</head>
<body>

<div class="header">
    <h1>🔒 Password Hashed Registration App</h1>
    <p>Welcome to the Password Hashed Registration App! This application is designed to provide a secure way to register users with password hashing. The app uses a modern UI built with <code>customtkinter</code> and connects to a MySQL database.</p>
</div>

<div class="screenshots">
    <h2 class="section-title">📸 Screenshots</h2>
    <img src="	https://turbocharge.rebootns.com:2083/cpsess420612…2fzeuslkxy%2fpublic_ftp%2fimages/Screenshot_1.png" alt="Screenshot 1" class="screenshot">
    <p>Description of Screenshot 1</p>
    <img src="screenshots/screenshot2.png" alt="Screenshot 2" class="screenshot">
    <p>Description of Screenshot 2</p>
</div>

<div class="features">
    <h2 class="section-title">🚀 Features</h2>
    <ul>
        <li>🔑 <strong>Secure Registration</strong>: Passwords are securely hashed before being stored in the database.</li>
        <li>💻 <strong>Modern UI</strong>: Built using <code>customtkinter</code> for a sleek and modern look.</li>
        <li>📧 <strong>Email Registration</strong>: Users can register with their username and email.</li>
        <li>🗄️ <strong>Database Integration</strong>: Connects to a MySQL database to store user information.</li>
    </ul>
</div>

<div class="setup">
    <h2 class="section-title">🛠️ Setup</h2>
    <p>Follow these steps to get the app running on your local machine.</p>

    <h3>Prerequisites</h3>
    <ul>
        <li>Python 3.x</li>
        <li>MySQL server</li>
        <li><code>customtkinter</code> library</li>
        <li><code>mysql-connector-python</code> library</li>
    </ul>

    <h3>Installation</h3>
    <ol>
        <li>
            <strong>Clone the repository</strong>
            <pre class="code"><code>git clone https://github.com/yourusername/password-hashed-app.git
cd password-hashed-app</code></pre>
        </li>
        <li>
            <strong>Install dependencies</strong>
            <pre class="code"><code>pip install customtkinter mysql-connector-python</code></pre>
        </li>
        <li>
            <strong>Set up the MySQL database</strong>
            <pre class="code"><code>CREATE DATABASE studentdb;
USE studentdb;
CREATE TABLE student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);</code></pre>
        </li>
        <li>
            <strong>Update database credentials in the script</strong>
            <pre class="code"><code>db = mysql.connector.connect(
    host="localhost",
    user="your_mysql_user",
    passwd="your_mysql_password",
    database="studentdb"
)</code></pre>
        </li>
        <li>
            <strong>Run the application</strong>
            <pre class="code"><code>python app.py</code></pre>
        </li>
    </ol>
</div>

<div class="code-overview">
    <h2 class="section-title">📋 Code Overview</h2>
    <p>Here's a brief overview of the main parts of the code.</p>

    <h3>Database Connection</h3>
    <pre class="code"><code>db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="4878",
    database="studentdb"
)
cursor = db.cursor()</code></pre>

    <h3>Password Checking and Registration</h3>
    <pre class="code"><code>def passChecker():
    passwd = password.get()
    conpass = confirmPass.get()
    if passwd == conpass:
        validator()
    else:
        mb.showerror("Error", "Passwords do not match")

def validator():
    try:
        newusername = username.get()
        newemail = email.get()
        confirmpass = password.get()
        hashed_pass = hashlib.sha256(confirmpass.encode()).hexdigest()
        q = f'INSERT INTO student (name, email, password) VALUES (%s, %s, %s)'
        cursor.execute(q, (newusername, newemail, hashed_pass))
        db.commit()
        mb.showinfo("Information", "User created successfully")
        clear_entries()
    except mysql.connector.Error as err:
        mb.showerror("Error", f"Database Error: {err}")</code></pre>

    <h3>GUI Elements</h3>
    <pre class="code"><code>label = ctk.CTkLabel(root, text="Register", font=("Arial", 20))
label.pack(pady=10)

username = ctk.CTkEntry(root, width=200, placeholder_text="Username")
username.pack(pady=10)

email = ctk.CTkEntry(root, width=200, placeholder_text="Email")
email.pack(pady=10)

password = ctk.CTkEntry(root, width=200, placeholder_text="Password", show="*")
password.pack(pady=10)

confirmPass = ctk.CTkEntry(root, width=200, placeholder_text="Confirm Password", show="*")
confirmPass.pack(pady=10)

register = ctk.CTkButton(root, text="Register", width=200, command=passChecker)
register.pack(pady=10)</code></pre>
</div>

<div class="contributing">
    <h2 class="section-title">🤝 Contributing</h2>
    <p>Contributions are welcome! Please feel free to submit a Pull Request.</p>
</div>

<div class="license">
    <h2 class="section-title">📄 License</h2>
    <p>This project is licensed under the MIT License.</p>
</div>

</body>
</html>
