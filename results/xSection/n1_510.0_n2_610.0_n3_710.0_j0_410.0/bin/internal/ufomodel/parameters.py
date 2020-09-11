# This file was automatically created by FeynRules 2.3.36
# Mathematica version: 12.0.0 for Mac OS X x86 (64-bit) (April 7, 2019)
# Date: Thu 14 May 2020 17:54:24



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
VeN1 = Parameter(name = 'VeN1',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'V_{\\text{eN1}}',
                 lhablock = 'NUMIXING',
                 lhacode = [ 1 ])

VeN2 = Parameter(name = 'VeN2',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = 'V_{\\text{eN2}}',
                 lhablock = 'NUMIXING',
                 lhacode = [ 2 ])

VeN3 = Parameter(name = 'VeN3',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = 'V_{\\text{eN3}}',
                 lhablock = 'NUMIXING',
                 lhacode = [ 3 ])

VmuN1 = Parameter(name = 'VmuN1',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'V_{\\text{muN1}}',
                  lhablock = 'NUMIXING',
                  lhacode = [ 4 ])

VmuN2 = Parameter(name = 'VmuN2',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'V_{\\text{muN2}}',
                  lhablock = 'NUMIXING',
                  lhacode = [ 5 ])

VmuN3 = Parameter(name = 'VmuN3',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'V_{\\text{muN3}}',
                  lhablock = 'NUMIXING',
                  lhacode = [ 6 ])

VtaN1 = Parameter(name = 'VtaN1',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'V_{\\text{taN1}}',
                  lhablock = 'NUMIXING',
                  lhacode = [ 7 ])

VtaN2 = Parameter(name = 'VtaN2',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'V_{\\text{taN2}}',
                  lhablock = 'NUMIXING',
                  lhacode = [ 8 ])

VtaN3 = Parameter(name = 'VtaN3',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'V_{\\text{taN3}}',
                  lhablock = 'NUMIXING',
                  lhacode = [ 9 ])

VN1N1 = Parameter(name = 'VN1N1',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'V_{\\text{N1N1}}',
                  lhablock = 'NUMIXING',
                  lhacode = [ 10 ])

VN1N2 = Parameter(name = 'VN1N2',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'V_{\\text{N1N2}}',
                  lhablock = 'NUMIXING',
                  lhacode = [ 11 ])

VN1N3 = Parameter(name = 'VN1N3',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'V_{\\text{N1N3}}',
                  lhablock = 'NUMIXING',
                  lhacode = [ 12 ])

VN2N2 = Parameter(name = 'VN2N2',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'V_{\\text{N2N2}}',
                  lhablock = 'NUMIXING',
                  lhacode = [ 13 ])

VN2N3 = Parameter(name = 'VN2N3',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'V_{\\text{N2N3}}',
                  lhablock = 'NUMIXING',
                  lhacode = [ 14 ])

VN3N3 = Parameter(name = 'VN3N3',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'V_{\\text{N3N3}}',
                  lhablock = 'NUMIXING',
                  lhacode = [ 15 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

vevf = Parameter(name = 'vevf',
                 nature = 'external',
                 type = 'real',
                 value = 50,
                 texname = '\\text{vevf}',
                 lhablock = 'FRBlock',
                 lhacode = [ 1 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

mN1 = Parameter(name = 'mN1',
                nature = 'external',
                type = 'real',
                value = 300.,
                texname = '\\text{mN1}',
                lhablock = 'MASS',
                lhacode = [ 9900012 ])

mN2 = Parameter(name = 'mN2',
                nature = 'external',
                type = 'real',
                value = 500.,
                texname = '\\text{mN2}',
                lhablock = 'MASS',
                lhacode = [ 9900014 ])

mN3 = Parameter(name = 'mN3',
                nature = 'external',
                type = 'real',
                value = 1000.,
                texname = '\\text{mN3}',
                lhablock = 'MASS',
                lhacode = [ 9900016 ])

MJ = Parameter(name = 'MJ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MJ}',
               lhablock = 'MASS',
               lhacode = [ 9900018 ])

MAx = Parameter(name = 'MAx',
                nature = 'external',
                type = 'real',
                value = 173.048,
                texname = '\\text{MAx}',
                lhablock = 'MASS',
                lhacode = [ 9900020 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WN1 = Parameter(name = 'WN1',
                nature = 'external',
                type = 'real',
                value = 0.303,
                texname = '\\text{WN1}',
                lhablock = 'DECAY',
                lhacode = [ 9900012 ])

WN2 = Parameter(name = 'WN2',
                nature = 'external',
                type = 'real',
                value = 1.5,
                texname = '\\text{WN2}',
                lhablock = 'DECAY',
                lhacode = [ 9900014 ])

WN3 = Parameter(name = 'WN3',
                nature = 'external',
                type = 'real',
                value = 12.3,
                texname = '\\text{WN3}',
                lhablock = 'DECAY',
                lhacode = [ 9900016 ])

WJ = Parameter(name = 'WJ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WJ}',
               lhablock = 'DECAY',
               lhacode = [ 9900018 ])

WAx = Parameter(name = 'WAx',
                nature = 'external',
                type = 'real',
                value = 0.00417,
                texname = '\\text{WAx}',
                lhablock = 'DECAY',
                lhacode = [ 9900020 ])

muJ = Parameter(name = 'muJ',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(vevf**2)',
                texname = '\\mu _J')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

lamJ = Parameter(name = 'lamJ',
                 nature = 'internal',
                 type = 'real',
                 value = '(MJ**2 + muJ**2)/vevf**2',
                 texname = '\\lambda _J')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gN = Parameter(name = 'gN',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_N')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

I2a33 = Parameter(name = 'I2a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I2a33}')

I3a33 = Parameter(name = 'I3a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I3a33}')

