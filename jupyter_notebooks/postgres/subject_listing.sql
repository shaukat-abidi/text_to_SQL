create table if not exists subject_listing (
	SUBJECTID VARCHAR(25) not null,
	GENDER VARCHAR(25) not null,
	STUDYID VARCHAR(25) not null,
	SENSOR VARCHAR(25) not null,
	COUNTRY VARCHAR(25) not null
);

insert into subject_listing (SUBJECTID, GENDER, STUDYID, SENSOR, COUNTRY)
values('1','Male','R3500-AD-1906','Actigraph','Germany');

insert into subject_listing (SUBJECTID, GENDER, STUDYID, SENSOR, COUNTRY)
values('2','Female','R3500-AD-1906','Actigraph','Germany');

insert into subject_listing (SUBJECTID, GENDER, STUDYID, SENSOR, COUNTRY)
values('3','Male','R3500-AD-1906','Actigraph','US');

insert into subject_listing (SUBJECTID, GENDER, STUDYID, SENSOR, COUNTRY)
values('4','Female','R3500-AD-1906','Actigraph','US');

insert into subject_listing (SUBJECTID, GENDER, STUDYID, SENSOR, COUNTRY)
values('5','Male','R3500-AD-1906','Actigraph','US');

insert into subject_listing (SUBJECTID, GENDER, STUDYID, SENSOR, COUNTRY)
values('ID01','Male','R5069-OA-1849','Moticon','Italy');

insert into subject_listing (SUBJECTID, GENDER, STUDYID, SENSOR, COUNTRY)
values('ID02','Female','R5069-OA-1849','Moticon','Italy');
