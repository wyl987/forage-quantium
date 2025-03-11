from dash_app import app
from selenium.webdriver.chrome.options import Options

# Test 1: The header is present.
def test_header(dash_duo):
    # Set Chrome options for headless mode
    chrome_options = Options()
    # Ensure the browser runs without UI
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--user-data-dir=/tmp/chrome_user_data")
    # Start the server with the headless browser option
    dash_duo.start_server(app, browser="chrome", options=chrome_options)
    
    dash_duo.wait_for_element('h1', timeout=10).text == 'Sales Data over time'

# Test 2: The visualisation is present.
def test_visualisation(dash_duo):
    # Set Chrome options for headless mode
    chrome_options = Options()
    # Ensure the browser runs without UI
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--user-data-dir=/tmp/chrome_user_data")
    # Start the server with the headless browser option
    dash_duo.start_server(app, browser="chrome", options=chrome_options)
    
    dash_duo.wait_for_element('#visualization', timeout=10)
    graph = dash_duo.find_element('#visualization')
    assert graph is not None, "Visualization (graph) is not present"

# Test 3: The region picker is present.
def test_radio(dash_duo):
    # Set Chrome options for headless mode
    chrome_options = Options()
    # Ensure the browser runs without UI
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--user-data-dir=/tmp/chrome_user_data")
    # Start the server with the headless browser option
    dash_duo.start_server(app, browser="chrome", options=chrome_options)
    
    dash_duo.wait_for_element('#region-selector', timeout=10)
    region_selector = dash_duo.find_element('#region-selector')
    assert region_selector is not None, "Region selector is not present"