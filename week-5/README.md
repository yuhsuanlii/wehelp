Week-5

要求三

INSERT INTO member (name,username,password,follower_count) VALUES ('test','test', 'test','50');
INSERT INTO member (name,username,password,follower_count) VALUES ('Kevin','kevin001', '001','100');
INSERT INTO member (name,username,password,follower_count) VALUES ('Mary','mary002', '002','200');
INSERT INTO member (name,username,password,follower_count) VALUES ('David','david003', '003','300');
INSERT INTO member (name,username,password,follower_count) VALUES ('Tony','tony004', '004','400');

select * from member;
select * from member order by time desc;
select * from member order by time desc LIMIT 1,3;
select * from member where username = "test";
select * from member where username = "test" and password = "test";
UPDATE member SET username = "test2" WHERE id = 1;

![3-1](https://user-images.githubusercontent.com/101781321/196498650-4f03d03f-7420-4ef5-8521-c3f85d4c51c5.JPG)
![3-2](https://user-images.githubusercontent.com/101781321/196498663-f467f42e-aeb8-47ea-a6af-3c949f515eb1.JPG)

要求四

SELECT COUNT(id) FROM member;
SELECT SUM(follower_count) FROM member;
SELECT AVG(follower_count) FROM member;

![4-1](https://user-images.githubusercontent.com/101781321/196498823-bc680203-ce19-4dff-a199-5b44e9f1103c.JPG)

要求五

INSERT INTO message (member_id,content, like_count) VALUES (1,'test','0');
INSERT INTO message (member_id,content, like_count) VALUES (1,'hello test','10');
INSERT INTO message (member_id,content, like_count) VALUES (1,"hello i'm test",'25');
INSERT INTO message (member_id,content, like_count) VALUES (2,"I'm Kevin",'2');
INSERT INTO message (member_id,content, like_count) VALUES (3,"I'm Mary",'3');
INSERT INTO message (member_id,content, like_count) VALUES (4,"I'm David",'4');
INSERT INTO message (member_id,content, like_count) VALUES (5,"I'm Tony",'5');

SELECT name, username, content FROM message INNER JOIN member ON member.id=message.member_id;
SELECT name, username, content FROM message INNER JOIN member ON ( member.id=message.member_id ) WHERE member.username like "%test%";
SELECT AVG(message.like_count) AS avg_like FROM message INNER JOIN member ON ( member.id=message.member_id ) WHERE member.username like "%test%";

![5-1](https://user-images.githubusercontent.com/101781321/196499098-1082dcd5-d0d5-4a5b-b759-03601df76389.JPG)
![5-2](https://user-images.githubusercontent.com/101781321/196499127-346a7831-0dd4-4e7a-aee5-911023354804.JPG)
