"""Module containing heap data structures."""

class Heap():
    """
    Class representing heap data structure.

    Parameters
    ----------
    A : array-like of shape (n,)
        Array representing heap.

    Attributes
    ----------
    heapsize : Int
        Number of elements in heap indexed at 0.
    """
    def __init__(self, A):
        self.heapsize = len(A) - 1

    def parent(i):
        """
        Get parent index of node i.
        """
        if i % 2 == 0:
            return i // 2 - 1
        elif i % 2 == 1:
            return i // 2

    def left(i):
        """
        Get left child index of node i.
        """
        return 2 * i + 1

    def right(i):
        """
        Get right child index of node i.
        """
        return 2 * i + 2

    def max_heapify(self, A, i):
        """
        Maintains the max-heap property.

        Parameters
        ----------
        A : array-like of shape (n,)
            Array representing heap.
        i : Int
            Represents index of node to maintain max heap property.
        """
        # Store right and left child indices in variables.
        l = self.left(i)
        r = self.right(i)

        # Check if left child is greater than parent.
        if l <= self.heapsize and A[l] > A[i]:
            largest = l 
        else:
            largest = i 
        
        # Check if right child is greater than max(left_child, parent).
        if r <= self.heapsize and A[r] > A[i]:
            largest = r 
        
        # Exchange largest and parents elements if parent isn't the largest.
        if largest != i:
            A[i], A[largest] = A[largest], A[i]

            self.max_heapify(A, largest)

    