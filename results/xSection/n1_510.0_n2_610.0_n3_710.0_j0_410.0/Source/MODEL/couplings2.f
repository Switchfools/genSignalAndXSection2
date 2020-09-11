ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      SUBROUTINE COUP2()

      IMPLICIT NONE
      INCLUDE 'model_functions.inc'

      DOUBLE PRECISION PI, ZERO
      PARAMETER  (PI=3.141592653589793D0)
      PARAMETER  (ZERO=0D0)
      INCLUDE 'input.inc'
      INCLUDE 'coupl.inc'
      GC_133 = (MDL_EE*MDL_COMPLEXI*MDL_VTAN3)/(MDL_SW*MDL_SQRT__2)
      GC_134 = (MDL_EE*MDL_COMPLEXI*MDL_VTAN3)/(2.000000D+00*MDL_CW
     $ *MDL_SW)
      GC_136 = -(MDL_EE*MDL_COMPLEXI*MDL_MN3*MDL_VTAN3)/(2.000000D+00
     $ *MDL_MW*MDL_SW)
      GC_81 = MDL_MN1/MDL_VEVF
      GC_82 = MDL_MN2/MDL_VEVF
      GC_83 = MDL_MN3/MDL_VEVF
      END
