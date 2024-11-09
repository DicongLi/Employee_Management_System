SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `security_questions_db`
--

-- --------------------------------------------------------
--
-- Table structure for table `security_questions`
--

CREATE TABLE `security_questions` (
  `ID` varchar(6) NOT NULL,
  `Question_1` varchar(50) DEFAULT NULL,
  `Answer_1` varchar(50) DEFAULT NULL,
  `Question_2` varchar(50) DEFAULT NULL,
  `Answer_2` varchar(50) DEFAULT NULL,
  `Question_3` varchar(50) DEFAULT NULL,
  `Answer_3` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `security_questions`
--

INSERT INTO `security_questions` (`ID`, `Question_1`, `Answer_1`, `Question_2`, `Answer_2`, `Question_3`, `Answer_3`) VALUES 
('m00001', 'Your favourite animal?', 'Number 8', 'Your favourite person?', 'Bob', 'Your favourite number?', 'Tiger'),
('m00002', 'Your favourite animal?', 'James', 'Your favourite person?', 'Lion', 'Your favourite number?', 'Elephant'),
('m00003', 'Your favourite animal?', 'Bob', 'Your favourite person?', 'Alice', 'Your favourite number?', 'Bob'),
('m00004', 'Your favourite animal?', 'Michael', 'Your favourite person?', 'Number 10', 'Your favourite number?', 'Catherine'),
('m00005', 'Your favourite animal?', 'Sarah', 'Your favourite person?', 'Number 10', 'Your favourite number?', 'Number 3'),
('m00006', 'Your favourite animal?', 'Bob', 'Your favourite person?', 'Number 8', 'Your favourite number?', 'Lion'),
('m00007', 'Your favourite animal?', 'Number 42', 'Your favourite person?', 'Alice', 'Your favourite number?', 'Number 7'),
('m00008', 'Your favourite animal?', 'Alice', 'Your favourite person?', 'Alice', 'Your favourite number?', 'Bob'),
('m00009', 'Your favourite animal?', 'Tiger', 'Your favourite person?', 'Number 8', 'Your favourite number?', 'Alice'),
('m00010', 'Your favourite animal?', 'Emma', 'Your favourite person?', 'Elephant', 'Your favourite number?', 'Number 3'),
('m00011', 'Your favourite animal?', 'Emma', 'Your favourite person?', 'Number 10', 'Your favourite number?', 'Number 10'),
('m00012', 'Your favourite animal?', 'Mary', 'Your favourite person?', 'James', 'Your favourite number?', 'Cat'),
('m00013', 'Your favourite animal?', 'Catherine', 'Your favourite person?', 'Sarah', 'Your favourite number?', 'Dog'),
('m00014', 'Your favourite animal?', 'Emma', 'Your favourite person?', 'Tiger', 'Your favourite number?', 'Number 3'),
('m00015', 'Your favourite animal?', 'Dog', 'Your favourite person?', 'Number 7', 'Your favourite number?', 'Sarah'),
('m00016', 'Your favourite animal?', 'John', 'Your favourite person?', 'Tiger', 'Your favourite number?', 'Lion'),
('m00017', 'Your favourite animal?', 'Mary', 'Your favourite person?', 'Alex', 'Your favourite number?', 'Lion'),
('m00018', 'Your favourite animal?', 'Mary', 'Your favourite person?', 'Emma', 'Your favourite number?', 'John'),
('m00019', 'Your favourite animal?', 'Elephant', 'Your favourite person?', 'Bob', 'Your favourite number?', 'Elephant'),
('m00020', 'Your favourite animal?', 'Dog', 'Your favourite person?', 'Number 42', 'Your favourite number?', 'Michael'),
('m00021', 'Your favourite animal?', 'John', 'Your favourite person?', 'Bob', 'Your favourite number?', 'Cat'),
('m00022', 'Your favourite animal?', 'Alice', 'Your favourite person?', 'Bob', 'Your favourite number?', 'Bob'),
('m00023', 'Your favourite animal?', 'Number 42', 'Your favourite person?', 'Mary', 'Your favourite number?', 'Dolphin'),
('m00024', 'Your favourite animal?', 'Alice', 'Your favourite person?', 'Sarah', 'Your favourite number?', 'Number 8'),
('m00025', 'Your favourite animal?', 'Number 42', 'Your favourite person?', 'James', 'Your favourite number?', 'Alex'),
('m00026', 'Your favourite animal?', 'Tiger', 'Your favourite person?', 'Dolphin', 'Your favourite number?', 'Cat'),
('m00027', 'Your favourite animal?', 'Number 42', 'Your favourite person?', 'Michael', 'Your favourite number?', 'Number 7'),
('m00028', 'Your favourite animal?', 'Lion', 'Your favourite person?', 'Elephant', 'Your favourite number?', 'Lion'),
('m00029', 'Your favourite animal?', 'Tiger', 'Your favourite person?', 'Alice', 'Your favourite number?', 'Dog'),
('m00030', 'Your favourite animal?', 'Cat', 'Your favourite person?', 'Alex', 'Your favourite number?', 'Alex'),
('m00031', 'Your favourite animal?', 'Number 10', 'Your favourite person?', 'Bob', 'Your favourite number?', 'Number 42'),
('m00032', 'Your favourite animal?', 'Number 8', 'Your favourite person?', 'Catherine', 'Your favourite number?', 'Michael'),
('m00033', 'Your favourite animal?', 'Number 42', 'Your favourite person?', 'Number 10', 'Your favourite number?', 'Elephant'),
('m00034', 'Your favourite animal?', 'Elephant', 'Your favourite person?', 'Number 7', 'Your favourite number?', 'Lion'),
('m00035', 'Your favourite animal?', 'Dolphin', 'Your favourite person?', 'Michael', 'Your favourite number?', 'Tiger'),
('m00036', 'Your favourite animal?', 'Emma', 'Your favourite person?', 'Sarah', 'Your favourite number?', 'Michael'),
('m00037', 'Your favourite animal?', 'Number 10', 'Your favourite person?', 'Number 42', 'Your favourite number?', 'Catherine'),
('m00038', 'Your favourite animal?', 'Elephant', 'Your favourite person?', 'Emma', 'Your favourite number?', 'Elephant'),
('m00039', 'Your favourite animal?', 'Emma', 'Your favourite person?', 'Alice', 'Your favourite number?', 'Catherine'),
('m00040', 'Your favourite animal?', 'Bob', 'Your favourite person?', 'Tiger', 'Your favourite number?', 'Dog'),
('m00041', 'Your favourite animal?', 'Elephant', 'Your favourite person?', 'Michael', 'Your favourite number?', 'Sarah'),
('m00042', 'Your favourite animal?', 'Number 10', 'Your favourite person?', 'Number 8', 'Your favourite number?', 'Dolphin'),
('m00043', 'Your favourite animal?', 'John', 'Your favourite person?', 'Number 7', 'Your favourite number?', 'Dolphin'),
('m00044', 'Your favourite animal?', 'Dog', 'Your favourite person?', 'Sarah', 'Your favourite number?', 'John'),
('m00045', 'Your favourite animal?', 'Dolphin', 'Your favourite person?', 'Sarah', 'Your favourite number?', 'John'),
('m00046', 'Your favourite animal?', 'Lion', 'Your favourite person?', 'Dolphin', 'Your favourite number?', 'Michael'),
('m00047', 'Your favourite animal?', 'Michael', 'Your favourite person?', 'Emma', 'Your favourite number?', 'Dolphin'),
('m00048', 'Your favourite animal?', 'Number 42', 'Your favourite person?', 'Alice', 'Your favourite number?', 'Mary'),
('m00049', 'Your favourite animal?', 'Tiger', 'Your favourite person?', 'Tiger', 'Your favourite number?', 'Emma'),
('m00050', 'Your favourite animal?', 'Sarah', 'Your favourite person?', 'John', 'Your favourite number?', 'Number 8'),
('d00001', 'Your favourite animal?', 'Sarah', 'Your favourite person?', 'Tiger', 'Your favourite number?', 'Tiger'),
('d00002', 'Your favourite animal?', 'Bob', 'Your favourite person?', 'Elephant', 'Your favourite number?', 'John'),
('d00003', 'Your favourite animal?', 'Number 8', 'Your favourite person?', 'Alice', 'Your favourite number?', 'Alex'),
('d00004', 'Your favourite animal?', 'Alex', 'Your favourite person?', 'Number 8', 'Your favourite number?', 'Dolphin'),
('d00005', 'Your favourite animal?', 'Alex', 'Your favourite person?', 'Mary', 'Your favourite number?', 'James'),
('d00006', 'Your favourite animal?', 'Bob', 'Your favourite person?', 'Sarah', 'Your favourite number?', 'James'),
('d00007', 'Your favourite animal?', 'Bob', 'Your favourite person?', 'Mary', 'Your favourite number?', 'Number 8'),
('d00008', 'Your favourite animal?', 'Bob', 'Your favourite person?', 'Number 10', 'Your favourite number?', 'Catherine'),
('d00009', 'Your favourite animal?', 'Dog', 'Your favourite person?', 'Alice', 'Your favourite number?', 'Catherine'),
('d00010', 'Your favourite animal?', 'Tiger', 'Your favourite person?', 'Dolphin', 'Your favourite number?', 'Lion'),
('d00011', 'Your favourite animal?', 'John', 'Your favourite person?', 'Mary', 'Your favourite number?', 'Sarah'),
('d00012', 'Your favourite animal?', 'Tiger', 'Your favourite person?', 'Lion', 'Your favourite number?', 'Tiger'),
('d00013', 'Your favourite animal?', 'Dog', 'Your favourite person?', 'Dolphin', 'Your favourite number?', 'Mary'),
('d00014', 'Your favourite animal?', 'Michael', 'Your favourite person?', 'Number 8', 'Your favourite number?', 'Michael'),
('d00015', 'Your favourite animal?', 'Lion', 'Your favourite person?', 'Alex', 'Your favourite number?', 'Emma'),
('d00016', 'Your favourite animal?', 'Lion', 'Your favourite person?', 'Mary', 'Your favourite number?', 'John'),
('d00017', 'Your favourite animal?', 'Tiger', 'Your favourite person?', 'James', 'Your favourite number?', 'Number 10'),
('d00018', 'Your favourite animal?', 'Catherine', 'Your favourite person?', 'Alice', 'Your favourite number?', 'Sarah'),
('d00019', 'Your favourite animal?', 'Michael', 'Your favourite person?', 'Tiger', 'Your favourite number?', 'Cat'),
('d00020', 'Your favourite animal?', 'Tiger', 'Your favourite person?', 'Cat', 'Your favourite number?', 'Alex'),
('d00021', 'Your favourite animal?', 'Cat', 'Your favourite person?', 'Bob', 'Your favourite number?', 'Alice'),
('d00022', 'Your favourite animal?', 'Alice', 'Your favourite person?', 'Number 8', 'Your favourite number?', 'Number 7'),
('d00023', 'Your favourite animal?', 'Elephant', 'Your favourite person?', 'John', 'Your favourite number?', 'Michael'),
('d00024', 'Your favourite animal?', 'Number 3', 'Your favourite person?', 'Number 10', 'Your favourite number?', 'Tiger'),
('d00025', 'Your favourite animal?', 'Mary', 'Your favourite person?', 'Number 42', 'Your favourite number?', 'Mary'),
('d00026', 'Your favourite animal?', 'Number 10', 'Your favourite person?', 'Dolphin', 'Your favourite number?', 'Emma'),
('d00027', 'Your favourite animal?', 'Sarah', 'Your favourite person?', 'John', 'Your favourite number?', 'Lion'),
('d00028', 'Your favourite animal?', 'Number 10', 'Your favourite person?', 'Alice', 'Your favourite number?', 'Mary'),
('d00029', 'Your favourite animal?', 'Dolphin', 'Your favourite person?', 'Number 42', 'Your favourite number?', 'Number 8'),
('d00030', 'Your favourite animal?', 'Dog', 'Your favourite person?', 'Tiger', 'Your favourite number?', 'Number 10'),
('d00031', 'Your favourite animal?', 'Tiger', 'Your favourite person?', 'Lion', 'Your favourite number?', 'Michael'),
('d00032', 'Your favourite animal?', 'Bob', 'Your favourite person?', 'Bob', 'Your favourite number?', 'Dog'),
('d00033', 'Your favourite animal?', 'Lion', 'Your favourite person?', 'Mary', 'Your favourite number?', 'Lion'),
('d00034', 'Your favourite animal?', 'Number 8', 'Your favourite person?', 'Cat', 'Your favourite number?', 'Dog'),
('d00035', 'Your favourite animal?', 'Number 8', 'Your favourite person?', 'Dolphin', 'Your favourite number?', 'Catherine'),
('d00036', 'Your favourite animal?', 'Number 42', 'Your favourite person?', 'Bob', 'Your favourite number?', 'Number 8'),
('d00037', 'Your favourite animal?', 'Number 7', 'Your favourite person?', 'Dolphin', 'Your favourite number?', 'James'),
('d00038', 'Your favourite animal?', 'Lion', 'Your favourite person?', 'Bob', 'Your favourite number?', 'Dog'),
('d00039', 'Your favourite animal?', 'Dolphin', 'Your favourite person?', 'Dolphin', 'Your favourite number?', 'Sarah'),
('d00040', 'Your favourite animal?', 'Cat', 'Your favourite person?', 'Cat', 'Your favourite number?', 'Cat'),
('d00041', 'Your favourite animal?', 'Alice', 'Your favourite person?', 'Number 3', 'Your favourite number?', 'Mary'),
('d00042', 'Your favourite animal?', 'Bob', 'Your favourite person?', 'Elephant', 'Your favourite number?', 'Mary'),
('d00043', 'Your favourite animal?', 'Dolphin', 'Your favourite person?', 'Sarah', 'Your favourite number?', 'Michael'),
('d00044', 'Your favourite animal?', 'Bob', 'Your favourite person?', 'Michael', 'Your favourite number?', 'Number 3'),
('d00045', 'Your favourite animal?', 'Emma', 'Your favourite person?', 'Alex', 'Your favourite number?', 'Lion'),
('d00046', 'Your favourite animal?', 'John', 'Your favourite person?', 'Lion', 'Your favourite number?', 'Michael'),
('d00047', 'Your favourite animal?', 'Number 10', 'Your favourite person?', 'Alex', 'Your favourite number?', 'Emma'),
('d00048', 'Your favourite animal?', 'Mary', 'Your favourite person?', 'Mary', 'Your favourite number?', 'Elephant'),
('d00049', 'Your favourite animal?', 'Number 3', 'Your favourite person?', 'Bob', 'Your favourite number?', 'Catherine'),
('d00050', 'Your favourite animal?', 'Michael', 'Your favourite person?', 'Elephant', 'Your favourite number?', 'Lion');

COMMIT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
