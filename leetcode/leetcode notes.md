#pyhon笔记  
+ **list合并操作中extend是将两数组内容合并在一起，而append是将第二个数组当作整体放入数组1尾部**  

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
+ **多维数组排序，使用lambda x:x[i]**

例:
<pre>
array = [ ['b', 4], ['e', 2], ['a', 5], ['d', 1], ['c', 3] ]
array.sort(key=lambda x:x[1])
结果：
[ ['d', 1], ['e', 2], ['c', 3], ['b', 4], ['a', 5] ]
</pre>

##爬楼梯问题
###爬楼梯问题实际上属于斐波那契数组问题
**题目：  
You are climbing a stair case. It takes n steps to reach to the top.  
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?**  

这道题自顶向下的思考：如果要爬到n台阶，有两种可能性:

+ 在n-1的台阶处爬一层台阶  
+ 在n-2的台阶处爬两层台阶

所以实际结果就是前两项结果相加可以得到第三项。

除此之外，通常对于这种问题的最基本解法为列举，
内容如同下文：
![5](images\images70_Climbing_Stairs_rt.jpg)//
尝试

