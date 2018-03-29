-- --------------------------------------------------------
-- Verkkotietokone:              127.0.0.1
-- Palvelinversio:               10.1.19-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Versio:              9.3.0.4984
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dumping database structure for asd_datav1
CREATE DATABASE IF NOT EXISTS `asd_datav1` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `asd_datav1`;


-- Dumping structure for taulu asd_datav1.enemy
CREATE TABLE IF NOT EXISTS `enemy` (
  `EnemyID` int(11) NOT NULL,
  `Location` int(11) DEFAULT NULL,
  `HP` int(11) NOT NULL,
  `EnemytypeID` int(11) NOT NULL,
  PRIMARY KEY (`EnemyID`),
  KEY `EnemytypeID` (`EnemytypeID`),
  KEY `Location` (`Location`),
  CONSTRAINT `enemy_ibfk_1` FOREIGN KEY (`EnemytypeID`) REFERENCES `enemytype` (`EnemytypeID`),
  CONSTRAINT `enemy_ibfk_2` FOREIGN KEY (`Location`) REFERENCES `rooms` (`Location`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table asd_datav1.enemy: ~1 rows (suunnilleen)
/*!40000 ALTER TABLE `enemy` DISABLE KEYS */;
REPLACE INTO `enemy` (`EnemyID`, `Location`, `HP`, `EnemytypeID`) VALUES
	(1, NULL, 60, 1),
	(2, 14, 60, 1),
	(3, 13, 80, 2),
	(4, 12, 80, 2),
	(5, 24, 999, 4),
	(6, 10, 60, 1),
	(7, 2, 60, 1),
	(8, 11, 60, 1);
/*!40000 ALTER TABLE `enemy` ENABLE KEYS */;


-- Dumping structure for taulu asd_datav1.enemytype
CREATE TABLE IF NOT EXISTS `enemytype` (
  `EnemytypeID` int(11) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `HP` int(11) NOT NULL,
  `Damage` int(11) NOT NULL,
  PRIMARY KEY (`EnemytypeID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table asd_datav1.enemytype: ~3 rows (suunnilleen)
/*!40000 ALTER TABLE `enemytype` DISABLE KEYS */;
REPLACE INTO `enemytype` (`EnemytypeID`, `Name`, `HP`, `Damage`) VALUES
	(1, 'MAIN-BOT', 60, 5),
	(2, 'SEC-BOT', 80, 10),
	(4, 'MADOS', 50, 0);
/*!40000 ALTER TABLE `enemytype` ENABLE KEYS */;


-- Dumping structure for taulu asd_datav1.object
CREATE TABLE IF NOT EXISTS `object` (
  `ObjectID` int(11) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `PlayerID` int(11) DEFAULT NULL,
  `EnemyID` int(11) DEFAULT NULL,
  `Location` int(11) DEFAULT NULL,
  `Ammo` int(11) DEFAULT NULL,
  `Damage` int(11) DEFAULT NULL,
  `Examine` varchar(1000) NOT NULL,
  `Pickup` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`ObjectID`),
  KEY `PlayerID` (`PlayerID`),
  KEY `EnemyID` (`EnemyID`),
  KEY `Location` (`Location`),
  CONSTRAINT `object_ibfk_1` FOREIGN KEY (`PlayerID`) REFERENCES `player` (`PlayerID`),
  CONSTRAINT `object_ibfk_2` FOREIGN KEY (`EnemyID`) REFERENCES `enemy` (`EnemyID`),
  CONSTRAINT `object_ibfk_3` FOREIGN KEY (`Location`) REFERENCES `rooms` (`Location`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table asd_datav1.object: ~17 rows (suunnilleen)
/*!40000 ALTER TABLE `object` DISABLE KEYS */;
REPLACE INTO `object` (`ObjectID`, `Name`, `PlayerID`, `EnemyID`, `Location`, `Ammo`, `Damage`, `Examine`, `Pickup`) VALUES
	(1, 'Crowbar', 1, NULL, NULL, NULL, 10, 'Made by Valve inc.', 1),
	(2, 'Taser', NULL, NULL, 15, 1, 60, 'ZapzapKILL corporation', 1),
	(3, 'Keycard', NULL, NULL, NULL, NULL, 0, 'KeyCard inc. \'made in china\' Colour: Red\r\n', 1),
	(4, 'Keycard', NULL, NULL, NULL, NULL, 0, 'KeyCard inc. \'made in china\' Colour:  Blue\r\n', 1),
	(5, 'Keycard', NULL, NULL, 20, NULL, 0, 'KeyCard inc. \'made in china\' Colour: Green\r\n', 1),
	(6, 'Radio', NULL, NULL, 9, NULL, 0, 'A radio, it seems like it has an incoming transmission.', 0),
	(7, 'Paper', NULL, NULL, 7, NULL, 0, 'It\'s a paper with hastly sketched instructions on it. It reads:\r\nup, right, up,up, left,up', 1),
	(8, 'Screen', NULL, NULL, 3, NULL, 0, 'The holoscreen trembles a bit when you get closer to it. 3D layout of H3LS1NK1 flicks alive in front of you. \r\n"H3L51nk1 - Traffic and settlement secured! The station keeps dangerous derelicts, space junk and other objects\r\nfrom causing damage by destroying or guiding them away!"\r\nScreen behind it displays ominous diagnostics: \r\n\'Severe damage in Entity Repositories. Hull breaches in passageway 3 and rooms V116. Lasers 2 and 4 inoperational.\r\nOrbital change initiated, Weapon Slots 50 prepared for planetary distance operation. Automated Security deployed in case of intruder.\'\r\nThere is no obvious interface or datajack visible', 0),
	(10, 'Tablet', NULL, NULL, 15, NULL, 0, 'There\'s a news page open on the tablet. \r\nArticle tells about the strained relationships of The New Martian Russia and Western Terra Nations.\r\nScanning the page, you gather, that the Martian Russia is making serious accusations about the nature of \r\nWestern Terra Nations lobbying and accusing the Earth Council of being reckless regarding their research politics.\r\n\'The New Martian Russia is now demanding neutral third party investigation from the Extra-terrestrial Union, and for the time being, \r\nlimiting their Spice exportation to litigant parties regions as a protest.\' ', 0),
	(11, 'Tabloid', NULL, NULL, 7, NULL, 0, 'It projects some miniature part of the security robots built-in plasma beam. \r\nCutline has obscure instructions and listed part numbers.\r\nTapping to tabloid the projection flicks and changes, now display overlay of the Security Robot instead.\r\nCaption says: \'Standard Security Robot version 31.4 \'M4RVIN\'. \r\nArmed for disarming and incapacitating unwanted personnel. \r\n\'Now with built-in laser! Keep safe, with M4RVIN!\'', 0),
	(12, 'Poster', NULL, NULL, 16, NULL, 0, 'Poster portrays a triumphant astronaut posing on the roof of a repaired space shuttle. \r\nThe poster is emitting a slogan: \'Keep safe with Suit M2077, for the toughest of workers!\r\nNow with boosting exoskeleton for the no-gravity work environments! \r\nComes with a full radiation protection up to level 6!\' ', 0),
	(13, 'Andy', NULL, NULL, 23, NULL, 0, 'That\'s Andy, robot bartender with magnificent mustache.', 0),
	(14, 'Spacesuit', NULL, NULL, 16, NULL, 0, 'Worn pace suit, model M2077. Someone did a nice custom paint job on this one. It\'s black with some red and white  stripes on the right arm. There\'s a red text \'N7\' on the chest. ', 1),
	(15, 'Jacket', NULL, NULL, 5, NULL, 0, 'On the jacket is a text: \'R.I.P Lost In Helsinki\'.', 0),
	(16, 'Cola', NULL, NULL, NULL, 0, 0, 'Nuka-Cola Corporation, incinc. corp', 1),
	(17, 'Beer', NULL, NULL, NULL, 0, 0, 'Iisalmen Oluttehdas Oy', 1),
	(18, 'Window', NULL, NULL, 8, NULL, 0, 'View out of the window is magnificent.\r\nFar down on your left you can see a peak of the Mars\' crimson surface.\r\nThe vast emptiness in front of you is filled with myriad of lights. \r\nLight from uncountable amount of stars are washing down on the side of the station, \r\nbending on their way so that you see all the colours of the spectrum visible to you.\r\nOn your right you can see broken a passageway leading to a outer room looking like a storage. \r\nYou see a blink of a synthetic blue and yellow light on the edge of your field of view, \r\nbut when you turn your head, you see only the cold chassis of the station, \r\nprotecting you from the void outside...', 0);
/*!40000 ALTER TABLE `object` ENABLE KEYS */;


-- Dumping structure for taulu asd_datav1.player
CREATE TABLE IF NOT EXISTS `player` (
  `PlayerID` int(11) NOT NULL,
  `Location` int(11) DEFAULT NULL,
  `HP` int(11) NOT NULL,
  PRIMARY KEY (`PlayerID`),
  KEY `Location` (`Location`),
  CONSTRAINT `player_ibfk_1` FOREIGN KEY (`Location`) REFERENCES `rooms` (`Location`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table asd_datav1.player: ~1 rows (suunnilleen)
/*!40000 ALTER TABLE `player` DISABLE KEYS */;
REPLACE INTO `player` (`PlayerID`, `Location`, `HP`) VALUES
	(1, 5, 100);
/*!40000 ALTER TABLE `player` ENABLE KEYS */;


-- Dumping structure for taulu asd_datav1.rooms
CREATE TABLE IF NOT EXISTS `rooms` (
  `Location` int(11) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Description` varchar(1000) DEFAULT NULL,
  `Description2` varchar(1000) DEFAULT NULL,
  `North` int(11) DEFAULT NULL,
  `East` int(11) DEFAULT NULL,
  `South` int(11) DEFAULT NULL,
  `West` int(11) DEFAULT NULL,
  `Visited` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`Location`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table asd_datav1.rooms: ~24 rows (suunnilleen)
/*!40000 ALTER TABLE `rooms` DISABLE KEYS */;
REPLACE INTO `rooms` (`Location`, `Name`, `Description`, `Description2`, `North`, `East`, `South`, `West`, `Visited`) VALUES
	(1, 'T1', 'I entered H3LS1NK1. There\'s a open door to the north. \r\nThe room I entered is empty of furniture’s, just white metal surfaces and a chest with a terminal on it.\r\nMaybe I should try my IT expertise and  hack the chest terminal?', 'Here again? The room  is empty of furniture’s, just white metal surfaces and a chest with a terminal on it. Better get going to north.', 2, NULL, NULL, NULL, 0),
	(2, 'T2', 'This room  looks identical to the previous one. \r\nThere\'s a open door to the north. Wait a moment, what\'s that? A maintenance robot?\r\nI see a Maintenance robot in the north side of the room, cleaning with a cleaning brush. It has seen me and looks angry.\r\nLet\'s go medieval on the robot and smash it with my crowbar!', 'There\'s nothing special here, I only see a smashed robot. Better get going.', 3, NULL, 1, NULL, 0),
	(3, 'B1', 'I seem to have entered a lobby room. Red doors to the west and east. \r\nThe room is a hall with a big diagnosis screen on the wall and a counter with some obscure techinal papers on it.', 'The lobby room. There are red doors to the west and east. This room is a hall with a big diagnosis screen on the wall.', NULL, 4, 2, 10, 0),
	(4, 'B2', 'I entered a room that is square shaped.\r\nThere\'s nothing special in this room but I notice an cold wind breeze from the ventilation grid at the east side of the room. \r\nI can see two red doors, one to the north and the second leading back to the west. ', 'The room  is square shaped. \r\nThere\'s nothing special in this room but I notice an cold wind breeze from the ventilation grid at the east side of the room.\r\nI can see two red doors, one to the north and the second leading back to the west. ', 12, 22, NULL, 3, 0),
	(5, 'B3', 'This room is a very long corridor with a red door to the north and to the east leading back.\r\nI can also see fancy, modern looking benches on the west and east side of the room.\r\nThere seems also be a nonfunctional security camera on the east side of the room and under it a jacket.', 'This room is a long corridor with a red door to the north and to the east leading back.\r\nI can also see fancy, modern looking benches on the west and east side of the room. \r\nThere seems to be a nonfunctional security camera on the east side of the room and under it a jacket.', 8, NULL, 11, NULL, 0),
	(6, 'B4', 'I get the feeling that big brother watches over me. \r\nThis is a square shaped surveillance room with big screens above a desk to the east.\r\nRoom is very dusty so no one has probably been here for a while. \r\nHere I can also feel the cold breeze coming from the open ventilation shaft on the east side of the room.\r\nThere are red doors are located in the north and south. \r\nThere\'s also a blue door to the west.', 'I get the feeling that big brother watches over me. \r\nThis is a square shaped surveillance room with big screens above a desk to the east.\r\nRoom is very dusty so no one has probably been here for a while. \r\nHere I can also feel the cold breeze coming from the ventilation grid at the east side of the room.\r\nThere are red doors are located in the north and south. \r\nThere\'s also a blue door to the west.', 23, 22, 12, 9, 0),
	(7, 'B5', 'Robot maintenance room.\r\nThe room is crowded because of five big maintenance platforms and shelves on the southern and northern walls.\r\nIn one of the platforms there seems to be a robot inside but it doesn’t show any signs of life. Maybe it\'s still broken. On the shelve I can see lots of tools and a paper note. \r\nMaybe I should examine this further.', 'Robot maintenance room. \r\nThe room is crowded because of five big maintenance platforms and shelves on the southern and northern walls.\r\nIn one of the platforms there seems to be a robot inside but it doesn’t show any signs of life. Maybe it\'s still broken.', NULL, 9, NULL, 8, 0),
	(8, 'B6', 'I\'ve entered a room with red doors to the north and south, to the east there’s a blue door. \r\nThere\'s a green HP station located in the southwest corner and on the east side of the room \r\nI can see a big, round shaped window that intrigues me.', 'I\'ve entered a room with red doors to the north and south, to the east there’s a blue door. \r\nThere\'s a green HP station located in the southwest corner and on the east side of the room \r\nI can see a big, round shaped window that intrigues me.', 13, 7, 5, NULL, 0),
	(9, 'B7', 'Radio room. Nothing much to it. I can see a radio and a chair on the south side of the room. \r\nRed doors are located to the west and north, for going back there’s the green door to the east.', 'Radio room. Nothing much to it. I can see a radio and a chair on the south side of the room. \r\nRed doors are located to the west and north, for going back there’s the green door to the east.', 14, 6, NULL, 7, 0),
	(10, 'E1', 'Ugh, this is such a filthy room.\r\nThe floor is sticky, broken screens on the north and south side and two security cameras watching my every move. \r\nWait what, is that a idling maintenance robot?\r\nThe next  red door is located at the west side where the robot is. \r\nI have no choice than to continue to west or go back to east through the red door. The robot spots me! \r\n', 'Ugh, this is such a filthy room. The robot that I destroyed earlier still lies on the ground.\r\nThe floor is sticky, broken screens on the north and south side and two security cameras watching my every move. \r\nThe next  red door is located at the west side.\r\nI have no choice than to continue to west or go back to east through the red door.', NULL, 3, NULL, 11, 0),
	(11, 'E2', 'Now that I enter this room I can see a black door to the west, with a console, a red door to the north and for going back the red door to the east. \r\nThe room seems to have a screen that is not working and a security camera watching my moves. \r\nOh DAMN, there\'s also a robot that seem to be powering up, it’s a security robot. \r\nI think it\'s time to use the crowbar again! Hammer time!', 'I see a black door at west with a console and a red door to the north. The room seems to have a screen that is not working and a security camera watching my moves. \r\nRobot that I destroyed earlier still lies on the ground.', 5, 10, NULL, 15, 0),
	(12, 'E3', 'When I entered this room I notice a very odd smell. I can see small holes at the east side wall with a recycle sign above. So they DO recycle in space too! \r\nRed doors can be found at north and for going back, south. Also a black door with a console to the east.\r\nThere’s one security robot to take care off.', 'When I entered this room I notice a very odd smell. I can see small holes at the east side wall with a recycle sign above. So they DO recycle in space too! \r\nRed doors can be found to the north and for going back, south. Also a black door with a console to the east. \r\nBroken robots still lies on the ground.', 6, NULL, 4, 16, 0),
	(13, 'E4', 'Intriguing, this room is shaped like a ball but doesn’t seem to have much in it. Maybe I should check the west end, there seems to be some kind of corridor. \r\nThere\'s a blue door to the north, and the red door back to the south. \r\nA security robot is waiting for me in the northern side of the room!', 'Intriguing, this room is shaped like a ball but doesn’t seem to have much in it. Maybe I should check the west end, there seems to be some kind of corridor. \r\nThere\'s a Green door to the north, and the red door back to the south. \r\nA dead robot still lies on the floor.', 19, NULL, 8, 17, 0),
	(14, 'E5', 'I\'ve entered a room which purpose is unclear to me.There is a fire extinguisher on the wall and big touchscreen on the north wall where a maintenance robot is working.\r\nThere seems to be a bunch of code on the screen, looks a little bit like a source code for an AI.\r\nMaybe I just smash the cleaning robot and examine the computer later. \r\nHail to the king baby!', 'I\'ve entered a room which purpose is unclear to me.There is a fire extinguisher on the wall and big touchscreen on the north wall where a dead maintenance robot lies.\r\nThere seems to be a bunch of code on the screen, looks a little bit like a source code for an AI.', NULL, 23, 9, NULL, 0),
	(15, 'S1', 'Seems like I entered a huge closet.\r\nThere are small shelves with small plastic boxes on them  in the northern and southern side of the room.\r\nIn the west side seems to be a taser gun on a desk, maybe it could be useful in a place like this.', 'Room looks like a huge closet.\r\nThere\'s small shelves with small plastic boxes on them, in the north and south side of the room.\r\nIn the west side there\'s a desk.', NULL, 11, NULL, NULL, 0),
	(16, 'S2', 'A normal looking locker room. In the end of the room to the west there’s a old dusty mirror and on the north and south there\'s a long row of opened lockers. \r\nThere\'s also a suit peaking out from one of the lockers. \r\nThere\'s only one door, the one that leads back to the east.', 'A normal looking locker room. In the end of the room to the west there’s a old dusty mirror and on the north and south there\'s a long row of opened lockers. \r\nThere\'s also a suit peaking out from one of the lockers. \r\nThere\'s only one door, the one that leads back to the east.', NULL, 12, NULL, NULL, 0),
	(17, 'S3', 'I arrive to the room which looks like a storage. There are crates full of spare parts unfamiliar for me.\r\nI can see a HP station and a desk. There\'s a chargin station on the table. It seems my taser fits in it. Lock and load!\r\nThere are no doors other than the passage I just came from.', 'The room looks like a storage. There are crates full of spare parts unfamiliar for me.\r\nI can see a HP station and a desk. There\'s a chargin station on the table. It seems my taser fits in it. Lock and load!\r\nThere are no doors other than the passage I just came from.', NULL, 13, NULL, NULL, 0),
	(18, 'TR1', 'A disco or a trap? I see colored lights in every corner and in the middle of the room a odd hologram of an old man.\r\nThe elevator leading to MadOS  is to the west behind the hologram, but I sure smell something fishy here! Better be cautious.', 'The elevator leading to MadOS is located to the west. Luckily the hologram hasn’t returned.', NULL, NULL, 23, 20, 0),
	(19, 'TR2', 'My god, what a room. It\'s probably filled with traps. Broken spotlights and blue sparks of electricity falling down from the ceiling. The floor consists of metallic tiles.\r\nI hear crackling sort of like a Tesla coil somewhere above the ceiling.\r\nI also see an elevator door at the east side of the room and some kind of  switch, I got to stay cautious here!', 'This trap was a piece of cake. I should continue to the elevators to the east.', NULL, 21, 13, NULL, 0),
	(20, 'EL1', 'An elevator. There\'s a control panel to choose which floor to go,though only one other floor than this, labeled \'MadOS\'.', 'An elevator. There\'s a control panel to choose which floor to go,though only one other floor than this, labeled \'MadOS\'.', 24, NULL, NULL, NULL, 0),
	(21, 'EL2', 'An elevator. There\'s a control panel to choose which floor to go,though only one other floor than this, labeled \'MadOS\'.', 'An elevator. There\'s a control panel to choose which floor to go,though only one other floor than this, labeled \'MadOS\'.', 24, NULL, NULL, NULL, 0),
	(22, 'VENT', 'It\'s dusty and dark here. I can only move forward or back to room where I came. Was that a scream?', 'It\'s dusty and dark here. I can only move forward or back to room where I came.', 6, NULL, 4, NULL, 0),
	(23, 'BAR', 'Wait, what?! A BAR?! This is really a bar! And it\'s bartender! \r\nHow convenient, I’ve entered a bar and there seems to be a bartender, who doesn\'t look hostile. In the corner there is a JUKEBOX.\r\nThe interior is made of wood as the bar counter which makes this place feel very cozy. \r\nThe bartender is a floating robot with a fancy looking moustache. In it\'s chassis hangs a name plate: \'Mr. ANDY\'.\r\nDoors are located to the north with a blue door, east with a black door but seems inaccessible from this side because there\'s no console and the red door to the south leading back.\r\nBut first things first, to the counter!\r\n\r\n', '"Howdy Andy, I’m back for some more."\r\nThe bartender is a floating robot with a fancy looking moustache. In it\'s chassis hangs a name plate: \'Mr. ANDY\'.\r\nThe interior is made of wood as the bar counter which makes this place feel very cozy. \r\nDoors are located to the north with a blue door, east with a black door but seems inaccessible from this side because there\'s no console and the red door to the south leading back.\r\nIn the corner stands a fancy looking, colorful jukebox.', 18, NULL, 6, 14, 0),
	(24, 'BOSS', 'Finally I’m here! The MadOS control room. I can\'t believe I made it. The room is very dark. The only thing that produces light are a bunch of server computers that blink randomly. \r\nThe walls also seem to have some kind of tech inbuilt because on them I can see white colored numbers that change randomly. \r\nIn the back of the room lays a pile of twisted metal, electronical components and pieces of server chassis. It looks like something crashed through this room! \r\nSeems like this whole place has gone mad... In the north side of the room I can see the terminal that says MadOS, and above the terminal there’s a screen that displays two large eyes that look twisted.\r\nI\'ve come this far, now it\'s time to end this madness!', 'Finally I’m here! The MadOS control room. I can\'t believe I made it. The room is very dark. The only thing that produces light are a bunch of server computers that blink randomly. \r\nThe walls also seem to have some kind of tech inbuilt because on them I can see white colored numbers that change randomly. \r\nIn the back of the room lays a pile of twisted metal, electronical components and pieces of server chassis. It looks like something crashed through this room! \r\nSeems like this whole place has gone mad... In the north side of the room I can see the terminal that says MadOS, and above the terminal there’s a screen that displays two large eyes that look twisted.\r\nI\'ve come this far, now it\'s time to end this madness!', NULL, 20, NULL, 20, 0);
/*!40000 ALTER TABLE `rooms` ENABLE KEYS */;


-- Dumping structure for taulu asd_datav1.station
CREATE TABLE IF NOT EXISTS `station` (
  `StationID` int(11) NOT NULL,
  `Location` int(11) DEFAULT NULL,
  `GivesHP` int(11) NOT NULL,
  `GivesAM` int(11) NOT NULL,
  `used` int(11) NOT NULL,
  PRIMARY KEY (`StationID`),
  KEY `Location` (`Location`),
  CONSTRAINT `station_ibfk_1` FOREIGN KEY (`Location`) REFERENCES `rooms` (`Location`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table asd_datav1.station: ~2 rows (suunnilleen)
/*!40000 ALTER TABLE `station` DISABLE KEYS */;
REPLACE INTO `station` (`StationID`, `Location`, `GivesHP`, `GivesAM`, `used`) VALUES
	(1, 7, 100, 0, 0),
	(2, 5, 0, 10, 0);
/*!40000 ALTER TABLE `station` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
