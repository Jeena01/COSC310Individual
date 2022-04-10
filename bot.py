from optimizer import InputProcess as ip
import wikipedia
import json
import random
from translate import Translator
name="User"
input_resp=""
opt_input=[]
query_words=["what", "search","information" "look up","tell"]
translate_words=["language","translate","french","german","spanish"]
languages=["german","french","spanish","english"]
bye_words=["go", "leave", "bye", "end" ]
prompts=[ "The silent treatment I see. Well I'm here if you need me.", "I can't help you if you don't talk to me!",
         "You can tell me anything! Type in the text box when you feel ready"]
apologies=["I don't understand. Could you try phrasing it a different way?","I'm not sure what you mean by that.", "Hmm. I'm not sure I can help with that. Anything else?",
           "I'm sorry, I'm not smart enough to understand what you meant. Try saying something else?",
           "I think I don't understand what you meant. Could you clarify?"]
with open('responses.json') as json_file:
    responses = json.load(json_file)
translator= Translator(to_lang="spanish")
trnsl_output=False
def print_output(s):
    if trnsl_output:
        print("Serenity: "+translator.translate(s))
    else:
        print("Serenity: "+s)
def get_input():
    #function gets input from user
    global input_resp
    input_resp = input((name+": "))
    global opt_input
    opt_input=ip.optimizer(input_resp)
def greet():
    #function greets user
    global input_resp
    input_resp=input("Serenity: Hi! I'm Serenity! What's your name?\n User:")
    global name
    name=input_resp
    print_output("Nice to meet you " +name+". How is it going?")
def check_query():
    #function checks if user is asking a query
    global opt_input
    for qword in query_words:
        for word in opt_input:
            if ip.is_same(qword,word):
                return True
    return False
def check_translate():
    #function checks if user is making a translation request
    global opt_input
    for qword in translate_words:
        for word in opt_input:
            if ip.is_same(qword,word):
                return True
    return False
def get_resp():
    #function gets response from dictionary
    for key, value in responses.items():
        for word in opt_input:
            if ip.is_same(key,word):
                return value
    
    return ""
def start():
    greet()
    talk()
def check_goodbye():
    global opt_input
    for qword in bye_words:
        for word in opt_input:
            if ip.is_same(qword,word):
                return True
    return False
def get_wiki():
    print_output("What would you like to know about?")
    query=input((name+":"))
    print_output(wikipedia.summary(query,sentences=3))
def talk():
    keep_going=True
    while(keep_going):
        get_input()
        if len(opt_input) ==0:
            print_output(random.choice(prompts))
            continue
            #working
        elif check_goodbye():
            print_output("It was great talking to you! Goodbye!")
            keep_going=False
            break
            #working
        elif check_translate():
            translate()
        elif check_query():
            get_wiki()
            print_output("What else can I help you with?")
            #working
        else:
            output=get_resp()
            if output =="":
                print_output(random.choice(apologies))
            else:
                print_output(output)
def translate():
    global trnsl_output
    global translator
    print_output("What language would you like to me to switch to?")
    get_input()
    lang=get_lang()
    if ip.is_same(lang,"english"):
        trnsl_output=False
        print_output("Okay! Switching back to English now!")
    elif lang == "err":
        print_output("Sorry that language is not supported. Anything else I can help with?")
    else:
        translator= Translator(to_lang=lang)
        trnsl_output=True
        print_output("You got it! Talk to me like you normally would!")
def get_lang():
    global opt_input
    for qword in languages:
        for word in opt_input:
            if ip.is_same(qword,word):
                return qword
    return "err"
