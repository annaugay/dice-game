# MAIN

import pygame
from Constants import *
from SceneStart import SceneStart
from ScenePlay import ScenePlay


# Class that manages which scene is active, switches between scenes, passes info between scenes
class SceneManager:
    def __init__(self, window):
        self.window = window
        self.data = {} # dictionary to store player info

        # Creating dictionary of scenes (name as the key, object as the value)
        self.scenes = {
            "START": SceneStart(window, self),
            "PLAY": ScenePlay(window, self)
        }

        # Setting the first scene to be the start scene
        self.currentScene = self.scenes["START"]

    # Setters and getters ----------------------------------------------
    # Changes scenes (setting active scene)
    def setScene(self, sceneName):
        self.currentScene = self.scenes[sceneName]

    # Getting active scene
    def getScene(self):
        return self.currentScene

    def setData(self, key, value):
        self.data[key] = value

    def getData(self, key):
        return self.data.get(key)


# Main ----------------------------------------------
def main():
    # Initializing pygame modules and building the window (and display name)
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Sum Dice Game")

    clock = pygame.time.Clock()     # clock object to control frames
    sceneManager = SceneManager(window)     # scene manager object

    # Looping forever
    while True:
        events = pygame.event.get()

        # Checking if user clicks 'x' to exit program
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        sceneManager.getScene().handleInputs(events)    # calling active scene's handleInputs method
        sceneManager.getScene().update()    # calling active scene's update method
        sceneManager.getScene().draw()    # calling active scene's draw method

        pygame.display.update()     # refreshing screen
        clock.tick(FRAMES_PER_SECOND)   # controlling frame rate (30 fps)


if __name__ == "__main__":
    main()