drop database if exists school;
-- 常见为school的数据库并指定默认的字符
create database school default charset utf8;
use school;

-- 如果存在就删除学生表
drop table if exists tb_student;

-- 创建学生表
create table tb_student
(
stuid int not null comment "学号",
stuname varchar(20) comment "姓名",
stusex bit default 1 comment "性别",
stubirth date comment "生日",
primary key (stuid)
)

-- 修改学生表
alter table tb_student add column stuaddr varchar(255);

-- 修改表，删除列
alter table tb_student drop column stuaddr;

alter table tb_student add column stuaddr varchar(255) comment "地址";

alter table tb_student change column stuaddr stuaddr varchar(512) comment "地址";

-- 插入数据
insert into tb_student values(1001, "张三丰", 1, "1982-2-2", "湖北十堰");
insert into tb_student values(1002, '张翠山', 1, "1982-2-2", "武当山");
insert into tb_student (stuid, stuname) values (1003, '宋远桥');
insert into tb_student (stuid, stusex, stuname) values (1004, 0, '殷素素');

insert into tb_student (stuid, stuname, stusex) values
(1005, '杨逍', 1),
(1006, '谢逊', 1),
(1007, '杨不悔', 0);

-- 删除学生
delete from tb_student where stuid=1007;


-- 截断全表
-- truncate table ...

insert into tb_student values
(1007, '周芷若', 0,'1990-5-1', '湖北武汉'),
(1008, '范瑶', 1,'1885-4-15','浙江杭州');





