def sequentialsearch(records, target):
    n = len(records)
    found="a"
    for i in range(n):
        # If the target is in the ith element, return True
        if records[i]["Customer Name"].upper() == target.upper():
            found=records[i]
            Package=records[i].get("Package Name")
            Name=records[i].get("Customer Name")
            NoPax=records[i].get("NoPax")
            Cost=records[i].get("CostperPax")
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
                records[i]["Package Name"]=NewPackage
                records[i]["Customer Name"]=Newname
                records[i]["NoPax"]=int(NewPax)
                records[i]["CostperPax"]=int(NewCost)
    if found=="a":
        print("Customer Name Not Found!")
    return records
