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

    def parent(self, i):
        """
        Get parent index of node i.
        """
        return (i - 1) // 2

    def left(self, i):
        """
        Get left child index of node i.
        """
        return 2 * i + 1

    def right(self, i):
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
        if r <= self.heapsize and A[r] > A[largest]:
            largest = r 
        
        # Exchange largest and parent elements if parent isn't the largest.
        if largest != i:
            A[i], A[largest] = A[largest], A[i]

            self.max_heapify(A, largest)

    def min_heapify(self, A, i):
        """
        Maintains the max-heap property.

        Parameters
        ----------
        A : array-like of shape (n,)
            Array representing heap.
        i : Int
            Represents index of node to maintain max heap property.
        """
        # Store left and right child indices in variables.
        l = self.left(i)
        r = self.right(i)

        # Check if left child exists and is smaller than parent node.
        if l <= self.heapsize and A[l] < A[i]:
            smallest = l
        else:
            smallest = i 

        # Check if right child exists and is smaller than left child and parent.
        if r <= self.heapsize and A[r] < A[smallest]:
            smallest = r 

        # Swap smallest value with parent node and recursivelt call procedure.
        if smallest != i:
            A[i], A[smallest] = A[smallest], A[i]
            self.min_heapify(A, smallest)

    def build_max_heap(self, A):
        """
        Turns unordered array into a max heap.

        Parameters
        ----------
        A : array-like of shape (n,)
            Unordered array.
        """
        # Get max index of non leaf nodes.
        max_node = (self.heapsize - 1) // 2

        # Call max heapify on non-leaf nodes.
        for i in range(max_node, -1, -1):
            self.max_heapify(A, i)

    def build_min_heap(self, A):
        """
        Turns unordered array into a min heap.

        Parameters
        ----------
        A : array-like of shape (n,)
            Unordered array.
        """
        # Get max index of non leaf nodes.
        max_node = (self.heapsize - 1) // 2

        # Call min heapify on non-leaf nodes.
        for i in range(max_node, -1, -1):
            self.min_heapify(A, i)    