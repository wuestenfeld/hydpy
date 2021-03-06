# -*- coding: utf-8 -*-
"""The HydPy-H-Branch model allows for branching the input from a
single inlet :class:`~hydpy.core.devicetools.Node` instance to
an arbitrary number of outlet :class:`~hydpy.core.devicetools.Node`
instances.  In the original  HBV96 implementation, it is supposed to
seperate inflowing discharge, but in :ref:`HydPy` it can be used for
arbitrary variables.  Calculations are performed for each branch
individually by linear interpolation (or extrapolation) in accordance
with tabulated supporting points.
"""
# import...
# ...from standard library
from __future__ import division, print_function
# ...from HydPy
from hydpy.core.modelimports import *
# ...from hbranch
from hydpy.models.hbranch.hbranch_control import ControlParameters
from hydpy.models.hbranch.hbranch_derived import DerivedParameters
from hydpy.models.hbranch.hbranch_fluxes import FluxSequences
from hydpy.models.hbranch.hbranch_inlets import InletSequences
from hydpy.models.hbranch.hbranch_outlets import OutletSequences
from hydpy.models.hbranch.hbranch_model import Model

autodoc_basemodel()
tester = Tester()
cythonizer = Cythonizer()
cythonizer.complete()
