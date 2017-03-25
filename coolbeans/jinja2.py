from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse

def environment(**options):
    env = Environment(**options)
    env.globals.update({
       'static': staticfiles_storage.url,
       'url': reverse,
    })
    return env


from jinja2.environment import Environment

class JinjaEnvironment(Environment):
    def __init__(self,**kwargs):
        super(JinjaEnvironment, self).__init__(**kwargs)
        self.filters['shuffle'] = filter_shuffle
        self.filters['shuffle_unique'] = filter_shuffle_unique


import random

def filter_shuffle(seq):
    try:
        result = list(seq)
        random.shuffle(result)
        return result
    except:
        return seq

def filter_shuffle_unique(seq):
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
    i=0
    for e in seq1:
        if(seq2[i]!=e):
            return False
        i+=1
    return True