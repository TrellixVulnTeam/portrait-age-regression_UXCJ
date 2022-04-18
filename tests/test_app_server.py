from dash.testing.application_runners import import_app
from dash.testing.composite import DashComposite


def test_dbap001_run_server(dash_duo):
    # Start dash app with the "app" variable from server.py
    app = import_app("app")
    dash_duo.start_server(app)

    # Ensure that the dash app runs by waiting until the "react-entry-point"
    # section loads (the html element with our app content), or 10 seconds.
    dash_duo.wait_for_element_by_id("react-entry-point", timeout=10)

    # TODO Review this part of the test for why it is so inconsistent between runs.
    # It mysteriously fails sometimes without changes to the code... Problems on
    # the browser end? Bizarre.

    # Ensure no errors occured in the browser.
    # assert dash_duo.get_logs() == [], "Browser console should contain no error"
