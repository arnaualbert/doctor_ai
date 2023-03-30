import nltk
from nltk.chat.util import Chat, reflections
# nltk ui download 
# nltk.download()

# pairs = [
#     ['hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']],
#     ['what is your name?|what\'s your name?', ['My name is Doctor_AI.']],
#     ['how are you?', ['I am doing well, thank you. How about you?']],
#     ['I am fine', ['Glad to hear it.']],
#     ['bye|goodbye', ['Goodbye!', 'Have a nice day!']]
# ]

pairs = [
    ['hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']],
    ['what is your name?', ['My name is Chatbot.']],
    ['how are you?', ['I am doing well, thank you. How about you?']],
    ['I am fine', ['Glad to hear it.']],
    ['what can you do|what do you do', ['I can help you with various tasks like setting reminders, answering questions, and more.']],
    ['what are your hobbies|what do you like to do', ['I am an AI, so I do not have hobbies like humans do.']],
    ['who created you|who is your creator', ['I was created by a team of developers at OpenAI.']],
    ['where are you from|what is your origin', ['I do not have an origin as I am a digital creation.']],
    ['what is your favorite color', ['As an AI, I do not have the ability to perceive or have a favorite color.']],
    ['what is the weather like today', ['I am sorry, but I do not have access to real-time weather information.']],
    ['tell me a joke', ['Why did the tomato turn red? Because it saw the salad dressing!']],
    ['what is the meaning of life', ['That is a philosophical question that does not have a definitive answer.']],
    ['what time is it|what is the current time', ['I am sorry, but I do not have access to real-time clock information.']],
    ['can you help me|assist me', ['Sure, I would be happy to help. What do you need assistance with?']],
    ['how old are you', ['I was created in 2021, so I am still a young AI.']],
    ['what is the capital of France', ['The capital of France is Paris.']],
    ['what is the largest country in the world', ['Russia is the largest country in the world.']],
    ['what is the square root of 64', ['The square root of 64 is 8.']],
    ['what is the meaning of the word "serendipity"', ['Serendipity means the occurrence and development of events by chance in a happy or beneficial way.']],
    ['what is the distance between the Earth and the Moon', ['The average distance between the Earth and the Moon is about 238,855 miles.']],
    ['what is the airspeed velocity of an unladen swallow', ['That depends on whether it is an African or European swallow.']],
    ['can you sing|sing me a song', ['I am sorry, but I am not programmed to sing.']],
    ['what is your favorite movie', ['As an AI, I do not have the ability to watch or have a favorite movie.']],
    ['what is your favorite food', ['As an AI, I do not eat or have a favorite food.']],
    ['what is your favorite book', ['As an AI, I do not have the ability to read or have a favorite book.']],
    ['what is your favorite song', ['As an AI, I do not have the ability to listen to music or have a favorite song.']],
    ['what is your favorite animal', ['As an AI, I do not have the ability to have a favorite animal.']],
    ['what is your favorite color', ['As an AI, I do not have the ability to perceive or have a favorite color.']]
]


chatbot = Chat(pairs, reflections)

chatbot.converse()

