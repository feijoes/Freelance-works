
# -------------------------------------------------------
#  ICC-211 DATA STRUCTURE & CLASSIC ALGORITHMS
#  LAB #2 - Priority Queue
#
#  Name  :
#  ID    :
#  Email :
#  Date  :
# -------------------------------------------------------

class PriorityQueue:

    # Class constructor
    def __init__(self):
        # Members of
        self.heap = []
        self.data_dict = {}
        
        # Additional code here

    # Insert or update item with priority and data given
    def insert_or_update(self, priority, data):
        self.data_dict[priority] = data
      


    # Extract element with lowest priority value
    # Return the element as tuple (priority, data)
    def extract(self):
        try:
            lowest = min(self.data_dict.items(), key=lambda x: x[0]) 
            self.data_dict.pop(lowest[0])
            return (lowest)
        except ValueError:
            return None

    # Return the element with lowest priority
    # as a tuple (priority, data)
    # DO NOT REMOVE from queue
    def peek(self):
        pass

    # Return a string representing the internal state
    def __str__(self):
        pass

    # Return number of elements in the queue
    def __len__(self):
        pass

    # Return True if queue is empty, False otherwise
    def is_empty(self):
        # Return queue is empty
        pass

