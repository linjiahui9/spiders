set foreign_key_checks = 0;

-- 管理员
drop table if exists `employee`;
create table `employee` (
    `id` bigint(20) not null comment '主键',
    `name` varchar(32) collate utf8_bin not null comment '姓名',
    `username` varchar(32) collate utf8_bin not null comment '用户名',
    `password` varchar(64) collate utf8_bin not null comment '密码',
    `phone` varchar(11) collate utf8_bin not null comment '手机号',
    `sex` varchar(2) collate utf8_bin not null comment '性别',
    `id_number` varchar(18) collate utf8_bin not null comment '身份证号',
    `status` int(11) not null default '1' comment '状态 0:禁用, 1:正常',
    `create_time` datetime not null comment '创建时间',
    `upate_time` datetime not null comment '更新时间',
    `create_user` bigint(20) not null comment '创建人',
    `update_user` bigint(20) not null comment '修改人',
    primary key ('id') using btree,
    unique key `idx_username` (`username`)
) engine=InnoDB default charset=utf collate utf8_bin comment='员工信息';

insert into `emolyee` values ('1', '管理员', 'admin', '123456', '13812312312', '1', '110101199001010047', '1', '2022-11-02 09:20:07', '2022-11-02 09:20:07', '1', '1')



-- 用户(客户端)
drop table if exists `user`;
create table `user` (
    `id` bigint(20) not null comment '主键',
    `name` varchar(32) collate utf8_bin not null comment '姓名',
    `username` varchar(32) collate utf8_bin not null comment '用户名',
    `password` varchar(64) collate utf8_bin not null comment '密码',
    `phone` varchar(11) collate utf8_bin not null comment '手机号',
    `sex` varchar(2) collate utf8_bin not null comment '性别',
    `id_number` varchar(18) collate utf8_bin not null comment '身份证号',
    `avatar` varchar(18) collate utf8_bin default null comment '头像',
    `status` int(11) not null default '1' comment '状态 0:禁用, 1:正常',
    primary key (`id`) using btree
) engine=InnoDB default charset=utf8 collate=utf8_bin comment='用户信息';



-- 分类记录
drop table if exists `category`;
create table `category` (
    `id` bigint(20) not null comment '主键',
    `village_id` bigint(20) not null comment '小区id',
    `type` int(11) default null comment '分类记录 0:分类成功 1:分类失败',
    `create_time` datetime not null comment '创建时间',
    `upate_time` datetime not null comment '更新时间',
    `create_user` bigint(20) not null comment '创建人',
    `update_user` bigint(20) not null comment '修改人',
    primary key (`id`) using btree,
) engine=InnoDB default charset=utf8 collate=utf8_bin comment='分类记录'



-- 地址表(客户端)
drop table if exists `address`;
create table `address` (
    `id` bigint(20) not null comment '主键',
    `user_id` bigint(20) not null comment '用户id',
    -- `user_username` varchar(50) collate utf8_bin not null comment '用户名',
    `sex` tinyint(4) not null comment '性别 0:女, 1:男',
    `phone` varchar(11) collate utf8_bin not null comment '手机号',
    `village_id` bigint(20) not null comment '小区id',
    -- `village_num` varchar(50) collate utf8_bin not null comment '小区编号'
    `detail` varchar(200) character set utf8mb4 default null comment '详细地址',
    `is_default` tinyint(1) not null default '0' comment '默认地址(个人存在多个地址？) 0:否, 1:是',
    `create_time` datetime not null comment '创建时间',
    `upate_time` datetime not null comment '更新时间',
    `create_user` bigint(20) not null comment '创建人',
    `update_user` bigint(20) not null comment '修改人',
    `is_deleted` int(11) not null default '0' comment '是否删除',
    primary key (`id`) using btree
) engine=InnoDB default charset=utf8 collate=utf8_bin comment='地址管理';



-- 小区表
drop table if exists `village`;
create table `village` (
    `id` bigint(20) not null comment '主键',
    `number` varchar(50) collate utf8_bin not null comment '小区编号'
    `create_time` datetime not null comment '创建时间',
    `upate_time` datetime not null comment '更新时间',
    `create_user` bigint(20) not null comment '创建人',
    `update_user` bigint(20) not null comment '修改人',
    `is_deleted` int(11) not null default '0' comment '是否删除',
    primary key (`id`) using btree,
    unique key `village_name` (`number`)
) engine=InnoDB default character=utf8 collate=utf8_bin comment='小区管理';
