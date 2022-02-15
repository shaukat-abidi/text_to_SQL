create table if not exists study_listing (
	STUDYID VARCHAR(25) not null,
	SENSOR VARCHAR(25) not null,
	SITES VARCHAR(25) not null
);

insert into study_listing (STUDYID, SENSOR, SITES)
values('R3500-AD-1906','Actigraph','Germany');

insert into study_listing (STUDYID, SENSOR, SITES)
values('R3500-AD-1906','Actigraph','France');

insert into study_listing (STUDYID, SENSOR, SITES)
values('R3500-AD-1906','Actigraph','US');

insert into study_listing (STUDYID, SENSOR, SITES)
values('R3918-MG-2018','Biostrap','Germany');

insert into study_listing (STUDYID, SENSOR, SITES)
values('R5069-OA-1849','Moticon','Spain');

