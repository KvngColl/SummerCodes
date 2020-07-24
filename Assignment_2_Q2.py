import time
import numpy as n

def Interpolation_Search(arr, target):
    Low = 0
    High = (len(arr) - 1)
    while Low <= High and target >= arr[Low] and target <= arr[High]:
        POS = Low + int(((( arr[High] - arr[Low])) * ( target - arr[Low]))/float(High - Low))

        if arr[POS] == target:
            return POS
        if arr[POS] < target:
            Low = POS + 1;
        else:
            High = POS - 1;
    
    return "Not in sequence"

def Binary_Search(arr, target):
    Low = 0
    High = (len(arr) - 1)
    while Low <= High and target >= arr[Low] and target <= arr[High]:
        POS = int((Low + High)/ 2)
        
        if arr[POS] == target:
            return POS
        if arr[POS] < target:
            Low = POS + 1;
        else:
            High = POS - 1;
    
    return "Not in sequence"


def main():

  # for 100
  sequence = n.random.randint(1,32767, 100)
  start_time = time.clock()
  Interpolation_Search(sequence, 6)
  end_time = time.clock()

  start_time1 = time.clock()
  Binary_Search(sequence, 6)
  end_time1 = time.clock()

  milsec = (end_time - start_time) * 1000
  print("The time taken for interpolation search using 100 is %.12f" % milsec)

  milsec1 = (end_time1 - start_time1) * 1000
  print("The time taken for binary search is using 100 %.12f" % milsec1)
  
  # for 1000
  sequence = n.random.randint(1,32767, 1000)
  start_time = time.clock()
  Interpolation_Search(sequence, 6)
  end_time = time.clock()

  start_time1 = time.clock()
  Binary_Search(sequence, 6)
  end_time1 = time.clock()

  milsec = (end_time - start_time) * 1000
  print("The time taken for interpolation search using 1000 is %.12f" % milsec)

  milsec1 = (end_time1 - start_time1) * 1000
  print("The time taken for binary search using 1000 is %.12f" % milsec1)

  # for 5000
  
  sequence = n.random.randint(1,32767, 5000)
  start_time = time.clock()
  Interpolation_Search(sequence, 6)
  end_time = time.clock()

  start_time1 = time.clock()
  Binary_Search(sequence, 6)
  end_time1 = time.clock()

  milsec = (end_time - start_time) * 1000
  print("The time taken for interpolation search using 5000 is %.12f" % milsec)

  milsec1 = (end_time1 - start_time1) * 1000
  print("The time taken for binary search using 5000 is %.12f" % milsec1)

if __name__ == "__main__":
    main()
