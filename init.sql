USE score;

INSERT INTO admin(account, password, username, is_super) VALUES ("chenliwei", "chenliwei123", "陈李维", 1);

INSERT INTO user(account, username, password, education, grade) VALUES ("ylhao", "衣龙浩", "123456", "硕士", "研二");
INSERT INTO user(account, username, password, education, grade) VALUES ("xiaohua", "肖华", "123456", "硕士", "研二");
INSERT INTO user(account, username, password, education, grade) VALUES ("shecairui", "佘才睿", "123456", "硕士", "研二");
INSERT INTO user(account, username, password, education, grade) VALUES ("gaoyuhan", "高语晗", "123456", "硕士", "研二");
INSERT INTO user(account, username, password, education, grade) VALUES ("yangyaxuan", "杨雅轩", "123456", "硕士", "研二");
INSERT INTO user(account, username, password, education, grade) VALUES ("zhangfei", "张飞", "123456", "硕士", "研二");
INSERT INTO user(account, username, password, education, grade) VALUES ("xuqizhen", "许奇臻", "123456", "硕士", "研二");
INSERT INTO user(account, username, password, education, grade) VALUES ("luguorui", "卢国瑞", "123456", "硕士", "研三");
INSERT INTO user(account, username, password, education, grade) VALUES ("guoyingjie", "郭英杰", "123456", "硕士", "研三");
INSERT INTO user(account, username, password, education, grade) VALUES ("zhangyuantong", "张元瞳", "123456", "硕士", "研三");
INSERT INTO user(account, username, password, education, grade) VALUES ("tianlinan", "田力楠", "123456", "硕士", "研三");
INSERT INTO user(account, username, password, education, grade) VALUES ("lijinfeng", "李锦峰", "123456", "博士", "博一");
INSERT INTO user(account, username, password, education, grade) VALUES ("mamengyu", "马梦雨", "123456", "博士", "博一");
INSERT INTO user(account, username, password, education, grade) VALUES ("liutong", "柳童", "123456", "博士", "研二");

INSERT INTO score_label(name) VALUES ("论文");
INSERT INTO score_label(name) VALUES ("工具");
INSERT INTO score_label(name) VALUES ("报告");
INSERT INTO score_label(name) VALUES ("发票");
INSERT INTO score_label(name) VALUES ("活动");
INSERT INTO score_label(name) VALUES ("迟到");
INSERT INTO score_label(name) VALUES ("早退");
INSERT INTO score_label(name) VALUES ("缺勤");
INSERT INTO score_label(name) VALUES ("其他");
