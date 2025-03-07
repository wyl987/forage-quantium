import pytest
from dash import html
from dash.testing.application_runners import import_app

@pytest.fixture
def dash_app(dash_duo):
    app = import_app("dash_app")  
    dash_duo.start_server(app)
    return dash_duo
  
# Test 1: The header is present.
def test_header(dash_app):
  dash_app.wait_for_element('h1', timeout=10)
  assert dash_app.find_element('h1').text == 'Sales Data over time'

# Test 2: The visualisation is present.
def test_visualisation(dash_app):
  dash_app.wait_for_element('#visualization', timeout=10)
  graph = dash_app.find_element('#visualization')
  assert graph is not None, "Visualization (graph) is not present"

# Test 2: The region picker is present.
def test_radio(dash_app):
  dash_app.wait_for_element('#region-selector', timeout=10)
  region_selector = dash_app.find_element('#region-selector')
  assert region_selector is not None, "Region selector is not present"