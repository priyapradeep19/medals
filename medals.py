

COUNTRIES = 7
MEDALS = 4

total = 0
gold = 0
silver = 0
bronze = 0


medal_counts = [
    ["Canada", 0, 3, 0],
    ["Italy", 0, 0, 1],
    ["Germany", 0, 0, 1],
    ["Japan", 1, 0, 0],
    ["Russia", 3, 1, 1],
    ["South Korea", 0, 1, 0],
    ["United States", 1, 0, 1]
]

print("%-20s %-20s %-20s %-20s" % ("", "Gold", "Silver", "Bronze"))
for i in range(COUNTRIES):
    for j in range(MEDALS):
        print("%-22s" % medal_counts[i][j], end='')
    print()
print()

for i in range(COUNTRIES):
    for j in range(1, MEDALS):
        total = total + medal_counts[i][j]
print("Total medals:", total)

for i in range(COUNTRIES):
    gold = gold + medal_counts[i][1]
print("Total gold medals:", gold)

for i in range(COUNTRIES):
    silver = silver + medal_counts[i][2]
print("Total silver medals:", silver)

for i in range(COUNTRIES):
    bronze = bronze + medal_counts[i][3]
print("Total bronze medals:", bronze)

newTable = list(medal_counts)
flag = True
i = 0
while flag:
    if newTable[i][1] == 0:
        newTable.remove(newTable[i])
    else:
        if i < len(newTable) - 1:
            i = i + 1
        else:
            flag = False

print("Countries without gold medal:\n")
print("%-20s %-20s %-20s %-20s" % ("", "Gold", "Silver", "Bronze"))
for i in range(len(newTable)):
    for j in range(MEDALS):
        print("%-22s" % newTable[i][j], end='')
    print()
print()


data = {"Canada": ["Gold", 0, "Silver", 3, "Bronze" , 0],
                  "Italy": ["Gold" , 0, "Silver", 0, "Bronze", 1],
                  "Germany": ["Gold" , 0, "Silver", 0, "Bronze", 1],
                  "Japan": ["Gold" , 1, "Silver", 0, "Bronze", 0],
                  "Russia": ["Gold" , 3, "Silver", 1, "Bronze", 1],
                  "South Korea": ["Gold" , 0, "Silver", 1, "Bronze", 0],
                  "United States": ["Gold" , 1, "Silver", 0, "Bronze", 1],
                  }
print (data)
