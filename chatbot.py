import aiml

# Create the kernel and learn AIML files during initialization
kernel = aiml.Kernel()
kernel.learn("std-startup1.xml")

# Press CTRL-C to break this loop
while True:
    message = input("Enter your message to the bot: ")
    if message == "quit":
        break
    else:
        bot_response = kernel.respond(message)
        print(bot_response)
