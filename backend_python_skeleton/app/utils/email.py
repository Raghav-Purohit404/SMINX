# app/utils/email.py
import os
import asyncio

async def send_email(to: str, subject: str, body: str):
    """
    Lightweight async email helper.
    Currently prints to stdout for development.
    To integrate with SendGrid/Resend/SMTP:
      - detect provider via env var (EMAIL_PROVIDER)
      - implement provider-specific code here
    """
    provider = os.getenv("EMAIL_PROVIDER", "").lower()
    # dev fallback: just print
    if not provider:
        print(f"[EMAIL DEV] To: {to}\nSubject: {subject}\n\n{body}\n")
        # emulate async work
        await asyncio.sleep(0)
        return True

    # Example hook for future integration:
    # if provider == "sendgrid":
    #    # use sendgrid library to send
    #    ...
    # elif provider == "smtp":
    #    # use aiosmtplib or smtplib
    #    ...
    # For now we fall back to printing
    print(f"[EMAIL-{provider}] To: {to} | Subject: {subject}")
    await asyncio.sleep(0)
    return True

