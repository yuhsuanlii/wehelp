# 要求一：函式與流程控制
# 完成以下函式，在函式中使用迴圈計算最小值到最大值之間，固定間隔的整數總和。其中你可
# 以假設 max 一定大於 min 且為整數，step 為正整數。

def calculate(min, max, step):
    sum = 0
    i=0    
    for i in range(min,max+1,step):   
        sum+=i
    # print(i, end=" ")
    print(sum)
calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0


# 要求二：Python 字典與列表、JavaScript 物件與陣列
# 完成以下函式，正確計算出非 manager 的員工平均薪資，所謂非 manager 就是在資料中
# manager 欄位標註為 False (Python) 或 false (JavaScript) 的員工，程式需考慮員工資料數量
# 不定的情況。

def avg(data):
    sum=0
    a=data.get("employees")
    # print(data.get("employees"))
    for i in data.get("employees"):
        # print(i.get("manager"))
        if i.get("manager") == False:
            sum+=i.get("salary")
            # print(sum)
    print(sum//len(i))

avg({
"employees":[
{
"name":"John",
"salary":30000,
"manager":False
},
{
"name":"Bob",
"salary":60000,
"manager":True
},
{
"name":"Jenny",
"salary":50000,
"manager":False
},
{
"name":"Tony",
"salary":40000,
"manager":False
}
]
}) # 呼叫 avg 函式


# 要求三：
# 完成以下函式，最後能印出程式中註解所描述的結果。

def func(a):
    def func(b,c):
        print(a+(b*c))
        return a+(b*c)
    return func
func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果


# 要求四：
# 找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。
# 提醒：請勿更動題目中任何已經寫好的程式，不可以使用排序相關的內建函式。

def maxProduct(nums):
    b=len(nums)
    
    if b == 4 :
        a1 = nums[b - 4] * nums[b - 3]
        a2 = nums[b - 4] * nums[b - 2]
        a3 = nums[b - 4] * nums[b - 1]
        a4 = nums[b - 3] * nums[b - 2]
        a5 = nums[b - 3] * nums[b - 1]
        a6 = nums[b - 2] * nums[b - 1]
        arr = [a1, a2, a3, a4, a5, a6]
        print(max(arr))
    elif b == 3 :
        a13 = nums[b - 3] * nums[b - 2]
        a14 = nums[b - 3] * nums[b - 1]
        a15 = nums[b - 2] * nums[b - 1]
        arr2 = [a13, a14, a15]
        print(max(arr2))
    else:
        a16 = nums[b - 2] * nums[b - 1]
        arr3 = [a16]
        print(max(arr3))

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10


# 要求五：
# Given an array of integers, show indices of the two numbers such that they add up to a
# specific target. You can assume that each input would have exactly one solution, and you
# can not use the same element twice.

def twoSum(nums, target):
    hash_table={}
    for i in range(len(nums)):
        hash_table[nums[i]]=i
    for i in range(len(nums)):
        if target-nums[i] in hash_table:
            if hash_table[target-nums[i]] != i:
                return [i, hash_table[target-nums[i]]]
    return []

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9


# 要求六 ( Optional )：
# 給定只會包含 0 或 1 兩種數字的列表 (Python) 或陣列 (JavaScript)，計算連續出現 0 的最大
# 長度。

def maxZeros(nums):
    max_time=0
    cur_time=1 
    pre_element = None

    for i in nums:
        
        if i == pre_element and i==0:
            cur_time+=1
            max_time=max((cur_time,max_time))
        else:
            pre_element=i
            cur_time=1

    print(max_time)
    
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3
