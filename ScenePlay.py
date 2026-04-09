# SCENE PLAY

import pygwidgets
import pygame
import random
from Constants import *


class ScenePlay:
    def __init__(self, window, sceneManager):
        # Referencing window and scene manager
        self.window = window
        self.sceneManager = sceneManager

        # Creating GUI elements (buttons)
        self.rollButton = pygwidgets.TextButton(window, (300, 520), "Roll Dice")
        self.playAgainButton = pygwidgets.TextButton(window, (300, 560), "Play Again")

        # Game variables -------------------------------
        self.playerScore = 0
        self.computerScore = 0

        self.playerDie = 1
        self.computerDie = 1
        self.currentSum = 0

        self.rollsCompleted = 0
        self.gameFinished = False
        self.winnerMessage = ""

    # Setters and getters -------------------------------
    def getPlayerScore(self):
        return self.playerScore

    def setPlayerScore(self, value):
        self.playerScore = value

    def getComputerScore(self):
        return self.computerScore

    def setComputerScore(self, value):
        self.computerScore = value

    # Method that handles the process of the game
    def rollDice(self):
        # Checking if game is finished (dice have been rolled 3 times)
        if self.gameFinished:
            return

        # Generating random dice rolls
        self.playerDie = random.randint(1, 6)
        self.computerDie = random.randint(1, 6)

        # Calculating and storing dice roll sum
        self.currentSum = self.playerDie + self.computerDie
        total = self.currentSum

        # Getting player data (choice and name)
        playerChoice = self.sceneManager.getData("playerChoice")
        playerName = self.sceneManager.getData("playerName")

        # Checking if dice roll sum is even or odd and assigning scores (according to player choice)
        if total % 2 == 0:
            if playerChoice == "Evens":
                self.setPlayerScore(self.getPlayerScore() + 1)
            else:
                self.setComputerScore(self.getComputerScore() + 1)
        else:
            if playerChoice == "Odds":
                self.setPlayerScore(self.getPlayerScore() + 1)
            else:
                self.setComputerScore(self.getComputerScore() + 1)

        self.rollsCompleted += 1    # incrementing rolls counter

        # Determining winner after 3rd roll
        if self.rollsCompleted == 3:
            self.gameFinished = True    # marking game over

            # Checking who has the higher score and displaying result
            if self.getPlayerScore() > self.getComputerScore():
                self.winnerMessage = f"{playerName} Wins!"
            elif self.getPlayerScore() < self.getComputerScore():
                self.winnerMessage = "Computer Wins!"
            else:
                self.winnerMessage = "It's a Tie!"

    # Method that resets the scores (and variables) for a new game
    def resetGame(self):
        self.setPlayerScore(0)
        self.setComputerScore(0)

        self.playerDie = 1
        self.computerDie = 1
        self.currentSum = 0

        self.rollsCompleted = 0
        self.gameFinished = False
        self.winnerMessage = ""

    # Handling event inputs from loop in Main
    def handleInputs(self, events):
        for event in events:
            # Checking if game is not finished to allow player to roll again
            if not self.gameFinished:
                if self.rollButton.handleEvent(event):
                    self.rollDice()
            # Checking if game is finished to go back to "Start" scene
            if self.gameFinished:
                if self.playAgainButton.handleEvent(event):
                    self.resetGame()
                    self.sceneManager.setScene("START")

    def update(self):
        pass

    # Drawing the scene (filling window, loading .png files, drawing widgets)
    def draw(self):
        self.window.fill(WHITE)

        # Loading dice images
        playerImage = pygame.image.load(f"dice{self.playerDie}.png")
        computerImage = pygame.image.load(f"dice{self.computerDie}.png")

        # Sizing images
        playerImage = pygame.transform.scale(playerImage, (150, 150))
        computerImage = pygame.transform.scale(computerImage, (150, 150))

        # Placing images
        self.window.blit(playerImage, (150, 250))
        self.window.blit(computerImage, (400, 250))

        # Displaying dice roll sum
        sumText = pygwidgets.DisplayText(self.window, (300, 200), f"Sum: {self.currentSum}", fontSize=32)
        sumText.draw()

        # Displaying scores
        scoreText = pygwidgets.DisplayText(self.window, (250, 150), f"Player: {self.playerScore}   Computer: {self.computerScore}", fontSize=28)
        scoreText.draw()

        # Displaying round number
        roundText = pygwidgets.DisplayText(self.window, (300, 120), f"Round: {self.rollsCompleted}/3",fontSize=28)
        roundText.draw()

        # Draw roll button if game is not finished
        if not self.gameFinished:
            self.rollButton.draw()

        # Showing  winner at bottom after 3rd roll
        if self.gameFinished:
            winnerText = pygwidgets.DisplayText(self.window, (300, 480), self.winnerMessage, fontSize=36)
            winnerText.draw()

            self.playAgainButton.draw()     # Drawing play again button