-- Run create database
CREATE DATABASE introverse;
USE introverse;


-- Table for forum message board, this table needs to be created in MySQL so that it can have the MySQL default method of getting the time for the example data
-- Going to drop the foreign key constraint on author to prevent any errors from creating mock posts to display the messages
CREATE TABLE message_board (
	post_id INT PRIMARY KEY AUTO_INCREMENT UNIQUE,
    post_content TEXT NOT NULL,
    post_category VARCHAR(50) NOT NULL,
	post_author VARCHAR(30) NOT NULL,
    post_date DATETIME NOT NULL DEFAULT NOW()
);


-- Tables for user profile and accounts (can also create them from Python - recommend create from python)
CREATE TABLE user_profiles (
        username VARCHAR(30) NOT NULL,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        email VARCHAR(254) NOT NULL,
        date_of_birth DATE,
        interests TEXT,
        date_joined DATETIME,
        PRIMARY KEY (username),
        UNIQUE (username),
        UNIQUE (email)
);

CREATE TABLE user_accounts (
        user_id VARCHAR(36) NOT NULL,
        username VARCHAR(30) NOT NULL,
        password VARCHAR(60) NOT NULL,
        PRIMARY KEY (user_id),
        UNIQUE (user_id),
        UNIQUE (username)
);



-- Mock posts
INSERT INTO message_board
(post_content, post_category, post_author)
VALUES
("What new Anime can I watch everyone?", "Anime", "BlueMonkey"),
("Is there a new season of FairyTail coming out?", "Anime", "MarshmellowDestroyer"),
("Should really get around to finishing Hokuto no Ken/FoTNS already...it's bad ass...", "Anime", "BlueMonkey"),
("Look to the 80's and 90's for anime that isn't trying to give you a stiffy. Sure, there's still women in skimpy outfits, but it's not a primary goal of the anime.", "Anime", "randomDUDEEEEEE"),
("I'm starting Welcome to the N.H.K myself. Reading the LN to and figure I might as well do a side by side comparison.", "Anime", "BloodLord55"),
("D.Gray man's OST is really good. Only watched the first two seasons but those two have both of some my favourite openings of all time.", "Anime", "DogWar");

INSERT INTO message_board
(post_content, post_category, post_author)
VALUES
("Hello I am BlueMonkey here I got the nickname from my friends a while back", "Introduce", "BlueMonkey"),
("Sup dudes, anyone play anything then?", "Introduce", "MarshmellowDestroyer"),
("So what are rules to these forums then?", "Introduce", "MonkeyFivesss"),
("Just some sound dude from new york.", "Introduce", "randomDUDEEEEEE"),
("I got a really cute puppy anyone wanna see?", "Introduce", "BloodLord55"),
("Just here for cool community!", "Introduce", "DogWar");

-- Content tables for recommendations
CREATE TABLE Books ( 
	Book_ID INTEGER PRIMARY KEY NOT NULL,
	Book_Name VARCHAR(100) UNIQUE NOT NULL,
    Book_Author VARCHAR(30),
    Book_Genre VARCHAR(25),
	Price FLOAT NOT NULL, 
    Book_Script VARCHAR(1000) 
    );

CREATE TABLE Anime ( 
	Anime_ID INTEGER PRIMARY KEY NOT NULL,
	Anime_Name VARCHAR(50) UNIQUE NOT NULL,
    Anime_Genre VARCHAR(25),
	Where_TW VARCHAR(25), 
    Anime_Script VARCHAR(1000) 
    );

CREATE TABLE Games ( 
	Game_ID INTEGER PRIMARY KEY NOT NULL,
	Game_Name VARCHAR(50) UNIQUE NOT NULL,
    Game_Genre VARCHAR(30),
	W_Console VARCHAR(100), 
    Price FLOAT NOT NULL,
    Game_Script VARCHAR(1000) 
    );


-- Values for recommendation tables    
INSERT INTO Books
(Book_ID, Book_Name, Book_Author, Book_Genre, Price, Book_Script)
VALUES
(1, 'Fourth Wing', 'Rebecca Yarros', 'Fantasy', 9.19, 'Twenty-year-old Violet Sorrengail was supposed to enter the Scribe Quadrant, living a quiet life among books and history. Now, the commanding general-also known as her tough-as-talons mother-has ordered Violet to join the hundreds of candidates striving to become the elite of Navarre: dragon riders.'),
(2, 'The Harry Potter Series', 'J.K. Rowling', 'Fantasy', 51.65, 'The Harry Potter books follow a young wizard named Harry as he attends Hogwarts School of Witchcraft and Wizardry. Alongside his friends Ron and Hermione, Harry faces challenges, discovers his past, and confronts the dark wizard Voldemort across seven books, filled with magic, friendship, and the battle between good and evil.'),
(3, 'A Court of Thorns and Roses Series', 'Sarah J. Maas', 'Fantasy', 31.74, 'ACOTAR Follows Feyre, a huntress who accidentally kills a faerie and is taken to the faerie lands as punishment. There, she navigates faerie politics, forms relationships with powerful fae like Tamlin and Rhysand, and becomes involved in a high-stakes battle that could impact both human and faerie realms across several books filled with magic, romance, and conflicts.'),
(4, 'To Kill a Kingdom', 'Alexandra Christo', 'Fantasy', 4.67, 'Princess Lira is siren royalty and the most lethal of them all. With the hearts of seventeen princes in her collection, she is revered across the sea. Until a twist of fate forces her to kill one of her own. To punish her daughter, the Sea Queen transforms Lira into the one thing they loathe most - a human. Robbed of her song, Lira has until the winter solstice to deliver Prince Elians heart to the Sea Queen or remain a human forever.'),
(5, 'Elizabeth Bathory: Life and Legacy of Historys Most Prolific Female Serial Killer', 'James Oliver', 'History', 6.12, 'This book explains the life and times of this powerful woman - and how she came to be accused of so many heinous crimes. Youll gain access to a variety of historical versions, perspectives, and accounts of her life - some of which paint her as a villain and others as a victim!'),
(6, 'The Great Empires of the Ancient World', 'Thomas Harrison', 'History', 11.63, 'A distinguished team of internationally renowned scholars surveys the great empires from 1600 BC to AD 500, from the ancient Mediterranean to China. Exploring the very nature of empire itself, the authors show how profoundly imperialism in the distant past influenced the 19th-century powers and the modern United States.'),
(7, 'Landlines', 'Raynor Winn', 'History', 6.00, 'Embarking on a journey across the Cape Wrath Trail, over 200 miles of gruelling terrain through Scotlands remotest mountains and lochs, Raynor and Moth look to an uncertain future. Fearing that miracles dont often repeat themselves.'), 
(8, 'Unbroken: A World War II Story of Survival', 'Lauren Hillenbrand', 'History', 4.71, 'On a May afternoon in 1943, an Army Air Forces bomber crashed into the Pacific Ocean and disappeared, leaving only a spray of debris and a slick of oil, gasoline, and blood. Then, on the ocean surface, a face appeared. It was that of a young lieutenant, the planes bombardier, who was struggling to a life raft and pulling himself aboard. So began one of the most extraordinary odysseys of the Second World War.'), 
(9, 'The Haunting of Hill House', 'Shirley Jackson', 'Horror', 9.90, 'Welcome to Hill House, an eerie mansion with a chilling past. When a group of individuals sets out to uncover its supernatural secrets, they find themselves trapped in a world where reality blurs with the terrifying unknown. Shirley Jacksons classic tale weaves a haunting narrative that explores the eerie power of a house that seems to have a mind of its own.'), 
(10, 'Dracula', 'Bram Stoker', 'Horror', 14.29, 'When Jonathan Harker visits Transylvania to help Count Dracula with the purchase of a London house, he makes a series of horrific discoveries about his client. Soon afterwards, various bizarre incidents unfold in England: an apparently unmanned ship is wrecked off the coast of Whitby; a young woman discovers strange puncture marks on her neck; and the inmate of a lunatic asylum raves about the Master and his imminent arrival.'),
(11, 'The Shining', 'Stephen King', 'Horror', 10.11, 'Danny is only five years old, but in the words of old Mr Hallorann he is a shiner, aglow with psychic voltage. When his father becomes caretaker of the Overlook Hotel, Dannys visions grow out of control. As winter closes in and blizzards cut them off, the hotel seems to develop a life of its own. It is meant to be empty. So who is the lady in Room 217 and who are the masked guests going up and down in the elevator? And why do the hedges shaped like animals seem so alive? Somewhere, somehow, there is an evil force in the hotel - and that, too, is beginning to shine.'),
(12, 'The Exorcist', 'William Peter Blatty', 'Horror', 9.19, 'The terror begins unobtrusively. Noises in the attic. In the childs room, an odd smell, the displacement of furniture, an icy chill. At first, easy explanations are offered. Then frightening changes begin to appear in eleven-year-old Regan. Medical tests fail to shed any light on her symptoms, but it is as if a different personality has invaded her body.');

INSERT INTO Anime
(Anime_ID, Anime_Name, Anime_Genre, Where_TW, Anime_Script)
VALUES
(1, 'Bleach', 'Shonen', 'Disney+', 'Ichigo Kurosaki is a teenager from Karakura Town who can see ghosts, a talent allowing him to meet a supernatural human Rukia Kuchiki, who enters the town in search of a Hollow, a kind of monstrous lost soul who can harm both ghosts and humans.'),
(2, 'Naruto', 'Shonen', 'Crunchyroll', 'The Village Hidden in the Leaves is home to the stealthiest ninja. But twelve years earlier, a fearsome Nine-tailed Fox terrorized the village before it was subdued and its spirit sealed within the body of a baby boy.'),
(3, 'Jujutsu Kaisen', 'Shonen', 'Crunchyroll', 'Yuji Itadori is a boy with tremendous physical strength, though he lives a completely ordinary high school life. One day, to save a classmate who has been attacked by curses, he eats the finger of Ryomen Sukuna, taking the curse into his own soul. From then on, he shares one body with Ryomen Sukuna. Guided by the most powerful of sorcerers, Satoru Gojo, Itadori is admitted to Tokyo Jujutsu High School, an organization that fights the curses... and thus begins the heroic tale of a boy who became a curse to exorcise a curse, a life from which he could never turn back.'),
(4, 'One Piece', 'Shonen', 'Crunchyroll', 'Monkey. D. Luffy refuses to let anyone or anything stand in the way of his quest to become the king of all pirates. With a course charted for the treacherous waters of the Grand Line and beyond, this is one captain who will never give up until he has claimed the greatest treasure on Earth: the Legendary One Piece!'),
(5, 'Attack on Titan', 'Seinen', 'Crunchyroll', 'Known in Japan as Shingeki no Kyojin, many years ago, the last remnants of humanity were forced to retreat behind the towering walls of a fortified city to escape the massive, man-eating Titans that roamed the land outside their fortress. Only the heroic members of the Scouting Legion dared to stray beyond the safety of the walls – but even those brave warriors seldom returned alive. Those within the city clung to the illusion of a peaceful existence until the day that dream was shattered, and their slim chance at survival was reduced to one horrifying choice: kill – or be devoured!'),
(6, 'Tokyo Ghoul', 'Seinen', 'Crunchyroll', 'Haise Sasaki has been tasked with teaching Qs Squad how to be outstanding investigators, but his assignment is complicated by the troublesome personalities of his students and his own uncertain grasp of his Ghoul powers. Can he pull them together as a team, or will Qs Squad first assignment be their last?'),
(7, 'Berserk', 'Seinen', 'Crunchyroll', 'Spurred by the flame raging in his heart, the Black Swordsman Guts continues his seemingly endless quest for revenge. Standing in his path are heinous outlaws, delusional evil spirits, and a devout child of god.Even as it chips away at his life, Guts continues to fight his enemies, who wield repulsive and inhumane power, with nary but his body and sword—his strength as a human. What lies at the end of his travels? The answer is shrouded in the night.'), 
(8, 'Death Note', 'Seinen', 'Crunchyroll', 'An intelligent high school student goes on a secret crusade to eliminate criminals from the world after discovering a notebook capable of killing anyone whose name is written into it.'), 
(9, 'Chainsaw Man', 'Fantasy', 'Crunchyroll', 'Denji is a young boy who works as a Devil Hunter with the Chainsaw Devil Pochita. One day, as he was living his miserable life trying to pay off the debt he inherited from his parents, he got betrayed and killed. As he was losing his consciousness, he made a deal with Pochita, and got resurrected as the Chainsaw Man: the owner of the Devil’s heart.'), 
(10, 'JoJos Bizarre Adventure', 'Fantasy', 'Netflix', 'In ancient Mexico, people of Aztec had prospered. They had historic and strange Stone Mask. It was a miraculous mask which brings eternal life and the power of authentic ruler. But the mask suddenly disappeared. A long time after that, in late 19th centuries when the thought and life of people were suddenly changing, Jonathan Joestar met with Dio Brando. They spend time together through boyhood to youth, and the Stone Mask brings curious fate to them.'),
(11, 'Black Clover', 'Fantasy', 'Crunchyroll', 'In a world where magic is everything, Asta and Yuno are both found abandoned at a church on the same day. While Yuno is gifted with exceptional magical powers, Asta is the only one in this world without any. At the age of fifteen, both receive grimoires, magic books that amplify their holder’s magic. Asta’s is a rare Grimoire of Anti-Magic that negates and repels his opponent’s spells. Being opposite but good rivals, Yuno and Asta are ready for the hardest of challenges to achieve their common dream: to be the Wizard King. Giving up is never an option!'),
(12, 'Link Click', 'Fantasy', 'Crunchyroll', 'Using superpowers to enter their clientele’s photos one by one, Cheng Xiaoshi and Lu Guang take their work seriously at Time Photo Studio, a small photography shop set in the backdrop of a modern metropolis. Each job can be full of danger, but nothing is more important than fulfilling every order, no matter the scale…or peril involved!');

INSERT INTO Games
(Game_ID, Game_Name, Game_Genre, W_Console, Price, Game_Script)
VALUES
(1, 'Fae Farm', 'Cozy Games', 'PC, NINTENDO SWITCH', 29.99, 'Escape to the magical life of your dreams in Fae Farm, a farm sim RPG for 1-4 players. Craft, cultivate, and decorate to grow your homestead, and use spells to explore the enchanted island of Azoria!'),
(2, 'Spellcaster University', 'Cozy Games', 'PC', 19.49, 'Develop a prestigious university of mages. Build rooms, train your students, fight orcs, slay the bureaucrats, manage your budget... a directors life is not a quiet one.'),
(3, 'Little Witch in the Woods', 'Cozy Games', 'PC, NINTENDO SWITCH', 12.39, ' Little Witch in the Woods tells the story of Ellie, an apprentice witch. Explore the mystical forest, help the charming residents, and experience the daily life of the witch.'),
(4, 'Cozy Grove', 'Cozy Games', 'PC, NINTENDO SWITCH', 11.39, 'Welcome to Cozy Grove, a game about camping on a haunted, ever-changing island. As a Spirit Scout, youll wander the islands forest each day, finding new hidden secrets and helping soothe the local ghosts. With a little time and a lot of crafting, youll bring color and joy back to Cozy Grove!'),
(5, 'Hogwarts Legacy', 'RPG', 'PC, XBOX, PLAYSTATION, NINTENDO SWITCH', 49.99, 'Hogwarts Legacy is an immersive, open-world action RPG. Now you can take control of the action and be at the center of your own adventure in the wizarding world.'),
(6, 'God of War', 'RPG', 'PLAYSTATION', 39.99, 'Against a backdrop of Norse Realms torn asunder by the fury of the Aesir, they’ve been trying their utmost to undo the end times. But despite their best efforts, Fimbulwinter presses onward. Witness the changing dynamic of the father-son relationship as they fight for survival. Atreus thirsts for knowledge to help him understand the prophecy of Loki, as Kratos struggles to break free of his past and be the father his son needs.'),
(7, 'Lies of P', 'RPG', 'PLAYSTATION, PC, XBOX', 49.99, 'Lies of P is a thrilling soulslike that takes the story of Pinocchio, turns it on its head, and sets it against the darkly elegant backdrop of the Belle Epoque era.'), 
(8, 'Marvels Spider Man 2', 'RPG', 'PLAYSTATION', 69.99, 'Peter Parker and Miles Morales return for an exciting new adventure in the critically acclaimed Marvel’s Spider-Man franchise. Swing, jump and utilize the new Web Wings to travel across Marvel’s New York, quickly switching between Peter Parker and Miles Morales to experience different stories and epic new powers, as the iconic villain Venom threatens to destroy their lives, their city and the ones they love.'), 
(9, 'STARDEW VALLEY', 'SIMULATION', 'PC, NINTENDO SWITCH, XBOX, PLAYSTATION', 10.99, 'Youve inherited your grandfathers old farm plot in Stardew Valley. Armed with hand-me-down tools and a few coins, you set out to begin your new life. Can you learn to live off the land and turn these overgrown fields into a thriving home?'),
(10, 'Two Point Hospital', 'SIMULATION', 'PC, NINTENDO SWITCH, XBOX, PLAYSTATION', 24.99, 'Design stunning hospitals, cure peculiar illnesses and manage troublesome staff as you spread your budding healthcare organisation across Two Point County.'),
(11, 'GAME DEV TYCOON', 'SIMULATION', 'PC', 8.50, 'In Game Dev Tycoon you replay the history of the gaming industry by starting your own video game development company in the 80s. Create best selling games. Research new technologies and invent new game types. Become the leader of the market and gain worldwide fans.'),
(12, 'NAHEULBEUKS DUNGEON MASTER', 'SIMULATION', 'PC', 20.99, 'A dungeon in danger ! Build, manage, and defend your tower in the satirical heroic fantasy universe of Dungeon of Naheulbeuk. From a shaky establishment to an infamous lair!');

-- Values for user tables, need to update and best not to insert directly from SQL because need to hash passwords, but keeping them here in meantime for an idea
-- Just for reference of some of the users added through the website
-- INSERT INTO Users (UserID, Username, Email, Name, DateOfBirth, Interests, Password)
-- VALUES
-- (1,'the_kickboxer', 'kathoop@email.com', 'Katherine Hooper', '1990-01-01', 'Gaming ', 'password1'),
-- (2,'pokemon_girl', 'angel.pika@email.com', 'Angel Witchell', '2001-02-02', 'Shonen' , 'password2' ) ,
-- (3,'lover_ofbooks', 'agd@email.com', 'Abbie-Gayle Daniel', '2002-03-03', 'Reading', 'password3'),
-- (4, 'dog_mum', 'haiyingl@email.com', 'Haiying Liao', '2003-04-04', 'Cozy_games', 'password4'),
-- (5, 'the_baroness', 'katbray@email.com', 'Katalin Bray', '1920-04-04', 'History', 'password5'),
-- (6, 'friday_13', 'jimmychamp@email.com', 'Jimmy Champagne', '1970-05-05', 'Horror', 'password6'),
-- (7, 'elder_scrolls', 'pewdiepie@email.com', 'Felix Kjellberg', '1995-06-06', 'Adventure', 'password7'),
-- (8,'nerdrotic', 'garyb@email.com', 'Gary Brown', '1950-07-07', 'Fantasy', 'password8'),
-- (9, 'critical_drinker', 'willjordan@email.com', 'Will Jordan', '1980-07-07', 'Simulation', 'password8');