# chatterbot is a machine learning lib
# this is used here so that we can make
# object of chat bot
from chatterbot import ChatBot
# this is imported for doing training
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
# for gui
from tkinter import *
import logging
from PIL import ImageTk, Image


# make object it is made like this
bot = ChatBot("Jarvis")

# Logging is a means of tracking events that happen when some software runs.
# for fixing a error
logger = logging.getLogger() 
# critical set kar ke error nahi aa raha vo kyuki that error is not
# above that threshold level
logger.setLevel(logging.CRITICAL)

# training part
# not mandatory here
# naive bayers classification is used in this
conversation = [
    "hi",
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "What is your name",
    "my name is jarvis",
    "Can you speak,write,do anything",
    "No I am currenlty under development",
    "Do you know anything about india",
    "yes it is a beautiful country",
    "aadadg2112asw",
    "Sorry what did you say? please say again",
    "tell me a joke",
    "You are fat",
    "what are you doing",
    "nothing much what are you doing?",
    "what is my name",
    "I dont know why dont you tell me",
    "My name is arin",
    "Its a nice name",
    "hahahahaha",
    "That was fun happy to make you laugh",
    "Thanks",
    "welcome",
    "bye",
    "Ok bye take care have a nice day"
]

trainer = ListTrainer(bot)
# model trained here
trainer.train(conversation)

    #or

trainer = ChatterBotCorpusTrainer(bot)

trainer.train(
    "chatterbot.corpus.english"
)


# for response
# while True:
#         input_data = input("You- ")

#         if(input_data == 'exit'):
#             break

#         response = bot.get_response(input_data)
#         print("Jarvis- ", response)

def ask():
    # whaterver in text field will come from here
    query = textF.get()
    # response from our query
    response = bot.get_response(query)
    # now insert messages
    msgs.insert(END,"you : "+query)
    msgs.insert(END,"Jarvis : "+str(response))
    textF.delete(0,END)


main = Tk()
# height and width set
main.geometry("500x650")

# for title
main.title("Jarvis")

# for image
canvas = Canvas(main, width=300, height=150)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("download.png"))
canvas.create_image(10, 10, anchor=NW, image=img)

# make a frame now
frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20)

sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()

# create text field
textF = Entry(main)
textF.pack(fill=X, pady=10)

# buttons
btn = Button(main, text="Ask from bot", font=("Verdana", 20), command=ask)
btn.pack()

main.mainloop()
