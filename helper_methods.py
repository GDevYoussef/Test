import random
import math


def choice_random_objects(from_list: [], number_of_random_objects: int = 0):
    """
    Get a random objects from specific list the default get only half of the list or over the half by one
    But, also you can specify how many random objects you want
    :param from_list: a list of objects
    :param number_of_random_objects: Default is zero which means getting half of the object in the list
    But you can change to any number you want from the list
    :return: a final list with new random objects
    """
    # if len(from_list) == 0:
    #     raise Exception("Sorry, no objects below zero")

    objects_count: int = number_of_random_objects
    if number_of_random_objects == 0:
        objects_count = int(math.ceil(math.sqrt(len(from_list))))
    return random.sample(from_list, objects_count)
