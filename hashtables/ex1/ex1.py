#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    # Use the enumerate method to extract the index and weight (key/value)
    for index, weight in enumerate(weights):
        #insert the weight as key and the index as value to the hash table
        hash_table_insert(ht, weight, index)

    # get the needed weight of each weight by subtracting the weight from the limit
    for index, weight in enumerate(weights):
        needed_weight = limit - weight
        # if not None find the index of the needed weight
        if hash_table_retrieve(ht, needed_weight) is not None:

            needed_weight_index = hash_table_retrieve(ht, needed_weight)
            # return whichever index is greater first
            if needed_weight_index >= index:
                return [needed_weight_index, index]
            else:
                return [index, needed_weight_index]

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
