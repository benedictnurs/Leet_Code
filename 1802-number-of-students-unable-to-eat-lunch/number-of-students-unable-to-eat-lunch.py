class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        flag = 0
        while flag < len(sandwiches):
            if not students:
                return True
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                flag = 0
            else:
                students.append(students.pop(0))
                flag += 1
        return len(sandwiches)