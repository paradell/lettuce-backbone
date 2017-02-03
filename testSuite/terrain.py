from lettuce import before, after, world


@before.all
def feature_setup():
    world.resp = None
