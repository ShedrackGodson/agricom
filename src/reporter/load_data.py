import os
from django.contrib.gis.utils import LayerMapping
from .models import Districts, Regions, County, Ward, TZAll

# Auto-generated `LayerMapping` dictionary for Districts model
districts_mapping = {
    'district_c': 'District_C',
    'district_n': 'District_N',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for Regions model
regions_mapping = {
    'region_cod': 'Region_Cod',
    'region_nam': 'Region_Nam',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for County model
county_mapping = {
    'objectid': 'OBJECTID',
    'area': 'AREA',
    'perimeter': 'PERIMETER',
    'county3_field': 'COUNTY3_',
    'county3_id': 'COUNTY3_ID',
    'county': 'COUNTY',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for Ward model
ward_mapping = {
    'et_id': 'ET_ID',
    'adm0_en': 'ADM0_EN',
    'adm0_sw': 'ADM0_SW',
    'adm0_pcode': 'ADM0_PCODE',
    'adm1_en': 'ADM1_EN',
    'adm1_pcode': 'ADM1_PCODE',
    'adm2_en': 'ADM2_EN',
    'adm2_pcode': 'ADM2_PCODE',
    'adm3_en': 'ADM3_EN',
    'adm3_pcode': 'ADM3_PCODE',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for TZAll model
tzall_mapping = {
    'et_id': 'ET_ID',
    'id': 'Id',
    'et_left': 'ET_Left',
    'et_right': 'ET_Right',
    'adm3_l': 'ADM3_L',
    'adm2_l': 'ADM2_L',
    'adm1_l': 'ADM1_L',
    'adm0_l': 'ADM0_L',
    'admlevel': 'AdmLevel',
    'adm0_r': 'ADM0_R',
    'adm1_r': 'ADM1_R',
    'adm2_r': 'ADM2_R',
    'adm3_r': 'ADM3_R',
    'geom': 'MULTILINESTRING',
}

all_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data5/tza_admbndl_ALL_20181019.shp'))

ward_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data4/tza_admbnda_adm3_20181019.shp'))

districts_shp = os.path .abspath(os.path.join(os.path.dirname(__file__), 'data/Districts.shp'))

regions_shp = os.path .abspath(os.path.join(os.path.dirname(__file__), 'data2/Regions.shp'))

county_shp = os.path .abspath(os.path.join(os.path.dirname(__file__), 'data3/County.shp'))


def run(verbose=True):
    lm = LayerMapping(TZAll, all_shp, tzall_mapping, transform=False, encoding="iso-8859-1")
    lm.save(strict=True, verbose=verbose)
