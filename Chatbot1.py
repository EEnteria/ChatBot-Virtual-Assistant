#Attempt 1 at a chatbot (Neutral Personality)
import random

#No need for a class since this program runs independently

greetings = ["Hello there", "How's your day?","How've you been?"]
goodbyes = ["Goodbye","Have a nice day","You have a good one"]#Come up with a better name? Sendoffs doesn't really work

keywords = ["hello","pet","seranoa","avlora","affirmations","garfield","benis"] #Expand the library of keywords based upon the topics at hand, responses are 1 to 1 for now. Program multiple responses?
responses = ["It's nice to meet you","Pets are pretty cool","Seranoa is stinky","I WOULD BARK FOR HER IF SHE ASKED","You're doing great and you deserve to be happy","https://cdn.discordapp.com/attachments/835649548923830282/1013172952793092106/unknown.png","penis"]
           


#Maybe have the next step be how it responds to your response? Question databank? How would it recognize a question


#Greeting
print("Bot:" + random.choice(greetings))

user = input("Say hello! (Or goodbye if you want to leave):\n ")
user = user.lower() #Doesn't properly handle uppercase




while (user != "goodbye" ): 
    keywordFound = False #Boolean for proper keywords
    
    for index in range(len(keywords)):
        if keywords[index] in user: #Used in the case where a 
            print("Bot:" + responses[index])
            keywordFound = True

        else:
            keywordFound = False


    user = input()
    user = user.lower()
        
print(random.choice(goodbyes))
