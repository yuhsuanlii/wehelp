

要求三  
--------------

```
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
UPDATE member SET name = "test2" WHERE id = 1;
```

<img src="https://user-images.githubusercontent.com/101781321/196498650-4f03d03f-7420-4ef5-8521-c3f85d4c51c5.JPG" alt="" width="600">
<img src="https://user-images.githubusercontent.com/101781321/196604917-b950afec-c842-4ce3-be7e-28b783d9806b.JPG" alt="" width="600">
<img src="https://user-images.githubusercontent.com/101781321/196604988-890e1138-9849-40cf-b28e-a528198ecec2.JPG" alt="" width="400">



要求四  
--------------

```
SELECT COUNT(id) FROM member;  
SELECT SUM(follower_count) FROM member;  
SELECT AVG(follower_count) FROM member;
```

<img src="https://user-images.githubusercontent.com/101781321/196498823-bc680203-ce19-4dff-a199-5b44e9f1103c.JPG" alt="" width="300">


要求五  
--------------

```
INSERT INTO message (member_id,content, like_count) VALUES (1,'test','0');  
INSERT INTO message (member_id,content, like_count) VALUES (1,'hello test','10');  
INSERT INTO message (member_id,content, like_count) VALUES (1,"hello i'm test",'25');  
INSERT INTO message (member_id,content, like_count) VALUES (2,"I'm Kevin",'2');  
INSERT INTO message (member_id,content, like_count) VALUES (3,"I'm Mary",'3');  
INSERT INTO message (member_id,content, like_count) VALUES (4,"I'm David",'4');  
INSERT INTO message (member_id,content, like_count) VALUES (5,"I'm Tony",'5');  

SELECT name, username, content FROM message INNER JOIN member ON member.id=message.member_id;  
SELECT name, username, content FROM message INNER JOIN member ON ( member.id=message.member_id ) WHERE member.username="test";
SELECT AVG(message.like_count) AS avg_like FROM message INNER JOIN member ON ( member.id=message.member_id ) WHERE member.username="test";
```

<img src="https://user-images.githubusercontent.com/101781321/196499098-1082dcd5-d0d5-4a5b-b759-03601df76389.JPG" alt="" width="600">
<img src="https://user-images.githubusercontent.com/101781321/196605085-9b71aa77-3dc8-4e0c-b2da-d8bb3efbc8bb.JPG" alt="" width="600">

