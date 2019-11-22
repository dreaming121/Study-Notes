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