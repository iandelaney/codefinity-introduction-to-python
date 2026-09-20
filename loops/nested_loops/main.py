produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

groceries = [produce, dairy]


for section in groceries:      # section is first the produce list, then the dairy list
    for item in section:       # item is each string inside that sub-list
        print("Item name:", item)
