
# coding: utf-8

# In[42]:

import random
import time

class TestBigONotation:
    itemsInArray = 0
    arraySize = None
    
    #constructor
    def __init__(self, size):
        self.arraySize = size
        self.Array = [0]* size
        
    # O(1): means the time to access something is independent of the number of items 
    #       in the collection. 
    def addItemToArray(newItem):
        self.itemsInArray += 1
        self.Array[self.itemsInArray] = newItem
    
    def generateRandomArray(self):
        for i in range(self.arraySize - 1):
            self.Array[i] = round(random.random() * 1000 + 10)
        self.itemsInArray = self.arraySize - 1
        
    # O(N): describes an algorithm whose performance will grow linearly and 
    #       in direct proportion to the size of the input data set. 
    def linearSearchForValue(self, value):
        exists = False
        indexsWithValue = 0
        
        start_time = time.clock()
        for i in range(self.arraySize - 1):
            if(self.Array[i] == value):
                exists = True
                indexsWithValue += i
        print("Value found: ", value)
        print(time.clock() - start_time, "seconds")
#O(N^2) represents an algorithm whose performance is directly proportional to the square of the size of the input data set. This is common with algorithms that involve nested iterations over the data set. 

    
test1 = TestBigONotation(1000000)
test1.generateRandomArray()
test1.linearSearchForValue(20)

test2 = TestBigONotation(2000000)
test2.generateRandomArray()
test2.linearSearchForValue(20)
        
test3 = TestBigONotation(3000000)
test3.generateRandomArray()
test3.linearSearchForValue(20)



# In[ ]:



