import string
import collections

#print(string.ascii_lowercase)

def main():
    mydeque = collections.deque(string.ascii_lowercase)
    print("Numbe of elements: ",len(mydeque))

    # for i in mydeque:
    #     print(i,end=',')
    mydeque.pop()
    print(mydeque)
    mydeque.popleft()
    print(mydeque)
    mydeque.append(9999)
    print(mydeque)
    mydeque.appendleft(1111)
    print(mydeque)
    mydeque.rotate()
    print(mydeque)
    mydeque.rotate(5)
    print(mydeque)



if __name__ == '__main__':
    main()
