from collections import defaultdict
from typing import List

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        # Initialize the data structures
        table_orders = defaultdict(lambda: defaultdict(int))  # table -> {food item -> count}
        food_items = set()  # To collect all unique food items
        
        # Process each order
        for customer, table, food in orders:
            table_orders[table][food] += 1  # Count the food ordered at each table
            food_items.add(food)  # Add the food item to the set of seen items
        
        # Sort the food items (for columns)
        sorted_food_items = sorted(food_items)
        
        # Prepare the header row (first row)
        result = [["Table"] + sorted_food_items]
        
        # Sort the tables numerically and construct each table row
        for table in sorted(table_orders.keys(), key=int):
            row = [table]  # The first element in the row is the table number
            for food in sorted_food_items:
                # Append the count of each food item ordered at this table (default to 0 if not found)
                row.append(str(table_orders[table][food]))
            result.append(row)
        
        return result
