# Python

[toc]

## Python 特点

* Python 是**完全面向对象的语言**
  * **函数**、**模块**、**数字**、**字符串**都是对象，**在 Python 中一切皆对象**
  * 完全支持继承、重载、多重继承
  * 支持重载运算符，也支持泛型设计
* Python **拥有一个强大的标准库**，Python 语言的核心只包含 **数字**、**字符串**、**列表**、**字典**、**文件** 等常见类型和函数，而由 Python 标准库提供了 **系统管理**、**网络通信**、**文本处理**、**数据库接口**、**图形系统**、**XML 处理** 等额外的功能
* Python 社区提供了**大量的第三方模块**，使用方式与标准库类似。它们的功能覆盖 **科学计算**、**人工智能**、**机器学习**、**Web 开发**、**数据库接口**、**图形系统** 多个领域

### 面向对象的思维方式

* **面向对象** 是一种 **思维方式**，也是一门 **程序设计技术**
* 要解决一个问题前，首先考虑 **由谁** 来做，怎么做事情是 **谁** 的职责，最后把事情做好就行！
  * **对象** 就是 **谁**
* 要解决复杂的问题，就可以找**多个不同的对象**，**各司其职**，共同实现，最终完成需求

## 开发环境

* 执行 `Python` 程序的三种方式
  * 解释器 —— `python` / `python3`
  * 交互式 —— `ipython`
  * 集成开发环境 —— `PyCharm`

## Python 的语法特点

- Python对语法格式要求极其严格
  - 每行只能写一行语句
  - 对缩进敏感，通过缩进显示嵌套

## 演练中的常见错误

* 1> **手误**，例如使用 `pirnt("Hello world")` 

```
NameError: name 'pirnt' is not defined

名称错误：'pirnt' 名字没有定义
```

* 2> 将多条 `print` 写在一行

```
SyntaxError: invalid syntax

语法错误：语法无效
```

> 每行代码负责完成一个动作

* 3> 缩进错误

```
IndentationError: unexpected indent

缩进错误：不期望出现的缩进
```

> * Python 是一个格式非常严格的程序设计语言
> * 目前而言，大家记住每行代码前面都不要增加空格

* 4> **python 2.x 默认不支持中文** 

目前市场上有两个 Python 的版本并存着，分别是 `Python 2.x` 和 `Python 3.x`

* **Python 2.x 默认不支持中文**，具体原因，等到介绍 **字符编码** 时给大家讲解
* Python 2.x 的解释器名称是 **python**
* Python 3.x 的解释器名称是 **python3**

```
SyntaxError: Non-ASCII character '\xe4' in file 01-HelloPython.py on line 3, 
but no encoding declared; 
see http://python.org/dev/peps/pep-0263/ for details

语法错误： 在 01-HelloPython.py 中第 3 行出现了非 ASCII 字符 '\xe4'，但是没有声明文件编码
请访问 http://python.org/dev/peps/pep-0263/ 了解详细信息
```

> * `ASCII` 字符只包含 `256` 个字符，不支持中文
> * 有关字符编码的问题，后续会讲

### 单词列表

```
* error 错误
* name 名字
* defined 已经定义
* syntax 语法
* invalid 无效
* Indentation 索引
* unexpected 意外的，不期望的
* character 字符
* line 行
* encoding 编码
* declared 声明
* details 细节，详细信息
* ASCII 一种字符编码
```

## `Python 2.x` 与 `3​​.x` 版本简介

目前市场上有两个 Python 的版本并存着，分别是 `Python 2.x` 和 `Python 3.x`

> 新的 Python 程序建议使用 `Python 3.0` 版本的语法

* Python 2.x 是 **过去的版本**
  * 解释器名称是 **python**
* Python 3.x 是 **现在和未来 主流的版本**
  * 解释器名称是 **python3**
  * 相对于 `Python` 的早期版本，这是一个 **较大的升级**
  * 为了不带入过多的累赘，`Python 3.0` 在设计的时候 **没有考虑向下兼容**
    * 许多早期 `Python` 版本设计的程序都无法在 `Python 3.0` 上正常执行
  * Python 3.0 发布于 **2008 年**
  * 到目前为止，Python 3.0 的稳定版本已经有很多年了
    * Python 3.3 发布于 2012
    * Python 3.4 发布于 2014
    * Python 3.5 发布于 2015
    * Python 3.6 发布于 2016
* 为了照顾现有的程序，官方提供了一个过渡版本 —— **Python 2.6**
  * 基本使用了 `Python 2.x` 的语法和库
  * 同时考虑了向 `Python 3.0` 的迁移，**允许使用部分** `Python 3.0` 的语法与函数
  * 2010 年中推出的 `Python 2.7` 被确定为 **最后一个Python 2.x 版本**

> 提示：如果开发时，无法立即使用 Python 3.0（还有极少的第三方库不支持 3.0 的语法），建议
>
> * 先使用 `Python 3.0` 版本进行开发
> * 然后使用 `Python 2.6`、`Python 2.7` 来执行，并且做一些兼容性的处理