### 前言
通过xlrd读取xlsx文件中的测试数据，在测试脚本通过ddt调用数据脚本中的数据
  
##### 分析  
1. 目录结构  
--DDT  
&nbsp;&nbsp;|--DDT.py  
&nbsp;&nbsp;|--baseinfo   
&nbsp;&nbsp;&nbsp;&nbsp;|--test.py   
&nbsp;&nbsp;&nbsp;&nbsp;|--__init__.py   
  
2. 功能剖析  
通过调用ddt来执行baseinfo文件夹下的测试数据

##### 代码实现  
1. 读取测试数据  
&nbsp;&nbsp;+ 在baseinfo文件夹下创建__init__.py  
&nbsp;&nbsp;+ 在__init__.py导入xlrd模块  
&nbsp;&nbsp;+ 创建测试数据test.xlsx  
&nbsp;&nbsp;+ 编写代码，详细内容请自行下载__init__.py  
  
2. ddt驱动数据  
&nbsp;&nbsp;+ 创建DDT.py  
&nbsp;&nbsp;+ 导入模块unittest/ddt/baseinfo  
&nbsp;&nbsp;+ 测试类前加修饰@ddt.ddt  
&nbsp;&nbsp;+ case前加修饰@ddt.data()  
&nbsp;&nbsp;+ 编写代码，详细内容请自行下载DDT.py  

---
注意，在第1步调用测试数据时，路径应该以DDT.py所在的目录为起点，  
因为是__init__.py是在DDT.py中执行的
