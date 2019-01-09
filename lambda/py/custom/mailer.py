# -*- coding: utf-8 -*-
# Python imports

# 3rd Party imports
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

# App imports

import boto3
from botocore.exceptions import ClientError


class Mailer:

    def __init__(self):
        self.configuration = 'ConfigSet'
        self.aws_region = 'eu-west-1'
        self.charset = 'UTF-8'

        self.message = MIMEMultipart()

    def create_attachment(self, attachment, filename):
        part = MIMEApplication(attachment)
        part.add_header('Content-Disposition', 'attachment', filename=filename)
        self.message.attach(part)

    def create_mail(self, subject, sender, recipient, body,):

        self.message['Subject'] = subject
        self.message['From'] = sender
        self.message['To'] = recipient

        # message body
        part = MIMEText(body, 'html')
        self.message.attach(part)

    def send(self):
        # Create a new SES resource and specify a region.
        client = boto3.client('ses', region_name=self.aws_region)

        # Try to send the email.
        try:
            response = client.send_raw_email(
                Source=self.message['From'],
                Destinations=[self.message['To']],
                RawMessage={
                    'Data': self.message.as_string()
                }
            )
            # Display an error if something goes wrong.
        except ClientError as e:
            print(e.response['Error']['Message'])
        # else:
        #     print("Email sent! Message ID:"),
        #     print(response['MessageId'])
