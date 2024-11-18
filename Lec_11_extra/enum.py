# use of enumerate function 
# https://www.freecodecamp.org/news/python-for-loop-example-and-tutorial/
'''So far we have not used any indexes when iterating. Sometimes, we need to access the index of the item we're looping through and display it.
We can loop over items with the index using enumerate().'''

groceries = ["bananas","butter","cheese","toothpaste"]
for index, grocery in enumerate(groceries):
    print(f"{grocery} is at index: {index}.")