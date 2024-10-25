class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        sol = []
        for f in folder:
            if not sol or not f.startswith(sol[-1] + '/'):
                sol.append(f)
        
        return (sol)