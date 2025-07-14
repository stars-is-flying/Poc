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
check():  (use this function check the performence is successed!, use this function print the exploit result,exploit successded use the blue failed use the blue)
'''

from colorama import init, Fore, Style, Back

init(autoreset=True)

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
        self.username = ""
        self.password = ""
        self.url = ""
        self.quary_word = ""
    
    
    def exploit(self):
        ...
    
    def check(self):
        code, message = self.exploit()
    
        # 定义漂亮的输出格式
        border = "═" * 70
        header = "╔" + border + "╗"
        footer = "╚" + border + "╝"
    
        # 根据结果代码选择不同颜色
        if code == 0:  # 成功 - 蓝色
            color = Fore.BLUE + Style.BRIGHT
            status = "漏洞利用成功!"
            icon = "✔"
        elif code == 1:  # 未成功 - 黄色
            color = Fore.YELLOW + Style.BRIGHT
            status = "执行完成但未成功"
            icon = "⚠"
        else:  # 错误 - 红色
            color = Fore.RED + Style.BRIGHT
            status = "执行失败"
            icon = "✘"
    
        # 构建输出内容
        output = f"""
        {color}{header}
        {color}║{icon}  {status.center(68)} ║
        {color}║{'详细信息:'.center(70)}║
        {color}║{message.center(70)}║
        {color}{footer}
            """
    
        print(output)
    
        # 额外添加彩色状态标签
        status_tag = {
            0: Back.BLUE + Fore.WHITE + " SUCCESS ",
            1: Back.YELLOW + Fore.BLACK + " WARNING ",
            -1: Back.RED + Fore.WHITE + " ERROR "
        }[code]
    
        print(f"\n{status_tag}{Style.RESET_ALL} 状态代码: {code}")
    
        # 返回结果代码
        return code
    