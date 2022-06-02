'''
    author: Rohan Niakal
'''

import requests
import json
import pyttsx3
import datetime
import time
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import random
import psutil
from urllib.request import urlopen
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
female = voices[1]
male = voices[0]
fm = voices[1]
engine.setProperty('voice', fm.id)

# this function for take_commands
def take_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print('\nlistening......')
        r.pause_threshold = 1
        r.energy_threshold = 5000
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f'You Said {query}\n')
    except Exception as e:
        print('Say that again please.....')
        return 'none'
    return query

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wakeup():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1
        r.energy_threshold = 5000
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f'You Said {query}\n')
    except Exception as e:
        return 'none'
    return query

def internet_on():
    try:
        page=urlopen("http://www.google.com")
        return 'on'
    except:
        return 'off'
internet_on()

if 'on' == internet_on():
    pass
    # check_internet() 
else:
    print('check your internet connection')
    speak('check your internet connection')
    exit()


def start():
    speak('sir iam going sleep if you whant to any help you call me jarvis')
    while True:
        query = wakeup().lower()
        if 'jarvis'in query or 'wakeup' in query:
            speak('ok sir how can i help you')
            break
        else:
            continue




# this function for wish to the user

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning!")
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        print("Good Afternoon!")
        speak("Good Afternoon!")

    else:
        print("Good Evening!")
        speak("Good Evening!")

    speak("I am rohan. Please tell me how may I help you")


def good():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        return "good morning"

    elif hour >= 12 and hour < 18:
        return "good afternoon"
    else:
        return "good evening"


# while True:
#     query = take_commands().lower()
#     if 'ok' in query:
#         break
#     else:
#         continue


# speak('hahahahahh')
def toss_coins():
    r = random.choice(['Heads', 'Tails'])
    print(r)
    speak(r)


def word_to_num(num):
    a = num.split()
    # print(a)
    wn = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
          'eight': 8, 'nine': 9, 'zero': 0, 'plus': '+', }
    try:
        if a[1] == '+':
            fnum = int(a[0])
            snum = int(a[2])
            return (fnum+snum)
        elif a[1] == '/':
            fnum = int(a[0])
            snum = int(a[2])
            return (fnum/snum)
        elif a[1] == '*' or a[1] == 'into':
            fnum = int(a[0])
            snum = int(a[2])
            return (fnum*snum)
        else:
            return 'please speak slowly'

    except Exception as e:
        return ('i think you drink')
        # print('I am not understand Say that again please.....')
        # speak('I am not understand Say that again please.....')


def game1():

    p = 'paper'
    s = 'stone'
    sci = 'scissor'

    speak('lets play stone  paper  scissor')
    # chance=take_commands().lower()
    # if 'stop' in chance:
    #     break
    # try:
    #     chance=int(chance)
    #     # break
    # except Exception as e:
    #     try:
    #         wn = {'one': 1,'two': 2,'three': 3,'four': 4,'five': 5,'six': 6,'seven': 7,
    #         'eight': 8,'nine': 9,'zero': 0
    #         }
    #         chance=wn[chance]
    #         # break
    #     except Exception as r:
    #         speak('please speak slowly')
    #         continue
    i = 0
    c=random.randint(5,10)
    while True:

        i=i+1
        if i == c:
            speak('Sir I am bored if you want stop me then I will stop')
            play = take_commands().lower()
            if 'stop' in play:
                speak('ok sir I am stopping now')
                break
            else:
                c=random.randint(10,20)
                continue
            
        speak('choose  stone  paper  scissor')

        print('enter any one', '[', p, s, sci, ']')
        a = [s, p, sci]
        comp = random.choice(a)

        play = take_commands().lower()
        if comp == play:

            print('You and I were thinking the same')
            speak('You and I were thinking the same')
            # print(f'me entered comp\nused chances{i}/{chance}')
        elif 'stop' in play:
            speak('ok sir I am stopping now')
            break
        elif s == comp:
            if play == sci:
                print('you loss sir you dont know I am the pro player of this game')
                speak('you loss sir you dont know I am the pro player of this game')
                # print(f'me entered comp\nused chances{i}/{chance}')
            elif play == p:
                print('you win sir  see next time I will win')
                speak('you win sir                        see next time I will win')
                # print(f'me entered comp\nused chances{i}/{chance}')
            else:
                print('please enter valid input', 'used chance')
        elif p == comp:

            if play == sci:
                print('you win sir  see next time I will win')
                speak('you win sir                        see next time I will win')
                # print(f'me entered comp\nused chances{i}/{chance}')
            elif play == s:
                print('you loss sir you dont know I am the pro player of this game')
                speak('you loss sir you dont know I am the pro player of this game')
                # print(f'me entered comp\nused chances{i}/{chance}')
            else:
                print('you win sir  see next time I will win')
                speak('you win sir                        see next time I will win')
                # print(f'me entered comp\nused chances{i}/{chance}')
        elif sci == comp:

            if play == p:
                print('you loss sir you dont know I am the pro player of this game')
                speak('you loss sir you dont know I am the pro player of this game')
                # print(f'me entered comp\nused chances{i}/{chance}')
            elif play == s:
                print('you win sir  see next time I will win')
                speak('you win sir                        see next time I will win')
                # print(f'me entered comp\nused chances{i}/{chance}')
            else:
                pass
                # print(f'me entered comp\nused chances{i}/{chance}')
        else:
            print("'please enter valid input','used chance',i,'/',chance'")

def introduction():
    while True:
        try:
            with open('introduction.txt') as r:
                w= r.read()
                w=w.split()
                name=f'{w[0]}'
                speak(f'hello {name}')
                break
        except Exception as e:
            r=open('introduction.txt','w')
            print('enter your name')
            speak('enter your name')
            r=open('introduction.txt','a')
            # query = take_commands().lower()
            query=input()
            name=r.write(f'{query}\n')
            print('enter your age')
            speak('your age')
            age=input()
            # age=query = take_commands().lower()
            r.write(f'{age}')
            speak(f'your name {name} and age {age} are updated')


introduction()

def notes(note):
    # add time
    strtime = datetime.datetime.now().strftime('%H:%M:%S')

    a = open('note.txt', 'a')
    a.write(f'\nTime:- [{strtime}]  {note}')
    a = open('note.txt', 'r')
    rea = a.read()
    print(rea)


if __name__ == '__main__':

    myName='jarvis'
    wishMe()
    i=0
    while True:
        query = take_commands().lower()
        # query=input()
        i=i+1
        if 'wikipedia' in query or 'tell me' in query and 'about' in query :
            try:
                speak('searching')
                results = wikipedia.summary(query, sentences=3)
                print('according to wikipedia\n')
                speak('according to wikipedia')
                print(results)
                speak(results)
            except Exception as e:
                webbrowser.open(f'https://www.google.com/search?q={query}')

        elif 'open youtube' in query :
            webbrowser.open('https://www.youtube.com')

        elif 'open google' in query :
            webbrowser.open('google.com')

        elif 'play music' in query :
            music_folder = 'C:\\Users\\91902\\Music'
            musics_list = os.listdir(music_folder)
            rand = random.randint(0, len(musics_list)-1)
            os.startfile(os.path.join(music_folder, musics_list[rand]))
            speak('music are played')
            start()
        elif 'time' in query :
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            print(strtime)
            speak(f'sir the time is {strtime}')

        elif 'open code' in query :
            codepath = r"d:\app\Microsoft VS Code\Code.exe"
            os.startfile(os.path.join(codepath))

        elif 'joke' in query :
            a = requests.get('https://v2.jokeapi.dev/joke/Any?type=single')
            j = json.loads(a.content)
            print(j['joke'])
            speak(j['joke'])
            speak('       hahahahah          you like                 it')

        elif 'quit' in query or 'stop' in query :
            speak('ok sir buy buy , take care')
            break
        elif 'speep' in query :
            start()
        elif 'rbsy' in query :
            speak(
                'RBSY is an Indian web service company that specializes in website-related services')

        elif 'rohan' in query :
            print('rohan nikale a web desiner form rbsy ')
            speak('rohan nikale a web desiner form rbsy ')

        elif 'good' in query or 'nice' in query or 'best' in query :
            if good() in query:
                speak(good())
                print(good())
            elif "good" == query or "good job" == query or 'nice' in query or 'best' in query:
                print('thank you sir')
                speak('thank you sir')
            else:
                speak(f'hahahahahh     no its {good()}')

        # elif good() != query:
        #     print('hahah')

        elif '-' in query or '+' in query or 'plus' in query or '/' in query or '*' in query or 'into' in query :
            print(word_to_num(query))
            speak(word_to_num(query))

        elif 'toss coin' in query:
            toss_coins()

        elif 'invented you' in query or 'developed you' in query :
            print('Mr Rohan Nikale')
            speak('mr.rohan nika  le')
            pass

        elif 'who are you' in query or 'your name' in query :
            speak('I am rohan')
        elif 'copy' in query:
            print(query)
            speak(query)
            while True:
                query = take_commands().lower()
                print(query)
                speak(query)
                if 'stop' in query:
                    speak('hahahahaha         you enjoyed sir')
                    break
        elif 'setting' in query or 'file' in query :
            if 'setting' in query:
                from pynput.keyboard import Key, Controller
                keyboard = Controller()
                with keyboard.pressed(Key.cmd_l):
                    keyboard.press('i')
                    keyboard.release('i')
            elif 'file' in query:
                from pynput.keyboard import Key, Controller
                keyboard = Controller()
                with keyboard.pressed(Key.cmd_l):
                    keyboard.press('e')
                    keyboard.release('e')
        elif 'screenshot' in query :
            from mss import mss
            with mss() as sct:
                sct.shot()
                speak('screenshot taked successfully')
        elif 'show' in query and 'note' in query :
            if 'all' in query:
                a = open('note.txt', 'r')
                rea = a.read()
                print(rea)
                speak(rea)
            elif 'all' not in query :
                a = open('note.txt', 'r')
                rea = a.read()
                lis = rea.split('\n')
                le = len(lis)
                print('this is your letest note ')
                speak('this is your letest note ')
                print(lis[le-1])
                speak(lis[le-1])
            else:
                speak('you have not any note')
        elif 'note' in query :
            speak('what you want to note')
            for i in range(7):
                query = take_commands().lower()
                if query != 'none':
                    notes(query)
                    speak('your notes are updated')
                    print('do you want to write more notes')
                    speak('do you want to write more notes')
                elif 'no' in query or 'cancel' in query :
                    print('ok')
                    speak('ok')
                    break

                else:
                    print('please speak loudly')
                    speak('please speak loudly')

        elif 'game' in query :
            game1()
        elif 'have you eaten' in query or 'eat' in query or 'eaten' in query :
            battery_data = psutil.sensors_battery()
            if battery_data.power_plugged:
                print('i am eating')
                speak('i am eating')
            elif battery_data.percent<=20:
                print('I am very hungry')
                speak('I am very hungry')
                print('I am only eat electricity')
                speak('I am only eat electricity')
            else:
                speak('no Iam full')

            pass
        elif 'battery' in query or 'health' in query :

            battery_data = psutil.sensors_battery()
            print('Battery power left: {}%'.format(battery_data.percent))
            speak('Battery power left: {}%'.format(battery_data.percent))
            if battery_data.power_plugged:
                print('Power is connected')
                speak('Power is connected')

            else:
                print('Power is not connected')
                speak('Power is not connected')
                print('Time left on battery: {}'.format(datetime.timedelta(seconds=battery_data.secsleft)))
                speak('Time left on battery: {}'.format(datetime.timedelta(seconds=battery_data.secsleft)))
        elif 'news' in query or 'headlines' in query :

            a = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=23dc71aa3f384611a9bc741c4cdbb122')
            data = json.loads(a.content)
            print('Here are the top 5 news of the awesome country India\n')
            speak('Here are the top ten news of the awesome country India')
            for i in range(1, 6):
                print(f'{i} .', data['articles'][i]['description'], '\n')
                news = data['articles'][i]['description']
                speak(news)
                time.sleep(1)
                if i == 4:
                    speak('So our last news for today is')
                    continue
                elif i == 5:
                    break
                else:
                    speak("Moving To Our next news")
        elif 'hello' in query :
            speak('Hello sir how are you?')
            query = take_commands().lower()
            if 'fine' in query or 'good' in query or 'thank' in query:
                speak('nice sir  what is your plan today can I note your plan ')
                query = take_commands().lower()
                if 'yes' in query or 'yeh' in query or 'ha'in query or 'why not' in query :
                    speak('tell your plan')
                    query = take_commands().lower()
                    notes(query)
                else:
                    speak('ok sir your choise')
                    pass
        elif 'how' in query and 'you' in query :
            speak('I am fine    how are you')
        elif 'fine' in query or 'good' in query:
            speak('nice')
        if 'fine' in query or 'good' in query or 'thank' in query:
            speak('nice sir')
        elif 'none' in query:
            pass
        elif 'how' in query and 'make'in query :
            result = f'https://www.youtube.com/results?search_query={query}'
            webbrowser.open(result)
        else:
            print('I am not understand Say that again please.....')
            speak('I am not understand Say that again please.....')
            if i==5:
                i=1
                a=0
                start()
exit()
