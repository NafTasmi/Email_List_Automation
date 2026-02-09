# Email List Automation Script

A Python script that creates email addresses from names, saves them to a file, and sends them via email using Gmail's SMTP service.

## 📁 Repository: `email-list-automation`

## ✨ Features
- **File Creation**: Generates email addresses by appending "@gmail.com" to names
- **File Reading**: Reads email addresses from a text file
- **Email Sending**: Sends the list of emails via Gmail with user confirmation
- **User Interaction**: Prompts user before sending emails
- **Error Handling**: Includes try-catch blocks for email operations

## 📋 Prerequisites
- Python 3.x
- Gmail account with App Password enabled

## 🔧 Setup

### 1. Enable Gmail App Password
1. Enable **2-Factor Authentication** on your Google Account
2. Generate **App Password** at: https://myaccount.google.com/apppasswords
   - Select "Mail" → Choose device → Generate
   - Copy the 16-character password

### 2. Configure Script
Edit these variables in the script:
```python
sender_email = "your_email@gmail.com"          # Your Gmail address
sender_password = "your_app_password_here"     # Your 16-char App Password
receiver_email = "recipient@example.com"       # Who receives the email
```

### 3. Customize Name List
Edit the `lines` list to add your names:
```python
lines = [
    "John",
    "Jane",
    "Mike",
    "Sarah"
]
```

## 🚀 How It Works

### **Step 1: File Creation**
Creates `abc.txt` with email addresses:
```
John@gmail.com
Jane@gmail.com
Mike@gmail.com
Sarah@gmail.com
```

### **Step 2: File Reading**
Reads the created file and displays emails in console.

### **Step 3: Email Sending**
- Prompts user for confirmation
- Connects to Gmail SMTP server
- Sends email containing all addresses from the file
- Uses secure SSL connection (port 465)

## 📊 Sample Output
```
File 'abc.txt' created successfully!
Emails read from file:
John@gmail.com
Jane@gmail.com
Mike@gmail.com
Sarah@gmail.com

Do you want to send the email? (yes/no): yes
Email sent successfully!
```

## 📁 File Structure
```
email-list-automation/
├── email_script.py          # Main script
├── abc.txt                 # Generated email file
└── README.md              # This file
```

## ⚠️ Security Notes

### **CRITICAL: Protect Your Credentials**
```python
# ❌ UNSAFE (in production code):
sender_password = "your_app_password_here"

# ✅ SAFE Alternatives:
# Option 1: Environment variables
import os
sender_password = os.getenv("GMAIL_APP_PASSWORD")

# Option 2: User input
sender_password = input("Enter your app password: ")

# Option 3: .env file (using python-dotenv)
```

### **Before Committing to Git:**
1. Replace real email addresses with placeholders
2. Remove or replace actual passwords
3. Add sensitive files to `.gitignore`:
   ```
   *.txt
   .env
   ```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| `Authentication failed` | Verify App Password is correct |
| `File not found` | Script must be run from correct directory |
| `SMTP connection error` | Check firewall/internet connection |
| `Permission denied` | Ensure you can write to current directory |
| `SSL errors` | Try port 587 with `starttls()` instead |

## 🔄 Alternative: Port 587 (TLS)
If SSL doesn't work, modify the sending function:
```python
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()  # Upgrade to TLS
    server.login(sender_email, sender_password)
    server.send_message(message)
```

## 📝 Customization Options

### 1. Change Email Domain
```python
# Replace "@gmail.com" with any domain
file.write(line + "@company.com\n")
file.write(line + "@yahoo.com\n")
```

### 2. Add More Names Dynamically
```python
# Read names from user input
names = []
while True:
    name = input("Enter name (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    names.append(name)
```

### 3. Format Email Content
```python
# Customize email body
email_content = "Employee Email Directory:\n\n"
for index, email in enumerate(emails, 1):
    email_content += f"{index}. {email}"
```

## 📈 Use Cases
- Creating contact lists from name databases
- Sending email directories to HR departments
- Generating test email accounts
- Educational demonstrations of file I/O and email automation

## 🧪 Testing Tips
1. Test with your own email as receiver first
2. Send to a test inbox before production use
3. Check spam folder if email doesn't arrive
4. Verify file permissions in your directory

## 📄 License
For educational purposes only. Ensure compliance with:
- Gmail's Terms of Service
- Anti-spam regulations (CAN-SPAM Act)
- Data privacy laws (GDPR, CCPA)

## 🔍 Quick Start Checklist
- [ ] Enable 2FA on Google Account
- [ ] Generate App Password
- [ ] Update script with your credentials
- [ ] Modify name list as needed
- [ ] Run script in safe environment
- [ ] Verify email receipt

---

**⚠️ Reminder**: This script contains hardcoded credentials. Always use secure methods for handling passwords in production environments. Never commit sensitive information to version control systems.
