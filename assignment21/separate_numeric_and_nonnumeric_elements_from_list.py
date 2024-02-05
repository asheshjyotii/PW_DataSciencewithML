list1 = ['apple',123,'orange',12,'banana']
numbers  = [i for i in list1 if isinstance(i,(int,float))]
words = [i for i in list1 if isinstance(i,str)]
print(f"The numeric are: {numbers}")
print(f"The words are are: {words}")