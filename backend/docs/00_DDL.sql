CREATE TABLE person(
    id                  SERIAL PRIMARY KEY,
    "name"              VARCHAR(50) NOT NULL,
    surname             VARCHAR(50) NOT NULL,
    email               VARCHAR(20) UNIQUE NOT NULL,
    pwd                 VARCHAR(20) NOT NULL
);

CREATE TABLE student(
    id_studente         INT PRIMARY KEY,
    absence_percentage  INT NOT NULL DEFAULT 0,
    FOREIGN KEY (id_studente) REFERENCES person(id) ON DELETE CASCADE
);

CREATE TABLE teacher(
    id_teacher          INT PRIMARY KEY,
    teaching_hours      INT NOT NULL DEFAULT 0,
    FOREIGN KEY (id_teacher) REFERENCES person(id) ON DELETE CASCADE
);

CREATE TABLE course(
    id_course           SERIAL PRIMARY KEY,
    "name"              VARCHAR(50) NOT NULL,
    "description"       VARCHAR(200) NOT NULL
);

CREATE TABLE professorship(
    id_teacher          INT NOT NULL,
    id_course           INT UNIQUE NOT NULL,
    PRIMARY KEY(id_teacher, id_course),
    FOREIGN KEY(id_teacher) REFERENCES teacher(id_teacher),
    FOREIGN KEY(id_course) REFERENCES course(id_course)
);

CREATE TABLE enrollment(
    id_student          INT NOT NULL,
    id_course           INT NOT NULL,
    PRIMARY KEY(id_student, id_course),
    FOREIGN KEY(id_student) REFERENCES student(id_student),
    FOREIGN KEY(id_course) REFERENCES course(id_course)
);

