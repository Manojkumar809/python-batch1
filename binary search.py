l = [1,3,4,6,8,9,10,11,14,17,18]
ele = 14
left=0
right=len(l)-1
while (left<=right):
    mid = (left+right)//2
    if (l[mid]== ele):
        print(mid)
        break;
    elif (mid<ele):
        left = mid+1
    else:
        right = mid-1
