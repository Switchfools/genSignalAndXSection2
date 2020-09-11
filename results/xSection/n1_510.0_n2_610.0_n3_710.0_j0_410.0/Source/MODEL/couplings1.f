ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      SUBROUTINE COUP1()

      IMPLICIT NONE
      INCLUDE 'model_functions.inc'

      DOUBLE PRECISION PI, ZERO
      PARAMETER  (PI=3.141592653589793D0)
      PARAMETER  (ZERO=0D0)
      INCLUDE 'input.inc'
      INCLUDE 'coupl.inc'
      GC_1 = -(MDL_EE*MDL_COMPLEXI)/3.000000D+00
      GC_2 = (2.000000D+00*MDL_EE*MDL_COMPLEXI)/3.000000D+00
      GC_3 = -(MDL_EE*MDL_COMPLEXI)
      GC_4 = MDL_EE*MDL_COMPLEXI
      GC_26 = (MDL_EE*MDL_COMPLEXI)/(MDL_SW*MDL_SQRT__2)
      GC_27 = -(MDL_CW*MDL_EE*MDL_COMPLEXI)/(2.000000D+00*MDL_SW)
      GC_28 = (MDL_CW*MDL_EE*MDL_COMPLEXI)/(2.000000D+00*MDL_SW)
      GC_30 = (MDL_CW*MDL_EE*MDL_COMPLEXI)/MDL_SW
      GC_35 = -(MDL_EE*MDL_COMPLEXI*MDL_SW)/(6.000000D+00*MDL_CW)
      GC_37 = (MDL_EE*MDL_COMPLEXI*MDL_SW)/MDL_CW
      GC_39 = -(MDL_CW*MDL_EE*MDL_COMPLEXI)/(2.000000D+00*MDL_SW)
     $ +(MDL_EE*MDL_COMPLEXI*MDL_SW)/(2.000000D+00*MDL_CW)
      GC_40 = (MDL_CW*MDL_EE*MDL_COMPLEXI)/(2.000000D+00*MDL_SW)
     $ +(MDL_EE*MDL_COMPLEXI*MDL_SW)/(2.000000D+00*MDL_CW)
      GC_80 = MDL_EE__EXP__2*MDL_COMPLEXI*MDL_VEV+(MDL_CW__EXP__2
     $ *MDL_EE__EXP__2*MDL_COMPLEXI*MDL_VEV)/(2.000000D+00
     $ *MDL_SW__EXP__2)+(MDL_EE__EXP__2*MDL_COMPLEXI*MDL_SW__EXP__2
     $ *MDL_VEV)/(2.000000D+00*MDL_CW__EXP__2)
      GC_107 = -((MDL_EE*MDL_COMPLEXI*MDL_VN1N1)/(MDL_CW*MDL_SW))
      GC_109 = -((MDL_EE*MDL_COMPLEXI*MDL_VN1N2)/(MDL_CW*MDL_SW))
      GC_111 = -((MDL_EE*MDL_COMPLEXI*MDL_VN1N3)/(MDL_CW*MDL_SW))
      GC_113 = -((MDL_EE*MDL_COMPLEXI*MDL_VN2N2)/(MDL_CW*MDL_SW))
      GC_115 = -((MDL_EE*MDL_COMPLEXI*MDL_VN2N3)/(MDL_CW*MDL_SW))
      GC_117 = -((MDL_EE*MDL_COMPLEXI*MDL_VN3N3)/(MDL_CW*MDL_SW))
      GC_119 = (MDL_EE*MDL_COMPLEXI*MDL_VTAN1)/(MDL_SW*MDL_SQRT__2)
      GC_120 = (MDL_EE*MDL_COMPLEXI*MDL_VTAN1)/(2.000000D+00*MDL_CW
     $ *MDL_SW)
      GC_122 = -(MDL_EE*MDL_COMPLEXI*MDL_MN1*MDL_VTAN1)/(2.000000D+00
     $ *MDL_MW*MDL_SW)
      GC_126 = (MDL_EE*MDL_COMPLEXI*MDL_VTAN2)/(MDL_SW*MDL_SQRT__2)
      GC_127 = (MDL_EE*MDL_COMPLEXI*MDL_VTAN2)/(2.000000D+00*MDL_CW
     $ *MDL_SW)
      GC_129 = -(MDL_EE*MDL_COMPLEXI*MDL_MN2*MDL_VTAN2)/(2.000000D+00
     $ *MDL_MW*MDL_SW)
      END