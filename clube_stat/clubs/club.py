from enum import Enum

import collections


class Statistics:
    def __init__(self):
        self.taken = {}
        self.load = {}
        self.free = {}
        self.guest = {}
        self.resident = {}
        self.admin = {}
        self.workers = {}
        self.school = {}


class Clubs(collections.MutableMapping):
    def __init__(self, *args, **kwargs):
        self.clubs = {}
        self.update(dict(*args, **kwargs))

    def add_club(self, club):
        self.clubs[club.name] = club

    def __getattr__(self, item):
        return self.clubs[item]

    def __str__(self):
        return str(self.clubs)

    def __getitem__(self, key):
        return self.clubs[key]

    def __setitem__(self, key, value):
        self.clubs[key] = value

    def __delitem__(self, key):
        del self.clubs[key]

    def __iter__(self):
        return iter(self.clubs)

    def __len__(self):
        return len(self.clubs)

class Club:
    LES = "les"
    TROYA = "troya"
    AKADEM = "akadem"
    DREAM = "dream"
    taken = "taken"
    load = "load"
    free = "free"
    guest = "guest"
    resident = "resident"
    admin = "admin"
    workers = "workers"
    school = "school"
    _id = {LES: 4, AKADEM: 3, DREAM: 2, TROYA: 1}
    _field_names = dict(
        les="IT Land Les",
        troya="IT Land Troya",
        akadem="IT Land Akadem",
        dream="IT Land DreamTown"
    )

    def __init__(self, club_name, max_visitor, pro_comps=None, **kwargs):
        if pro_comps is not None:
            self.pro_comps = pro_comps
        else: self.pro_comps = []
        self.max_visitor = max_visitor
        self.store ={}
        self.name = club_name

    @property
    def id(self):
        return self._id[self.name]

    @property
    def field_name(self):
        return self._field_names[self.name]

    @staticmethod
    def get_field_by_name(name):
        return Club._field_names[name]

    def __repr__(self):
        return "{} - {}".format(self.__class__.__name__, self.name)






if __name__ == '__main__':
    clubs = Clubs()
    clubs.add_club(Club(Club.LES, 30))
    clubs.add_club(Club(Club.TROYA, 30))
    clubs.add_club(Club(Club.AKADEM, 30))
    clubs.add_club(Club(Club.DREAM, 30))


    print(clubs["les"].field_name)
