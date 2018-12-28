import boto3
from botocore.exceptions import ClientError


class Mailer:

    def __init__(self):
        self.configuration = 'ConfigSet'
        self.aws_region = 'eu-west-1'
        self.charset = 'UTF-8'

    def send(self, subject, sender, recipient, body, body_text):
        # Create a new SES resource and specify a region.
        client = boto3.client('ses', region_name=self.aws_region)

        # Try to send the email.
        try:
            # Provide the contents of the email.
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        recipient,
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': self.charset,
                            'Data': body,
                        },
                        'Text': {
                            'Charset': self.charset,
                            'Data': body_text,
                        },
                    },
                    'Subject': {
                        'Charset': self.charset,
                        'Data': subject,
                    },
                },
                Source=sender,
                # If you are not using a configuration set, comment or delete the
                # following line
                # ConfigurationSetName=self.configuration,
            )
        # Display an error if something goes wrong.
        except ClientError as e:
            print(e.response['Error']['Message'])
        # else:
        #     print("Email sent! Message ID:"),
        #     print(response['MessageId'])
