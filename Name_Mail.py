import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Step 1: Create the file with @gmail.com added to each line
lines = [
    "Abu",
    "Babu",
    "Koli",
    "Mamun"
]

with open("abc.txt", "w") as file:
    for line in lines:
        file.write(line + "@gmail.com\n")

print("File 'abc.txt' created successfully!")

# Step 2: Open and read the file line by line
with open("abc.txt", "r") as file:
    emails = file.readlines()

print("Emails read from file:")
for email in emails:
    print(email.strip())

# Step 3: Send email through Python
def send_email():
    # Email configuration - YOU NEED TO FILL THESE!
    sender_email = "nafisatasmiya@gmail.com"  # Replace with your email
    sender_password = "ilrh rtxm wpvm qwsf"  # Replace with your app password
    receiver_email = "tasmiyanafisa12@gmail.com"  # Replace with recipient email
    
    # Create message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "List of emails from abc.txt"
    
    # Create email content
    email_content = "Here are the emails from abc.txt:\n\n"
    for email in emails:
        email_content += email
    
    message.attach(MIMEText(email_content, "plain"))
    
    try:
        # Connect to Gmail's SMTP server
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(message)
        
        print("\nEmail sent successfully!")
        
    except Exception as e:
        print(f"\nError sending email: {e}")

# Ask user if they want to send email
response = input("\nDo you want to send the email? (yes/no): ").lower()
if response == "yes":
    send_email()
else:
    print("Email not sent.")