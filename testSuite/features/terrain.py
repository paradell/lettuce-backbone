from lettuce import before, world

from utils.api_utils import GitHubApiClient


@before.all
def feature_setup():
    world.api = GitHubApiClient()
