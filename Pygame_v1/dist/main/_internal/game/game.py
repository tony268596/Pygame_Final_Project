import pygame
from game.controller import GameControl
from game.model import GameModel
from game.view import GameView
from settings import FPS, game_status, LEVEL_FINISH_TIMES


class Game:
    def run(self, checkpoint):
        '''game start'''

        # initialization
        pygame.init()
        # core of the game (database, game logic...)
        game_model = GameModel(checkpoint)
        game_view = GameView(checkpoint)  # render everything
        # deal with the game flow and user request
        game_control = GameControl(game_model, game_view)
        while game_status["run"] and not game_status["go_start_menu"] and not game_status["go_level_menu"]:
            pygame.time.Clock().tick(FPS)  # control the frame rate
            game_control.receive_user_input()  # receive user input
            game_control.money_counter()
            game_control.update_model()  # update the model
            game_control.update_view()  # update the view
            pygame.display.update()
            if checkpoint == 1:
                if game_control.win_or_not:
                    LEVEL_FINISH_TIMES[0] += 1
            elif checkpoint == 2:
                if game_control.win_or_not:
                    LEVEL_FINISH_TIMES[1] += 1
            else:
                if game_control.win_or_not:
                    LEVEL_FINISH_TIMES[2] += 1
            game_status["run"] = game_control.quit_game
