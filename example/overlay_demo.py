import sys
sys.path.append("..")

from logconfig import configure_logger_with_name
configure_logger_with_name("demo")


import os
import logging

import remi.gui as gui
from remi import start, App

import remijquerytools


log = logging.getLogger("demo")



class ExampleFrame(gui.VBox):
    def __init__(self, **kwargs):
        super(ExampleFrame, self).__init__(**kwargs)

        self.row1 = gui.HBox()
        self.append(self.row1)

        self.label = gui.Button('Click here for an overlay.', width=200, height=50, margin='10px')
        self.row1.append(self.label)

        self.overlay = remijquerytools.Overlay(trigger=self.label)
        self.overlay.style["padding"]="30px 30px 30px 30px"
        self.row1.append(self.overlay)

        label = gui.Label("This is the overlay.")
        self.overlay.append(label)



class DemoApp(App):
    def __init__(self, *args):
        res_path = remijquerytools.get_res_path()
        log.debug("DemoApp: res_path=%s", res_path)
        html_head = """
            <link rel="stylesheet" type="text/css" href="/res/overlay-basic.css"/>
            <script type="text/javascript" src="/res/jquery-2.2.4.min.js"></script>
            <script type="text/javascript" src="/res/jquery.tools.min.js"></script>
        """
        super(DemoApp, self).__init__(*args, static_file_path=res_path, html_head=html_head)

    def main(self):
        main_container = ExampleFrame(width=700, height=300)
        return main_container


if __name__ == "__main__":
    # starts the webserver
    # optional parameters
    # start(DemoApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(DemoApp, title="Overlay Demo", debug=True, standalone=True)
