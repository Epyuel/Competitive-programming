class MyCalendar:

    def __init__(self):
        self.calander=[]
        

    def book(self, start: int, end: int) -> bool:
        if len(self.calander)==0:
            self.calander.append([start,end])
            return True
        self.calander=sorted(self.calander,key= lambda x:x[0])

        l_pointer,r_pointer,mid=0,len(self.calander)-1,0
        while l_pointer <= r_pointer:
            mid=(l_pointer+r_pointer)//2
            if self.calander[mid][0] < start:
                l_pointer= mid+1
            else:
                r_pointer= mid-1
        if l_pointer > mid:
            if len(self.calander)-1==mid and self.calander[mid][1] <= start:
                self.calander.append([start,end])
                return True
            if self.calander[mid][1] <= start and self.calander[l_pointer][0]>=end:
                self.calander.append([start,end])
                return True
            else:
                return False
        elif r_pointer < mid:
            if mid==0 and self.calander[mid][0] >= end:
                self.calander.append([start,end])
                return True
            if self.calander[r_pointer][1]<=start and self.calander[mid][0]>=end:
                self.calander.append([start,end])
                return True
            else:
                return False
        





# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
