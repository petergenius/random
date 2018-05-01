#!/usr/bin/env python3
from selenium import webdriver
import time, json, requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

def find_answers(quizID):
    quizInfo = requests.get(f"https://quizizz.com/quiz/{quizID}/").json()
    answers = {}
    if quizInfo["data"] == None:
        print("I couldn't find that quiz")

    for question in quizInfo["data"]["quiz"]["info"]["questions"]:
        if question["type"] == "MCQ":
            if question["structure"]["options"][int(question["structure"]["answer"])]["text"] == "":
                # image answer
                answer = question["structure"]["options"][int(question["structure"]["answer"])]["media"][0]["url"]
            else:
                answer = question["structure"]["options"][int(question["structure"]["answer"])]["text"]
        elif question["type"] == "MSQ":
            # multiple answers
            answer = []
            for answerC in question["structure"]["answer"]:
                if question["structure"]["options"][int(answerC)]["text"] == "":
                    answer.append(question["structure"]["options"][int(answerC)]["media"][0]["url"])
                else:
                    answer.append(question["structure"]["options"][int(answerC)]["text"])
        else:
            print(question["type"])
        questionID = question["structure"]["query"]["text"]
        answers[questionID] = answer

    return answers
def play(gamecode, name):
    driver = webdriver.Chrome()
    driver.get("https://quizizz.com/join/")
    time.sleep(2)
    driver.find_element_by_css_selector('.check-room-input').send_keys(gamecode)
    driver.find_element_by_css_selector('.check-room-btn').click()
    time.sleep(2)
    driver.find_element_by_css_selector('.check-player-input').send_keys(name)
    driver.find_element_by_css_selector('.left-section').find_element_by_css_selector('.menu-icon').click()
    time.sleep(0.4)
    driver.find_element_by_css_selector('.game-section').find_element_by_css_selector('.toggle-button').click()
    driver.find_element_by_css_selector('.back-btn').click()
    time.sleep(0.4)
    driver.find_element_by_css_selector('.check-player-btn').click()
    answers = find_answers(input("QuizID > "))
    while True:
        try:
            WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'question-text-color')))
        except TimeoutException:
            driver.quit()
            break
        try:
            questionAnswer = answers[driver.find_element_by_css_selector('.question-text-color').get_attribute('innerHTML')]
            choices = driver.find_element_by_css_selector('.options-container').find_elements_by_css_selector('.option')
            firstAnswer = True
            for answer in choices:
                try:
                    if isinstance(questionAnswer, list):
                        if firstAnswer:
                            time.sleep(0.2)
                            firstAnswer = False
                        if answer.find_element_by_css_selector(".resizeable").get_attribute('innerHTML') in questionAnswer:
                            answer.click()
                    elif answer.find_element_by_css_selector(".resizeable").get_attribute('innerHTML') == questionAnswer:
                        answer.click()
                        break
                except NoSuchElementException:
                    style = answer.find_element_by_css_selector(".option-image").get_attribute("style")
                    if isinstance(questionAnswer, list):
                        for correctAnswer in questionAnswer:
                            if style in correctAnswer:
                                answer.click()
                                break
                    elif questionAnswer in style:
                        answer.click()
                        break
            if isinstance(questionAnswer, list):
                driver.find_element_by_css_selector(".multiselect-submit-btn").click()
        except KeyError:
            input("I couldn't get the answer. Please click it then hit [enter]")
    driver.quit()    


print('''
 ██████╗ ██╗   ██╗██╗███████╗██╗███████╗███████╗
██╔═══██╗██║   ██║██║╚══███╔╝██║╚══███╔╝╚══███╔╝
██║   ██║██║   ██║██║  ███╔╝ ██║  ███╔╝   ███╔╝ 
██║▄▄ ██║██║   ██║██║ ███╔╝  ██║ ███╔╝   ███╔╝  
╚██████╔╝╚██████╔╝██║███████╗██║███████╗███████╗
 ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝╚═╝╚══════╝╚══════╝
                                                
                Peter Stenger
                Version 1.0''')
play(input("Gamecode > "), input("Name > "))
