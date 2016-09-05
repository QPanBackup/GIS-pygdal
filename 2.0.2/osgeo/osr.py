# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_osr', [dirname(__file__)])
        except ImportError:
            import _osr
            return _osr
        if fp is not None:
            try:
                _mod = imp.load_module('_osr', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _osr = swig_import_helper()
    del swig_import_helper
else:
    import _osr
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


SRS_WKT_WGS84 = _osr.SRS_WKT_WGS84
SRS_PT_ALBERS_CONIC_EQUAL_AREA = _osr.SRS_PT_ALBERS_CONIC_EQUAL_AREA
SRS_PT_AZIMUTHAL_EQUIDISTANT = _osr.SRS_PT_AZIMUTHAL_EQUIDISTANT
SRS_PT_CASSINI_SOLDNER = _osr.SRS_PT_CASSINI_SOLDNER
SRS_PT_CYLINDRICAL_EQUAL_AREA = _osr.SRS_PT_CYLINDRICAL_EQUAL_AREA
SRS_PT_BONNE = _osr.SRS_PT_BONNE
SRS_PT_ECKERT_I = _osr.SRS_PT_ECKERT_I
SRS_PT_ECKERT_II = _osr.SRS_PT_ECKERT_II
SRS_PT_ECKERT_III = _osr.SRS_PT_ECKERT_III
SRS_PT_ECKERT_IV = _osr.SRS_PT_ECKERT_IV
SRS_PT_ECKERT_V = _osr.SRS_PT_ECKERT_V
SRS_PT_ECKERT_VI = _osr.SRS_PT_ECKERT_VI
SRS_PT_EQUIDISTANT_CONIC = _osr.SRS_PT_EQUIDISTANT_CONIC
SRS_PT_EQUIRECTANGULAR = _osr.SRS_PT_EQUIRECTANGULAR
SRS_PT_GALL_STEREOGRAPHIC = _osr.SRS_PT_GALL_STEREOGRAPHIC
SRS_PT_GAUSSSCHREIBERTMERCATOR = _osr.SRS_PT_GAUSSSCHREIBERTMERCATOR
SRS_PT_GEOSTATIONARY_SATELLITE = _osr.SRS_PT_GEOSTATIONARY_SATELLITE
SRS_PT_GOODE_HOMOLOSINE = _osr.SRS_PT_GOODE_HOMOLOSINE
SRS_PT_IGH = _osr.SRS_PT_IGH
SRS_PT_GNOMONIC = _osr.SRS_PT_GNOMONIC
SRS_PT_HOTINE_OBLIQUE_MERCATOR_AZIMUTH_CENTER = _osr.SRS_PT_HOTINE_OBLIQUE_MERCATOR_AZIMUTH_CENTER
SRS_PT_HOTINE_OBLIQUE_MERCATOR = _osr.SRS_PT_HOTINE_OBLIQUE_MERCATOR
SRS_PT_HOTINE_OBLIQUE_MERCATOR_TWO_POINT_NATURAL_ORIGIN = _osr.SRS_PT_HOTINE_OBLIQUE_MERCATOR_TWO_POINT_NATURAL_ORIGIN
SRS_PT_LABORDE_OBLIQUE_MERCATOR = _osr.SRS_PT_LABORDE_OBLIQUE_MERCATOR
SRS_PT_LAMBERT_CONFORMAL_CONIC_1SP = _osr.SRS_PT_LAMBERT_CONFORMAL_CONIC_1SP
SRS_PT_LAMBERT_CONFORMAL_CONIC_2SP = _osr.SRS_PT_LAMBERT_CONFORMAL_CONIC_2SP
SRS_PT_LAMBERT_CONFORMAL_CONIC_2SP_BELGIUM = _osr.SRS_PT_LAMBERT_CONFORMAL_CONIC_2SP_BELGIUM
SRS_PT_LAMBERT_AZIMUTHAL_EQUAL_AREA = _osr.SRS_PT_LAMBERT_AZIMUTHAL_EQUAL_AREA
SRS_PT_MERCATOR_1SP = _osr.SRS_PT_MERCATOR_1SP
SRS_PT_MERCATOR_2SP = _osr.SRS_PT_MERCATOR_2SP
SRS_PT_MERCATOR_AUXILIARY_SPHERE = _osr.SRS_PT_MERCATOR_AUXILIARY_SPHERE
SRS_PT_MILLER_CYLINDRICAL = _osr.SRS_PT_MILLER_CYLINDRICAL
SRS_PT_MOLLWEIDE = _osr.SRS_PT_MOLLWEIDE
SRS_PT_NEW_ZEALAND_MAP_GRID = _osr.SRS_PT_NEW_ZEALAND_MAP_GRID
SRS_PT_OBLIQUE_STEREOGRAPHIC = _osr.SRS_PT_OBLIQUE_STEREOGRAPHIC
SRS_PT_ORTHOGRAPHIC = _osr.SRS_PT_ORTHOGRAPHIC
SRS_PT_POLAR_STEREOGRAPHIC = _osr.SRS_PT_POLAR_STEREOGRAPHIC
SRS_PT_POLYCONIC = _osr.SRS_PT_POLYCONIC
SRS_PT_ROBINSON = _osr.SRS_PT_ROBINSON
SRS_PT_SINUSOIDAL = _osr.SRS_PT_SINUSOIDAL
SRS_PT_STEREOGRAPHIC = _osr.SRS_PT_STEREOGRAPHIC
SRS_PT_SWISS_OBLIQUE_CYLINDRICAL = _osr.SRS_PT_SWISS_OBLIQUE_CYLINDRICAL
SRS_PT_TRANSVERSE_MERCATOR = _osr.SRS_PT_TRANSVERSE_MERCATOR
SRS_PT_TRANSVERSE_MERCATOR_SOUTH_ORIENTED = _osr.SRS_PT_TRANSVERSE_MERCATOR_SOUTH_ORIENTED
SRS_PT_TRANSVERSE_MERCATOR_MI_21 = _osr.SRS_PT_TRANSVERSE_MERCATOR_MI_21
SRS_PT_TRANSVERSE_MERCATOR_MI_22 = _osr.SRS_PT_TRANSVERSE_MERCATOR_MI_22
SRS_PT_TRANSVERSE_MERCATOR_MI_23 = _osr.SRS_PT_TRANSVERSE_MERCATOR_MI_23
SRS_PT_TRANSVERSE_MERCATOR_MI_24 = _osr.SRS_PT_TRANSVERSE_MERCATOR_MI_24
SRS_PT_TRANSVERSE_MERCATOR_MI_25 = _osr.SRS_PT_TRANSVERSE_MERCATOR_MI_25
SRS_PT_TUNISIA_MINING_GRID = _osr.SRS_PT_TUNISIA_MINING_GRID
SRS_PT_TWO_POINT_EQUIDISTANT = _osr.SRS_PT_TWO_POINT_EQUIDISTANT
SRS_PT_VANDERGRINTEN = _osr.SRS_PT_VANDERGRINTEN
SRS_PT_KROVAK = _osr.SRS_PT_KROVAK
SRS_PT_IMW_POLYCONIC = _osr.SRS_PT_IMW_POLYCONIC
SRS_PT_WAGNER_I = _osr.SRS_PT_WAGNER_I
SRS_PT_WAGNER_II = _osr.SRS_PT_WAGNER_II
SRS_PT_WAGNER_III = _osr.SRS_PT_WAGNER_III
SRS_PT_WAGNER_IV = _osr.SRS_PT_WAGNER_IV
SRS_PT_WAGNER_V = _osr.SRS_PT_WAGNER_V
SRS_PT_WAGNER_VI = _osr.SRS_PT_WAGNER_VI
SRS_PT_WAGNER_VII = _osr.SRS_PT_WAGNER_VII
SRS_PT_QSC = _osr.SRS_PT_QSC
SRS_PT_AITOFF = _osr.SRS_PT_AITOFF
SRS_PT_WINKEL_I = _osr.SRS_PT_WINKEL_I
SRS_PT_WINKEL_II = _osr.SRS_PT_WINKEL_II
SRS_PT_WINKEL_TRIPEL = _osr.SRS_PT_WINKEL_TRIPEL
SRS_PT_CRASTER_PARABOLIC = _osr.SRS_PT_CRASTER_PARABOLIC
SRS_PT_LOXIMUTHAL = _osr.SRS_PT_LOXIMUTHAL
SRS_PT_QUARTIC_AUTHALIC = _osr.SRS_PT_QUARTIC_AUTHALIC
SRS_PP_CENTRAL_MERIDIAN = _osr.SRS_PP_CENTRAL_MERIDIAN
SRS_PP_SCALE_FACTOR = _osr.SRS_PP_SCALE_FACTOR
SRS_PP_STANDARD_PARALLEL_1 = _osr.SRS_PP_STANDARD_PARALLEL_1
SRS_PP_STANDARD_PARALLEL_2 = _osr.SRS_PP_STANDARD_PARALLEL_2
SRS_PP_PSEUDO_STD_PARALLEL_1 = _osr.SRS_PP_PSEUDO_STD_PARALLEL_1
SRS_PP_LONGITUDE_OF_CENTER = _osr.SRS_PP_LONGITUDE_OF_CENTER
SRS_PP_LATITUDE_OF_CENTER = _osr.SRS_PP_LATITUDE_OF_CENTER
SRS_PP_LONGITUDE_OF_ORIGIN = _osr.SRS_PP_LONGITUDE_OF_ORIGIN
SRS_PP_LATITUDE_OF_ORIGIN = _osr.SRS_PP_LATITUDE_OF_ORIGIN
SRS_PP_FALSE_EASTING = _osr.SRS_PP_FALSE_EASTING
SRS_PP_FALSE_NORTHING = _osr.SRS_PP_FALSE_NORTHING
SRS_PP_AZIMUTH = _osr.SRS_PP_AZIMUTH
SRS_PP_LONGITUDE_OF_POINT_1 = _osr.SRS_PP_LONGITUDE_OF_POINT_1
SRS_PP_LATITUDE_OF_POINT_1 = _osr.SRS_PP_LATITUDE_OF_POINT_1
SRS_PP_LONGITUDE_OF_POINT_2 = _osr.SRS_PP_LONGITUDE_OF_POINT_2
SRS_PP_LATITUDE_OF_POINT_2 = _osr.SRS_PP_LATITUDE_OF_POINT_2
SRS_PP_LONGITUDE_OF_POINT_3 = _osr.SRS_PP_LONGITUDE_OF_POINT_3
SRS_PP_LATITUDE_OF_POINT_3 = _osr.SRS_PP_LATITUDE_OF_POINT_3
SRS_PP_RECTIFIED_GRID_ANGLE = _osr.SRS_PP_RECTIFIED_GRID_ANGLE
SRS_PP_LANDSAT_NUMBER = _osr.SRS_PP_LANDSAT_NUMBER
SRS_PP_PATH_NUMBER = _osr.SRS_PP_PATH_NUMBER
SRS_PP_PERSPECTIVE_POINT_HEIGHT = _osr.SRS_PP_PERSPECTIVE_POINT_HEIGHT
SRS_PP_SATELLITE_HEIGHT = _osr.SRS_PP_SATELLITE_HEIGHT
SRS_PP_FIPSZONE = _osr.SRS_PP_FIPSZONE
SRS_PP_ZONE = _osr.SRS_PP_ZONE
SRS_PP_LATITUDE_OF_1ST_POINT = _osr.SRS_PP_LATITUDE_OF_1ST_POINT
SRS_PP_LONGITUDE_OF_1ST_POINT = _osr.SRS_PP_LONGITUDE_OF_1ST_POINT
SRS_PP_LATITUDE_OF_2ND_POINT = _osr.SRS_PP_LATITUDE_OF_2ND_POINT
SRS_PP_LONGITUDE_OF_2ND_POINT = _osr.SRS_PP_LONGITUDE_OF_2ND_POINT
SRS_UL_METER = _osr.SRS_UL_METER
SRS_UL_FOOT = _osr.SRS_UL_FOOT
SRS_UL_FOOT_CONV = _osr.SRS_UL_FOOT_CONV
SRS_UL_US_FOOT = _osr.SRS_UL_US_FOOT
SRS_UL_US_FOOT_CONV = _osr.SRS_UL_US_FOOT_CONV
SRS_UL_NAUTICAL_MILE = _osr.SRS_UL_NAUTICAL_MILE
SRS_UL_NAUTICAL_MILE_CONV = _osr.SRS_UL_NAUTICAL_MILE_CONV
SRS_UL_LINK = _osr.SRS_UL_LINK
SRS_UL_LINK_CONV = _osr.SRS_UL_LINK_CONV
SRS_UL_CHAIN = _osr.SRS_UL_CHAIN
SRS_UL_CHAIN_CONV = _osr.SRS_UL_CHAIN_CONV
SRS_UL_ROD = _osr.SRS_UL_ROD
SRS_UL_ROD_CONV = _osr.SRS_UL_ROD_CONV
SRS_UL_LINK_Clarke = _osr.SRS_UL_LINK_Clarke
SRS_UL_LINK_Clarke_CONV = _osr.SRS_UL_LINK_Clarke_CONV
SRS_UL_KILOMETER = _osr.SRS_UL_KILOMETER
SRS_UL_KILOMETER_CONV = _osr.SRS_UL_KILOMETER_CONV
SRS_UL_DECIMETER = _osr.SRS_UL_DECIMETER
SRS_UL_DECIMETER_CONV = _osr.SRS_UL_DECIMETER_CONV
SRS_UL_CENTIMETER = _osr.SRS_UL_CENTIMETER
SRS_UL_CENTIMETER_CONV = _osr.SRS_UL_CENTIMETER_CONV
SRS_UL_MILLIMETER = _osr.SRS_UL_MILLIMETER
SRS_UL_MILLIMETER_CONV = _osr.SRS_UL_MILLIMETER_CONV
SRS_UL_INTL_NAUT_MILE = _osr.SRS_UL_INTL_NAUT_MILE
SRS_UL_INTL_NAUT_MILE_CONV = _osr.SRS_UL_INTL_NAUT_MILE_CONV
SRS_UL_INTL_INCH = _osr.SRS_UL_INTL_INCH
SRS_UL_INTL_INCH_CONV = _osr.SRS_UL_INTL_INCH_CONV
SRS_UL_INTL_FOOT = _osr.SRS_UL_INTL_FOOT
SRS_UL_INTL_FOOT_CONV = _osr.SRS_UL_INTL_FOOT_CONV
SRS_UL_INTL_YARD = _osr.SRS_UL_INTL_YARD
SRS_UL_INTL_YARD_CONV = _osr.SRS_UL_INTL_YARD_CONV
SRS_UL_INTL_STAT_MILE = _osr.SRS_UL_INTL_STAT_MILE
SRS_UL_INTL_STAT_MILE_CONV = _osr.SRS_UL_INTL_STAT_MILE_CONV
SRS_UL_INTL_FATHOM = _osr.SRS_UL_INTL_FATHOM
SRS_UL_INTL_FATHOM_CONV = _osr.SRS_UL_INTL_FATHOM_CONV
SRS_UL_INTL_CHAIN = _osr.SRS_UL_INTL_CHAIN
SRS_UL_INTL_CHAIN_CONV = _osr.SRS_UL_INTL_CHAIN_CONV
SRS_UL_INTL_LINK = _osr.SRS_UL_INTL_LINK
SRS_UL_INTL_LINK_CONV = _osr.SRS_UL_INTL_LINK_CONV
SRS_UL_US_INCH = _osr.SRS_UL_US_INCH
SRS_UL_US_INCH_CONV = _osr.SRS_UL_US_INCH_CONV
SRS_UL_US_YARD = _osr.SRS_UL_US_YARD
SRS_UL_US_YARD_CONV = _osr.SRS_UL_US_YARD_CONV
SRS_UL_US_CHAIN = _osr.SRS_UL_US_CHAIN
SRS_UL_US_CHAIN_CONV = _osr.SRS_UL_US_CHAIN_CONV
SRS_UL_US_STAT_MILE = _osr.SRS_UL_US_STAT_MILE
SRS_UL_US_STAT_MILE_CONV = _osr.SRS_UL_US_STAT_MILE_CONV
SRS_UL_INDIAN_YARD = _osr.SRS_UL_INDIAN_YARD
SRS_UL_INDIAN_YARD_CONV = _osr.SRS_UL_INDIAN_YARD_CONV
SRS_UL_INDIAN_FOOT = _osr.SRS_UL_INDIAN_FOOT
SRS_UL_INDIAN_FOOT_CONV = _osr.SRS_UL_INDIAN_FOOT_CONV
SRS_UL_INDIAN_CHAIN = _osr.SRS_UL_INDIAN_CHAIN
SRS_UL_INDIAN_CHAIN_CONV = _osr.SRS_UL_INDIAN_CHAIN_CONV
SRS_UA_DEGREE = _osr.SRS_UA_DEGREE
SRS_UA_DEGREE_CONV = _osr.SRS_UA_DEGREE_CONV
SRS_UA_RADIAN = _osr.SRS_UA_RADIAN
SRS_PM_GREENWICH = _osr.SRS_PM_GREENWICH
SRS_DN_NAD27 = _osr.SRS_DN_NAD27
SRS_DN_NAD83 = _osr.SRS_DN_NAD83
SRS_DN_WGS72 = _osr.SRS_DN_WGS72
SRS_DN_WGS84 = _osr.SRS_DN_WGS84
SRS_WGS84_SEMIMAJOR = _osr.SRS_WGS84_SEMIMAJOR
SRS_WGS84_INVFLATTENING = _osr.SRS_WGS84_INVFLATTENING

def GetUseExceptions(*args):
  """GetUseExceptions() -> int"""
  return _osr.GetUseExceptions(*args)

def UseExceptions(*args):
  """UseExceptions()"""
  return _osr.UseExceptions(*args)

def DontUseExceptions(*args):
  """DontUseExceptions()"""
  return _osr.DontUseExceptions(*args)

def GetWellKnownGeogCSAsWKT(*args):
  """GetWellKnownGeogCSAsWKT(char name) -> OGRErr"""
  return _osr.GetWellKnownGeogCSAsWKT(*args)

def GetUserInputAsWKT(*args):
  """GetUserInputAsWKT(char name) -> OGRErr"""
  return _osr.GetUserInputAsWKT(*args)
class SpatialReference(_object):
    """Proxy of C++ OSRSpatialReferenceShadow class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SpatialReference, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SpatialReference, name)
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, char wkt = "") -> SpatialReference"""
        this = _osr.new_SpatialReference(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _osr.delete_SpatialReference
    __del__ = lambda self : None;
    def __str__(self, *args):
        """__str__(self) -> retStringAndCPLFree"""
        return _osr.SpatialReference___str__(self, *args)

    def IsSame(self, *args):
        """IsSame(self, SpatialReference rhs) -> int"""
        return _osr.SpatialReference_IsSame(self, *args)

    def IsSameGeogCS(self, *args):
        """IsSameGeogCS(self, SpatialReference rhs) -> int"""
        return _osr.SpatialReference_IsSameGeogCS(self, *args)

    def IsSameVertCS(self, *args):
        """IsSameVertCS(self, SpatialReference rhs) -> int"""
        return _osr.SpatialReference_IsSameVertCS(self, *args)

    def IsGeographic(self, *args):
        """IsGeographic(self) -> int"""
        return _osr.SpatialReference_IsGeographic(self, *args)

    def IsProjected(self, *args):
        """IsProjected(self) -> int"""
        return _osr.SpatialReference_IsProjected(self, *args)

    def IsCompound(self, *args):
        """IsCompound(self) -> int"""
        return _osr.SpatialReference_IsCompound(self, *args)

    def IsGeocentric(self, *args):
        """IsGeocentric(self) -> int"""
        return _osr.SpatialReference_IsGeocentric(self, *args)

    def IsLocal(self, *args):
        """IsLocal(self) -> int"""
        return _osr.SpatialReference_IsLocal(self, *args)

    def IsVertical(self, *args):
        """IsVertical(self) -> int"""
        return _osr.SpatialReference_IsVertical(self, *args)

    def EPSGTreatsAsLatLong(self, *args):
        """EPSGTreatsAsLatLong(self) -> int"""
        return _osr.SpatialReference_EPSGTreatsAsLatLong(self, *args)

    def EPSGTreatsAsNorthingEasting(self, *args):
        """EPSGTreatsAsNorthingEasting(self) -> int"""
        return _osr.SpatialReference_EPSGTreatsAsNorthingEasting(self, *args)

    def SetAuthority(self, *args):
        """SetAuthority(self, char pszTargetKey, char pszAuthority, int nCode) -> OGRErr"""
        return _osr.SpatialReference_SetAuthority(self, *args)

    def GetAttrValue(self, *args):
        """GetAttrValue(self, char name, int child = 0) -> char"""
        return _osr.SpatialReference_GetAttrValue(self, *args)

    def SetAttrValue(self, *args):
        """SetAttrValue(self, char name, char value) -> OGRErr"""
        return _osr.SpatialReference_SetAttrValue(self, *args)

    def SetAngularUnits(self, *args):
        """SetAngularUnits(self, char name, double to_radians) -> OGRErr"""
        return _osr.SpatialReference_SetAngularUnits(self, *args)

    def GetAngularUnits(self, *args):
        """GetAngularUnits(self) -> double"""
        return _osr.SpatialReference_GetAngularUnits(self, *args)

    def SetTargetLinearUnits(self, *args):
        """SetTargetLinearUnits(self, char target, char name, double to_meters) -> OGRErr"""
        return _osr.SpatialReference_SetTargetLinearUnits(self, *args)

    def SetLinearUnits(self, *args):
        """SetLinearUnits(self, char name, double to_meters) -> OGRErr"""
        return _osr.SpatialReference_SetLinearUnits(self, *args)

    def SetLinearUnitsAndUpdateParameters(self, *args):
        """SetLinearUnitsAndUpdateParameters(self, char name, double to_meters) -> OGRErr"""
        return _osr.SpatialReference_SetLinearUnitsAndUpdateParameters(self, *args)

    def GetLinearUnits(self, *args):
        """GetLinearUnits(self) -> double"""
        return _osr.SpatialReference_GetLinearUnits(self, *args)

    def GetLinearUnitsName(self, *args):
        """GetLinearUnitsName(self) -> char"""
        return _osr.SpatialReference_GetLinearUnitsName(self, *args)

    def GetAuthorityCode(self, *args):
        """GetAuthorityCode(self, char target_key) -> char"""
        return _osr.SpatialReference_GetAuthorityCode(self, *args)

    def GetAuthorityName(self, *args):
        """GetAuthorityName(self, char target_key) -> char"""
        return _osr.SpatialReference_GetAuthorityName(self, *args)

    def SetUTM(self, *args):
        """SetUTM(self, int zone, int north = 1) -> OGRErr"""
        return _osr.SpatialReference_SetUTM(self, *args)

    def GetUTMZone(self, *args):
        """GetUTMZone(self) -> int"""
        return _osr.SpatialReference_GetUTMZone(self, *args)

    def SetStatePlane(self, *args):
        """SetStatePlane(self, int zone, int is_nad83 = 1, char unitsname = "", double units = 0.0) -> OGRErr"""
        return _osr.SpatialReference_SetStatePlane(self, *args)

    def AutoIdentifyEPSG(self, *args):
        """AutoIdentifyEPSG(self) -> OGRErr"""
        return _osr.SpatialReference_AutoIdentifyEPSG(self, *args)

    def SetProjection(self, *args):
        """SetProjection(self, char arg) -> OGRErr"""
        return _osr.SpatialReference_SetProjection(self, *args)

    def SetProjParm(self, *args):
        """SetProjParm(self, char name, double val) -> OGRErr"""
        return _osr.SpatialReference_SetProjParm(self, *args)

    def GetProjParm(self, *args):
        """GetProjParm(self, char name, double default_val = 0.0) -> double"""
        return _osr.SpatialReference_GetProjParm(self, *args)

    def SetNormProjParm(self, *args):
        """SetNormProjParm(self, char name, double val) -> OGRErr"""
        return _osr.SpatialReference_SetNormProjParm(self, *args)

    def GetNormProjParm(self, *args):
        """GetNormProjParm(self, char name, double default_val = 0.0) -> double"""
        return _osr.SpatialReference_GetNormProjParm(self, *args)

    def GetSemiMajor(self, *args):
        """GetSemiMajor(self) -> double"""
        return _osr.SpatialReference_GetSemiMajor(self, *args)

    def GetSemiMinor(self, *args):
        """GetSemiMinor(self) -> double"""
        return _osr.SpatialReference_GetSemiMinor(self, *args)

    def GetInvFlattening(self, *args):
        """GetInvFlattening(self) -> double"""
        return _osr.SpatialReference_GetInvFlattening(self, *args)

    def SetACEA(self, *args, **kwargs):
        """
        SetACEA(self, double stdp1, double stdp2, double clat, double clong, 
            double fe, double fn) -> OGRErr
        """
        return _osr.SpatialReference_SetACEA(self, *args, **kwargs)

    def SetAE(self, *args, **kwargs):
        """SetAE(self, double clat, double clong, double fe, double fn) -> OGRErr"""
        return _osr.SpatialReference_SetAE(self, *args, **kwargs)

    def SetBonne(self, *args, **kwargs):
        """SetBonne(self, double stdp, double cm, double fe, double fn) -> OGRErr"""
        return _osr.SpatialReference_SetBonne(self, *args, **kwargs)

    def SetCEA(self, *args, **kwargs):
        """SetCEA(self, double stdp1, double cm, double fe, double fn) -> OGRErr"""
        return _osr.SpatialReference_SetCEA(self, *args, **kwargs)

    def SetCS(self, *args, **kwargs):
        """SetCS(self, double clat, double clong, double fe, double fn) -> OGRErr"""
        return _osr.SpatialReference_SetCS(self, *args, **kwargs)

    def SetEC(self, *args, **kwargs):
        """
        SetEC(self, double stdp1, double stdp2, double clat, double clong, 
            double fe, double fn) -> OGRErr
        """
        return _osr.SpatialReference_SetEC(self, *args, **kwargs)

    def SetEckertIV(self, *args, **kwargs):
        """SetEckertIV(self, double cm, double fe, double fn) -> OGRErr"""
        return _osr.SpatialReference_SetEckertIV(self, *args, **kwargs)

    def SetEckertVI(self, *args, **kwargs):
        """SetEckertVI(self, double cm, double fe, double fn) -> OGRErr"""
        return _osr.SpatialReference_SetEckertVI(self, *args, **kwargs)

    def SetEquirectangular(self, *args, **kwargs):
        """SetEquirectangular(self, double clat, double clong, double fe, double fn) -> OGRErr"""
        return _osr.SpatialReference_SetEquirectangular(self, *args, **kwargs)

    def SetEquirectangular2(self, *args, **kwargs):
        """
        SetEquirectangular2(self, double clat, double clong, double pseudostdparallellat, 
            double fe, double fn) -> OGRErr
        """
        return _osr.SpatialReference_SetEquirectangular2(self, *args, **kwargs)

    def SetGaussSchreiberTMercator(self, *args, **kwargs):
        """SetGaussSchreiberTMercator(self, double clat, double clong, double sc, double fe, double fn) -> OGRErr"""
        return _osr.SpatialReference_SetGaussSchreiberTMercator(self, *args, **kwargs)

    def SetGS(self, *args, **kwargs):
        """SetGS(self, double cm, double fe, double fn) -> OGRErr"""
        return _osr.SpatialReference_SetGS(self, *args, **kwargs)

    def SetGH(self, *args, **kwargs):
        """SetGH(self, double cm, double fe, double fn) -> OGRErr"""
        return _osr.SpatialReference_SetGH(self, *args, **kwargs)

    def SetIGH(self, *args):
        """SetIGH(self) -> OGRErr"""
        return _osr.SpatialReference_SetIGH(self, *args)

    def SetGEOS(self, *args, **kwargs):
        """SetGEOS(self, double cm, double satelliteheight, double fe, double fn) -> OGRErr"""
        return _osr.SpatialReference_SetGEOS(self, *args, **kwargs)

    def SetGnomonic(self, *args, **kwargs):
        """SetGnomonic(self, double clat, double clong, double fe, double fn) -> OGRErr"""
        return _osr.SpatialReference_SetGnomonic(self, *args, **kwargs)

    def SetHOM(self, *args, **kwargs):
        """
        SetHOM(self, double clat, double clong, double azimuth, double recttoskew, 
            double scale, double fe, double fn) -> OGRErr
        """
        return _osr.SpatialReference_SetHOM(self, *args, **kwargs)

    def SetHOM2PNO(self, *args, **kwargs):
        """
        SetHOM2PNO(self, double clat, double dfLat1, double dfLong1, double dfLat2, 
            double dfLong2, double scale, double fe, 
            double fn) -> OGRErr
        """
        return _osr.SpatialReference_SetHOM2PNO(self, *args, **kwargs)

    def SetKrovak(self, *args, **kwargs):
        """
        SetKrovak(self, double clat, double clong, double azimuth, double pseudostdparallellat, 
            double scale, double fe, 
            double fn) -> OGRErr
        """
        return _osr.SpatialReference_SetKrovak(self, *args, **kwargs)

    def SetLAEA(self, *args, **kwargs):
        """SetLAEA(self, double clat, double clong, double fe, double fn) -> OGRErr"""
        return _osr.SpatialReference_SetLAEA(self, *args, **kwargs)

    def SetLCC(self, *args, **kwargs):
        """
        SetLCC(self, double stdp1, double stdp2, double clat, double clong, 
            double fe, double fn) -> OGRErr
        """
        return _osr.SpatialReference_SetLCC(self, *args, **kwargs)

    def SetLCC1SP(self, *args, **kwargs):
        """
        SetLCC1SP(self, double clat, double clong, double scale, double fe, 
            double fn) -> OGRErr
        """
        return _osr.SpatialReference_SetLCC1SP(self, *args, **kwargs)

    def SetLCCB(self, *args, **kwargs):
        """
        SetLCCB(self, double stdp1, double stdp2, double clat, double clong, 
            double fe, double fn) -> OGRErr
        """
        return _osr.SpatialReference_SetLCCB(self, *args, **kwargs)

    def SetMC(self, *args, **kwargs):
        """SetMC(self, double clat, double clong, double fe, double fn) -> OGRErr"""
        return _osr.SpatialReference_SetMC(self, *args, **kwargs)

    def SetMercator(self, *args, **kwargs):
        """
        SetMercator(self, double clat, double clong, double scale, double fe, 
            double fn) -> OGRErr
        """
        return _osr.SpatialReference_SetMercator(self, *args, **kwargs)

    def SetMollweide(self, *args, **kwargs):
        """SetMollweide(self, double cm, double fe, double fn) -> OGRErr"""
        return _osr.SpatialReference_SetMollweide(self, *args, **kwargs)

    def SetNZMG(self, *args, **kwargs):
        """SetNZMG(self, double clat, double clong, double fe, double fn) -> OGRErr"""
        return _osr.SpatialReference_SetNZMG(self, *args, **kwargs)

    def SetOS(self, *args, **kwargs):
        """
        SetOS(self, double dfOriginLat, double dfCMeridian, double scale, 
            double fe, double fn) -> OGRErr
        """
        return _osr.SpatialReference_SetOS(self, *args, **kwargs)

    def SetOrthographic(self, *args, **kwargs):
        """SetOrthographic(self, double clat, double clong, double fe, double fn) -> OGRErr"""
        return _osr.SpatialReference_SetOrthographic(self, *args, **kwargs)

    def SetPolyconic(self, *args, **kwargs):
        """SetPolyconic(self, double clat, double clong, double fe, double fn) -> OGRErr"""
        return _osr.SpatialReference_SetPolyconic(self, *args, **kwargs)

    def SetPS(self, *args, **kwargs):
        """
        SetPS(self, double clat, double clong, double scale, double fe, 
            double fn) -> OGRErr
        """
        return _osr.SpatialReference_SetPS(self, *args, **kwargs)

    def SetRobinson(self, *args, **kwargs):
        """SetRobinson(self, double clong, double fe, double fn) -> OGRErr"""
        return _osr.SpatialReference_SetRobinson(self, *args, **kwargs)

    def SetSinusoidal(self, *args, **kwargs):
        """SetSinusoidal(self, double clong, double fe, double fn) -> OGRErr"""
        return _osr.SpatialReference_SetSinusoidal(self, *args, **kwargs)

    def SetStereographic(self, *args, **kwargs):
        """
        SetStereographic(self, double clat, double clong, double scale, double fe, 
            double fn) -> OGRErr
        """
        return _osr.SpatialReference_SetStereographic(self, *args, **kwargs)

    def SetSOC(self, *args, **kwargs):
        """SetSOC(self, double latitudeoforigin, double cm, double fe, double fn) -> OGRErr"""
        return _osr.SpatialReference_SetSOC(self, *args, **kwargs)

    def SetTM(self, *args, **kwargs):
        """
        SetTM(self, double clat, double clong, double scale, double fe, 
            double fn) -> OGRErr
        """
        return _osr.SpatialReference_SetTM(self, *args, **kwargs)

    def SetTMVariant(self, *args, **kwargs):
        """
        SetTMVariant(self, char pszVariantName, double clat, double clong, double scale, 
            double fe, double fn) -> OGRErr
        """
        return _osr.SpatialReference_SetTMVariant(self, *args, **kwargs)

    def SetTMG(self, *args, **kwargs):
        """SetTMG(self, double clat, double clong, double fe, double fn) -> OGRErr"""
        return _osr.SpatialReference_SetTMG(self, *args, **kwargs)

    def SetTMSO(self, *args, **kwargs):
        """
        SetTMSO(self, double clat, double clong, double scale, double fe, 
            double fn) -> OGRErr
        """
        return _osr.SpatialReference_SetTMSO(self, *args, **kwargs)

    def SetVDG(self, *args, **kwargs):
        """SetVDG(self, double clong, double fe, double fn) -> OGRErr"""
        return _osr.SpatialReference_SetVDG(self, *args, **kwargs)

    def SetWellKnownGeogCS(self, *args):
        """SetWellKnownGeogCS(self, char name) -> OGRErr"""
        return _osr.SpatialReference_SetWellKnownGeogCS(self, *args)

    def SetFromUserInput(self, *args):
        """SetFromUserInput(self, char name) -> OGRErr"""
        return _osr.SpatialReference_SetFromUserInput(self, *args)

    def CopyGeogCSFrom(self, *args):
        """CopyGeogCSFrom(self, SpatialReference rhs) -> OGRErr"""
        return _osr.SpatialReference_CopyGeogCSFrom(self, *args)

    def SetTOWGS84(self, *args):
        """
        SetTOWGS84(self, double p1, double p2, double p3, double p4 = 0.0, double p5 = 0.0, 
            double p6 = 0.0, double p7 = 0.0) -> OGRErr
        """
        return _osr.SpatialReference_SetTOWGS84(self, *args)

    def GetTOWGS84(self, *args):
        """GetTOWGS84(self) -> OGRErr"""
        return _osr.SpatialReference_GetTOWGS84(self, *args)

    def SetLocalCS(self, *args):
        """SetLocalCS(self, char pszName) -> OGRErr"""
        return _osr.SpatialReference_SetLocalCS(self, *args)

    def SetGeogCS(self, *args):
        """
        SetGeogCS(self, char pszGeogName, char pszDatumName, char pszEllipsoidName, 
            double dfSemiMajor, double dfInvFlattening, 
            char pszPMName = "Greenwich", double dfPMOffset = 0.0, 
            char pszUnits = "degree", double dfConvertToRadians = 0.0174532925199433) -> OGRErr
        """
        return _osr.SpatialReference_SetGeogCS(self, *args)

    def SetProjCS(self, *args):
        """SetProjCS(self, char name = "unnamed") -> OGRErr"""
        return _osr.SpatialReference_SetProjCS(self, *args)

    def SetGeocCS(self, *args):
        """SetGeocCS(self, char name = "unnamed") -> OGRErr"""
        return _osr.SpatialReference_SetGeocCS(self, *args)

    def SetVertCS(self, *args):
        """
        SetVertCS(self, char VertCSName = "unnamed", char VertDatumName = "unnamed", 
            int VertDatumType = 0) -> OGRErr
        """
        return _osr.SpatialReference_SetVertCS(self, *args)

    def SetCompoundCS(self, *args):
        """SetCompoundCS(self, char name, SpatialReference horizcs, SpatialReference vertcs) -> OGRErr"""
        return _osr.SpatialReference_SetCompoundCS(self, *args)

    def ImportFromWkt(self, *args):
        """ImportFromWkt(self, char ppszInput) -> OGRErr"""
        return _osr.SpatialReference_ImportFromWkt(self, *args)

    def ImportFromProj4(self, *args):
        """ImportFromProj4(self, char ppszInput) -> OGRErr"""
        return _osr.SpatialReference_ImportFromProj4(self, *args)

    def ImportFromUrl(self, *args):
        """ImportFromUrl(self, char url) -> OGRErr"""
        return _osr.SpatialReference_ImportFromUrl(self, *args)

    def ImportFromESRI(self, *args):
        """ImportFromESRI(self, char ppszInput) -> OGRErr"""
        return _osr.SpatialReference_ImportFromESRI(self, *args)

    def ImportFromEPSG(self, *args):
        """ImportFromEPSG(self, int arg) -> OGRErr"""
        return _osr.SpatialReference_ImportFromEPSG(self, *args)

    def ImportFromEPSGA(self, *args):
        """ImportFromEPSGA(self, int arg) -> OGRErr"""
        return _osr.SpatialReference_ImportFromEPSGA(self, *args)

    def ImportFromPCI(self, *args):
        """ImportFromPCI(self, char proj, char units = "METRE", double argin = 0) -> OGRErr"""
        return _osr.SpatialReference_ImportFromPCI(self, *args)

    def ImportFromUSGS(self, *args):
        """ImportFromUSGS(self, long proj_code, long zone = 0, double argin = 0, long datum_code = 0) -> OGRErr"""
        return _osr.SpatialReference_ImportFromUSGS(self, *args)

    def ImportFromXML(self, *args):
        """ImportFromXML(self, char xmlString) -> OGRErr"""
        return _osr.SpatialReference_ImportFromXML(self, *args)

    def ImportFromERM(self, *args):
        """ImportFromERM(self, char proj, char datum, char units) -> OGRErr"""
        return _osr.SpatialReference_ImportFromERM(self, *args)

    def ImportFromMICoordSys(self, *args):
        """ImportFromMICoordSys(self, char pszCoordSys) -> OGRErr"""
        return _osr.SpatialReference_ImportFromMICoordSys(self, *args)

    def ImportFromOzi(self, *args):
        """ImportFromOzi(self, char papszLines) -> OGRErr"""
        return _osr.SpatialReference_ImportFromOzi(self, *args)

    def ExportToWkt(self, *args):
        """ExportToWkt(self) -> OGRErr"""
        return _osr.SpatialReference_ExportToWkt(self, *args)

    def ExportToPrettyWkt(self, *args):
        """ExportToPrettyWkt(self, int simplify = 0) -> OGRErr"""
        return _osr.SpatialReference_ExportToPrettyWkt(self, *args)

    def ExportToProj4(self, *args):
        """ExportToProj4(self) -> OGRErr"""
        return _osr.SpatialReference_ExportToProj4(self, *args)

    def ExportToPCI(self, *args):
        """ExportToPCI(self) -> OGRErr"""
        return _osr.SpatialReference_ExportToPCI(self, *args)

    def ExportToUSGS(self, *args):
        """ExportToUSGS(self) -> OGRErr"""
        return _osr.SpatialReference_ExportToUSGS(self, *args)

    def ExportToXML(self, *args):
        """ExportToXML(self, char dialect = "") -> OGRErr"""
        return _osr.SpatialReference_ExportToXML(self, *args)

    def ExportToMICoordSys(self, *args):
        """ExportToMICoordSys(self) -> OGRErr"""
        return _osr.SpatialReference_ExportToMICoordSys(self, *args)

    def CloneGeogCS(self, *args):
        """CloneGeogCS(self) -> SpatialReference"""
        return _osr.SpatialReference_CloneGeogCS(self, *args)

    def Clone(self, *args):
        """Clone(self) -> SpatialReference"""
        return _osr.SpatialReference_Clone(self, *args)

    def Validate(self, *args):
        """Validate(self) -> OGRErr"""
        return _osr.SpatialReference_Validate(self, *args)

    def StripCTParms(self, *args):
        """StripCTParms(self) -> OGRErr"""
        return _osr.SpatialReference_StripCTParms(self, *args)

    def FixupOrdering(self, *args):
        """FixupOrdering(self) -> OGRErr"""
        return _osr.SpatialReference_FixupOrdering(self, *args)

    def Fixup(self, *args):
        """Fixup(self) -> OGRErr"""
        return _osr.SpatialReference_Fixup(self, *args)

    def MorphToESRI(self, *args):
        """MorphToESRI(self) -> OGRErr"""
        return _osr.SpatialReference_MorphToESRI(self, *args)

    def MorphFromESRI(self, *args):
        """MorphFromESRI(self) -> OGRErr"""
        return _osr.SpatialReference_MorphFromESRI(self, *args)

SpatialReference_swigregister = _osr.SpatialReference_swigregister
SpatialReference_swigregister(SpatialReference)
GetProjectionMethods = _osr.GetProjectionMethods

class CoordinateTransformation(_object):
    """Proxy of C++ OSRCoordinateTransformationShadow class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CoordinateTransformation, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CoordinateTransformation, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """__init__(self, SpatialReference src, SpatialReference dst) -> CoordinateTransformation"""
        this = _osr.new_CoordinateTransformation(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _osr.delete_CoordinateTransformation
    __del__ = lambda self : None;
    def TransformPoint(self, *args):
        """
        TransformPoint(self, double inout)
        TransformPoint(self, double x, double y, double z = 0.0)
        """
        return _osr.CoordinateTransformation_TransformPoint(self, *args)

    def TransformPoints(self, *args):
        """TransformPoints(self, int nCount)"""
        return _osr.CoordinateTransformation_TransformPoints(self, *args)

CoordinateTransformation_swigregister = _osr.CoordinateTransformation_swigregister
CoordinateTransformation_swigregister(CoordinateTransformation)


def CreateCoordinateTransformation(*args):
  """CreateCoordinateTransformation(SpatialReference src, SpatialReference dst) -> CoordinateTransformation"""
  return _osr.CreateCoordinateTransformation(*args)


