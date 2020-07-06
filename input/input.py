# car = {}
# car["color"] = input("What color you want: ")
# car["mark"] = input("What mark you want: ")
# car["price"] = int(input("What price you want: "))

# print(car)

table_sizes = [8, 4, 8, 10, 12, 15]
tables = []

for num in range(0, len(table_sizes)):
    table = {"number": num, "seats": table_sizes[num]}
    tables.append(table)

print(tables)

table_choosed = -1
seats_needed = int(input("How much seats you need? "))

for table in tables:
    if table["seats"] >= seats_needed:
        print(f"\nWe have a table number {table['number']} ---> {table}")
        if input("Do you want to choose this table? (Y/N): ").upper() == "Y":
            table_choosed = table["number"]
            break

if table_choosed == -1:
    print(f"You have not choose enything")
else:
    print(f"You have choose table number {table_choosed}. {tables[table_choosed]}")
