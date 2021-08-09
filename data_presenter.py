cupcakes = open('CupcakeInvoices.csv')

# for line in cupcakes:
#     print(line)

total_chocolate = 0
total_vanilla = 0
total_strawberry = 0

for types in cupcakes:

    if "Chocolate" in types:
        total_chocolate += 1
    elif "Vanilla" in types:
        total_vanilla += 1
    elif "Strawberry" in types:
        total_strawberry += 1

# print(total_chocolate)
# print(total_vanilla)
# print(total_strawberry)

for invoice in cupcakes:
    
    value = invoice.split(',')

    person_total = int(value[3]) * float(value[4])

    print(person_total)
# next part 
grand_total = []

for invoice in cupcakes:

  value = invoice.split(',')

  person_total = int(value[3]) * float(value[4])

  grand_total.append(person_total)

  # print(person_total)
  # print(grand_total)

  print (sum(grand_total))

  cupcakes.close()