#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

# Function to perform mathematical operation on X and Y
def do_operation(X, Y):
    add=X+Y
    print(add)
    sub=X-Y
    print(sub)
    mul=X*Y
    print(mul)
    div=X/Y
    print(div)
    rasd=X**Y
    print(rasd)
    floor=X//Y
    print(floor)# Your code here

#{ 
#Driver Code Starts.

# Python Code to perform mathematical operation
def main():
    testcase = int(input())
    
    while(testcase > 0):
        input1 = input().split()
        X = int(input1[0])
        Y = int(input1[1])
        do_operation(X, Y)
        
        testcase -= 1
        

if __name__ == '__main__':
    main()
    
#} Driver Code Ends
