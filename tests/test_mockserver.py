"""
Mockserver provides a way to check if the protocol between endpoints are complied.

Example:
Let's say we need to test a project's API, this API depends on some external
endpoints which are not under our control and we know the protocol between them.

There is one way to check if the talk between dependencies and our API is working
as expected, which is to reproduce in our tests the conversation between these endpoints.

mockserver = MockServer('my_external_dependency_api',host='localhost', port=5000)

mockserver.load()

"""


def test_mockserver_load_scenario(mockserver):
    assert 0


def test_mockserver_run_step(mockserver):
    pass


def test_start_mockserver(mockserver):
    pass
