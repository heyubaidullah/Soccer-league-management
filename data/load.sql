- Insert data into Tournament table
INSERT INTO Tournament (to_id, to_name) VALUES
(1, 'Belgium Jupiler League'),
(2, 'England Premier League'),
(3, 'France Ligue 1'),
(4, 'Germany Bundesliga'),
(5, 'Italy Serie A'),
(6, 'Netherlands Eredivisie'),
(7, 'Poland Ekstraklasa'),
(8, 'Portugal Liga ZON Sagres'),
(9, 'Scotland Premier League'),
(10, 'Spain LIGA BBVA'),
(11, 'Switzerland Super League');

-- Insert data into Team table
COPY Team (te_id, te_name, home_stadium, to_id)
FROM 'C:/Users/del028/Downloads/DBMS_Proj/del028_project/data/transformed/Team.csv'
DELIMITER ',' CSV HEADER;

-- Insert data into Venue table
INSERT INTO Venue (v_id, v_name, location, capacity) VALUES
(1, 'Stamford Bridge', 'London', 40000),
(2, 'San Siro', 'Milan', 75000),
(3, 'Allianz Arena', 'Munich', 70000),
(4, 'Old Trafford', 'Manchester', 76000),
(5, 'Camp Nou', 'Barcelona', 99354),
(6, 'Santiago Bernabéu', 'Madrid', 81000),
(7, 'Wembley Stadium', 'London', 90000),
(8, 'Anfield', 'Liverpool', 54000),
(9, 'Etihad Stadium', 'Manchester', 55000),
(10, 'Parc des Princes', 'Paris', 48000),
(11, 'Signal Iduna Park', 'Dortmund', 81365),
(12, 'Emirates Stadium', 'London', 60000),
(13, 'Stadio Olimpico', 'Rome', 70000),
(14, 'King Power Stadium', 'Leicester', 32000),
(15, 'Veltins-Arena', 'Gelsenkirchen', 62271),
(16, 'Giuseppe Meazza', 'Milan', 80000),
(17, 'Puskás Aréna', 'Budapest', 67000),
(18, 'Amsterdam Arena', 'Amsterdam', 53700),
(19, 'Red Bull Arena', 'Leipzig', 42558),
(20, 'Turf Moor', 'Burnley', 22000),
(21, 'Ibrox Stadium', 'Glasgow', 50000),
(22, 'Stade de France', 'Saint-Denis', 81000),
(23, 'Stamford Bridge', 'London', 40000),
(24, 'Molineux Stadium', 'Wolverhampton', 32000);


-- Insert data into Player table
COPY Player (p_id, player_name, te_id)
FROM 'C:/Users/del028/Downloads/DBMS_Proj/del028_project/data/transformed/Player.csv'
DELIMITER ',' CSV HEADER;

INSERT INTO coach (c_id, c_name, te_id) VALUES
(6, 'Alex Hamilton', 6),
(7, 'Sophia Johnson', 7),
(8, 'Liam Smith', 8),
(9, 'Olivia Martinez', 9),
(10, 'James Anderson', 10),
(11, 'Isabella Garcia', 11),
(12, 'Ethan Thomas', 12),
(13, 'Mia Wilson', 13),
(14, 'Aiden Brown', 14),
(15, 'Charlotte Moore', 15),
(16, 'Lucas Lee', 16),
(17, 'Amelia Taylor', 17),
(18, 'Benjamin Davis', 18),
(19, 'Harper Hernandez', 19),
(20, 'Michael Robinson', 20),
(21, 'Ella Clark', 21),
(22, 'Alexander Lewis', 22),
(23, 'Abigail Young', 23),
(24, 'Daniel King', 24),
(25, 'Emily Martinez', 25),
(26, 'Matthew Hall', 26),
(27, 'Ava Allen', 27),
(28, 'Joseph Scott', 28),
(29, 'Sofia Green', 29),
(30, 'Samuel Perez', 30),
(31, 'Scarlett Walker', 31),
(32, 'Jackson Harris', 32),
(33, 'Victoria Carter', 33),
(34, 'Henry Adams', 34),
(35, 'Aria Nelson', 35),
(36, 'Sebastian Baker', 36),
(37, 'Grace Mitchell', 37),
(38, 'Owen Edwards', 38),
(39, 'Chloe Rivera', 39),
(40, 'Jack Ramirez', 40),
(41, 'Layla Phillips', 41),
(42, 'Levi Campbell', 42),
(43, 'Penelope Evans', 43),
(44, 'Gabriel Turner', 44),
(45, 'Hannah Torres', 45),
(46, 'Carter Parker', 46),
(47, 'Zoey Collins', 47),
(48, 'Julian Stewart', 48),
(49, 'Lillian Sanchez', 49),
(50, 'Wyatt Morris', 50),
(51, 'Addison Rogers', 51),
(52, 'Ryan Murphy', 52),
(53, 'Natalie Reed', 53),
(54, 'Nathan Cook', 54),
(55, 'Stella Morgan', 55),
(56, 'Caleb Bell', 56),
(57, 'Lucy Bailey', 57),
(58, 'Isaiah Rivera', 58),
(59, 'Paisley Jenkins', 59),
(60, 'Hunter Brooks', 60),
(61, 'Nora Howard', 61),
(62, 'Andrew Ward', 62),
(63, 'Zoe Griffin', 63),
(64, 'Christian Cooper', 64),
(65, 'Audrey Cox', 65),
(66, 'Jonathan Peterson', 66),
(67, 'Ellie Powell', 67),
(68, 'Thomas Richardson', 68),
(69, 'Riley James', 69),
(70, 'Charles Bennett', 70),
(71, 'Savannah Coleman', 71),
(72, 'Christopher Gray', 72),
(73, 'Skylar Foster', 73),
(74, 'Jaxon Simmons', 74),
(75, 'Brooklyn Ross', 75),
(76, 'Ezra Diaz', 76),
(77, 'Claire Myers', 77),
(78, 'Aaron Ward', 78),
(79, 'Camila Long', 79),
(80, 'Eli Kelly', 80),
(81, 'Violet Sanders', 81),
(82, 'Anthony Price', 82),
(83, 'Aurora Russell', 83),
(84, 'Isaac Butler', 84),
(85, 'Hazel Barnes', 85),
(86, 'Luke Hayes', 86),
(87, 'Bella Ramirez', 87),
(88, 'Lincoln Cox', 88),
(89, 'Samantha Powell', 89),
(90, 'Hudson Hughes', 90),
(91, 'Leah Perry', 91),
(92, 'Grayson Wood', 92),
(93, 'Sadie Brooks', 93),
(94, 'Dylan Evans', 94),
(95, 'Madelyn Jenkins', 95),
(96, 'Wyatt Simmons', 96),
(97, 'Aubrey Foster', 97),
(98, 'Asher Sanders', 98),
(99, 'Eleanor Cook', 99),
(100, 'Miles Butler', 100),
(101, 'Stella Wright', 101),
(102, 'Landon Green', 102);

