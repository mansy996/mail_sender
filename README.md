# Mail Sender Module
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-Module">About The Module</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
  </ol>
</details>

<!-- ABOUT THE MODULE -->
## About The Module

Mail Sender Module is python module that helps you send your emails perfectly.

This module is built with Python >= 3.7

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get started with this module just clone it into your repo then do the following:
* define `SENDER_ADDR` & `SENDER_PASS` & `SMTP_PORT` & `SMTP_SERVER` env variables
* import the `MailSendera` class as follows
    ```python
    from mail_sender import MailSendera
    ```
* initialize an instance from the `MailSendera` class
    ```python
    import os
    sender_address = os.environ.get("SENDER_ADDR")
    sender_pass = os.environ.get("SENDER_PASS")
    smtp_port = os.environ.get("SMTP_PORT")
    smtp_server = os.environ.get("SMTP_SERVER")
    mail_sender = MailSendera()
    ```
* call the `send_mail` method and provide the mail attributes:
    Receiver Address | Subject | Email Content | attached files
    :------------ | :-------------| :-------------| :-------------|
    noreply@gmail.com | any subject |  content message | attached file list |
    ```python
    mail_sender.send_mail(
        receiver_address = "test@gmail.com", subject = "email subject",
        content = "message content", attach_files = (("filename.ext", file),)
    )
    ```

<p align="right">(<a href="#top">back to top</a>)</p>