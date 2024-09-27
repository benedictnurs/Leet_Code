class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        sol = []
        hm = {}

        seen = set()
        seen2 = set()

        for order in orders:
            seen.add(order[2])
        
        for order in orders:
            if order[1] not in hm:
                hm[order[1]] = [order[2]]
            else:
                hm[order[1]].append(order[2])

        rows = []
        row1 = ["Table"] + sorted(seen)
        rows.append(row1)
        row2 = dict(sorted(hm.items(), key=lambda item: int(item[0])))
        for row in row2.items():
            foodItems = []
            for item in range(1, len(row1)):
                foodItems.append(str(row[1].count(row1[item])))
            tableRow = [row[0]] + foodItems
            rows.append(tableRow)
        
        return (rows)