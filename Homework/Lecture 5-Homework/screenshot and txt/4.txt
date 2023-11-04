def quickSort(a):
    if len(a) <= 1:
        return a
    else:
        nvidia = a[0]  
        lessThanNvidia = []  
        greaterThanNvidia = []  
        for i in a[1:]:  
            if i <= nvidia:
                lessThanNvidia.append(i)  
            else:
                greaterThanNvidia.append(i)  
        
        return quickSort(lessThanNvidia) + [nvidia] + quickSort(greaterThanNvidia)



