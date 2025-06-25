import smtplib, os
from email.message import EmailMessage

def send_email(to_list, attachment_path):
    msg = EmailMessage()
    msg['Subject'] = "TNA Report"
    msg['From'] = os.getenv("SMTP_USER")
    msg['To'] = ", ".join(to_list)
    msg.set_content("Find attached your TNA report.")

    with open(attachment_path, 'rb') as f:
        msg.add_attachment(f.read(), maintype='application', subtype='octet-stream', filename='TNA_Report.docx')

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASS"))
        smtp.send_message(msg)
