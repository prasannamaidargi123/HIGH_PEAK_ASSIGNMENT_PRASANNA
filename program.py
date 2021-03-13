with open('sample_input.txt', 'r') as file: # Reading the input file
    details = file.readlines()

details = [line for line in details if line.strip() != ""] # Removing empty lines
details1 = []

for line in details:
    details1.append(line.replace('\n', '')) # Removing \n characters

goodie_details = {}
output = {}

for i in range(len(details1)): 
    if i==0:
        emp = int(details1[i].split(':')[1]) # Taking the no. of employees
    elif i==1:
        continue
    else:
        goodie_name, goodie_price = details1[i].split(':') # Taking the goodie name and price
        goodie_details[goodie_name] = int(goodie_price)

sorted_values = sorted(goodie_details.values()) # Sorting the values of prices
sorted_goodie_details = {}

for i in sorted_values:
    for k in goodie_details.keys(): # Sorting the dictionary based on price values
        if goodie_details[k] == i:
            sorted_goodie_details[k] = goodie_details[k]
            break

values = list(sorted_goodie_details.values()) # Taking all the price values

min_index = 0
max_index = emp-1
min_price = abs(values[min_index] - values[max_index]) # Taking first minimum price

for i in range(1, len(values)-(emp-1)):
    price = abs(values[i] - values[i+emp-1])
    if price<min_price: # Updating the price
        min_price = price
        min_index = i
        max_index = i+emp-1

keys = list(sorted_goodie_details.keys()) # Taking all the keys

for i in range(min_index, max_index+1): 
    k = keys[i]
    output[k] = sorted_goodie_details[k] # Taking the goodie names and prices which are giving minimum price

with open('sample_output.txt', 'w') as file: # Writing in the output file
    file.write('The goodies selected for distribution are:\n\n')
    for i in output:
        file.write(i+": "+str(output[i])+"\n")
    file.write('And the difference between the chosen goodie with highest price and the lowest price is '+str(min_price))