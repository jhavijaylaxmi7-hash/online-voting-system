from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import random

app = Flask(__name__)
CORS(app)

# DB connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="voting_db"
)
cursor = db.cursor()

# 🔹 SEND OTP
@app.route('/send_otp', methods=['POST'])
def send_otp():
    data = request.get_json()
    email = data['email']
    otp = str(random.randint(1000, 9999))

    cursor.execute("INSERT INTO users (email, otp) VALUES (%s, %s)", (email, otp))
    db.commit()

    return jsonify({"otp": otp})

# 🔹 VERIFY OTP
@app.route('/verify_otp', methods=['POST'])
def verify_otp():
    data = request.get_json()
    email = data['email']
    otp = data['otp']

    cursor.execute("SELECT * FROM users WHERE email=%s AND otp=%s", (email, otp))
    user = cursor.fetchone()

    if user:
        cursor.execute("UPDATE users SET is_verified=TRUE WHERE email=%s", (email,))
        db.commit()
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "Invalid OTP"}), 400

# 🔹 VOTE
@app.route('/vote', methods=['POST'])
def vote():
    try:
        data = request.get_json()
        print(data)  # debug ke liye
        return {"message": "vote submitted successfully"}
    except Exception as e:
        print(e)
        return {"error": str(e)}, 500
    email = data['email']
    candidate = data['candidate']

    # check already voted
    cursor.execute("SELECT * FROM votes WHERE email=%s", (email,))
    if cursor.fetchone():
        return jsonify({"message": "You have already voted"}), 400

    cursor.execute("INSERT INTO votes (email, candidate) VALUES (%s, %s)", (email, candidate))
    db.commit()

    return jsonify({"message": "Vote submitted successfully"})

# 🔹 RESULTS
@app.route('/results', methods=['GET'])
def results():
    cursor.execute("""
        SELECT candidate, COUNT(*) 
        FROM votes 
        GROUP BY candidate
    """)
    data = cursor.fetchall()

    # 🔥 default values (important)
    result = {
        "Candidate A": 0,
        "Candidate B": 0,
        "Candidate C": 0
    }

    for row in data:
        result[row[0]] = row[1]

    return jsonify(result)

    # ADMIN LOGIN
@app.route('/admin_login', methods=['POST'])
def admin_login():
    data = request.get_json()
    password = data['password']

    if password == "admin123":
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "Wrong password"}), 401


# RESET VOTES
@app.route('/reset_votes', methods=['POST'])
def reset_votes():
    cursor.execute("DELETE FROM votes")
    db.commit()
    return jsonify({"message": "All votes cleared"})

if __name__ == '__main__':
    app.run(debug=True)
    