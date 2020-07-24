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
  sequence = n.random.randint(1,32767, 5000)
  start_time = time.time()
  InterpolationSearch(sequence, 6)
  end_time = time.time()

  start_time1 = time.time()
  BinarySearch(sequence, 6)
  end_time1 = time.time()

  milsec = (end_time - start_time) * 1000
  print("The time taken for interpolation search is %.12f" % milsec)

  milsec1 = (end_time1 - start_time1) * 1000
  print("The time taken for binary search is %.12f" % milsec1)

if __name__ == "__main__":
    main()
