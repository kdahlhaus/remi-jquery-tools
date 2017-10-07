import remi.gui as gui

import os
import logging

log = logging.getLogger('remi.gui.remijquerytools.overlay')

def get_res_path():
    """ return addtion to 'res' path for items needed by this lib """
    res_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'res')
    return res_path


class Overlay(gui.Widget):


    @gui.decorate_constructor_parameter_types([dict, ])
    def __init__(self, trigger, **kwargs):
        self.trigger = trigger
        super(Overlay, self).__init__(**kwargs)

    def repr(self, client, changed_widgets={}):
        """ It is used to automatically represent the object to HTML format
            packs all the attributes, children and so on.

            Args:
                client (App): The client instance.
                changed_widgets (dict): A dictionary containing a collection of tags that have to be updated.
                    The tag that have to be updated is the key, and the value is its textual repr.
        """

        self.attributes['style'] = gui.jsonize(self.style)

        # ensure overlay class is in the class attibutes once
        overlay_class="simple_overlay black"
        class_attribute=self.attributes.get('class','')
        if not overlay_class in class_attribute:
            class_attribute += " " + overlay_class
        self.attributes['class'] = class_attribute

        attribute_string = ' '.join('%s="%s"' %
            (k, v) if v is not None else k for k, v in
            self.attributes.items())

        trigger_id = self.trigger.attributes["id"]
        overlay_id = self.attributes["id"]

        html = '<div %s>'%(attribute_string)

        local_changed_widgets = {}
        innerHTML = ''
        for k in self._render_children_list:
            s = self.children[k]
            if isinstance(s, type('')):
                innerHTML = innerHTML + s
            elif isinstance(s, type(u'')):
                innerHTML = innerHTML + s.encode('utf-8')
            else:
                try:
                    innerHTML = innerHTML + s.repr(client, local_changed_widgets)
                except AttributeError:
                    innerHTML = innerHTML + repr(s)

        html += innerHTML
        html += '</div>'

        html += """
        <script>
            $(document).ready(function(){{
            var dt = $('#{trigger_id}').overlay({{target:'#{overlay_id}'}})
            }});
        </script>""".format(trigger_id=trigger_id, overlay_id=overlay_id)

        log.debug('overlay html:%s', html)

        return html
