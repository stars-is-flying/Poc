'''
poc base class **Poc**,include:
1.Author name
2.CVE name(CVE-2025-7089......)
3.Vulnerability type(xss,sql-injection,remote-execute........)
4.Score(1.0-10.0)
5.Affected vertion(wordpress 1.20.1,wordpress 1.21.3.........)
6.Date(2024.6.19)
7.Reference link(https://github.com/kkkkk.........)
8.Operate system(Linux,windows,macos,android........)
9.Description
10.Interaction Method(Local exploit,Remote exploit)
11.Remote-address,Remote-port,Local-address,Local-port,username,password,url
12.Search Quary simple word(sql,injection,remote,xss,burp.........)
13.Usage(Show how to use the script)

Functions:
exploit():(use this function performe the exploit and return a result!)
check():  (use this function check the performence is successed!)
log():    (use this function print the exploit result,exploit successded use the blue failed use the blue)
'''



class Poc:
    def __init__(self):
        self.author_name = "Kuber0010"
        self.cve_name = ""
        self.vuln_type = ""
        self.score = 0
        self.affect_version = ""
        self.date = ""
        self.refer_link = ""
        self.oprate_system = ""
        self.description = ""
        self.inte_methode = ""
        self.remote_address = ""
        self.remote_port = ""
        self.local_address = ""
        self.local_port = ""
        self.url = ""
        self.quary_word = ""
        self.usage = ""
    
    
    def exploit():
        ...
    
    def check():
        ...
    
    def log():
        ...