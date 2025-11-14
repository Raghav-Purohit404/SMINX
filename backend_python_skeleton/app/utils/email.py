async def send_email(to: str, subject: str, body: str):
    # TODO: integrate with an email provider (SendGrid/Resend/Nodemailer equivalent)
    print(f"Sending email to {to}: {subject}")
