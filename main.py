import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3
from random import *
import json


jokes = []
audio = []
help_ = []


try:
    with open("jokes.json", "r", encoding="utf-8") as fh:
        jokes = json.load(fh)

    print("Сборник анекдотов был успешно загружена ")
    with open("help.json","r", encoding="utf-8") as h:
        help_ = json.load(h)
except:

    jokes.append(
        "В салоне красоты. — Мне маникюр, пожалуйста, как у Бритни Спирс, макияж, как у Анджелины Джоли, педикюр как у Наоми Кэмпбелл… — А лицо как у Жерара Депардье оставляем?")
    jokes.append("Однажды я не вовремя зашла в спальню родителей. Они клеили обои, пришлось им помогать.")
    jokes.append(
        "Когда ты холостяк — всё валяется по своим местам. Женился — и всё аккуратно сложено чёрт знает где!")
    jokes.append("Разговор по телефону: — Я хочу в Астрахань. — Извините, не расслышала: Я хочу вас что?.. ")


def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()


talk("Привет, я Ваш карманный сборник анекдотов  У меня хорошее чувство юмора  Очень рада видеть вас")

def save():
    with open("jokes.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(jokes, ensure_ascii=False))
    talk("Сборник анекдотов был успешно сохранен в файле jokes.json")

def load():
    with open("jokes.json", "r", encoding="utf-8") as fh:

        jokes = json.load(fh)
    talk("Сборник анекдотов был успешно загружен ")



'''
у меня микрафон поломан пришлось переделать на ввод команд в консоле
'''
def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говорите")
        # r.pause_threshold = 1
        # r.adjust_for_ambient_noise(source, duration=1)
        # audio = r.listen(source)
        audio = input("-> ")
        # пример -> открой youtoobe распознавание объектов на python / глубокое машинное обучение
    try:
        # zadacha = r.recognize_google(audio, language="ru == RU").lower()
        zadacha = audio.lower()   #
        print("Вы сказали " + zadacha)
        # talk("Вы сказали " + zadacha)

    except sr.UnknownValueError:
        talk("Я вас не поняла ")
        zadacha = command()
    return zadacha

def makeSomething(zadacha):
    if 'youtoobe' in zadacha:
        talk("Уже открываю")
        url = "https://www.youtube.com/results?search_query=" + zadacha
        webbrowser.open(url)
    elif 'stop' in zadacha:
        save()
        talk("Жаль что вы так рано завершаете работу, у меня осталось много не рассказанных анекдотов")
        sys.exit()
    elif 'jokes' in zadacha:
        talk(choice(jokes))
    elif "add" in zadacha:
        f = input(" добавьте анегдот я записую ")
        jokes.append(f)
        talk("Анекдот был успешно добавлен в коллекцию ")
    elif "all" in zadacha:
        talk(jokes)
    elif 'help' in zadacha:
        for h in help_:
             print(h)
        talk(help_)
    else:
        talk("Я не распознала команду обратиттесь в справочную")


while True:
    makeSomething(command())





