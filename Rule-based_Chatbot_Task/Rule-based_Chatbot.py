import random

# Define a dictionary of rules and responses
ai_guide_rules = {
    "What is artificial intelligence?": "Artificial Intelligence (AI) is a broad field in computer science that focuses on creating intelligent machines capable of simulating human-like intelligence and performing tasks that typically require human intelligence.",
    
    "Types of AI": "There are primarily three types of AI:\n1. Narrow AI (Weak AI): Designed for specific tasks, like virtual personal assistants (e.g., Siri, Alexa).\n2. General AI (Strong AI): Possesses human-like intelligence and can handle various tasks.\n3. Artificial Superintelligence (ASI): Hypothetical AI that surpasses human intelligence.",
    
    "Machine Learning": "Machine Learning is a subset of AI that enables computers to learn and make predictions from data without being explicitly programmed. An example is training a model to recognize handwritten digits (e.g., MNIST dataset).",
    
    "Deep Learning": "Deep Learning is a subfield of machine learning that uses neural networks with multiple layers to model complex patterns. It's widely used in image recognition, such as identifying objects in photos.",
    
    "Natural Language Processing (NLP)": "NLP focuses on enabling computers to understand, interpret, and generate human language. Chatbots and language translation services are common applications of NLP.",
    
    "Computer Vision": "Computer Vision involves teaching machines to interpret and understand visual information from the world, like facial recognition systems or self-driving car perception.",
    
    "Reinforcement Learning": "Reinforcement Learning is about training agents to make decisions by interacting with an environment. For instance, training a robot to play chess or navigate a maze.",
    
    "Robotics": "AI and robotics combine to create intelligent robots that can perform tasks autonomously or semi-autonomously, such as industrial robots used in manufacturing.",
    
    "AI in Healthcare": "AI is used in healthcare to assist with diagnosis, drug discovery, and treatment recommendation. For example, AI can help analyze medical images like X-rays.",
    
    "AI in Finance": "AI is used in finance for algorithmic trading, fraud detection, and risk assessment. One application is predicting stock prices using historical data.",
    
    "AI in Autonomous Vehicles": "AI plays a crucial role in self-driving cars, enabling them to perceive their environment, make driving decisions, and navigate safely.",
    
    "AI Ethics": "AI ethics addresses moral and ethical considerations surrounding AI, including bias in algorithms, privacy concerns, and ensuring AI is used for the benefit of society.",
    
    "How to start a career in AI?": "To start a career in AI, you can begin by learning programming languages like Python, mastering math and statistics, and taking online courses or pursuing a degree in AI or related fields.",
    
    "Tell me a joke": "Why do AI programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25! 😄"
}

# Define a function to generate responses based on user input
def get_response(user_input):
    user_input = user_input.strip()
    for rule, response in ai_guide_rules.items():
        if user_input.lower() == rule.lower():
            return response
    return "I'm sorry, I don't have information on that specific topic. Please ask about a different aspect of AI."

# Main loop to interact with the chatbot
print("AI Guide Chatbot: Hello! How can I assist you with information about AI?")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("AI Guide Chatbot: Goodbye! If you have more questions in the future, feel free to return.")
        break
    response = get_response(user_input)
    print("AI Guide Chatbot:", response)

