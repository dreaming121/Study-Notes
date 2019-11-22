#pyhon笔记  
###**list合并操作中extend是将两数组内容合并在一起，而append是将第二个数组当作整体放入数组1尾部**  

例:  
 <pre>
a=[1,2,3]  
b=[4,5,6]  
print(a.append(b))  
print(a.extend(b))
#结果：
[1,2,3,[4,5,6]]
[1,2,3,4,5,6]
</pre>
###**多维数组排序，使用lambda x:x[i]**

例:
<pre>
array = [ ['b', 4], ['e', 2], ['a', 5], ['d', 1], ['c', 3] ]
array.sort(key=lambda x:x[1])
结果：
[ ['d', 1], ['e', 2], ['c', 3], ['b', 4], ['a', 5] ]
</pre>

###**pyhton中值互换更简单**
例：  
<pre>
class Solution(object):
    def climbStairs(self, n):
        a = 0
        b = 1
        for i in range(n):
            a,b = b,a+b       #在python中可以这么写
        return b
</pre>
注：在python中可以按照`a,b = b,a+b`来写，但是别的语言需要使用一个中间值temp来暂存a的值，然后再进行`b = temp+b`操作。

###**条件语句要注意的细节**
+ 在条件语句中，如果有多重条件要注意条件的先后
+ 在条件语句中，也要注意条件判断的前提是否成立

例：
<pre>
if (qlist[0] == None and plist[0] == None) or qlist[0].val == plist[0].val:
    return True
</pre>
在此语句中要注意:

1. 首先，两个语句的顺序不能调整，因为如果先做之判断，会产生None没有值的情况，从而无法进行，所以要先把None的情况判断完。
2. 此情况还有另外一种情况是`qlist`和`plist`有一个为None，会跳过前一个判断而进入第二个判断，仍然会导致None没有值的问题。 


###用等号可以简单完成判断
例：
<pre>
if L == R: 
    return True
else:
    return False
</pre>

可以直接写成：
<pre>
return L == R
</pre>
如果成立则返回True，不成立则返回False。