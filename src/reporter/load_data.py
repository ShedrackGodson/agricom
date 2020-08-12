import os
from django.contrib.gis.utils import LayerMapping
from .models import Districts

# Auto-generated `LayerMapping` dictionary for Districts model
districts_mapping = {
    'district_c': 'District_C',
    'district_n': 'District_N',
    'geom': 'MULTIPOLYGON',
}

districts_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/Districts.shp'))

def run(verbose=True):
    lm = LayerMapping(Districts, districts_shp, districts_mapping, transform=False, encoding="iso-8859-1")
    lm.save(strict=True, verbose=verbose)