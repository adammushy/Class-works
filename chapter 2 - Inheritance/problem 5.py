class WinTeam:
    goal_scorer=input("enter the goal scorer:: ")
    
    def Display(self):
        print("\nThere is no giant club in Tanzania such as YANGA \n")
        
class SomeWonGames(WinTeam):
    def display_games(self):
        print("Azam lost 2-0 in the first Leg \n")
        print("KMC lost 2-0 in First leg and Second leg \n")
        

class YangaBingwa(SomeWonGames):
    def display_message(self):
        
        print(f"No one like {self.goal_scorer.upper()} \n")
        



mpira=YangaBingwa()
mpira.Display()
mpira.display_games()
mpira.display_message()