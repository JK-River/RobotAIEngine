# QueryAnalysis #

当前业界文本语义信息抽取基本是使用正则表达式来完成的，正则表达式本身并不提供管理与测试功能。  
在进行基于正则的文本语义抽取的时候，还需要做大量的基础工作，来便于编写、管理和测试正则表达式。  
本项目提供大量底层与框架支持，便于使用者方便的编写，管理与测试大批量的正则表达式，以支持高效稳定的语义抽取服务。  

## 本项目由3块组成 ##
* 1.词典（用于组织需要被正则模板使用的底层词库）  
* 2.正则语义模板（根据不同业务编写的一组正则表达式）  
* 3.框架与lib包（用于加载正则表达式完成对输入文本的语义抽取）  

## 1.词典模块 ##
词典模块位于dict目录  
对于需要公共使用的词典放到common目录里，其它各语义需要使用的词典放到各自的目录中  
词典模块中的词典文件使用csv文件格式  
词典内容支持多列形式，支持对词典中每个词添加一个或多个属性（词典中用,分隔）  
对于写成的词典需要在/dict/dict.py中加载上来，供正则模板使用  
方法如下：  
方法一：加载不带属性  
stop_words = WordsDict(  
    './dict/common/stop_words.csv')  

方法二：加载带属性的字典（字典中用逗号分隔的）  
animal_name = WordsDict(  
    './dict/animal/animal.csv',  
    property_name_list=['arid'],  
    group_name='animal')  
property_name_list参数，指定逗号分隔，依次第n个参数返回时的字段名  
group_name参数，指定被命中的信息，在字典中返回的key名  
如：我要看老虎，这句老虎在字典中定义如下：  
老虎,1  
被正则命中后取得的返回结果中就会包含如下信息：  
{'arid': '1', 'animal': '老虎'}  

## 2.正则语义模板 ##
正则语义模板位于/nlu目录  
media目录是指用于需播放的信息，如相声，戏曲，动画，故事等，这类播放结构较为类似，故放在同一目录下
使用/nlu/media/common提取公共部分，在各模块内部只完成各自不同的信息即可。  
smart目录下是指智能硬件的模块。  

在/nlu目录下的其它模块，每个模块均代表1种语义  
每个正则语义模块下有2个需要添加的内容：  
1.service属性，这个属性指明这个类是代表什么语义的，在输入文本命中本类中包含的正则语义后，  
返回的信息里会包含这个service属性。  
2.nlu.rule.Rule对象，这个对象中包含的正则表达式信息，框架会用来对输入文本进行匹配。  

## 3.框架与lib包 ##
当包含有正则表达式的语义类完成之后，需要把这个类注册到框架中去，方法如下：  
import nlu.animal as animal  
from nlu.nlu_framework import Nlu_Framework  
Nlu_Framework.register(animal.Animal)  
这样框架就可以用Animal类里的Rule对象所指定的正则变量来处理输入文本了  

使用框架匹配正则模块如下：  
match_dict_list = Nlu_Framework.match('我想看老虎')  
print  match_dict_list[0].items()  
输出如下：  
[('operation', 'query'), ('service', 'animal'),  
('parameters', {'arid': '1', 'rule': '5', 'animal': '\xe8\x80\x81\xe8\x99\x8e'})]  

lib包里提供了一些在完成正则语义编写非常常用的函数  
attach_name函数：对指定正则附加一个名字属性，当命中这个正则时会返回这个属性  
attach_perperty函数：对指定的正则表达式附加一个属性，当命中此正则时返回这个属性  
e函数：表示正则里的可出现也可不出现（({})?）  
o函数：表示正则里的或条件（({a|b})）  
r函数：表示正则里的重复  

#Docker支持#
本项目支持在docker容器中运行  
方法1(自制镜象)：  
* 1.进入本目录  
* 2.docker build -t query_analysis .  
* 3.docker run --rm --name query_analysis --net=host hub.c.163.com/yufeiok/query_analysis  

方法2(直接下载镜象)：  
* 1.docker pull hub.c.163.com/yufeiok/query_analysis:latest  
* 2.docker run --rm --name query_analysis --net=host hub.c.163.com/yufeiok/query_analysis  
* 3.curl '127.0.0.1:8700/interpreter/info?speech=%E6%88%91%E8%A6%81%E7%9C%8B%E8%80%81%E8%99%8E&robot_code=0'（测试）  

这就可以直接在本机的8700端口进行测试了，返回结果如下：  
curl '127.0.0.1:8700/interpreter/info?speech=%E6%88%91%E8%A6%81%E7%9C%8B%E8%80%81%E8%99%8E&robot_code=0' (发送文本：我要看老虎)  

返回结果：  
{"msg": "OK", "body": {"operation": "query", "service": "animal", "parameters": {"arid": "1", "rule": "5", "animal":   "\u8001\u864e"}}, "code": 0}  

#使用方法#
* 1.编写用于提取语义的类，如下所示：
> usage.py
> class Test(object):
>     # 标识是test领域(这个service字段必须存在，命中本类中正则时，会输出这个字段)
>     service = 'test'
> 
>     # 表示抓取2个字长度的信息,输出字段为name
>     name = range_tag(2, 'user_name')
> 
>     # 正则规则：我的名字是小明
>     name_case1 = '我的名字是' + name
> 
>     # 生成规则对象（附加的参数会在输出结果中被输出，operation代表具体的操作）
>     rule_case1 = Rule(attach_perperty(name_case1, {'operation': 'query', 'rule': 1}))

* 2.把本类注册到NLU框架中  
> from nlu.nlu_framework import Nlu_Framework  
> Nlu_Framework.register(Test)  

* 3.使用规则来处理输入文本  
> match_dict_list = Nlu_Framework.match('我的名字是小明')  
> for k, v in match_dict_list[0].items():  
>    print '{} : {}'.format(k, v)  

输出结果如下：  
> operation : query  
> service : test  
> parameters : {'user_name': '\xe5\xb0\x8f\xe6\x98\x8e', 'rule': '1'}  
