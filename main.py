from tests import test_scenarios

t = test_scenarios.test_scenarios()
t.setUp()
t.test_airbnb_scenario()
t.tearDown()
