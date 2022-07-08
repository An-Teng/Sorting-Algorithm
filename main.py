from BubbleSort import bubblesort
from SelectionSort import selectionsort
from InsertionSort import insertionsort
from SequentialSearch import sequentialsearch
from BinarySearch import  binarysearch
from RangeSort import rangesort
from MergeSort import mergeSort
record=[{"Package Name":"D","Customer Name":"Daniel","NoPax":7,"CostperPax":250},
        {"Package Name":"C","Customer Name":"John","NoPax":5,"CostperPax":900},
         {"Package Name":"B","Customer Name":"Bob","NoPax":20,"CostperPax":300},
         {"Package Name":"G","Customer Name":"Alice","NoPax":3,"CostperPax":150},
         ]
choice=1
Sorted=False
try:
    while choice!=0:
        print("~~~~~~Menu~~~~~~ \n 1. Display Records \n 2. Sort Record by Customer Name (Bubble Sort) \n 3. Sort Record by Package name (Selection Sort) \n 4. Sort Record by Pacakage Cost (Insertion)"
              "\n 5. Search Record by Customer Name and update (Linear Search) \n 6. Search Record by Package Name and update (Binary Search) \n 7. List Records range \n 8. Sort Record by Number of Pax (Merge Sort) \n 0. Exit")
        choice=int(input('Enter choice'))
        if choice==1:
            for key in record:
                Package=key.get("Package Name")
                Name=key.get("Customer Name")
                NoPax=key.get("NoPax")
                Cost=key.get("CostperPax")
                print("Package Name:%s Customer Name:%s Number of Pax:%s Cost Per Pax:$%s" %(Package,Name,NoPax,Cost))
        elif choice==2:
            x=bubblesort(record)
            record=x
            print("Newly Sorted List:")
            for key in x:
                Package=key.get("Package Name")
                Name=key.get("Customer Name")
                NoPax=key.get("NoPax")
                Cost=key.get("CostperPax")
                print("Package Name:%s Customer Name:%s Number of Pax:%s Cost Per Pax:$%s" %(Package,Name,NoPax,Cost))
            Sorted=False
        elif choice==3:
            x=selectionsort(record)
            record=x
            print("Newly Sorted List:")
            for key in x:
                Package=key.get("Package Name")
                Name=key.get("Customer Name")
                NoPax=key.get("NoPax")
                Cost=key.get("CostperPax")
                print("Package Name:%s Customer Name:%s Number of Pax:%s Cost Per Pax:$%s" %(Package,Name,NoPax,Cost))
            Sorted=True
        elif choice==4:
            x=insertionsort(record)
            record=x
            print("Newly Sorted List:")
            for key in x:
                Package=key.get("Package Name")
                Name=key.get("Customer Name")
                NoPax=key.get("NoPax")
                Cost=key.get("CostperPax")
                print("Package Name:%s Customer Name:%s Number of Pax:%s Cost Per Pax:$%s" %(Package,Name,NoPax,Cost))
            Sorted=False
        elif choice==5:
            target=input("Enter Customer Name to search:")
            while target.isalpha()==False:
                    print("Customer Name Should only contain Alphabets!")
                    target=input("Enter Customer Name to search:")
            x=sequentialsearch(record,target)
            record=x
        elif choice==6:
            if Sorted==True:
                target=input("Enter Package Name to search:")
                while target.isalpha()==False:
                    print("Package Name Should only contain Alphabets!")
                    target=input("Enter Package Name to search:")
                x=binarysearch(record,target)
                record=x
            else:
                print("Please Sort the Records by Package Name before searching")
        elif choice==7:
            start=input("Enter starting range value to search:")
            while start.isnumeric()==False:
                print("Starting range value should be an integer")
                start=input("Enter starting range value to search:")
            end=input("Enter ending range value to search:")
            while end.isnumeric()==False:
                print("Ending range value should be an integer")
                end=input("Enter ending range value to search:")
            while start>end:
                print("Start Value cannot be bigger than End Value")
                start=input("Enter starting range value to search:")
                while start.isnumeric()==False:
                    print("Starting range value should be an integer")
                    start=input("Enter starting range value to search:")
                end=input("Enter ending range value to search:")
                while end.isnumeric()==False:
                    print("Ending range value should be an integer")
                    end=input("Enter ending range value to search:")
            rangesort(record,int(start),int(end))
        elif choice==8:
            x=mergeSort(record)
            record=x
            print("Newly Sorted List:")
            for key in x:
                Package=key.get("Package Name")
                Name=key.get("Customer Name")
                NoPax=key.get("NoPax")
                Cost=key.get("CostperPax")
                print("Package Name:%s Customer Name:%s Number of Pax:%s Cost Per Pax:$%s" %(Package,Name,NoPax,Cost))
            Sorted=False
except ValueError:
    print("Invalid Choice")




