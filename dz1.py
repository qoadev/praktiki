#exercise 1
def make_tshirt(size,text):
    s = size+" "+ text
    return s
print(make_tshirt('L',"Python"))

#exercise 2
def make_tshirt2(size="L",text="I love python"):
    s = size+" "+ text
    return s
print(make_tshirt2())
print(make_tshirt2(size="XS",text="python"))
    
