from lettuce import world, step


@step('the user tries to get the repositories of (\w+) user')
def get_user_repositories(step, user):
    # curl https://api.github.com/users/paradell/repos
    # world.response =
    pass