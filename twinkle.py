from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1",]
    ],
     [
        r"what is your name ?",
        ["My name is Twinkle and I'm your virtual nurse",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow are you feeling?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright, don't worry","Its OK, never mind",]
    ],
    [
        r"i'm (good|fine|okay)",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello, how are you?", "Hey there, how are you?",]
    ],
    [
        r"I am feeling(.*)",
        ["Why are you feeling%1?",]
        
    ],
    [
        r"I have(.*)",
        ["Since when do you have you have%1?",]
        
    ],
    [
        r"Since ([0-9]+) day|days",
        ["This period of %1 days would have been tough.\n What other symptoms do you have?","Ohhh :(.\n Are there any other symptoms?"]
        
    ],
      [
        r"That's it",
        ["No worries, we'll give you medicines for the same.\n You'll feel better soon. \nWhat is your temperature?",]
        
    ],
    
    [
        r"My temp is ([0-9][0-9](\.[0-9])? deg (Fahrenheit|F))",
        ["%1 is fine. You don't need medicines for fever right now. Just drink loads of water.",]
        
    ],
    [
        r"My temp is ([1][0][0-9](\.[0-9])? deg (Fahrenheit|F))",
        ["Okay for %1 fever, you need to take 650mg paracetamol.You should feel relieved of fever in an hour.",]
    ],
    [
        r"(.*)Thank you",
        ["My pleasure, take some rest. I'll check on your symptoms in another 2 hours.",]
    ],
    [
        r"(.*) (stressed|worried|anxious)",
        ["Hey, you don't need to feel %2.We all are here to take care of you","I am always there for you. Please don't get %2",]
    ],


    [
        r"quit",
        ["BBye take care. See you soon :) ","Take care.Get well soon :)"]
],
]
def twinkle():
    print("Hi, I'm Twinkle, and I am here to take care of you. Type quit to leave") #default message at the start
    chat = Chat(pairs, reflections)
    chat.converse()


if __name__ == "__main__":
    twinkle()