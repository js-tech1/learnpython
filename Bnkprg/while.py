"""
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
 message = input(prompt)
 print(message)

 if message != 'quit':
  print(message)
  
  """
unconfirmed_users= ['ab','cd','ef']
confirmed_users=[]
while unconfirmed_users:
    current_user= unconfirmed_users.pop(0)

    print("verifying users:" + current_user.title())
    confirmed_users.append(current_user)

    print("\nthe following users have been confirmed:")
    
print(confirmed_users)
        

