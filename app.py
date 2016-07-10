import weatherDetails
import sendMails


def get_emails():

    emails = {}
    try:
        email_list = open('resources/emailIds', 'r')

        for line in email_list:
            (email, name) = line.split(',')
            emails[email] = name.strip()

    except IOError as err:
        print(err)

    return emails

def get_schedule():

    schedule = '';
    try:
        schedule_file = open('resources/funSchedule', 'r')

        schedule = schedule_file.read()
    except IOError as err:
        print(err)

    return schedule


def main():
    emails = get_emails()
    schedule = get_schedule()
    forecast = weatherDetails.get_forecast()
    sendMails.send_mails(emails, schedule, forecast)

main()