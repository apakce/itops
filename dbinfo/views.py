import pymysql
from datetime import datetime
from dbinfo.models import dbinfo

from django.contrib.auth.hashers import make_password

#保存内容
def savemessa(title, tab, name,username):
    createtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "INSERT INTO Mess(title,tab,message,user,date) VALUES (%s,%s,%s,%s,%s) "
        conncur.execute(connsql, (title, tab, name,username,createtime))
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        print(e)
        return False


#保存内容
def saveearromessa(title, userper,affect,inpendtimeid, tab,name, username):
    createtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "INSERT INTO messgerro(title, userper,accfet,datetime, tips,marke, creatuser,creatime) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) "
        conncur.execute(connsql, (title, userper,affect,inpendtimeid, tab,name, username,createtime))
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        print(e)
        return False

def upsaves(texid, title, tab,name):
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "UPDATE Mess SET title=%s,tab=%s,message=%s WHERE id=%s"
        conncur.execute(connsql, (title, tab, name,texid))
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        print(e)
        return False

def upsaveerr(title, userper,affect,inpendtimeid, tab,name, username,texid):
    conn = dbinfo()
    createtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        conncur = conn.cursor()
        connsql = "UPDATE messgerro SET title=%s, userper=%s,accfet=%s,datetime=%s, tips=%s,marke=%s, creatuser=%s,creatime=%s WHERE id=%s"
        conncur.execute(connsql, (title, userper,affect,inpendtimeid, tab,name, username,createtime,texid))
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        print(e)
        return False

# 验证ldaprecord表是否存在
def selectldaprecord():
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "show tables like 'record_ldap'"
        conncur.execute(connsql)
        histroycounts = conncur.fetchone()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        print(e)
        return False

# 创建ldaprecord表
def crear_record_ldap():
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = '''CREATE TABLE `record_ldap` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `account` varchar(255) NOT NULL,
  `apps` varchar(255) NOT NULL,
  `applicant` varchar(255) NOT NULL,
  `application_division` varchar(255) NOT NULL,
  `manager` varchar(255) NOT NULL,
  `permission` varchar(255) NOT NULL,
  `Application_Date` varchar(255) NOT NULL,
  `end` varchar(255) NOT NULL,
  `link_server` varchar(255) NOT NULL,
  `Status` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8'''
        conncur.execute(connsql)
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        print(e)
        return False

# 验证dnsrecord表是否存在
def selectdnsrecord():
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "show tables like 'record_dns'"
        conncur.execute(connsql)
        histroycounts = conncur.fetchone()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        print(e)
        return False

# 创建dnsrecord表
def crear_record_dns():
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = '''CREATE TABLE `record_dns` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain_name` varchar(255) NOT NULL,
  `apps` varchar(255) NOT NULL,
  `applicant` varchar(255) NOT NULL,
  `application_division` varchar(255) NOT NULL,
  `ops` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `Applicant_time` varchar(255) NOT NULL,
  `Status` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8'''
        conncur.execute(connsql)
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        print(e)
        return False


#查询数据库
def selectdb(dbname,Status):
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "select * from " + dbname + " where Status='" + Status+"'"
        conncur.execute(connsql)
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        print(e)
        return False

# 验证indexmessage表是否存在
def selectindexmessagesrecord():
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "show tables like 'indexmessage'"
        conncur.execute(connsql)
        histroycounts = conncur.fetchone()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        print(e)
        return False

#查询数据库
def selectindexmessagedb():
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "select * from indexmessage where id=(select max(id) from indexmessage)"
        conncur.execute(connsql)
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        print(e)
        return False

#插入indexmessage数据库
def insert_indexmessagedb(allusercountvalue, alldisableusercountvalue, allexpiredpasswordusercountvalue, alllockusercountvalue, nologoinusercountvalue, allgroupcountvalue, allgrouptalkgroupcountvalue,allgroupsavegroupcpuntvalue,allgroupnomembercountvalue,allgrouphasmailcountvalue,allcomputercountvalue,allcomputernologoincountvalue,allcomputernodisablecpuntvalue,allcomputerdisablecountvalue,allexchangeusercountvalue,allnoexchangeusercountvalue,allexchangehasarchivecpuntvalue,allexchangenodizhicountvalue,allexchangenoarchivecountvalue): #写入数据
    conn = dbinfo()
    try:
        createtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        conncur = conn.cursor()
        connsql = "INSERT INTO indexmessage (allusercountvalue, alldisableusercountvalue, allexpiredpasswordusercountvalue, alllockusercountvalue, nologoinusercountvalue, allgroupcountvalue, allgrouptalkgroupcountvalue, allgroupsavegroupcpuntvalue,allgroupnomembercountvalue,allgrouphasmailcountvalue,allcomputercountvalue,allcomputernologoincountvalue,allcomputernodisablecpuntvalue,allcomputerdisablecountvalue,allexchangeusercountvalue,allnoexchangeusercountvalue,allexchangehasarchivecpuntvalue,allexchangenodizhicountvalue,allexchangenoarchivecountvalue,datetime) VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        aa=conncur.execute(connsql, (allusercountvalue, alldisableusercountvalue, allexpiredpasswordusercountvalue, alllockusercountvalue, nologoinusercountvalue, allgroupcountvalue, allgrouptalkgroupcountvalue,allgroupsavegroupcpuntvalue,allgroupnomembercountvalue,allgrouphasmailcountvalue,allcomputercountvalue,allcomputernologoincountvalue,allcomputernodisablecpuntvalue,allcomputerdisablecountvalue,allexchangeusercountvalue,allnoexchangeusercountvalue,allexchangehasarchivecpuntvalue,allexchangenodizhicountvalue,allexchangenoarchivecountvalue,createtime))
        conn.commit()
        conn.close()
        return aa
    except Exception as e:
        print(e)
        return False

#插入ldap数据库
def insert_ldapdb(account, apps, applicant, application_division, manager, permission, Application_Date,end,link_server,Status): #写入数据
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "INSERT INTO record_ldap (account, apps, applicant, application_division, manager, permission, Application_Date, end,link_server,Status) VALUE (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        aa=conncur.execute(connsql, (account, apps, applicant, application_division, manager, permission, Application_Date,end,link_server,Status))
        conn.commit()
        conn.close()
        return aa
    except Exception as e:
        print(e)
        return False

#更新LDAP数据库
def upadte_ldapdb(ID,account, apps, applicant, application_division, manager, permission, Application_Date,end,link_server):
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "update record_ldap SET account= %s, apps= %s, applicant= %s, application_division= %s, manager= %s, permission= %s, Application_Date= %s,end= %s,link_server= %s where ID= %s"
        aa = conncur.execute(connsql, (account, apps, applicant, application_division, manager, permission, Application_Date,end,link_server,ID)) #数据库写入续约失败返回0，续约成功返回1
        conn.commit()
        conn.close()
        return aa #返回1或者0 1成功 0失败
    except Exception as e:
        print(e)
        return False

#删除LDAP数据
def delete_ldapdb(ID,Status):  #
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "update record_ldap SET status=%s  where ID=%s"
        aa=conncur.execute(connsql, (Status, ID))   #数据库删除失败返回0，删除成功返回1
        conn.commit()
        conn.close()
        return aa
    except Exception as e:
        print(e)
        return False

#插入DNS数据库
def insert_dnsdb(domain_name, apps, applicant, application_division, ops, type, Applicant_time,Status): #写入数据
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "INSERT INTO record_dns (domain_name, apps, applicant, application_division, ops, type, Applicant_time,Status) VALUE (%s, %s, %s, %s, %s, %s, %s, %s)"
        aa=conncur.execute(connsql, (domain_name, apps, applicant, application_division, ops, type, Applicant_time,Status))
        conn.commit()
        conn.close()
        return aa
    except Exception as e:
        print(e)
        return False

#更新DNS数据库
def upadte_dnsdb(ID,domain_name, apps, applicant, application_division, ops, type, Applicant_time):
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "update record_dns SET domain_name= %s, apps= %s, applicant= %s, application_division= %s, ops= %s, type= %s, Applicant_time= %s where ID= %s"
        aa = conncur.execute(connsql, (domain_name, apps, applicant, application_division, ops, type, Applicant_time,ID)) #数据库写入续约失败返回0，续约成功返回1
        conn.commit()
        conn.close()
        return aa #返回1或者0 1成功 0失败
    except Exception as e:
        print(e)
        return False

#删除DNS数据
def delete_dnsdb(ID,Status):  #
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "update record_dns SET status=%s  where ID=%s"
        aa=conncur.execute(connsql, (Status, ID))   #数据库删除失败返回0，删除成功返回1
        conn.commit()
        conn.close()
        return aa
    except Exception as e:
        print(e)
        return False

#根据id 获取dns数据
def get_dnsdbvaule(ID):  #
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "select * from record_dns where ID=%s"
        conncur.execute(connsql, (ID))
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return False

#根据id 获取ldap数据
def get_ldapdbvaule(ID):  #
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "select * from record_ldap where ID=%s"
        conncur.execute(connsql, (ID))
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return False


def getldap3configtion():
    try:
        conn = dbinfo()
        conncur = conn.cursor()
        connsql = "SELECT * FROM ldap3_configtion LIMIT 1"
        conncur.execute(connsql)
        histroycounts = conncur.fetchone()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return None

def getskey():
    try:
        conn = dbinfo()
        conncur = conn.cursor()
        connsql = "SELECT * FROM exiisconfig LIMIT 1"
        conncur.execute(connsql)
        histroycounts = conncur.fetchone()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return None


#iis
def getliisconfigtion():
    try:
        conn = dbinfo()
        conncur = conn.cursor()
        connsql = "SELECT * FROM exiisconfig LIMIT 1"
        conncur.execute(connsql)
        histroycounts = conncur.fetchone()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return None


# 获取UserPer 权限,监控 的第一条数据
def getpermsessage():
    try:
        conn = dbinfo()
        conncur = conn.cursor()
        connsql = "SELECT fieldgroup,changepwdgroup,logongroup,operagroup,monitor,zabbixurl,zabbixuser,zabbixpassword FROM UserPer LIMIT 1"
        conncur.execute(connsql)
        histroycounts = conncur.fetchone()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return None

def insert_log_table_name(table_name, ip, apiname, username, isSuccess, request,message,other):
    time_m = datetime.now().strftime('%Y_%m')
    table_name = str(table_name)+"_"+str(time_m)
    conn = dbinfo()
    try:
        createtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        conncur = conn.cursor()
        connsql = "INSERT INTO "+table_name +"(ip, apiname,username,isSuccess,request,message,other,times) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) "
        conncur.execute(connsql, (ip, apiname, username, isSuccess, request,message,other,createtime))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        try:
            conn = dbinfo()
            conncur = conn.cursor()
            connsql = "CREATE TABLE `%s` (`id` int(11) NOT NULL AUTO_INCREMENT,`ip` varchar(255) DEFAULT NULL,`apiname` varchar(255) DEFAULT NULL,`username` varchar(255) NOT NULL,`isSuccess` varchar(255) DEFAULT NULL,`request` mediumtext,`message` mediumtext,`other` varchar(2550) DEFAULT NULL,`times` datetime DEFAULT NULL,PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;" % (
            table_name)
            conncur.execute(connsql)
            conn.commit()
            createtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            conncur = conn.cursor()
            connsql = "INSERT INTO " + table_name + "(ip, apiname,username,isSuccess,request,message,other,times) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) "
            conncur.execute(connsql, (ip, apiname, username, isSuccess, request, message, other, createtime))
            conn.commit()
            conn.close()
            return True
        except Exception as es:
            return False


def insert_log(username,request,isSuccess,message,other):
    try:
        ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR'))
        apiname = request.path_info
        #apiname = request.path_info.split('/')[-1]
        if request.method == 'GET':
            request = str(request.GET)
        else:
            request = str(request.POST)
        insert_log_table_names = insert_log_table_name('log', ip, apiname, username, isSuccess, request,message,other)
        return insert_log_table_names
    except Exception as e:
        print(e)
        return False


def get_log(sqlname=None):
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        time_m = datetime.now().strftime('%Y_%m')
        if sqlname:
            table_name = sqlname
        else:
            table_name = str('log') + "_" + str(time_m)
        connsql = "select * from "+table_name+" order by times desc"
        conncur.execute(connsql, ())
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return False

def show_tables():
    try:
        conn = dbinfo()
        conncur = conn.cursor()
        connsql = "show tables;"
        conncur.execute(connsql, ())
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return False

#数据库查询
def show_sqllog(sqlname,vaules):
    conn = dbinfo()
    try:
        vaules = '%'+vaules+'%'
        conncur = conn.cursor()
        connsql = "SELECT * FROM "+ sqlname +" WHERE CONCAT(id,ip,apiname,username,isSuccess,request,message,other,times) LIKE %s"
        conncur.execute(connsql, (vaules))
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return False


def get_log_ldapattributes():
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "select * from LDAPAttributes"
        conncur.execute(connsql, ())
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return False

# 单条件加查询表
# 表明，需要查询的字段，依据字段名，依据字段值，
def onefindadmintable(table, text, field1, field1value):
    conn = dbinfo()
    try:
        table = table.replace("'", r"\'")
        text = text.replace("'", r"\'")
        field1 = field1.replace("'", r"\'")
        field1value = field1value.replace("'", r"\'")
        conncur = conn.cursor()
        connsql = "select %s from %s where %s ='%s'" % (text, table, field1, field1value)
        conncur.execute(connsql)
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        print(e)
        return False




def findadmintable():
    try:
        conn = dbinfo()
        conncur = conn.cursor()
        connsql = "SELECT * FROM Mess  order by date desc "
        conncur.execute(connsql)
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return None
def finderromintable():
    try:
        conn = dbinfo()
        conncur = conn.cursor()
        connsql = "SELECT * FROM messgerro  order by creatime desc "
        conncur.execute(connsql)
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return None


#id查询内容
def searmessid(textid):
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "select * from Mess where id = %s"
        conncur.execute(connsql, (textid))
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        print(e)
        return False

#id查询内容
def searmesserrid(textid):
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "select * from messgerro where id = %s"
        conncur.execute(connsql, (textid))
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        print(e)
        return False

#判断是否使用使用谷歌二次验证
def goostatus():
    try:
        conn = dbinfo()
        conncur = conn.cursor()
        connsql = "SELECT * FROM tokenstatus LIMIT 1"
        conncur.execute(connsql)
        histroycounts = conncur.fetchone()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        print(e)
        return False

def creatUsertoken():
    try:
        conn = dbinfo()
        conncur = conn.cursor()
        connsql = "show tables like 'usertoken'"
        conncur.execute(connsql)
        usertoken = conncur.fetchone()
        conn.commit()
        if not usertoken:
            conncur = conn.cursor()
            connsql = '''DROP TABLE IF EXISTS `usertoken`;
                           CREATE TABLE `usertoken` (
                           `id` int(11) NOT NULL AUTO_INCREMENT,
                           `username` varchar(255) DEFAULT NULL,
                           `token` varchar(255) DEFAULT NULL,
                           `date` datetime DEFAULT NULL,
                           `ip` varchar(255) DEFAULT NULL,
                           `agent` varchar(255) DEFAULT NULL,
                           PRIMARY KEY (`id`)
                           ) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
                       '''
            conncur.execute(connsql)
            conn.commit()
        else:
            try:
                conncur = conn.cursor()
                connsql = '''ALTER TABLE usertoken ADD COLUMN `ip` VARCHAR(255) DEFAULT NULL;
                      ALTER TABLE usertoken ADD COLUMN `agent` VARCHAR(255) DEFAULT NULL;
                '''
                conncur.execute(connsql)
                conn.commit()
            except Exception as e:
                pass
    except Exception as e:
        insert_log_table_name('log', '127.0.0.1', 'creatUsertoken', 'adminportal', 'False', 'usertoken', '创建usertoken表', str(e))
    return 1


#查询密钥是否存在
def seargooled(username):
    conn = dbinfo()
    try:
        creatUsertoken()
        conncur = conn.cursor()
        connsql = "select * from usertoken where username = %s"
        conncur.execute(connsql, (username))
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        print(e)
        return False

# 更新密钥相关ip mac
def updateUsertoken(username, ip, agent):
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "update usertoken set ip=%s, agent=%s where username = %s"
        conncur.execute(connsql, (ip, agent, username))
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        print(e)
        return False

#验证成功插入密钥
def insert_tokenb(username, token): #写入数据
    conn = dbinfo()
    try:
        createtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        conncur = conn.cursor()
        connsql = "INSERT INTO usertoken (username, token,date ) VALUE (%s,%s,%s)"
        aa=conncur.execute(connsql, (username, token,createtime))
        conn.commit()
        conn.close()
        return aa
    except Exception as e:
        print(e)
        return False

def onedeltable(id):
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "DELETE FROM  Mess where id = %s"
        conncur.execute(connsql, (id))
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        print (e)
        return False
def derroltable(id):
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "DELETE FROM  messgerro where id = %s"
        conncur.execute(connsql, (id))
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        print (e)
        return False

# 单条件加查询不过滤text
# 表明，需要查询的字段，依据字段名，依据字段值，
def onefindadmintablenoreplace(table, text, field1, field1value):
    conn = dbinfo()
    try:
        table = table.replace("'", r"\'")
        field1 = field1.replace("'", r"\'")
        field1value = field1value.replace("'", r"\'")
        conncur = conn.cursor()
        connsql = "select %s from %s where %s ='%s'" % (text, table, field1, field1value)
        conncur.execute(connsql)
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        print(e)
        return False

# 查找api 普通权限
def select_apipermissions(apiname, username):
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "SELECT `apiusers_apinamepermissions`.`apiname` FROM `apiusers_apinamepermissions`,apiusers_profile WHERE (apiusers_profile.is_active = 1 AND `apiusers_apinamepermissions`.`apiname` = %s AND apiusers_profile.username = %s)"
        conncur.execute(connsql, (apiname, username,))
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return False

# print(select_apipermissions('Ldap3Search', 'admin'))
# DRF API 日志
def insert_drf_api_log(request,isSuccess,message):
    try:
        ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR'))
        try:
            apiname = request.path.split(r"/")[1]
        except Exception as e:
            apiname = request._request.split(r'/')[-2]
        apiusername = request.user
        insert_log_table_names = insert_log_table_name('log_api', str(ip), str(apiname), str(apiusername), isSuccess, str(request.data), message, str(request.auth))
        return insert_log_table_names
    except Exception as e:
        print(e)
        return False

def get_apiusers_profile():
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "SELECT id,username,is_active,name,department,description FROM apiusers_profile "
        conncur.execute(connsql, ())
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return False

def update_apiusers_profile(id,name,vaule):
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "UPDATE apiusers_profile SET "+name+"=%s WHERE id=%s"
        conncur.execute(connsql, (vaule, id))
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        return False

def delect_apiusers_profile(id):
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "DELETE FROM apiusers_profile WHERE id=%s"
        conncur.execute(connsql, (id))
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        return False

def insert_apiusers_profile(username,password,name=None,department=None,description=None):
    try:
        password = make_password(password)
        createtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        conn = dbinfo()
        conncur = conn.cursor()
        connsql = "INSERT INTO apiusers_profile (username,password,name,department,description,is_active,date_joined) VALUES (%s,%s,%s,%s,%s,1,%s)"
        conncur.execute(connsql, (username,password,name,department,description,createtime))
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        return False

def get_apinamepermissions(username_id):
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "SELECT * FROM apiusers_apinamepermissions WHERE username_id=%s"
        conncur.execute(connsql, (username_id))
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return False

def get_apinamepermissions_is(username_id,apiname):
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "SELECT * FROM apiusers_apinamepermissions WHERE username_id=%s AND apiname=%s"
        conncur.execute(connsql, (username_id,apiname))
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return False


def delect_apinamepermissions(id):
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "DELETE FROM apiusers_apinamepermissions WHERE id=%s"
        conncur.execute(connsql, (id))
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        return False

def delect_apinamepermissions_username_id(username_id):
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "DELETE FROM apiusers_apinamepermissions WHERE username_id=%s"
        conncur.execute(connsql, (username_id))
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        return False


def insert_apinamepermissions(username_id,apiname):
    try:
        conn = dbinfo()
        conncur = conn.cursor()
        connsql = "INSERT INTO apiusers_apinamepermissions (username_id,apiname) VALUES (%s,%s)"
        conncur.execute(connsql, (username_id,apiname))
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        return False


def get_attributeslevel():
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "SELECT * FROM apiusers_attributeslevel"
        conncur.execute(connsql, ())
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return False

def get_attributeslevel_apiname(apiname):
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "SELECT * FROM apiusers_attributeslevel WHERE apiname=%s"
        conncur.execute(connsql, (apiname))
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return False


def delect_attributeslevel(id):
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "DELETE FROM apiusers_attributeslevel WHERE id=%s"
        conncur.execute(connsql, (id))
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        return False

def insert_attributeslevel(apiname,attributes):
    try:
        conn = dbinfo()
        conncur = conn.cursor()
        connsql = "INSERT INTO apiusers_attributeslevel (apiname,attributes) VALUES (%s,%s)"
        conncur.execute(connsql, (apiname,attributes))
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        return False

def update_attributeslevel(attributes,id):
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "UPDATE apiusers_attributeslevel SET attributes=%s WHERE id=%s"
        conncur.execute(connsql, (attributes,id))
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        return False



#查询当天获取数据库信息是否执行
def getexchangedbexmailboxsize(datatimevalue):
    try:
        conn = dbinfo()
        conncur = conn.cursor()
        connsql = "SELECT * FROM exmailboxsize Where messageDatetime = %s ORDER BY databaseSizeInt DESC "
        conncur.execute(connsql,(datatimevalue))
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return None

#查询当天获取数据库信息是否执行
def getexchangedbexmailboxsizeValue(datatimevalue,databaseIdentity,typeValue):
    try:
        conn = dbinfo()
        conncur = conn.cursor()
        if typeValue == 'true':
            connsql = "SELECT databaseGuid,databaseIdentity FROM exmailboxsize Where messageDatetime = %s and databaseIdentity like %s"
        else:
            connsql = "SELECT * FROM exmailboxsize Where messageDatetime = %s and databaseIdentity like %s"
        conncur.execute(connsql,(datatimevalue,"%"+databaseIdentity+"%"))
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return None


#查询当天获取数据库信息是否执行
def getMailboxMessagebyGuidAndDays(mailboxGuid,datatimeValuetoday,datatimeValuestartday):
    try:
        conn = dbinfo()
        conncur = conn.cursor()
        connsql = "SELECT * FROM exmailboxsize where databaseGuid = %s and messageDatetime <= %s and  messageDatetime >= %s"
        conncur.execute(connsql,(mailboxGuid,datatimeValuetoday,datatimeValuestartday))
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return None



# 验证exchangedbmessage表是否存在
def selectexchangedbmessage():
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "show tables like 'exchangedbmessage'"
        conncur.execute(connsql)
        histroycounts = conncur.fetchone()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return False


# 创建exchangedbmessage表
def crear_exchangedbmessage():
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = '''CREATE TABLE `exchangedbmessage` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `datatimes` datetime DEFAULT NULL COMMENT '插入时间',
  `mailboxname` varchar(255) DEFAULT NULL COMMENT '数据库名称',
  `mailboxsite` bigint(20) DEFAULT '0' COMMENT '数据库大小',
  `increaseday` bigint(20) DEFAULT '0' COMMENT '较昨日增加',
  `increaseweek` bigint(20) DEFAULT '0' COMMENT '较前7天平均每天增加',
  `estimateday` bigint(20) DEFAULT '0' COMMENT '明日mailbox数据库大小预估',
  `estimateweek` bigint(20) DEFAULT '0' COMMENT '7天后mailbox大小预估',
  `memberaccount` int(11) DEFAULT '0' COMMENT '数据库成员',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;'''
        conncur.execute(connsql)
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return False

def getexchangedbmessage(datatimevalue):
    try:
        conn = dbinfo()
        conncur = conn.cursor()
        connsql = "SELECT * FROM exchangedbmessage Where DATE_FORMAT(datatimes, '%%Y-%%m-%%d' )  = %s"
        conncur.execute(connsql,(datatimevalue))
        histroycounts = conncur.fetchone()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return None


def getexchangedblastdaymessage(dbname,datatimevalue):
    try:
        conn = dbinfo()
        conncur = conn.cursor()
        connsql = "SELECT * FROM exchangedbmessage Where DATE_FORMAT(datatimes, '%%Y-%%m-%%d' )  = %s and mailboxname = %s"
        conncur.execute(connsql,(datatimevalue,dbname))
        histroycounts = conncur.fetchone()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return None

#验证成功插入密钥
def insert_exchangedbmessage(mailboxname, mailboxsite,increaseday,increaseweek,estimateday,estimateweek,memberaccount): #写入数据
    conn = dbinfo()
    try:
        createtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        conncur = conn.cursor()
        connsql = "INSERT INTO exchangedbmessage (mailboxname, mailboxsite,datatimes,increaseday,increaseweek,estimateday,estimateweek,memberaccount) VALUE (%s,%s,%s,%s,%s,%s,%s,%s)"
        aa=conncur.execute(connsql, (mailboxname, mailboxsite,createtime,increaseday,increaseweek,estimateday,estimateweek,memberaccount))
        conn.commit()
        conn.close()
        return aa
    except Exception as e:
        return False

# 验证exchangedbmessage表是否存在
def selectexchangedbisStartMailboxMessageHas():
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "show tables like 'isStartMailboxMessageHas'"
        conncur.execute(connsql)
        histroycounts = conncur.fetchone()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return False


# 创建isStartMailboxMessageHas表
def create_isStartMailboxMessageHas():
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = '''CREATE TABLE `isStartMailboxMessageHas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `datetimeValue` datetime DEFAULT NULL COMMENT '数据库信息获取执行时间',
  `isStart` int(11) DEFAULT NULL COMMENT '当前时间是否执行，1（执行），0（未执行）',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;'''
        conncur.execute(connsql)
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return False


#查询当天获取数据库信息是否执行
def getexchangedbisStartMailboxMessageHas(datatimevalue):
    try:
        conn = dbinfo()
        conncur = conn.cursor()
        connsql = "SELECT * FROM isStartMailboxMessageHas Where DATE_FORMAT(datetimeValue, '%%Y-%%m-%%d' )  = %s and isStart = 1 ORDER BY datetimeValue ASC"
        conncur.execute(connsql,(datatimevalue))
        histroycounts = conncur.fetchone()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return None



#插入当天信息获取执行记录
def insert_isStartMailboxMessageHas(datatimevalue): #写入数据
    conn = dbinfo()
    try:
        createtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        conncur = conn.cursor()
        connsql = "INSERT INTO isStartMailboxMessageHas (datetimeValue, isStart) VALUE (%s,1)"
        aa=conncur.execute(connsql, (datatimevalue))
        conn.commit()
        conn.close()
        return aa
    except Exception as e:
        return False



# 验证exchangedbmessage表是否存在
def selectexmailboxsizeHas():
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "show tables like 'exmailboxsize'"
        conncur.execute(connsql)
        histroycounts = conncur.fetchone()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return False

# 创建isStartMailboxMessageHas表
def create_exmailboxsize():
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = '''DROP TABLE IF EXISTS `exmailboxsize`;
CREATE TABLE `exmailboxsize` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `databaseIdentity` varchar(255) DEFAULT NULL COMMENT '数据库名称',
  `databaseGuid` varchar(255) DEFAULT NULL COMMENT '数据库guid（唯一标识）',
  `databaseSizeStr` varchar(255) DEFAULT NULL COMMENT '数据库大小（显示）',
  `databaseSizeInt` bigint(255) DEFAULT NULL COMMENT '数据库实际大小（单位：b）',
  `databaseSpaceStr` varchar(255) DEFAULT NULL COMMENT '数据库空白空间大小（显示）',
  `databaseSpaceInt` bigint(255) DEFAULT NULL COMMENT '数据库空白空间大小(单位：b）',
  `databaseMailboxNumber` int(11) DEFAULT NULL COMMENT 'DB内数据库数量',
  `databaseSpaceProportion` int(11) DEFAULT NULL COMMENT '空白空间占比',
  `messageDatetime` datetime DEFAULT NULL COMMENT '数据时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;'''
        conncur.execute(connsql)
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return False



#插入indexmessage数据库
def insert_exmailboxsizedb(databaseIdentity,databaseGuid, databaseSizeStr, databaseSizeInt, databaseSpaceStr, databaseSpaceInt, databaseMailboxNumber, databaseSpaceProportion,messageDatetime): #写入数据
    conn = dbinfo()
    try:
        createtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        conncur = conn.cursor()
        connsql = "INSERT INTO exmailboxsize (databaseIdentity,databaseGuid, databaseSizeStr, databaseSizeInt, databaseSpaceStr, databaseSpaceInt, databaseMailboxNumber, databaseSpaceProportion,messageDatetime) VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        aa=conncur.execute(connsql, (databaseIdentity,str(databaseGuid), databaseSizeStr, int(databaseSizeInt), databaseSpaceStr, int(databaseSpaceInt), int(databaseMailboxNumber), int(databaseSpaceProportion),messageDatetime))
        conn.commit()
        conn.close()
        return aa
    except Exception as e:
        return False

#查询当天获取数据库信息是否执行
def getexchangedbisStartMailboxMessageHas_Nodate():
    try:
        conn = dbinfo()
        conncur = conn.cursor()
        connsql = "SELECT * FROM isStartMailboxMessageHas Where isStart = 1 ORDER BY datetimeValue desc"
        conncur.execute(connsql)
        histroycounts = conncur.fetchone()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return None

# 验证exchangedbmessage表是否存在
def selectMailboxConfigMessageHas():
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = "show tables like 'mailboxmessageconfig'"
        conncur.execute(connsql)
        histroycounts = conncur.fetchone()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return False

# 创建isStartMailboxMessageHas表
def create_mailboxMessageConfigHas():
    conn = dbinfo()
    try:
        conncur = conn.cursor()
        connsql = '''CREATE TABLE `mailboxmessageconfig` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mailboxSizeThresholdIntValue` int(11) DEFAULT NULL COMMENT '数据库大小阈值数字显示值',
  `mailboxSizeThresholdCompanyValue` varchar(255) DEFAULT NULL COMMENT '数据库大小阈值展示单位',
  `mailboxSizeThresholdInt` bigint(20) DEFAULT NULL COMMENT 'mailbox大小阈值',
  `mailboxNumThresholdIntValue` int(11) DEFAULT NULL COMMENT '数据库mailbox数量阈值',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
INSERT INTO `mailboxmessageconfig` VALUES ('1', '2', 'TB', '2199023255552','2000');
'''
        conncur.execute(connsql)
        histroycounts = conncur.fetchall()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return False


#查询数据库配置
def getMailboxMessageConfigHas():
    try:
        conn = dbinfo()
        conncur = conn.cursor()
        connsql = "SELECT * FROM mailboxmessageconfig"
        conncur.execute(connsql)
        histroycounts = conncur.fetchone()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return None


#查询当天获取数据库信息是否执行
def updateMailboxMessageConfigDB(id,mailboxSizeThresholdIntValue,mailboxSizeThresholdCompanyValue,mailboxSizeThresholdInt):
    try:
        conn = dbinfo()
        conncur = conn.cursor()
        connsql = "UPDATE mailboxmessageconfig SET mailboxSizeThresholdIntValue=%s , mailboxSizeThresholdCompanyValue=%s , mailboxSizeThresholdInt=%s WHERE id=%s"
        conncur.execute(connsql,(int(mailboxSizeThresholdIntValue),mailboxSizeThresholdCompanyValue,int(mailboxSizeThresholdInt),id))
        histroycounts = conncur.fetchone()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return None

#查询当天获取数据库信息是否执行
def updateMailboxMessageConfigDBMailboxNum(id,mailboxNumThresholdIntValue):
    try:
        conn = dbinfo()
        conncur = conn.cursor()
        connsql = "UPDATE mailboxmessageconfig SET mailboxNumThresholdIntValue=%s WHERE id=%s"
        conncur.execute(connsql,(int(mailboxNumThresholdIntValue),id))
        histroycounts = conncur.fetchone()
        conn.commit()
        conn.close()
        return histroycounts
    except Exception as e:
        return None

