import plotly.graph_objects as go


cupcakes = open('CupcakeInvoices.csv')

# # for line in cupcakes:
# #     print(line)

# total_chocolate = 0
# total_vanilla = 0
# total_strawberry = 0

# for types in cupcakes:

#     if "Chocolate" in types:
#         total_chocolate += 1
#     elif "Vanilla" in types:
#         total_vanilla += 1
#     elif "Strawberry" in types:
#         total_strawberry += 1

# # print(total_chocolate)
# # print(total_vanilla)
# # print(total_strawberry)

# for invoice in cupcakes:
    
#     value = invoice.split(',')

#     person_total = int(value[3]) * float(value[4])

#     print(person_total)
# next part 

chocolate = 0
strawberry = 0
vanilla = 0

for line in cupcakes:
    line = line.split(',')
    if line[2] == 'Chocolate':
        chocolate += int(line[3]) * float(line[4])
    elif line[2] == 'Strawberry':
        strawberry += int(line[3]) * float(line[4])
    elif line[2] == 'Vanilla':
        vanilla += int(line[3]) * float(line[4])

grand_total = chocolate + strawberry + vanilla
print(round(grand_total, 2))
print(chocolate + strawberry + vanilla)

fig = go.Figure(data=go.Bar(y=[chocolate,vanilla,strawberry],x=["Chocolate", "Vanilla", "Strawberry"]))

fig.show()

