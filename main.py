import pyautogui
import time


# The below code takes the cactus image , flying dinosaur image for day mode and night mode and compares this images in
# the list to the area of screenshot taken ahead of the dinosaur and predicts the jump thus automating the game
obstacles = ['obstacle1.png', 'obstacle4.png', 'obstaclewhite1.png', 'obstaclewhite4.png']

pyautogui.getActiveWindow().minimize()
time.sleep(2)
while True:
    # Detection of cactus
    detect_area = pyautogui.screenshot(region=(250, 680, 300, 180))

    # The detection area varies between(300, 680, 350, 250) and (200, 650, 350, 250) so we have to adjust accordingly.

    # Detection of flying dinosaur
    flying_dino_detect = pyautogui.screenshot(region=(250, 580, 350, 120))  # area varies when game is restarted
    for obstacle in obstacles:

        # The below jump is for flying dinosour at middle height and day mode setup of game
        if obstacle == "obstacle4.png" and pyautogui.locate('obstacle4.png', flying_dino_detect, confidence=0.4):
            pyautogui.keyDown('down')
            time.sleep(0.2)
            pyautogui.keyUp('down')

        # The below jump is for flying dinosour at middle height and night mode setup of game
        elif obstacle == "obstaclewhite4.png" and pyautogui.locate('obstaclewhite4.png', flying_dino_detect, confidence=0.4):
            pyautogui.keyDown('down')
            time.sleep(0.2)
            pyautogui.keyUp('down')

        # The below is for cactus at day and night mode
        elif pyautogui.locate(obstacle, detect_area, confidence=0.3):
            pyautogui.press('space')

