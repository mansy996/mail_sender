# Mail Sender Module
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-module">About The Module</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
  </ol>
</details>

<!-- ABOUT THE MODULE -->
## About The Module

Mail Sender Module is a python module that helps you send your emails perfectly.

it also supports send mails with attachments.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### How To Install

* using python pip
  ```sh
  pip install python-mail-sender
  ```
### How To Use

Just do the following steps:
* define `SENDER_ADDR` & `SENDER_PASS` & `SMTP_PORT` & `SMTP_SERVER` env variables
  * Using python:
    ```python
    import os
    os.environ["SENDER_ADDR"] = "sender_address"
    os.environ["SENDER_PASS"] = "sender_pass"
    os.environ["SMTP_PORT"]   = "smtp_port"
    os.environ["SMTP_SERVER"] = "smtp_server"
    ```
  * Or using the os terminal.
  * Or using the venv activate file:
    * depending on the os open the corresponding activate file
    * on windows `activate.bat`
      ```bat
      set SENDER_ADDR=sender_address
      set SENDER_PASS=sender_pass
      set SMTP_PORT=smtp_port
      set SMTP_SERVER=smtp_server
      ```
    * on non-windows  `activate.sh`
      ```sh
      export SENDER_ADDR=sender_address
      export SENDER_PASS=sender_pass
      export SMTP_PORT=smtp_port
      export SMTP_SERVER=smtp_server
      ```
* initialize an instance from the `MailSender` class
    ```python
    from mail_sender import MailSender
    mail_sender = MailSender()
    ```
* call the `send_mail` method and provide the mail attributes:
    Receiver Address | Subject | Email Content | attached files (`optional`)
    :------------ | :-------------| :-------------| :-------------|
    noreply@gmail.com | any subject |  content message | attached file list |
    ```python
    mail_sender.send_mail(
        receiver_address = "test@gmail.com", subject = "email subject",
        content = "message content", attach_files = (("filename.ext", file),)
    )
    ```

<p align="right">(<a href="#top">back to top</a>)</p>