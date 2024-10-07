from uagents import Agent

# Create an instance of the uAgent
agent = Agent()

@agent.on_message
def handle_message(sender, message):
    print(f"Received message from {sender}: {message}")

if __name__ == '__main__':
    agent.run()
