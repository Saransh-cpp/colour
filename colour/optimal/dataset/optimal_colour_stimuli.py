#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Optimal Colour Stimuli
======================

Defines *MacAdam* optimal colour stimuli for various illuminants in *CIE xyY*
colourspace.

The optimal colour stimuli data is in the form of a *dict* of
*tuple* as follows::

    {'name': tuple, ..., 'name': tuple}

where each *tuple* contains a collection of optimal colour stimulus *tuple* as
follows::

     (('x', 'y', 'Y'), ..., ('x', 'y', 'Y'))

See Also
--------
`Optimal Colour Stimuli - MacAdam Limits IPython Notebook
<http://nbviewer.ipython.org/github/colour-science/colour-ipython/blob/master/notebooks/optimal/macadam_limits.ipynb>`_  # noqa

References
----------
.. [1]  http://en.wikipedia.org/wiki/Gamut#Surfaces
"""

from __future__ import division, unicode_literals

from colour.utilities import CaseInsensitiveMapping

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013 - 2014 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['A_OPTIMAL_COLOUR_STIMULI',
           'C_OPTIMAL_COLOUR_STIMULI',
           'D65_OPTIMAL_COLOUR_STIMULI',
           'ILLUMINANTS_OPTIMAL_COLOUR_STIMULI']

A_OPTIMAL_COLOUR_STIMULI = (
    (0.0000, 0.0000, 0),
    (0.1120, 0.1985, 10),
    (0.0859, 0.2957, 10),
    (0.0549, 0.4593, 10),
    (0.0433, 0.5548, 10),
    (0.0386, 0.6764, 10),
    (0.0441, 0.7368, 10),
    (0.0578, 0.7834, 10),
    (0.0786, 0.8102, 10),
    (0.1030, 0.8188, 10),
    (0.1276, 0.8151, 10),
    (0.1510, 0.8054, 10),
    (0.7188, 0.2812, 10),
    (0.7112, 0.2773, 10),
    (0.6506, 0.2469, 10),
    (0.6015, 0.2228, 10),
    (0.5604, 0.2032, 10),
    (0.5179, 0.1839, 10),
    (0.4590, 0.1606, 10),
    (0.4302, 0.1526, 10),
    (0.3946, 0.1488, 10),
    (0.3514, 0.1519, 10),
    (0.2949, 0.1610, 10),
    (0.2452, 0.1706, 10),
    (0.2009, 0.1797, 10),
    (0.1197, 0.3185, 20),
    (0.0977, 0.4993, 20),
    (0.0929, 0.6609, 20),
    (0.1073, 0.7534, 20),
    (0.1187, 0.7744, 20),
    (0.1335, 0.7863, 20),
    (0.1505, 0.7896, 20),
    (0.1683, 0.7863, 20),
    (0.2028, 0.7690, 20),
    (0.3641, 0.6326, 20),
    (0.4206, 0.5776, 20),
    (0.7008, 0.2991, 20),
    (0.6726, 0.2834, 20),
    (0.6350, 0.2629, 20),
    (0.6020, 0.2454, 20),
    (0.5601, 0.2246, 20),
    (0.5005, 0.2027, 20),
    (0.4823, 0.2013, 20),
    (0.4532, 0.2053, 20),
    (0.4281, 0.2118, 20),
    (0.3651, 0.2320, 20),
    (0.3070, 0.2521, 20),
    (0.2500, 0.2721, 20),
    (0.1828, 0.2960, 20),
    (0.1442, 0.3923, 30),
    (0.1407, 0.4547, 30),
    (0.1393, 0.4995, 30),
    (0.1390, 0.5533, 30),
    (0.1402, 0.6008, 30),
    (0.1439, 0.6546, 30),
    (0.1535, 0.7106, 30),
    (0.1667, 0.7410, 30),
    (0.1763, 0.7503, 30),
    (0.2002, 0.7548, 30),
    (0.2403, 0.7366, 30),
    (0.6800, 0.3198, 30),
    (0.6759, 0.3173, 30),
    (0.6488, 0.3006, 30),
    (0.6208, 0.2837, 30),
    (0.5863, 0.2637, 30),
    (0.5606, 0.2500, 30),
    (0.5382, 0.2402, 30),
    (0.5168, 0.2358, 30),
    (0.4791, 0.2435, 30),
    (0.4295, 0.2636, 30),
    (0.3905, 0.2807, 30),
    (0.3290, 0.3083, 30),
    (0.2202, 0.3576, 30),
    (0.1769, 0.4360, 40),
    (0.1800, 0.5225, 40),
    (0.1881, 0.6104, 40),
    (0.1958, 0.6562, 40),
    (0.2019, 0.6791, 40),
    (0.2106, 0.6997, 40),
    (0.2314, 0.7173, 40),
    (0.2405, 0.7178, 40),
    (0.2607, 0.7118, 40),
    (0.3023, 0.6839, 40),
    (0.5021, 0.4968, 40),
    (0.6570, 0.3427, 40),
    (0.2151, 0.4588, 50),
    (0.2202, 0.5035, 50),
    (0.2303, 0.5698, 50),
    (0.2392, 0.6119, 50),
    (0.2507, 0.6483, 50),
    (0.2574, 0.6615, 50),
    (0.2660, 0.6720, 50),
    (0.2842, 0.6781, 50),
    (0.2994, 0.6742, 50),
    (0.3244, 0.6595, 50),
    (0.5025, 0.4961, 50),
    (0.6332, 0.3664, 50),
    (0.6296, 0.3635, 50),
    (0.6054, 0.3447, 50),
    (0.5803, 0.3257, 50),
    (0.5600, 0.3111, 50),
    (0.5350, 0.2957, 50),
    (0.5207, 0.2913, 50),
    (0.4996, 0.2960, 50),
    (0.4503, 0.3221, 50),
    (0.4000, 0.3511, 50),
    (0.3587, 0.3751, 50),
    (0.3105, 0.4031, 50),
    (0.2546, 0.4358, 50),
    (0.2576, 0.4662, 60),
    (0.2656, 0.5051, 60),
    (0.2702, 0.5247, 60),
    (0.2806, 0.5633, 60),
    (0.2898, 0.5910, 60),
    (0.3000, 0.6140, 60),
    (0.3192, 0.6345, 60),
    (0.3400, 0.6339, 60),
    (0.3797, 0.6090, 60),
    (0.4252, 0.5692, 60),
    (0.4923, 0.5056, 60),
    (0.5995, 0.3999, 60),
    (0.6065, 0.3871, 60),
    (0.5751, 0.3606, 60),
    (0.5508, 0.3403, 60),
    (0.5252, 0.3217, 60),
    (0.5139, 0.3168, 60),
    (0.5005, 0.3178, 60),
    (0.4761, 0.3301, 60),
    (0.4496, 0.3461, 60),
    (0.4103, 0.3705, 60),
    (0.3375, 0.4161, 60),
    (0.3124, 0.4318, 60),
    (0.2634, 0.4626, 60),
    (0.3038, 0.4616, 70),
    (0.3105, 0.4832, 70),
    (0.3202, 0.5119, 70),
    (0.3255, 0.5258, 70),
    (0.3395, 0.5580, 70),
    (0.3537, 0.5806, 70),
    (0.3810, 0.5916, 70),
    (0.3900, 0.5886, 70),
    (0.3999, 0.5835, 70),
    (0.5005, 0.4967, 70),
    (0.5690, 0.4300, 70),
    (0.5849, 0.4143, 70),
    (0.5812, 0.4106, 70),
    (0.5776, 0.4070, 70),
    (0.5706, 0.4001, 70),
    (0.5351, 0.3661, 70),
    (0.5202, 0.3530, 70),
    (0.5004, 0.3407, 70),
    (0.4904, 0.3412, 70),
    (0.4794, 0.3466, 70),
    (0.4703, 0.3519, 70),
    (0.3706, 0.4174, 70),
    (0.3501, 0.4310, 70),
    (0.3219, 0.4497, 70),
    (0.3527, 0.4480, 80),
    (0.3603, 0.4657, 80),
    (0.3803, 0.5061, 80),
    (0.4100, 0.5440, 80),
    (0.4299, 0.5467, 80),
    (0.4402, 0.5426, 80),
    (0.4598, 0.5298, 80),
    (0.4803, 0.5130, 80),
    (0.5000, 0.4954, 80),
    (0.5218, 0.4750, 80),
    (0.5419, 0.4559, 80),
    (0.5603, 0.4380, 80),
    (0.5566, 0.4338, 80),
    (0.5457, 0.4217, 80),
    (0.5190, 0.3928, 80),
    (0.5004, 0.3744, 80),
    (0.4916, 0.3672, 80),
    (0.4799, 0.3636, 80),
    (0.4751, 0.3652, 80),
    (0.4698, 0.3679, 80),
    (0.4560, 0.3767, 80),
    (0.4011, 0.4146, 80),
    (0.3805, 0.4289, 80),
    (0.3704, 0.4358, 80),
    (0.4016, 0.4288, 90),
    (0.4033, 0.4319, 90),
    (0.4081, 0.4402, 90),
    (0.4158, 0.4531, 90),
    (0.4308, 0.4756, 90),
    (0.4458, 0.4935, 90),
    (0.4552, 0.5011, 90),
    (0.4658, 0.5049, 90),
    (0.4854, 0.4999, 90),
    (0.5081, 0.4842, 90),
    (0.5228, 0.4717, 90),
    (0.5343, 0.4614, 90),
    (0.5304, 0.4565, 90),
    (0.5158, 0.4381, 90),
    (0.4987, 0.4173, 90),
    (0.4827, 0.3990, 90),
    (0.4656, 0.3859, 90),
    (0.4562, 0.3900, 90),
    (0.4420, 0.3999, 90),
    (0.4275, 0.4103, 90),
    (0.4079, 0.4244, 90),
    (0.4024, 0.4283, 90),
    (0.4250, 0.4183, 95),
    (0.4276, 0.4223, 95),
    (0.4351, 0.4339, 95),
    (0.4447, 0.4476, 95),
    (0.4550, 0.4607, 95),
    (0.4660, 0.4728, 95),
    (0.4787, 0.4823, 95),
    (0.4921, 0.4849, 95),
    (0.5032, 0.4816, 95),
    (0.5189, 0.4719, 95),
    (0.5151, 0.4667, 95),
    (0.4901, 0.4334, 95),
    (0.4740, 0.4131, 95),
    (0.4588, 0.3975, 95),
    (0.4504, 0.3999, 95),
    (0.4392, 0.4080, 95),
    (0.4294, 0.4151, 95),
    (0.4254, 0.4180, 95),
    (0.4475, 0.4075, 100))
"""
*CIE Standard Illuminant A* optimal colour stimuli.

A_OPTIMAL_COLOUR_STIMULI : tuple

References
----------
.. [2]  **Wyszecki & Stiles**,
        *Color Science - Concepts and Methods Data and Formulae -
        Second Edition*,
        Wiley Classics Library Edition, published 2000, ISBN-10: 0-471-39918-3,
        pages 776, 777.
"""

C_OPTIMAL_COLOUR_STIMULI = (
    (0.0000, 0.0000, 0),
    (0.1363, 0.0692, 10),
    (0.1308, 0.0792, 10),
    (0.0808, 0.2132, 10),
    (0.0371, 0.4135, 10),
    (0.0251, 0.5007, 10),
    (0.0181, 0.5893, 10),
    (0.0181, 0.6718, 10),
    (0.0276, 0.7416, 10),
    (0.0434, 0.7890, 10),
    (0.0687, 0.8178, 10),
    (0.0996, 0.8252, 10),
    (0.7040, 0.2946, 10),
    (0.5126, 0.1913, 10),
    (0.3424, 0.1028, 10),
    (0.2813, 0.0771, 10),
    (0.2518, 0.0693, 10),
    (0.2378, 0.0674, 10),
    (0.2230, 0.0663, 10),
    (0.1868, 0.0664, 10),
    (0.1628, 0.0676, 10),
    (0.1289, 0.1268, 20),
    (0.1230, 0.1438, 20),
    (0.1027, 0.2152, 20),
    (0.0762, 0.3420, 20),
    (0.0572, 0.4775, 20),
    (0.0500, 0.6250, 20),
    (0.0637, 0.7410, 20),
    (0.0787, 0.7747, 20),
    (0.0992, 0.7975, 20),
    (0.1239, 0.8055, 20),
    (0.1518, 0.7983, 20),
    (0.6717, 0.3273, 20),
    (0.5542, 0.2513, 20),
    (0.4077, 0.1603, 20),
    (0.3463, 0.1263, 20),
    (0.3195, 0.1150, 20),
    (0.3075, 0.1122, 20),
    (0.2968, 0.1104, 20),
    (0.2586, 0.1104, 20),
    (0.1918, 0.1182, 20),
    (0.1302, 0.1764, 30),
    (0.1255, 0.1980, 30),
    (0.1092, 0.2845, 30),
    (0.0909, 0.4178, 30),
    (0.0855, 0.5500, 30),
    (0.0836, 0.6110, 30),
    (0.0911, 0.6700, 30),
    (0.0975, 0.7140, 30),
    (0.1100, 0.7487, 30),
    (0.1294, 0.7700, 30),
    (0.1462, 0.7806, 30),
    (0.1698, 0.7793, 30),
    (0.1957, 0.7696, 30),
    (0.6390, 0.3613, 30),
    (0.5530, 0.2950, 30),
    (0.4300, 0.2040, 30),
    (0.3733, 0.1658, 30),
    (0.3485, 0.1528, 30),
    (0.3300, 0.1462, 30),
    (0.3140, 0.1443, 30),
    (0.3045, 0.1447, 30),
    (0.2643, 0.1503, 30),
    (0.1383, 0.2180, 40),
    (0.1350, 0.2425, 40),
    (0.1246, 0.3363, 40),
    (0.1179, 0.4720, 40),
    (0.1343, 0.6800, 40),
    (0.1596, 0.7377, 40),
    (0.1766, 0.7470, 40),
    (0.1952, 0.7500, 40),
    (0.2437, 0.7305, 40),
    (0.2964, 0.6903, 40),
    (0.3200, 0.6357, 40),
    (0.6065, 0.3925, 40),
    (0.5395, 0.3320, 40),
    (0.4347, 0.2410, 40),
    (0.3833, 0.2000, 40),
    (0.3607, 0.1851, 40),
    (0.3527, 0.1807, 40),
    (0.3453, 0.1777, 40),
    (0.3325, 0.1752, 40),
    (0.3260, 0.1750, 40),
    (0.3003, 0.1783, 40),
    (0.2727, 0.1844, 40),
    (0.2276, 0.1955, 40),
    (0.1510, 0.2520, 50),
    (0.1497, 0.2785, 50),
    (0.1462, 0.3736, 50),
    (0.1490, 0.5017, 50),
    (0.1589, 0.5990, 50),
    (0.1677, 0.6411, 50),
    (0.1782, 0.6750, 50),
    (0.1913, 0.6980, 50),
    (0.2222, 0.7185, 50),
    (0.2867, 0.6936, 50),
    (0.3412, 0.6493, 50),
    (0.4066, 0.5890, 50),
    (0.5759, 0.4231, 50),
    (0.5207, 0.3655, 50),
    (0.4304, 0.2737, 50),
    (0.3844, 0.2309, 50),
    (0.3489, 0.2071, 50),
    (0.3347, 0.2026, 50),
    (0.3175, 0.2046, 50),
    (0.3000, 0.2092, 50),
    (0.2746, 0.2162, 50),
    (0.2024, 0.2373, 50),
    (0.1694, 0.2797, 60),
    (0.1698, 0.3065, 60),
    (0.1732, 0.3995, 60),
    (0.1847, 0.5156, 60),
    (0.2011, 0.5982, 60),
    (0.2117, 0.6316, 60),
    (0.2238, 0.6567, 60),
    (0.2525, 0.6823, 60),
    (0.2694, 0.6840, 60),
    (0.3344, 0.6502, 60),
    (0.3908, 0.6016, 60),
    (0.4605, 0.5364, 60),
    (0.5470, 0.4514, 60),
    (0.5004, 0.3963, 60),
    (0.4217, 0.3042, 60),
    (0.3803, 0.2593, 60),
    (0.3500, 0.2330, 60),
    (0.3376, 0.2284, 60),
    (0.3238, 0.2294, 60),
    (0.3132, 0.2322, 60),
    (0.2593, 0.2497, 60),
    (0.1932, 0.3005, 70),
    (0.1953, 0.3263, 70),
    (0.2064, 0.4136, 70),
    (0.2261, 0.5163, 70),
    (0.2495, 0.5835, 70),
    (0.2733, 0.6282, 70),
    (0.3063, 0.6432, 70),
    (0.3213, 0.6415, 70),
    (0.3408, 0.6316, 70),
    (0.3876, 0.5999, 70),
    (0.5187, 0.4780, 70),
    (0.4795, 0.4243, 70),
    (0.4107, 0.3319, 70),
    (0.3566, 0.2675, 70),
    (0.3460, 0.2578, 70),
    (0.3356, 0.2525, 70),
    (0.3185, 0.2544, 70),
    (0.2875, 0.2651, 70),
    (0.2290, 0.2868, 70),
    (0.2236, 0.3120, 80),
    (0.2282, 0.3382, 80),
    (0.2465, 0.4183, 80),
    (0.2743, 0.5056, 80),
    (0.2991, 0.5591, 80),
    (0.3136, 0.5784, 80),
    (0.3284, 0.5913, 80),
    (0.3570, 0.5932, 80),
    (0.3785, 0.5912, 80),
    (0.4493, 0.5433, 80),
    (0.4901, 0.5038, 80),
    (0.4562, 0.4505, 80),
    (0.3966, 0.3584, 80),
    (0.3631, 0.3103, 80),
    (0.3391, 0.2815, 80),
    (0.3304, 0.2754, 80),
    (0.3229, 0.2756, 80),
    (0.3035, 0.2802, 80),
    (0.2747, 0.2926, 80),
    (0.2276, 0.3119, 80),
    (0.2631, 0.3192, 90),
    (0.2697, 0.3410, 90),
    (0.2956, 0.4111, 90),
    (0.3302, 0.4827, 90),
    (0.3590, 0.5232, 90),
    (0.3742, 0.5364, 90),
    (0.3896, 0.5438, 90),
    (0.4020, 0.5493, 90),
    (0.4221, 0.5430, 90),
    (0.4397, 0.5350, 90),
    (0.4555, 0.5235, 90),
    (0.4295, 0.4741, 90),
    (0.3330, 0.3080, 90),
    (0.3230, 0.2975, 90),
    (0.3180, 0.2958, 90),
    (0.2980, 0.3030, 90),
    (0.2813, 0.3106, 90),
    (0.2857, 0.3185, 95),
    (0.2943, 0.3395, 95),
    (0.3226, 0.4055, 95),
    (0.3608, 0.4679, 95),
    (0.3907, 0.5025, 95),
    (0.4055, 0.5126, 95),
    (0.4209, 0.5180, 95),
    (0.4300, 0.5195, 95),
    (0.4070, 0.4720, 95),
    (0.3630, 0.3855, 95),
    (0.3270, 0.3172, 95),
    (0.3160, 0.3069, 95),
    (0.3053, 0.3096, 95),
    (0.31006, 0.31616, 100))
"""
*CIE Illuminant C* optimal colour stimuli.

C_OPTIMAL_COLOUR_STIMULI : tuple

References
----------
.. [3]  **David MacAdam**,
        *Maximum Visual Efficiency of Colored Materials* JOSA, Vol. 25,
        DOI: http://dx.doi.org/10.1364/JOSA.25.000361,
        pages 361, 367.
"""

D65_OPTIMAL_COLOUR_STIMULI = (
    (0.0000, 0.0000, 0),
    (0.1346, 0.0747, 10),
    (0.0990, 0.1607, 10),
    (0.0751, 0.2403, 10),
    (0.0391, 0.4074, 10),
    (0.0211, 0.5490, 10),
    (0.0177, 0.6693, 10),
    (0.0344, 0.7732, 10),
    (0.0516, 0.8055, 10),
    (0.0727, 0.8223, 10),
    (0.0959, 0.8261, 10),
    (0.1188, 0.8213, 10),
    (0.7035, 0.2965, 10),
    (0.6832, 0.2853, 10),
    (0.6470, 0.2653, 10),
    (0.5517, 0.2132, 10),
    (0.5309, 0.2019, 10),
    (0.4346, 0.1504, 10),
    (0.3999, 0.1324, 10),
    (0.3549, 0.1101, 10),
    (0.3207, 0.0945, 10),
    (0.2989, 0.0857, 10),
    (0.2852, 0.0808, 10),
    (0.2660, 0.0755, 10),
    (0.2186, 0.0707, 10),
    (0.1268, 0.1365, 20),
    (0.1081, 0.1984, 20),
    (0.0894, 0.2766, 20),
    (0.0660, 0.4074, 20),
    (0.0549, 0.4971, 20),
    (0.0479, 0.6227, 20),
    (0.0565, 0.7312, 20),
    (0.0927, 0.8005, 20),
    (0.1289, 0.8078, 20),
    (0.1479, 0.8026, 20),
    (0.1664, 0.7941, 20),
    (0.6708, 0.3289, 20),
    (0.6591, 0.3213, 20),
    (0.5988, 0.2820, 20),
    (0.5514, 0.2513, 20),
    (0.5018, 0.2197, 20),
    (0.4502, 0.1874, 20),
    (0.4045, 0.1601, 20),
    (0.3762, 0.1443, 20),
    (0.3440, 0.1284, 20),
    (0.3185, 0.1196, 20),
    (0.2935, 0.1164, 20),
    (0.2528, 0.1189, 20),
    (0.2205, 0.1229, 20),
    (0.1282, 0.1889, 30),
    (0.1067, 0.3003, 30),
    (0.0990, 0.3535, 30),
    (0.0929, 0.4041, 30),
    (0.0846, 0.5028, 30),
    (0.0819, 0.6020, 30),
    (0.0836, 0.6491, 30),
    (0.1004, 0.7433, 30),
    (0.1481, 0.7857, 30),
    (0.1799, 0.7787, 30),
    (0.2119, 0.7609, 30),
    (0.6368, 0.3628, 30),
    (0.6281, 0.3561, 30),
    (0.5682, 0.3098, 30),
    (0.5271, 0.2784, 30),
    (0.4977, 0.2562, 30),
    (0.4504, 0.2212, 30),
    (0.4219, 0.2008, 30),
    (0.3999, 0.1859, 30),
    (0.3801, 0.1732, 30),
    (0.3491, 0.1574, 30),
    (0.3350, 0.1536, 30),
    (0.3197, 0.1526, 30),
    (0.2021, 0.1732, 30),
    (0.1360, 0.2324, 40),
    (0.1266, 0.3030, 40),
    (0.1219, 0.3504, 40),
    (0.1183, 0.3985, 40),
    (0.1155, 0.4509, 40),
    (0.1141, 0.5055, 40),
    (0.1312, 0.7047, 40),
    (0.1516, 0.7454, 40),
    (0.1853, 0.7587, 40),
    (0.2129, 0.7510, 40),
    (0.2415, 0.7344, 40),
    (0.6041, 0.3954, 40),
    (0.5969, 0.3888, 40),
    (0.5524, 0.3484, 40),
    (0.5257, 0.3244, 40),
    (0.4980, 0.2997, 40),
    (0.4598, 0.2661, 40),
    (0.3696, 0.1949, 40),
    (0.3603, 0.1898, 40),
    (0.3501, 0.1859, 40),
    (0.3375, 0.1841, 40),
    (0.2581, 0.2001, 40),
    (0.2220, 0.2095, 40),
    (0.1771, 0.2214, 40),
    (0.1491, 0.2679, 50),
    (0.1441, 0.3511, 50),
    (0.1429, 0.4025, 50),
    (0.1429, 0.4479, 50),
    (0.1472, 0.5522, 50),
    (0.1548, 0.6201, 50),
    (0.1621, 0.6570, 50),
    (0.1790, 0.7035, 50),
    (0.1929, 0.7201, 50),
    (0.2114, 0.7277, 50),
    (0.2991, 0.6851, 50),
    (0.5731, 0.4262, 50),
    (0.5668, 0.4195, 50),
    (0.5492, 0.4009, 50),
    (0.4795, 0.3281, 50),
    (0.4514, 0.2994, 50),
    (0.4113, 0.2600, 50),
    (0.3897, 0.2401, 50),
    (0.3509, 0.2139, 50),
    (0.3391, 0.2126, 50),
    (0.3211, 0.2155, 50),
    (0.3042, 0.2200, 50),
    (0.2466, 0.2374, 50),
    (0.2041, 0.2507, 50),
    (0.1674, 0.2959, 60),
    (0.1677, 0.3520, 60),
    (0.1700, 0.4130, 60),
    (0.1749, 0.4782, 60),
    (0.1801, 0.5257, 60),
    (0.1873, 0.5730, 60),
    (0.1994, 0.6257, 60),
    (0.2088, 0.6523, 60),
    (0.2506, 0.6927, 60),
    (0.3703, 0.6900, 60),
    (0.2930, 0.6798, 60),
    (0.5435, 0.4552, 60),
    (0.5379, 0.4483, 60),
    (0.4775, 0.3751, 60),
    (0.4522, 0.3450, 60),
    (0.4138, 0.3005, 60),
    (0.3611, 0.2472, 60),
    (0.3497, 0.2405, 60),
    (0.3395, 0.2388, 60),
    (0.3195, 0.2429, 60),
    (0.2963, 0.2505, 60),
    (0.2701, 0.2595, 60),
    (0.2270, 0.2747, 60),
    (0.2037, 0.2830, 60),
    (0.1916, 0.3164, 70),
    (0.1958, 0.3656, 70),
    (0.2003, 0.4069, 70),
    (0.2065, 0.4485, 70),
    (0.2150, 0.4963, 70),
    (0.2221, 0.5295, 70),
    (0.2298, 0.5597, 70),
    (0.2402, 0.5918, 70),
    (0.2550, 0.6237, 70),
    (0.2784, 0.6484, 70),
    (0.3000, 0.6521, 70),
    (0.5148, 0.4825, 70),
    (0.5097, 0.4753, 70),
    (0.4776, 0.4304, 70),
    (0.4508, 0.3933, 70),
    (0.4192, 0.3505, 70),
    (0.4005, 0.3259, 70),
    (0.3706, 0.2890, 70),
    (0.3663, 0.2842, 70),
    (0.3517, 0.2699, 70),
    (0.3364, 0.2634, 70),
    (0.3194, 0.2671, 70),
    (0.3007, 0.2739, 70),
    (0.2664, 0.2872, 70),
    (0.2232, 0.3290, 80),
    (0.2404, 0.4145, 80),
    (0.2496, 0.4504, 80),
    (0.2583, 0.4801, 80),
    (0.2760, 0.5308, 80),
    (0.3023, 0.5809, 80),
    (0.3092, 0.5892, 80),
    (0.3318, 0.6041, 80),
    (0.3515, 0.6048, 80),
    (0.3679, 0.5995, 80),
    (0.4080, 0.5750, 80),
    (0.4858, 0.5081, 80),
    (0.4811, 0.5005, 80),
    (0.4634, 0.4719, 80),
    (0.4514, 0.4526, 80),
    (0.4299, 0.4158, 80),
    (0.4001, 0.3720, 80),
    (0.3732, 0.3319, 80),
    (0.3603, 0.3139, 80),
    (0.3500, 0.3009, 80),
    (0.3307, 0.2866, 80),
    (0.2730, 0.3080, 80),
    (0.2519, 0.3169, 80),
    (0.2400, 0.3219, 80),
    (0.2639, 0.3331, 90),
    (0.2801, 0.3832, 90),
    (0.2864, 0.4008, 90),
    (0.3059, 0.4486, 90),
    (0.3182, 0.4746, 90),
    (0.3317, 0.4994, 90),
    (0.3513, 0.5278, 90),
    (0.3657, 0.5421, 90),
    (0.3946, 0.5537, 90),
    (0.4126, 0.5510, 90),
    (0.4354, 0.5406, 90),
    (0.4530, 0.5293, 90),
    (0.4486, 0.5210, 90),
    (0.4444, 0.5131, 90),
    (0.4325, 0.4906, 90),
    (0.4215, 0.4700, 90),
    (0.3990, 0.4284, 90),
    (0.3749, 0.3849, 90),
    (0.3504, 0.3431, 90),
    (0.3349, 0.3196, 90),
    (0.3217, 0.3084, 90),
    (0.3099, 0.3124, 90),
    (0.2852, 0.3235, 90),
    (0.2711, 0.3299, 90),
    (0.2875, 0.3320, 95),
    (0.2949, 0.3513, 95),
    (0.3067, 0.3800, 95),
    (0.3230, 0.4150, 95),
    (0.3368, 0.4415, 95),
    (0.3508, 0.4654, 95),
    (0.3644, 0.4856, 95),
    (0.3765, 0.5007, 95),
    (0.3887, 0.5126, 95),
    (0.4003, 0.5206, 95),
    (0.4108, 0.5251, 95),
    (0.4281, 0.5268, 95),
    (0.4204, 0.5109, 95),
    (0.4132, 0.4959, 95),
    (0.4031, 0.4751, 95),
    (0.3697, 0.4076, 95),
    (0.3498, 0.3692, 95),
    (0.3401, 0.3513, 95),
    (0.3295, 0.3331, 95),
    (0.3167, 0.3189, 95),
    (0.3148, 0.3195, 95),
    (0.3103, 0.3214, 95),
    (0.3006, 0.3259, 95),
    (0.2900, 0.3308, 95),
    (0.3127, 0.3290, 100))
"""
*CIE Standard Illuminant D Series D65* optimal colour stimuli.

D65_OPTIMAL_COLOUR_STIMULI : tuple

References
----------
.. [4]  **Wyszecki & Stiles**,
        *Color Science - Concepts and Methods Data and Formulae -
        Second Edition*,
        Wiley Classics Library Edition, published 2000, ISBN-10: 0-471-39918-3,
        pages 778, 779.
"""

ILLUMINANTS_OPTIMAL_COLOUR_STIMULI = CaseInsensitiveMapping(
    {'A': A_OPTIMAL_COLOUR_STIMULI,
     'C': C_OPTIMAL_COLOUR_STIMULI,
     'D65': D65_OPTIMAL_COLOUR_STIMULI})
"""
Illuminants optimal colour stimuli.

ILLUMINANTS_OPTIMAL_COLOUR_STIMULI : CaseInsensitiveMapping
    ('A', 'C', 'D65')
"""