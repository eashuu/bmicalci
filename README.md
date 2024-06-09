<!DOCTYPE html>
<html>

<h>BMI Calculator</h1>

<body>

<h1>Project Overview</h1>
<p>This project is a BMI (Body Mass Index) calculator web application built using Streamlit and MySQL. It allows users to calculate their BMI and receive personalized advice based on their BMI category. The application also includes user authentication features to securely manage user accounts.</p>

  <h1>Description</h1>
    <p>The BMI calculator application provides a user-friendly interface for users to input their weight, height, and diabetes status. Based on this information, the application calculates the user's BMI and provides personalized advice and recommendations for diet and exercise.</p>

  <h1>Folder Structure</h1>
    <pre>
    bmi/
    ├── requirements.txt
    ├── app.py
    ├── config/
    │   └── config.py
    └── database/
        ├── __init__.py
        └── db_utils.py
    </pre>

   <h1>Packages and Modules</h1>
    <p>The project uses the following packages and modules:</p>
    <ul>
        <li><strong>Streamlit:</strong> Used for building the web application interface.</li>
        <li><strong>MySQL Connector/Python:</strong> Used for connecting to and interacting with the MySQL database.</li>
        <li><strong>bcrypt:</strong> Used for securely hashing and verifying user passwords.</li>
    </ul>

  <h1>Requirements</h1>
    <p>To run this project, you need to have Python installed on your system. Additionally, you'll need to install the dependencies listed in the <code>requirements.txt</code> file.</p>

  <h1>Database Schema</h1>
    <p>The project uses a MySQL database with the following schema and make sure to run this by creating a new db bmi</p>
    <pre>
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
    </pre>

  <h1>Configuration</h1>
    <p>Update the <code>config.py</code> file in the <code>config/</code> directory with the following database connection details:</p>
    <pre>
DB_CONFIG = {
    'host': 'localhost',
    'user': 'myapp_user',
    'password': 'secure_password',
    'database': 'myapp_db'
}
    </pre>

  <h1>Installation</h1>
    <ol>
        <li>Clone the repository:</li>
        <pre><code>git clone https://github.com/yourusername/bmi.git</code></pre>
        <li>Navigate to the project directory:</li>
        <pre><code>cd bmi</code></pre>
        <li>Install the dependencies:</li>
        <pre><code>pip install -r requirements.txt</code></pre>
    </ol>

  <h1>How to Run</h1>
    <p>To run the BMI calculator application:</p>
    <ol>
        <li>Ensure you're in the project directory.</li>
        <li>Run the following command:</li>
        <pre><code>streamlit run app.py</code></pre>
        <li>Open your web browser and navigate to the URL provided by Streamlit to access the application.</li>
    </ol>

  <hr>
    <p align="center">Made with ❤️‍🔥 by eashuu</p>

</body>

</html>
