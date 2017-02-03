from lettuce import world, step


@step('the api response is a 200 code')
def check_http_response_code(step):
    # curl https://api.github.com/users/paradell/repos
    # world.response =
    pass


@step('the response includes a list with all user repositories')
def check_http_response_code(step):
    # curl https://api.github.com/users/paradell/repos
    # world.response =
    pass
