SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `project`
--

-- --------------------------------------------------------

--
-- 表的结构 `department`
--

CREATE TABLE `department` (
  `Department_ID` varchar(2) NOT NULL,
  `Department_Name` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `department`
--

INSERT INTO `department` (`Department_ID`, `Department_Name`) VALUES
('01', 'RQA Engineer'),
('02', 'Embedded Software En'),
('03', 'PC Software Engineer'),
('04', 'Hardware Development'),
('05', 'Test Engineer'),
('06', 'Marketing'),
('07', 'Operation'),
('08', 'Customer Service'),
('09', 'Planning'),
('10', 'Adminstrative');

--
-- 转储表的索引
--

--
-- 表的索引 `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`Department_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
