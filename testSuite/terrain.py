from lettuce import before, after, world

@before.all
def feature_steup():
    world.resp = None
