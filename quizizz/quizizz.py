#!/usr/bin/env python3
from selenium import webdriver
import time, json, requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

def play(gamecode, name):
    driver = webdriver.Chrome()
    driver.get("https://quizizz.com/join/")
    time.sleep(2)
    room_input = driver.find_element_by_css_selector('.check-room-input')
    room_input.send_keys(gamecode)
    driver.find_element_by_css_selector('.check-room-btn').click()
    time.sleep(2)
    player_input = driver.find_element_by_css_selector('.check-player-input')
    player_input.send_keys(name)
    button = driver.find_element_by_css_selector('.check-player-btn')
    button.click()
    quizID = input("QuizID > ")
    quizInfo = requests.get(f"https://quizizz.com/quiz/{quizID}/").json()
    answers = {}
    for question in quizInfo["data"]["quiz"]["info"]["questions"]:
        answers[question["structure"]["query"]["text"]] = question["structure"]["options"][int(question["structure"]["answer"])]["text"]
    for _ in range(len(answers)):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'question-text-color')))
        try:
            questionAnswer = answers[driver.find_element_by_css_selector('.question-text-color').get_attribute('innerHTML')]
            choices = driver.find_element_by_css_selector('.options-container').find_elements_by_css_selector('.option')
            for answer in choices:
                if answer.find_element_by_css_selector(".resizeable").get_attribute('innerHTML') == questionAnswer:
                        answer.click()
                        break
        except KeyError:
            input("I couldn't find the answer, please click it yourself. [ENTER] ")

    driver.quit()    
gamecode = input("gamecode > ")
name = input("name > ")
play(gamecode, name)



