class Notification:
    def send(self):
        print("Sending a generic notification.")

class EmailNotification(Notification):
    def send(self):
        print("Sending an Email notification.")

class SMSNotification(Notification):
    def send(self):
        print("Sending an SMS notification.")

notifications = [Notification(), EmailNotification(), SMSNotification()]

for notif in notifications:
    notif.send()