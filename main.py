import pyaudio
import pyttsx3
import speech_recognition as sr
import phrases

def get_audio():
    bot_names = ['совенок', 'сова', 'сынок', 'совеночек', 'совёнок', 'бот', 'sevinch', 'совёночек']
    while True:
        try:
            r = sr.Recognizer()
            with sr.Microphone(device_index=1) as sourse:
                print('Say something')
                audio = r.listen(sourse)
            query = r.recognize_google(audio, language='ru-RU')
            print('[log_1] You say: ', query.lower())
            fl = False
            quer = query.split()
            for i in quer:
                if i in bot_names:
                    fl = True
                    break
            if fl:
                command = converter(query.lower())
                print('[log_2] Convertered: ' + command)
                answer = phrases.check_command(command)
                print('[log_3] After_all: ' + answer)
                speak(answer)
        except Exception:
            pass


def speak(phrase):
    speak_engine.say(phrase)
    speak_engine.runAndWait()
    speak_engine.stop()


def converter(word):
    change_dict = ['в', 'на', 'ка', 'совенок', 'сова', 'совеночек', 'какая', 'открой',
                   'совёнок', 'бот', 'включи', 'запусти', 'сколько', 'сейчас', 'какое', 'расскажи', 'ответь',
                   'ты', 'мне', 'давай', 'открой', 'зайди', 'что', 'мне', 'ответь', 'к', 'примеру']
    word = word.split()
    output = ''
    for i in word:
        if i not in change_dict:
            output += i + ' '
    output = output.strip()
    return output


if __name__ == '__main__':
    speak_engine = pyttsx3.init()
    #voices = speak_engine.getProperty('voices')
    #speak_engine.setProperty('voice', voices[4].id)
    get_audio()
