def binarysearch( records, target ):
    low = 0
    high = len( records ) - 1
    while low <= high:
        mid = (high + low) // 2
        if records[mid]["Package Name"].upper() == target.upper():
            Package=records[mid].get("Package Name")
            Name=records[mid].get("Customer Name")
            NoPax=records[mid].get("NoPax")
            Cost=records[mid].get("CostperPax")
            print("Package Name:%s Customer Name:%s Number of Pax:%s Cost Per Pax:$%s" %(Package,Name,NoPax,Cost))
            update=input("Enter do you want to update Record?(Y/N):")
            if update.upper()=="Y":
                NewPackage=input('Enter New Package Name:')
                while NewPackage.isalpha()==False:
                    print("Package Name should only contain Alphabets")
                    NewPackage=input('Enter New Package Name:')
                Newname=input("Enter New Name:")
                while Newname.isalpha()==False:
                    print("Name should only contain Alphabets")
                    Newname=input("Enter New Name:")
                NewPax=input("Enter New Number of Pax")
                while NewPax.isnumeric()==False:
                    print("Number of Pax should be an integer")
                    NewPax=input("Enter New number of Pax")
                NewCost=input("Enter New Cost Per Pax:")
                while NewCost.isnumeric()==False:
                    print("Cost Per Pax should be an integer")
                    NewCost=input("Enter New Cost Per Pax:")
                records[mid]["Package Name"]=NewPackage
                records[mid]["Customer Name"]=Newname
                records[mid]["NoPax"]=int(NewPax)
                records[mid]["CostperPax"]=int(NewCost)
            return records
        elif target.upper() < records[mid]["Package Name"].upper():
            high = mid - 1
        else:
            low = mid + 1
    else:
        print("Package Name Not Found!")


