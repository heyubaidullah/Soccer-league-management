import pandas as pd

# File paths
data_dir = 'C:/Users/del028/Downloads/DBMS_Proj/del028_project/data/csv/'
output_dir = 'C:/Users/del028/Downloads/DBMS_Proj/del028_project/data/transformed/'

# Load CSV files
league = pd.read_csv(data_dir + 'League.csv')
match = pd.read_csv(data_dir + 'Match.csv')
player = pd.read_csv(data_dir + 'Player.csv')
team = pd.read_csv(data_dir + 'Team.csv')

# Transform League → Tournament
tournament = league[['id', 'name']].rename(columns={
    'id': 'to_id',
    'name': 'to_name'
})
tournament['year'] = 2024  # Placeholder year
tournament.to_csv(output_dir + 'Tournament.csv', index=False)

# Transform Team
team_transformed = team[['id', 'team_long_name']].rename(columns={
    'id': 'te_id',
    'team_long_name': 'te_name'
})
team_transformed['home_stadium'] = None  # Placeholder for missing data
team_transformed['to_id'] = None  # Placeholder, requires mapping
team_transformed.to_csv(output_dir + 'Team.csv', index=False)

# Transform Player
player_transformed = player[['id', 'player_name']].rename(columns={
    'id': 'p_id'
})
player_transformed['te_id'] = None  # Placeholder, requires mapping
player_transformed.to_csv(output_dir + 'Player.csv', index=False)

# Transform Match
match['score'] = match['home_team_goal'].astype(str) + '-' + match['away_team_goal'].astype(str)
match_transformed = match[['id', 'home_team_api_id', 'away_team_api_id', 'date', 'score']].rename(columns={
    'id': 'm_id',
    'home_team_api_id': 'home_team_id',
    'away_team_api_id': 'away_team_id'
})
match_transformed['v_id'] = None  # Placeholder for venue data
match_transformed.to_csv(output_dir + 'Match.csv', index=False)

print("Transformation complete. Files saved in", output_dir)
