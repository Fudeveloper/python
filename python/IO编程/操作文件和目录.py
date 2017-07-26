#-*-coding:utf-8-*-
import os
#操作系统名称，nt即为windows
print os.name       #nt

#操作系统中的系统变量
print os.environ
'''
{'TMP': 'C:\\Users\\Administrator\\AppData\\Local\\Temp', 'PYTHONIOENCODING': 'UTF-8', 'COMPUTERNAME': 'LIK', 'USERDOMAIN': 'LIK', 'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\windows\\system32\\WindowsPowerShell\\v1.0\\Modules', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 42 Stepping 7, GenuineIntel', 'PROGRAMFILES': 'C:\\Program Files', 'PROCESSOR_REVISION': '2a07', 'SYSTEMROOT': 'C:\\windows', 'PATH': 'C:\\ProgramData\\Oracle\\Java\\javapath;C:\\windows\\system32;C:\\windows;C:\\windows\\System32\\Wbem;C:\\windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files (x86)\\MacType;C:\\Program Files (x86)\\GtkSharp\\2.12\\bin;C:\\Program Files\\Microsoft SQL Server\\130\\Tools\\Binn\\;F:\\Git\\cmd;C:\\Users\\Administrator\\AppData\\Local\\Microsoft\\WindowsApps;E:\\python;', 'PYTHONUNBUFFERED': '1', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'COMSPEC': 'C:\\windows\\system32\\cmd.exe', 'TEMP': 'C:\\Users\\Administrator\\AppData\\Local\\Temp', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'ALLUSERSPROFILE': 'C:\\ProgramData', 'USERPROFILE': 'C:\\Users\\Administrator', 'LOCALAPPDATA': 'C:\\Users\\Administrator\\AppData\\Local', 'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 'HOMEPATH': '\\Users\\Administrator', 'USERDOMAIN_ROAMINGPROFILE': 'LIK', 'PROGRAMW6432': 'C:\\Program Files', 'USERNAME': 'Administrator', 'LOGONSERVER': '\\\\LIK', 'SESSIONNAME': 'Console', 'PROGRAMDATA': 'C:\\ProgramData', 'PYTHONPATH': 'F:\\learngit\\python', 'MEMUHYPERV_PATH': 'E:\\moniqi\\Microvirt\\MEmuHyperv', 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'WINDIR': 'C:\\windows', 'APPDATA': 'C:\\Users\\Administrator\\AppData\\Roaming', 'HOMEDRIVE': 'C:', 'GTK_BASEPATH': 'C:\\Program Files (x86)\\GtkSharp\\2.12\\', 'SYSTEMDRIVE': 'C:', 'PYCHARM_HOSTED': '1', 'NUMBER_OF_PROCESSORS': '4', 'PROCESSOR_LEVEL': '6', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'OS': 'Windows_NT', 'PUBLIC': 'C:\\Users\\Public', 'MEMU_PATH': 'E:\\moniqi\\Microvirt'}
'''

#要获取某个环境变量的值，可以调用os.getenv()函数：
print os.getenv('PYTHONIOENCODING')     #UTF-8

#查看当前绝对路径
print os.path.abspath('.')      #F:\learngit\python\python\IO���

#在这个目录下创建一个新目录：

#首先明确新目录的绝对路径：
newpath=os.path.join(os.path.abspath('.'),'testdir')

#创建目录
os.mkdir(newpath)
#删除目录
os.rmdir(newpath)

'''
把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串：

part-1/part-2
而Windows下会返回这样的字符串：

part-1\part-2
'''

#os.path.splitext()可以直接让你得到文件扩展名
print os.path.splitext('GBK.txt')       #('GBK', '.txt')

#列出当前目录下的所有文件，只需要一行代码：
print [x for x in os.listdir('.') if os.path.isfile(x)]    #['GBK.txt', 'test.txt', '\xb2\xd9\xd7\xf7\xce\xc4\xbc\xfe\xba\xcd\xc4\xbf\xc2\xbc.py', '\xce\xc4\xbc\xfe\xb6\xc1\xd0\xb4.py']

#列出所有.py文件：
print list(x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py')
#['\xb2\xd9\xd7\xf7\xce\xc4\xbc\xfe\xba\xcd\xc4\xbf\xc2\xbc.py', '\xce\xc4\xbc\xfe\xb6\xc1\xd0\xb4.py']