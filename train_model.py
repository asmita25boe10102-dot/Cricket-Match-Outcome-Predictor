import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import joblib


df = pd.read_csv('../data/matches.csv')


df = df.dropna(subset=['winner'])


df = df[['team1', 'team2', 'toss_winner', 'toss_decision', 'venue', 'season', 'winner']]


le_team = LabelEncoder()
le_venue = LabelEncoder()
le_toss = LabelEncoder()
le_decision = LabelEncoder()
le_winner = LabelEncoder()


df['team1'] = le_team.fit_transform(df['team1'])
df['team2'] = le_team.transform(df['team2'])
df['toss_winner'] = le_toss.fit_transform(df['toss_winner'])
df['toss_decision'] = le_decision.fit_transform(df['toss_decision'])
df['venue'] = le_venue.fit_transform(df['venue'])
df['winner'] = le_winner.fit_transform(df['winner'])


X = df.drop('winner', axis=1)
y = df['winner']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)


joblib.dump(model, '../model/predictor.pkl')
joblib.dump(le_team, '../model/team_encoder.pkl')
joblib.dump(le_venue, '../model/venue_encoder.pkl')
joblib.dump(le_toss, '../model/toss_encoder.pkl')
joblib.dump(le_decision, '../model/decision_encoder.pkl')
joblib.dump(le_winner, '../model/winner_encoder.pkl')

print("Model trained and saved successfully!")
