#Returns the most common element in a list
def mostCommon(lst):
    # IMPLEMENT HERE
    return
​
#Used to calculate m[0]
def flaw1(file):
    with open(file, "r") as f:
        arr = []
        for line in f:
            entry = line.strip().split(' ')       # Entry      = ['0X01FF00', '0XDB']
            arr.append() # IMPLEMENT HERE
​
        return mostCommon(arr)        
​
​
#Used to calculate k[0]
def flaw2(file, m):
    with open(file, "r") as f:
        arr = []
        for line in f:
            entry = line.strip().split(' ')       # Entry      = ['0X01FF00', '0XDB']
            arr.append() # IMPLEMENT HERE
​
        return mostCommon(arr)
​
#Used to calculate k[1], k[2], ... k[12]
def flaw3(file, m, k, n):
    with open(file, "r") as f:
        arr = []
        for line in f:
            entry = line.strip().split(' ')       # Entry      = ['0X01FF00', '0XDB']
            arr.append()  # IMPLEMENT HERE
​
        return mostCommon(arr)
    
​
def main():
    # IMPLEMENT HERE
    return
​
if __name__ == '__main__':
    main()
