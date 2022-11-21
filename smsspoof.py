# /usr/bin/python3

import requests

# Contacts list to use for easy number input (optional)
contacts = {
    # Format:
    # 'Contact Name' : 441234567890
    # Where 44 is the country code without the + ^^^^
    'Test' : 441234567890
    }


# Request for the sender and receiver name / number
sender = input("Enter Sender CID: \t")
receiver = input("Enter Receiver CID: \t")
message = input("Enter Message: \t")
# Either dspoof or smsroute
service = input("Choose Service: \t")

# https://dspoof.com to sign up. BTC payments only.
if service == "dspoof":
    print("dSpoof Selected")

    api_key = "<<ENTER API KEY>>" # Enter API key for https://dspoof.com !
    username = "<<ENTER USERNAME>>" # Enter username for https://dspoof.com !

    # Checks if name put in sender / receiver is in the 'contacts' list and replaces name with phone number
    if any(sender in sublist for sublist in contacts):
        sender = contacts.__getitem__(sender)
        # Prints out the value before confirming
        print(sender)
    else:
        print("Defaulting to PLAIN number")
        print("\n" + sender)

    # Checks if name put in sender / receiver is in the 'contacts' list and replaces name with phone number 
    if any(receiver in sublist for sublist in contacts):
        receiver = contacts.__getitem__(receiver)
        # Prints out the value before confirming
        print(receiver)
    else:
        print("Defaulting to plain number")
        print("\n" + receiver)
    # dspoof dows not allow over 160 characters for one message.
    if len(message) >= 160:
        print("Your message is too long")
        exit()

    # Joins it into a HTTP request to be sent with URL encoded message
    spoofurl = f'https://dspoof.com/api/?user={username}&key={api_key}&from={sender}&to={receiver}&msg={message}'
    print(spoofurl)
    confirm = input("Press ENTER to send message!\t")

    # Confirms message
    if confirm == "":
        print("Sent!")
        r = requests.get(spoofurl)
    else:
        exit()

    # Prints response
    print(r.text)

# SMSRoute -> https://beta.smsroute.to Option 2 (More reliable) (Higher minimum top up)
elif service == "smsroute":
    print("SMSRoute Selected!")

    # Enter account username and password
    username = "<< Username >>" # Enter Username
    password = "<< Password >>" # Enter Password

    # Checks if name put in sender / receiver is in the 'contacts' list and replaces name with phone number 
    if any(sender in sublist for sublist in contacts):
        sender = contacts.__getitem__(sender)
        # Prints out the value before confirming
        print(sender)
    else:
        print("Defaulting to PLAIN number")
        print("\n" + sender)

    # Checks if name put in sender / receiver is in the 'contacts' list and replaces name with phone number
    if any(receiver in sublist for sublist in contacts):
        receiver = contacts.__getitem__(receiver)
        # Prints out the value before confirming
        print(receiver)
    else:
        print("Defaulting to plain number")
        print("\n" + receiver)

    # smsroute does not allow for messages over 160 characters (for some encoding)
    if len(message) >= 160:
        print("Your message is too long")
        exit()

    # Joins it into a HTTP request to be sent with URL encoded message. You can mess around with the 'type' in the link and in the SMSRoute docs
    spoofurl =  f'https://beta.smsroute.to/sendsms?username={username}&password={password}&type=1&source={sender}&destinations={receiver}&message={message}'

    print(spoofurl)
    confirm = input("Press ENTER to send message!\t")

    # Confirms message
    if confirm == "":
        print("Sent!")
        r = requests.get(spoofurl)
    else:
        exit()
    
    # Prints response
    print(r.text)

# If none of the two options are selected
else:
    print("You Silly Man")
    quit()
