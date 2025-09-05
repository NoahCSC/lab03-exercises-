def find_duplicates_nested_loop(l: list) -> list:
    result=[]
    for i in range(len(l)):
        for j in range(i+1,len(l)):

            if l[i]==l[j]:
                if l[i] not in result:
                    result.append(l[i])
    return result
def find_duplicates_set(l:list)->list:
    s1=set()
    result=[]
    for i in range(len(l)):
        if l[i] in s1:
            if l[i] not in result:
                result.append(l[i])
        else:
            s1.add(l[i])
    return result       
    
if __name__ == "__main__":
    sample1 = [3, 7, 5, 6, 7, 4, 8, 5, 7, 66]
    sample2 = [3, 5, 6, 4, 4, 5, 66, 6, 7, 6]
    sample3 = [3, 0, 5, 1, 0]
    sample4 = [3]
    
    print("Sample 1:", find_duplicates_nested_loop(sample1))
    print("Sample 2:", find_duplicates_nested_loop(sample2))
    print("Sample 3:", find_duplicates_nested_loop(sample3))
    print("Sample 4:", find_duplicates_nested_loop(sample4))
    print("Sample 5:", find_duplicates_set(sample1))
    print("Sample 6:", find_duplicates_set(sample2))
    print("Sample 7:", find_duplicates_set(sample3))
    print("Sample 8:", find_duplicates_set(sample4))