# process_formdata is different from origin:
# one line is commented out

from wtforms import FloatField 
from wtforms.compat import text_type

class MyFloatField(FloatField): 

    def process_formdata(self, valuelist):
        if valuelist:
            try:
                self.data = float(valuelist[0])
            except ValueError:
                self.data = None

                #raise ValueError(self.gettext('Not a valid float value'))