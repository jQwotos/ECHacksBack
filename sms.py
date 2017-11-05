from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC83a5ddf364deb5ad803e8f5733e29243"
# Your Auth Token from twilio.com/console
auth_token  = "xxxxxxxxxxxxxxxxxxx"

#"bfeaf2637aeff6f8d8a65a6622e57fc9"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16478813051",
    from_="+16479526242",
    body="Hello from Python!")

print(message.sid)
