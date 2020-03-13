#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # Loop over array and add tickets to the hash table
    for x in range(length):
        hash_table_insert(hashtable, tickets[x].source, tickets[x].destination)

    # loop over array to find each destination after

    for y in range(length):
        # Find the first destination
        if y == 0:
            destination = hash_table_retrieve(hashtable, "NONE")
            route[y] = destination
        else:
        #Find consequent source,using the returned destination
            source = hash_table_retrieve(hashtable, destination)
            route[y] = source
            #new source becomes next destination
            destination = source
    #remove returned "NONE" from route at final destination
    route = route[:-1]
    return route
