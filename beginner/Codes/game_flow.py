import random
from crewai.flow.flow import Flow, listen, router, start
from pydantic import BaseModel


class GameSession(BaseModel):
    player_won: bool = False


class GameFlow(Flow[GameSession]):

    @start()
    def begin_start(self):
        print("Starting the game session")
        player_outcome = random.choice([True, False])
        self.state.player_won = player_outcome

    @router(begin_start)
    def check_outcome(self):
        if self.state.player_won:
            return "win"
        else:
            return "lose"

    @listen("win")
    def celebrate_win(self):
        print("Congratulations!")

    @listen("lose")
    def console_loss(self):
        print("Game Over!")


flow = GameFlow()
flow.kickoff()
