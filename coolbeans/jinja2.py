from jinja2.environment import Environment
import random


class JinjaEnvironment(Environment):
    """
    Jinja environment
    """
    def __init__(self,**kwargs):
        """
        Initializing jinja environment with filters
        :param kwargs:
        """
        super(JinjaEnvironment, self).__init__(**kwargs)
        self.filters['shuffle'] = filter_shuffle
        self.filters['shuffle_unique'] = filter_shuffle_unique

def filter_shuffle(seq):
    """
    Basic shuffle filter
    :param seq: list to be shuffled
    :return: shuffled list
    """
    try:
        result = list(seq)
        random.shuffle(result)
        return result
    except:
        return seq

def filter_shuffle_unique(seq):
    """
    Shuffle list and make sure it's not the same as before
    :param seq: list to be shuffled
    :return: shuffled list
    """
    try:
        scrambled = list(seq)
        original = list(seq)
        random.shuffle(scrambled)
        while(equals_list(scrambled,original)):
            random.shuffle(scrambled)
        return scrambled
    except:
        return seq

def equals_list(seq1, seq2):
    """
    Arrays equality check
    :param seq1: first list
    :param seq2: second list
    :return: bool Whether the lists are the same
    """
    i=0
    for e in seq1:
        if(seq2[i]!=e):
            return False
        i+=1
    return True