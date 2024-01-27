def find_peak(list_of_integers):
    # base case: empty list or single element
    if not list_of_integers or len(list_of_integers) == 1:
        return None
    
    # recursive helper function
    def binary_search(left, right):
        # base case: only two elements
        if right - left == 1:
            return max(list_of_integers[left], list_of_integers[right])
        
        # find the middle index
        mid = (left + right) // 2
        
        # compare the middle element with its neighbors
        if list_of_integers[mid] > list_of_integers[mid - 1] and list_of_integers[mid] > list_of_integers[mid + 1]:
            # middle element is a peak
            return list_of_integers[mid]
        elif list_of_integers[mid] < list_of_integers[mid - 1]:
            # left neighbor is larger, search in the left half
            return binary_search(left, mid - 1)
        else:
            # right neighbor is larger, search in the right half
            return binary_search(mid + 1, right)
    
    # call the helper function with the whole list
    return binary_search(0, len(list_of_integers) - 1)
