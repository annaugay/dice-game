# SCENE START

import pygwidgets
from Constants import *


class SceneStart:
    def __init__(self, window, sceneManager):
        # Referencing window and scene manager
        self.window = window
        self.sceneManager = sceneManager

        # Creating GUI elements (label, input text box, buttons)
        self.titleText = pygwidgets.DisplayText(window, (300, 100), "Sum Dice Game")
        self.nameLabel = pygwidgets.DisplayText(window, (200, 250), "Enter Player Name:")

        self.playerNameInput = pygwidgets.InputText(window, (400, 250), width=200)

        self.evensButton = pygwidgets.TextButton(window, (200, 400), "Play Evens")
        self.oddsButton = pygwidgets.TextButton(window, (400, 400), "Play Odds")

    # Getter for player name
    def getPlayerName(self):
        return self.playerNameInput.getValue()

    # Handling event inputs from loop in Main
    def handleInputs(self, events):
        for event in events:
            # Getting input (player name)
            self.playerNameInput.handleEvent(event)

            # Checking if player clicked "Evens"
            if self.evensButton.handleEvent(event):
                self.sceneManager.setData("playerName", self.getPlayerName())   # storing player name in dictionary
                self.sceneManager.setData("playerChoice", "Evens")
                self.sceneManager.setScene("PLAY")      # switching to "Play" scene

            # Checking if player clicked "Odds"
            if self.oddsButton.handleEvent(event):
                self.sceneManager.setData("playerName", self.getPlayerName())   # storing player name in dictionary
                self.sceneManager.setData("playerChoice", "Odds")
                self.sceneManager.setScene("PLAY")      # switching to "Play" scene

    def update(self):
        pass

    # Drawing the scene (filling window and drawing widgets)
    def draw(self):
        self.window.fill(WHITE)

        self.titleText.draw()
        self.nameLabel.draw()
        self.playerNameInput.draw()
        self.evensButton.draw()
        self.oddsButton.draw()