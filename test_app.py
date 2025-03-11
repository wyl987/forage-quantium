from dash_app import app

# Test 1: The header is present.
def test_header(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element('h1', timeout=10).text == 'Sales Data over time'

# Test 2: The visualisation is present.
def test_visualisation(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element('#visualization', timeout=10)
    graph = dash_duo.find_element('#visualization')
    assert graph is not None, "Visualization (graph) is not present"

# Test 3: The region picker is present.
def test_radio(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element('#region-selector', timeout=10)
    region_selector = dash_duo.find_element('#region-selector')
    assert region_selector is not None, "Region selector is not present"