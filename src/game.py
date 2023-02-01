import pygame
from src.settings import *
from src.button import displayBtn, clickedBtn
from src.dice import displayDice, rollDice
from src.draw import displayItem, displayStats, renderFont, backGround
import time
import random

pygame.init()
pygame.display.set_caption('Dice Game')


def welcomePage():
    global gameTitle
    gameTitle = renderFont(100).render('DICE GAME', True, WHITE)

    while True:
        backGround('bgc')
        displayItem(gameTitle, (HEIGHT/2-(gameTitle.get_height()/2)))
        startBtnY = 475
        leaderboardBtnY = 525
        displayBtn(renderFont(20), 'START GAME', startBtnY)
        displayBtn(renderFont(20), 'LEADERBOARD', leaderboardBtnY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if clickedBtn(event.pos, startBtnY):
                        runGame()
                    if clickedBtn(event.pos, leaderboardBtnY):
                        leaderboard()

        pygame.display.update()


def runGame():
    whoseTurn = 0
    diceNumber = 6
    playerPoints = 0
    playerTurnPoints = 0
    computerPoints = 0
    computerTurnPoints = 0

    i = 1

    while True:
        backGround('game-bgc')
        displayStats('You', playerPoints, playerTurnPoints, 400)
        displayStats('Computer', computerPoints, computerTurnPoints, 800)
        newGameBtnY = 175
        backBtnX = 1180
        backBtnY = 650
        holdBtnY = 525
        rollBtnY = 475
        displayBtn(renderFont(20), 'ROLL DICE', rollBtnY)
        displayBtn(renderFont(20), 'HOLD', holdBtnY)
        displayBtn(renderFont(20), 'NEW GAME', newGameBtnY)
        displayBtn(renderFont(20), 'GO BACK',
                   backBtnY, width=100, posX=backBtnX)

        time.sleep(0.4)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if clickedBtn(event.pos, newGameBtnY):
                    diceNumber = 6
                    whoseTurn = 0
                    playerPoints = 0
                    playerTurnPoints = 0
                    computerPoints = 0
                    computerTurnPoints = 0

                if clickedBtn(event.pos, backBtnY, x=backBtnX, width=100):
                    welcomePage()

                if whoseTurn == 0:
                    if clickedBtn(event.pos, rollBtnY):
                        score = rollDice()
                        playerTurnPoints += score
                        diceNumber = score

                        if score == 1:
                            playerTurnPoints = 0
                            displayDice(diceNumber)
                            pygame.display.update()
                            rollTimes = random.randint(1, 6)
                            time.sleep(0.4)
                            whoseTurn = 1

                    if clickedBtn(event.pos, holdBtnY):
                        playerPoints += playerTurnPoints
                        playerTurnPoints = 0
                        rollTimes = random.randint(1, 6)
                        whoseTurn = 1

        if whoseTurn == 1:
            displayBtn(renderFont(20), 'ROLL DICE', rollBtnY, color=GREY)
            displayBtn(renderFont(20), 'HOLD', holdBtnY, color=GREY)

            if computerPoints + computerTurnPoints >= 100:
                global winnerName
                winnerName = 'Computer'
                saveWinner('COMPUTER')
                gameEnded()

            if i <= rollTimes:
                score = rollDice()
                i += 1
                computerTurnPoints += score
                diceNumber = score

                if score == 1:
                    i = 1
                    computerTurnPoints = 0
                    whoseTurn = 0

            else:
                computerPoints += computerTurnPoints
                computerTurnPoints = 0
                i = 1
                whoseTurn = 0

        displayDice(diceNumber)

        def saveWinner(name):
            winnerList = open("data/winners.txt", "a")
            winnerList.write(name + "\n")
            winnerList.close()

        if playerPoints >= 100:
            winnerName = 'You'
            saveWinner('YOU')
            gameEnded()

        CLOCK.tick(FPS)
        pygame.display.update()


def leaderboard():
    winners = [winner.rstrip() for winner in open("data/winners.txt", "r")]

    def victories(name):
        sum = 0
        for i in winners:
            if i == name:
                sum += 1

        assert sum == winners.count(name)

        return sum

    winnersDict = {'YOU': victories('YOU'), 'COMPUTER': victories('COMPUTER')}
    assert len(winnersDict) == 2, "Number of players must equal 2"

    def stats(id):
        return f'{list(winnersDict.keys())[id]}: {list(winnersDict.values())[id]}'

    result = renderFont(75).render('DICE GAME', True, WHITE)

    player = renderFont(25).render(stats(0), True, WHITE)
    computer = renderFont(25).render(stats(1), True, WHITE)

    while True:
        backGround('bgc')

        displayItem(result, 100)
        if victories('YOU') >= victories('COMPUTER'):
            displayItem(player, 250)
            displayItem(computer, 300)
        else:
            displayItem(computer, 250)
            displayItem(player, 300)

        btnY = 600
        displayBtn(renderFont(20), 'GO BACK', btnY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if clickedBtn(event.pos, btnY):
                        return

        pygame.display.update()


def gameEnded():
    winner = renderFont(50).render(f'{winnerName} win!', True, WHITE)

    while True:
        backGround('bgc')
        displayItem(gameTitle, 100)
        displayItem(winner, 300)
        btnY = 475
        displayBtn(renderFont(20), 'GO BACK', btnY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if clickedBtn(event.pos, btnY):
                        welcomePage()

        pygame.display.update()
