import streamlit as st
import psycopg2
import pandas as pd

# Database connection parameters
def init_connection():
    return psycopg2.connect(
        host="localhost",
        database="sports_league",  
        user="postgres",             
        password="admin"             
    )

conn = init_connection()

# Function to execute a query
def run_query(query, params=None):
    with conn.cursor() as cur:
        cur.execute(query, params)
        if query.strip().lower().startswith("select"):
            return cur.fetchall()
        else:
            conn.commit()

# Function to fetch data as DataFrame
def fetch_dataframe(query, params=None):
    return pd.read_sql(query, conn, params=params)

# Customizing page layout and style
st.set_page_config(page_title="Sports Management System", layout="wide")
st.markdown("""
    <style>
    .main {
        background-color: #18b5a0;
        color: #333;
    }
    .sidebar .sidebar-content {
        background-color: #95f0d7;
    }
    h1, h2, h3 {
        color: #edec9f;
    }
    .stButton>button {
        background-color: #3D8C7A;
        color: white;
    }
    .stSelectbox>label {
        text-align: center;
    }
    .menu-container {
        display: flex;
        justify-content: center;
        gap: 20px;
    }
    .menu-container button {
        padding: 10px 20px;
        background-color: #3D8C7A;
        color: white;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Horizontal navigation with buttons
st.title("Soccer League Management System 🏆")
menu = None  # Variable to hold the selected menu option

# Create a container for the menu buttons
st.markdown('<div class="menu-container">', unsafe_allow_html=True)

# Define columns for each button
col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    if st.button("Teams"):
        menu = "Teams"
with col2:
    if st.button("Matches"):
        menu = "Matches"
with col3:
    if st.button("Tournaments"):
        menu = "Tournaments"
with col4:
    if st.button("Players"):
        menu = "Players"
with col5:
    if st.button("Coaches"):
        menu = "Coaches"
with col6:
    if st.button("Venues"):
        menu = "Venues"

st.markdown('</div>', unsafe_allow_html=True)


if menu == "Teams":
    st.title("Teams Management")

    # Add filter for tournaments
    tournaments = fetch_dataframe("SELECT to_id, to_name FROM Tournament")
    tournament_options = dict(zip(tournaments['to_name'], tournaments['to_id']))
    selected_tournament = st.selectbox("Filter by Tournament", ["All"] + list(tournament_options.keys()))

    query = "SELECT te_id, te_name, home_stadium FROM Team"
    params = []
    if selected_tournament != "All":
        query += " WHERE to_id = %s"
        params.append(tournament_options[selected_tournament])
    teams = fetch_dataframe(query, params)

    st.dataframe(teams)

    # Add a new team
    st.subheader("Add New Team")
    with st.form(key='add_team'):
        team_name = st.text_input("Team Name")
        home_stadium = st.text_input("Home Stadium")
        tournament_choice = st.selectbox("Assign to Tournament", options=tournament_options.keys())
        submit = st.form_submit_button(label='Add Team')
    if submit:
        if team_name and home_stadium and tournament_choice:
            run_query(
                "INSERT INTO Team (te_name, home_stadium, to_id) VALUES (%s, %s, %s)",
                (team_name, home_stadium, tournament_options[tournament_choice])
            )
            st.success("Team added successfully!")

    # Delete a team
    st.subheader("Delete a Team")
    if not teams.empty:
        team_options = dict(zip(teams['te_name'], teams['te_id']))
        team_to_delete = st.selectbox("Select Team to Delete", options=team_options.keys())
        delete_confirm = st.button("Delete Team")
        if delete_confirm:
            run_query("DELETE FROM Team WHERE te_id = %s", (team_options[team_to_delete],))
            st.success(f"Team '{team_to_delete}' deleted successfully!")
    else:
        st.info("No teams available to delete.")

elif menu == "Matches":
    st.title("Matches Management")

    # Filter matches by venue
    venues = fetch_dataframe("SELECT v_id, v_name FROM Venue")
    venue_options = dict(zip(venues['v_name'], venues['v_id']))
    selected_venue = st.selectbox("Filter by Venue", ["All"] + list(venue_options.keys()))

    query = """
        SELECT m.m_id, t1.te_name AS home_team, t2.te_name AS away_team, 
               m.date, m.score, v.v_name AS venue
        FROM Match m
        JOIN Team t1 ON m.home_team_id = t1.te_id
        JOIN Team t2 ON m.away_team_id = t2.te_id
        JOIN Venue v ON m.v_id = v.v_id
    """
    params = []
    if selected_venue != "All":
        query += " WHERE m.v_id = %s"
        params.append(venue_options[selected_venue])
    matches = fetch_dataframe(query, params)

    st.dataframe(matches)

    # Add a new match
    st.subheader("Add New Match")
    with st.form(key='add_match'):
        teams = fetch_dataframe("SELECT te_id, te_name FROM Team")
        team_options = dict(zip(teams['te_name'], teams['te_id']))
        home_team = st.selectbox("Home Team", options=team_options.keys())
        away_team = st.selectbox("Away Team", options=team_options.keys())
        match_date = st.date_input("Match Date")
        venue_choice = st.selectbox("Venue", options=venue_options.keys())
        submit = st.form_submit_button(label='Add Match')
    if submit:
        if home_team and away_team and match_date and venue_choice:
            run_query(
                "INSERT INTO Match (home_team_id, away_team_id, date, v_id) VALUES (%s, %s, %s, %s)",
                (team_options[home_team], team_options[away_team], match_date, venue_options[venue_choice])
            )
            st.success("Match added successfully!")

    # Delete a match
    st.subheader("Delete a Match")
    if not matches.empty:
        match_options = dict(zip(matches['m_id'], matches['home_team'] + " vs " + matches['away_team']))
        match_to_delete = st.selectbox("Select Match to Delete", options=match_options.keys())
        delete_confirm = st.button("Delete Match")
        if delete_confirm:
            run_query("DELETE FROM Match WHERE m_id = %s", (match_to_delete,))
            st.success("Match deleted successfully!")
    else:
        st.info("No matches available to delete.")

elif menu == "Tournaments":
    st.title("Tournaments Management")
    tournaments = fetch_dataframe("SELECT to_id, to_name, year FROM Tournament")
    st.dataframe(tournaments)

    # Add a new tournament
    st.subheader("Add New Tournament")
    with st.form(key='add_tournament'):
        tournament_name = st.text_input("Tournament Name")
        year = st.number_input("Year", min_value=1900, max_value=2100, step=1)
        submit = st.form_submit_button(label='Add Tournament')
    if submit:
        if tournament_name and year:
            run_query(
                "INSERT INTO Tournament (to_name, year) VALUES (%s, %s)",
                (tournament_name, year)
            )
            st.success("Tournament added successfully!")

    # Delete a tournament
    st.subheader("Delete a Tournament")
    if not tournaments.empty:
        tournament_options = dict(zip(tournaments['to_name'], tournaments['to_id']))
        tournament_to_delete = st.selectbox("Select Tournament to Delete", options=tournament_options.keys())
        delete_confirm = st.button("Delete Tournament")
        if delete_confirm:
            run_query("DELETE FROM Tournament WHERE to_id = %s", (tournament_options[tournament_to_delete],))
            st.success(f"Tournament '{tournament_to_delete}' deleted successfully!")
    else:
        st.info("No tournaments available to delete.")

elif menu == "Players":
    st.title("Players Management")
    players = fetch_dataframe("""
        SELECT p.p_id, p.player_name, t.te_name AS team
        FROM Player p
        JOIN Team t ON p.te_id = t.te_id
    """)
    st.dataframe(players)

    # Add a new player
    st.subheader("Add New Player")
    with st.form(key='add_player'):
        player_name = st.text_input("Player Name")
        teams = fetch_dataframe("SELECT te_id, te_name FROM Team")
        team_options = dict(zip(teams['te_name'], teams['te_id']))
        team_choice = st.selectbox("Assign to Team", options=team_options.keys())
        submit = st.form_submit_button(label='Add Player')
    if submit:
        if player_name and team_choice:
            run_query(
                "INSERT INTO Player (player_name, te_id) VALUES (%s, %s)",
                (player_name, team_options[team_choice])
            )
            st.success("Player added successfully!")

    # Delete a player
    st.subheader("Delete a Player")
    if not players.empty:
        player_options = dict(zip(players['player_name'], players['p_id']))
        player_to_delete = st.selectbox("Select Player to Delete", options=player_options.keys())
        delete_confirm = st.button("Delete Player")
        if delete_confirm:
            run_query("DELETE FROM Player WHERE p_id = %s", (player_options[player_to_delete],))
            st.success(f"Player '{player_to_delete}' deleted successfully!")
    else:
        st.info("No players available to delete.")

elif menu == "Coaches":
    st.title("Coaches Management")
    coaches = fetch_dataframe("""
        SELECT c.c_id, c.c_name AS coach_name, t.te_name AS team
        FROM Coach c
        JOIN Team t ON c.te_id = t.te_id
    """)
    st.dataframe(coaches)

    # Add a new coach
    # Add a new coach
    st.subheader("Add New Coach")
    with st.form(key='add_coach'):
        coach_name = st.text_input("Coach Name")
        teams = fetch_dataframe("SELECT te_id, te_name FROM Team")
        team_options = dict(zip(teams['te_name'], teams['te_id']))
        team_choice = st.selectbox("Assign to Team", options=team_options.keys())
        submit = st.form_submit_button(label='Add Coach')
    if submit:
        if coach_name and team_choice:
            run_query(
                "INSERT INTO Coach (c_name, te_id) VALUES (%s, %s)",
                (coach_name, team_options[team_choice])
            )
            st.success("Coach added successfully!")

    # Delete a coach
    st.subheader("Delete a Coach")
    if not coaches.empty:
        coach_options = dict(zip(coaches['coach_name'], coaches['c_id']))
        coach_to_delete = st.selectbox("Select Coach to Delete", options=coach_options.keys())
        delete_confirm = st.button("Delete Coach")
        if delete_confirm:
            run_query("DELETE FROM Coach WHERE c_id = %s", (coach_options[coach_to_delete],))
            st.success(f"Coach '{coach_to_delete}' deleted successfully!")
    else:
        st.info("No coaches available to delete.")

elif menu == "Venues":
    st.title("Venues Management")
    venues = fetch_dataframe("SELECT v_id, v_name, location FROM Venue")
    st.dataframe(venues)

    # Add a new venue
    st.subheader("Add New Venue")
    with st.form(key='add_venue'):
        venue_name = st.text_input("Venue Name")
        location = st.text_input("Location")
        submit = st.form_submit_button(label='Add Venue')
    if submit:
        if venue_name and location:
            run_query(
                "INSERT INTO Venue (v_name, location) VALUES (%s, %s)",
                (venue_name, location)
            )
            st.success("Venue added successfully!")

    # Delete a venue
    st.subheader("Delete a Venue")
    if not venues.empty:
        venue_options = dict(zip(venues['v_name'], venues['v_id']))
        venue_to_delete = st.selectbox("Select Venue to Delete", options=venue_options.keys())
        delete_confirm = st.button("Delete Venue")
        if delete_confirm:
            run_query("DELETE FROM Venue WHERE v_id = %s", (venue_options[venue_to_delete],))
            st.success(f"Venue '{venue_to_delete}' deleted successfully!")
    else:
        st.info("No venues available to delete.")

elif menu == "Your Team":
    st.title("Create Your Team 🏆")

    # Team name input
    team_name = st.text_input("Enter Team Name")

    # Home stadium selection
    venues = fetch_dataframe("SELECT v_id, v_name FROM Venue")
    venue_options = dict(zip(venues['v_name'], venues['v_id']))
    home_stadium = st.selectbox("Select Home Stadium", options=venue_options.keys())

    # Tournament selection
    tournaments = fetch_dataframe("SELECT to_id, to_name FROM Tournament")
    tournament_options = dict(zip(tournaments['to_name'], tournaments['to_id']))
    selected_tournament = st.selectbox("Select Tournament", options=tournament_options.keys())

    # Player selection
    players = fetch_dataframe("SELECT p_id, player_name FROM Player")
    player_options = dict(zip(players['player_name'], players['p_id']))
    selected_players = st.multiselect("Select Players for Your Team", options=player_options.keys())

    # Submit form
    submit = st.button("Create Team")
    
    if submit:
        if team_name and home_stadium and selected_players and selected_tournament:
            # Insert new team into Team table
            run_query(
                "INSERT INTO Team (te_name, home_stadium, to_id) VALUES (%s, %s, %s)",
                (team_name, home_stadium, tournament_options[selected_tournament])
            )

            # Get the ID of the newly added team
            team_id = fetch_dataframe("SELECT te_id FROM Team WHERE te_name = %s", (team_name,)).iloc[0]['te_id']

            # Associate selected players with the new team
            for player in selected_players:
                player_id = player_options[player]
                run_query(
                    "UPDATE Player SET te_id = %s WHERE p_id = %s",
                    (team_id, player_id)
                )

            st.success(f"Your team '{team_name}' has been created and players have been added!")
        else:
            st.warning("Please fill out all fields to create your team.")
