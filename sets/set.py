s = {10, 20, 30}

s.add(4)
print(s)
s.update([5,6,7]) #Add multiple items
print(s)
s.remove(20)#⚠️ If item does NOT exist → Error
print(s)
s.discard(67) # it doesnt show error when item doesnt exist
print(s)
s.pop() #Removes a random item (because set is unordered).
print(s)
s.clear() #Removes everything
print(s)