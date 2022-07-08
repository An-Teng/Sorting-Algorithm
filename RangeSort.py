def rangesort(records,start,end):
    count=0
    for i in records:
        if i["CostperPax"] in range(start,end+1):
            Package=i.get("Package Name")
            Name=i.get("Customer Name")
            NoPax=i.get("NoPax")
            Cost=i.get("CostperPax")
            print("Package Name:%s Customer Name:%s Number of Pax:%s Cost Per Pax:$%s" %(Package,Name,NoPax,Cost))
            count+=1
    if count==0:
        print('No Item Found In Range!')

