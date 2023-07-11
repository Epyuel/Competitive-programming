class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l_pointer=count=max_fruits=0
        dic=collections.defaultdict(int)
        for r_pointer in range(len(fruits)):
            count+=1
            dic[fruits[r_pointer]]+=1

            while len(dic)>2:
                count-=1
                dic[fruits[l_pointer]]-=1
                if dic[fruits[l_pointer]]==0:
                    dic.pop(fruits[l_pointer])
                l_pointer+=1
            max_fruits=max(max_fruits,count) 
        return max_fruits       
