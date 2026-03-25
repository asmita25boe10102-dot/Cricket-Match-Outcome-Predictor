import joblib
import numpy as np

model = joblib.load('model.pkl')
team_enc = joblib.load('team.pkl')
venue_enc = joblib.load('venue.pkl')
toss_enc = joblib.load('toss.pkl')
decision_enc = joblib.load('decision.pkl')
winner_enc = joblib.load('winner.pkl')

def get_input(options, name):
    print(f"\nSelect {name}:")
    for i, opt in enumerate(options):
        print(f"{i}: {opt}")
    choice = int(input("Enter number: "))
    return options[choice]

def main():
    print("🏏 IPL Match Predictor (Python Version)\n")

    teams = list(team_enc.classes_)
    venues = list(venue_enc.classes_)

    team1 = get_input(teams, "Team 1")
    team2 = get_input(teams, "Team 2")
    venue = get_input(venues, "Venue")
    toss_winner = get_input(teams, "Toss Winner")

    print("\nToss Decision:")
    print("0: Bat\n1: Field")
    decision = int(input("Enter number: "))
    toss_decision = "bat" if decision == 0 else "field"

    season = int(input("\nEnter Season (e.g., 2019): "))

    
    data = np.array([[
        team_enc.transform([team1])[0],
        team_enc.transform([team2])[0],
        toss_enc.transform([toss_winner])[0],
        decision_enc.transform([toss_decision])[0],
        venue_enc.transform([venue])[0],
        season
    ]])

    
    pred = model.predict(data)[0]
    prob = max(model.predict_proba(data)[0]) * 100

    winner = winner_enc.inverse_transform([pred])[0]

    print("\n🏆 Predicted Winner:", winner)
    print(f"📊 Win Probability: {prob:.2f}%")

if __name__ == "__main__":
    main()
