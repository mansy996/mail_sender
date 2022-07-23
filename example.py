from mail_sender import MailSender
import io, os

os.environ["SENDER_ADDR"] = "test@test.com"
os.environ["SENDER_PASS"] = "P@$$w0rd"
os.environ["SMTP_PORT"] = "587"
os.environ["SMTP_SERVER"] = "smtp.google.com"

def main():
    file_1 = io.BytesIO(b"mail sender test file 1")
    file_2 = io.StringIO("mail sender test file 2")

    mail_sender = MailSender()
    sent, msg = mail_sender.send_mail(
        receiver_address = "ahmedmansy1996@gmail.com", subject = "test subject",
        content = "message content", attach_files = (("file_1.txt", file_1), ("file_2.txt", file_2))
    )
    print(sent, msg)

if __name__ == "__main__":
    main()