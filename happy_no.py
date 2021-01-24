/* Happy Numbers - A happy number is defined by the following process. Starting with any positive integer,
 replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 
 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for
 which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers.
 Display an example of your output here. Find first 8 happynumbers. */


def happy_check(n):
    prev = []
    
    while True:
        total_sum = sum_dig_sq(n)
        if total_sum == 1:
            return True
        elif n in prev:
            return False
        else:
            n = total_sum
            prev.append(n)
            
def sum_dig_sq(n):
    s = 0
    while n != 0:
        d = n % 10
        n //= 10
        s += d ** 2
    return s         
    
def main():
    happy_no = []
    no = int(input("Enter no."))
    count = 0
    while count < 8:
        
        if happy_check(no):
            happy_no.append(no)
            count += 1
        no += 1
        
    print(happy_no)
    
if __name__ == "__main__":
    main()
