class Player:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

class CricketGame:
    def __init__(self):
        self.team1 = None
        self.team2 = None

    def welcome_msg(self):
        print("Welcome to the cricket score board")
        print("In this game, a team is allowed to score the following:")
        print("1: for a single (causes change in strike)")
        print("2: for a double")
        print("3: for a triple (causes change of strike)")
        print("4: for a four (boundary)")
        print("W: for a wicket (next batsman comes in)")
        print("WD: for a wide (need to bowl the same delivery)")

    def get_players(self, team):
        for i in range(1, 5):
            player_name = input(f"Enter name of player {i} for {team.name}: ")
            player = Player(player_name)
            team.add_player(player)

    def set_over(self, ball_number):
        first = ball_number // 7
        second = ball_number % 7
        over_number = str(first) + "." + str(second)
        return over_number

    def over_summary(self, team, over, wicket, score):
        print()
        print("END of OVER")
        print(f"{team.name} {score}/{wicket} {over}")

    def first_innings(self, team):
        ball_counter = 1
        wicket_counter = 0
        team_score = 0
        temp_over = 1
        while ball_counter <= 12 and wicket_counter < 3:
            over = self.set_over(ball_counter)
            if int(over[0]) == temp_over:
                self.over_summary(team, over, wicket_counter, team_score)
                temp_over += 1
            run = input(f"Enter the run for over {over}?  ")
            if run in ["0", "1", "2", "3", "4", "6"]:
                team_score += int(run)
                ball_counter += 1
            elif run == "WD":
                team_score += 1
            elif run == "W":
                wicket_counter += 1
                ball_counter += 1
            else:
                print("Enter a valid run [1, 2, 3, 4, 6, W, WD]")
        self.over_summary(team, over, wicket_counter, team_score)
        print()
        print("End of first innings")

    def second_innings(self):
        print(f"Second innings summary for {self.team2.name}")
        ball_counter = 1
        wicket_counter = 0
        team2_score = 0
        temp_over = 1

        while ball_counter <= 12 and wicket_counter < 3:
            over = self.set_over(ball_counter)
            if int(over[0]) == temp_over:
                self.over_summary(self.team2, over, wicket_counter, team2_score)
                temp_over += 1

            run = input(f"Enter the run for over {over}?  ")
            if run in ["0", "1", "2", "3", "4", "6"]:
                team2_score += int(run)
                ball_counter += 1
            elif run == "WD":
                team2_score += 1
            elif run == "W":
                wicket_counter += 1
                ball_counter += 1
            else:
                print("Enter a valid run [1, 2, 3, 4, 6, W, WD]")

        self.over_summary(self.team2, over, wicket_counter, team2_score)
        print()
        print(f"End of {self.team2.name}'s innings")
        print(f"{self.team1.name} needs {team2_score + 1} runs to win.")


    def start_game(self):
        while True:
            self.welcome_msg()
            self.team1 = Team(input("Enter the team 1 name? "))
            self.team2 = Team(input("Enter the team 2 name? "))
            self.get_players(self.team1)
            self.get_players(self.team2)
            self.first_innings(self.team1)
            self.second_innings()
            self.final_summary()
            while True:
                answer = input("Do you want to play again? (Y/N) ")
                if answer not in ["Y", "N"]:
                    print("Enter a valid choice (Y/N)")
                else:
                    break
            if answer == "N":
                break

    def final_summary(self, team1_score, team2_score):
        print("Final Summary:")
        print(f"{self.team1.name}: {team1_score} runs")
        print(f"{self.team2.name}: {team2_score} runs")

        if team1_score > team2_score:
            print(f"{self.team1.name} wins by {team1_score - team2_score} runs!")
        elif team1_score < team2_score:
            print(f"{self.team2.name} wins by {team2_score - team1_score} runs!")
        else:
            print("It's a tie!")


if __name__ == "__main__":
    game = CricketGame()
    game.start_game()
