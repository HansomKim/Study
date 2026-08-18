USE edulinkdb;
CREATE TABLE Student (
  student_id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50),
  birthdate DATE,
  grade INT,
  school VARCHAR(100),
  phone VARCHAR(20),
  gender VARCHAR(10),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Parent (
  parent_id INT PRIMARY KEY AUTO_INCREMENT,
  student_id INT,
  name VARCHAR(50),
  relation_type VARCHAR(20),
  phone VARCHAR(20),
  email VARCHAR(50),
  FOREIGN KEY (student_id) REFERENCES Student(student_id)
);

CREATE TABLE Tutor (
  tutor_id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50),
  phone VARCHAR(20),
  specialty VARCHAR(50),
  hire_date DATE
);

CREATE TABLE Subject (
  subject_id INT PRIMARY KEY AUTO_INCREMENT,
  subject_name VARCHAR(50),
  grade_level INT,
  tutor_id INT,
  FOREIGN KEY (tutor_id) REFERENCES Tutor(tutor_id)
);

CREATE TABLE Enrollment (
  enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
  student_id INT,
  subject_id INT,
  enrolled_date DATE,
  FOREIGN KEY (student_id) REFERENCES Student(student_id),
  FOREIGN KEY (subject_id) REFERENCES Subject(subject_id)
);

CREATE TABLE Score (
  score_id INT PRIMARY KEY AUTO_INCREMENT,
  student_id INT,
  subject_id INT,
  exam_type VARCHAR(30),
  score INT,
  exam_date DATE,
  FOREIGN KEY (student_id) REFERENCES Student(student_id),
  FOREIGN KEY (subject_id) REFERENCES Subject(subject_id)
);

CREATE TABLE Attendance (
  attendance_id INT PRIMARY KEY AUTO_INCREMENT,
  student_id INT,
  subject_id INT,
  date DATE,
  status VARCHAR(20),
  FOREIGN KEY (student_id) REFERENCES Student(student_id),
  FOREIGN KEY (subject_id) REFERENCES Subject(subject_id)
);

CREATE TABLE Consultation (
  consultation_id INT PRIMARY KEY AUTO_INCREMENT,
  student_id INT,
  tutor_id INT,
  parent_id INT NULL,
  date DATE,
  category VARCHAR(30),
  notes TEXT,
  FOREIGN KEY (student_id) REFERENCES Student(student_id),
  FOREIGN KEY (tutor_id) REFERENCES Tutor(tutor_id),
  FOREIGN KEY (parent_id) REFERENCES Parent(parent_id)
);


