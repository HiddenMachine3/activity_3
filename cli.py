from funcs import *

if __name__ == "__main__":

    while True:
        print("1. add\n2. sub\n3. mult\n4. exit")
    
        op = int(input())

        if op==4:
            print("exiting")
            break

        elif op not in [1,2,3]:
            print("invalid")
            continue
        
        print("a : ", end="")
        a = int(input())
        print("b : ", end="")
        b = int(input())

        print("ans :", add(a, b) if op==1 else (sub(a,b) if op==2 else mult(a, b)))
