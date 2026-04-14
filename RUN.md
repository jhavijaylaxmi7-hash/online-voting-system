# Online Voting System - Setup और Run करने के लिए

## Step 1: Database Setup
```sql
-- MySQL में यह SQL चलाएं:
CREATE DATABASE voting_db;
USE voting_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100),
    otp VARCHAR(10),
    is_verified BOOLEAN DEFAULT FALSE
);

CREATE TABLE votes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100),
    candidate VARCHAR(50)
);
```

या `database.sql` file को import करें:
```bash
mysql -u root -p1234 < database.sql
```

## Step 2: Python Dependencies Install करें
```bash
pip install -r requirements.txt
```

## Step 3: Flask App Run करें
```bash
python app.py
```

या

```bash
flask run
```

## API Endpoints:

### 1. OTP भेजें
```
POST /send_otp
{
    "email": "user@example.com"
}
```

### 2. OTP Verify करें
```
POST /verify_otp
{
    "email": "user@example.com",
    "otp": "1234"
}
```

### 3. Vote करें
```
POST /vote
{
    "email": "user@example.com",
    "candidate": "candidate_name"
}
```

## Requirements:
- Python 3.7+
- MySQL Server running on localhost
- MySQL credentials: user=root, password=1234
