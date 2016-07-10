import smtplib


def send_mails(emails, schedule, forecast):
    # Connect to the smtp server
    server = smtplib.SMTP('smtp.gmail.com', '587')

    # start TLS encryption
    server.starttls()

    # login
    from_email = '**************'
    server.login(from_email, "***********")

    # send mail to everyone
    for to_email, name in emails.items():
        message = "Subject:Anurag invites you to Wonderla\n"
        message += "Hi " + name + "!\n\n"
        message += "Anurag has specially invited you for this wonderful event \n\n"
        message += forecast + '\n'
        message += schedule + '\n'
        message += "Please come with your families as he loves you all so much\n"
        server.sendmail(from_email, to_email, message)

    server.quit()
