class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = {}
        for files in paths:
            cont = files.split()
            n = len(cont)
            if n <= 1:
                continue
            
            for i in range(1, n):
                file_, content = cont[i].split("(")
                if content not in dic:
                    dic[content] = []

                full_path = cont[0]+"/"+file_
                dic[content].append(full_path)
        res = []
        for files in dic.values():
            if len(files) > 1:
                res.append(files)
                
        return res
