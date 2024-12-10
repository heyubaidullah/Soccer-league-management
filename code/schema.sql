-- Drop tables if they already exist
DROP TABLE IF EXISTS Match CASCADE;
DROP TABLE IF EXISTS Match_Tournament CASCADE;
DROP TABLE IF EXISTS Team_Tournament CASCADE;
DROP TABLE IF EXISTS Player CASCADE;
DROP TABLE IF EXISTS Coach CASCADE;
DROP TABLE IF EXISTS Tournament CASCADE;
DROP TABLE IF EXISTS Venue CASCADE;
DROP TABLE IF EXISTS Team CASCADE;

-- Create Tournament Table
CREATE TABLE Tournament (
    to_id SERIAL PRIMARY KEY,
    to_name VARCHAR(100) NOT NULL,
    year INT
);

-- Create Team Table with Mandatory Tournament Association
CREATE TABLE Team (
    te_id SERIAL PRIMARY KEY,
    te_name VARCHAR(100) NOT NULL,
    home_stadium VARCHAR(100),
    to_id INT NOT NULL,  -- Participation constraint: each team must participate in at least one tournament
    FOREIGN KEY (to_id) REFERENCES Tournament(to_id) ON DELETE CASCADE
);

-- Create Team_Tournament Table for Many-to-Many Relationship
CREATE TABLE Team_Tournament (
    te_id INT NOT NULL,
    to_id INT NOT NULL,
    PRIMARY KEY (te_id, to_id),
    FOREIGN KEY (te_id) REFERENCES Team(te_id) ON DELETE CASCADE,
    FOREIGN KEY (to_id) REFERENCES Tournament(to_id) ON DELETE CASCADE
);

-- Create Player Table with Team Participation Constraint
CREATE TABLE Player (
    p_id SERIAL PRIMARY KEY,
    player_name VARCHAR(100) NOT NULL,
    te_id INT NOT NULL,  -- Participation and Key Constraint: each player must belong to a team
    FOREIGN KEY (te_id) REFERENCES Team(te_id) ON DELETE CASCADE
);

-- Create Coach Table with Team Participation Constraint (without UNIQUE)
CREATE TABLE Coach (
    c_id SERIAL PRIMARY KEY,
    c_name VARCHAR(100) NOT NULL,
    te_id INT NOT NULL,  -- Participation constraint: each coach must belong to one team
    FOREIGN KEY (te_id) REFERENCES Team(te_id) ON DELETE CASCADE
);

-- Create Venue Table
CREATE TABLE Venue (
    v_id SERIAL PRIMARY KEY,
    v_name VARCHAR(100) NOT NULL,
    location VARCHAR(100),
    capacity INT
);

-- Create Match Table with Venue Participation Constraint
CREATE TABLE Match (
    m_id SERIAL PRIMARY KEY,
    home_team_id INT NOT NULL,
    away_team_id INT NOT NULL,
    date DATE NOT NULL,
    score VARCHAR(10),
    v_id INT NOT NULL,  -- Participation constraint: each match must be scheduled at one venue
    FOREIGN KEY (home_team_id) REFERENCES Team(te_id) ON DELETE CASCADE,
    FOREIGN KEY (away_team_id) REFERENCES Team(te_id) ON DELETE CASCADE,
    FOREIGN KEY (v_id) REFERENCES Venue(v_id) ON DELETE CASCADE
);

-- Create Match_Tournament Table for Many-to-Many Relationship
CREATE TABLE Match_Tournament (
    m_id INT NOT NULL,
    to_id INT NOT NULL,
    PRIMARY KEY (m_id, to_id),
    FOREIGN KEY (m_id) REFERENCES Match(m_id) ON DELETE CASCADE,
    FOREIGN KEY (to_id) REFERENCES Tournament(to_id) ON DELETE CASCADE
);
