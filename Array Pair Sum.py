''' Problem
    Given an integer array,output all the unique pairs that sum up to a specific value k
    so the input:
    pair_sum([1,3,2,2],4)
    would return 2 pairs:
    (1,3)
    (2,2)'''

'''O(N) algorithm uses set data structure.We perform a linear pass from beginning 
    and each element we check whether k-element is in set of seen numbers.If it is 
    then we found a pair of sum k and add it to the output.If not this element doesn't belong
    to a pair yet, and we add it to set of seen elements.
    Insert and find operation of a set are both average O(1),so algo is O(N) in total.'''

def pair_sum(arr,k):

    if len(arr)<2:
        return

    #Sets for tracking

    seen = set()        #strategy to converting things that might seem
                        # take order of n^2 and reducing down to linear
    output = set()

    for num in arr:
        target = k-num
        if target not in seen:
            seen.add(num)
        else:
            output.add( ((min(num,target)), max(num,target)))

    print(len(output))
    return len(output)


pair_sum([1,3,2,2],4)