from rodents import Rodent

rodents = {}

file = open("measures.csv")

for line in file:
    line = line.rstrip()
    line = line
    tag_id, weight = line.split(',')
    if tag_id in rodents:
        rodents[tag_id].add_weigth(weight)
    else:
        rodents[tag_id] = Rodent(tag_id)
        rodents[tag_id].add_weigth(weight)
    
file.close()

print rodents
for key in rodents:
    print rodents[key].tag_id, rodents[key].weights
