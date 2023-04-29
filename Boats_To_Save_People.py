class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        sorted_people=sorted(people)
        boats=0
        i=0
        j=len(people)-1
        while True:
            if i==j :
                boats+=1
                break
            elif i>j:
                break
            if (sorted_people[i]+sorted_people[j])>limit:
                j-=1
                boats+=1
            else:
                i+=1
                j-=1
                boats+=1
        return boats
