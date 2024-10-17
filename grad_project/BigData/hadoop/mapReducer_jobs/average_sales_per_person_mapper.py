import sys
import json


print("Salesperson_ID\tSales")

for line in sys.stdin:
    try:
        record = json.loads(line)
        salesperson_id = record['salesperson_id']
        total_sales = record['totalsales']
        print(f"{salesperson_id}\t{total_sales}")
    except:
        continue
