C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     (Gamma5(-1,1)*Gamma(3,2,-1)) * C(51,2) * C(52,1)
C     
      SUBROUTINE FFV2C1_2(F2, V3, COUP, M1, W1,F1)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 F2(*)
      COMPLEX*16 V3(*)
      REAL*8 P1(0:3)
      REAL*8 M1
      REAL*8 W1
      COMPLEX*16 F1(6)
      COMPLEX*16 DENOM
      COMPLEX*16 COUP
      F1(1) = +F2(1)+V3(1)
      F1(2) = +F2(2)+V3(2)
      P1(0) = -DBLE(F1(1))
      P1(1) = -DBLE(F1(2))
      P1(2) = -DIMAG(F1(2))
      P1(3) = -DIMAG(F1(1))
      DENOM = COUP/(P1(0)**2-P1(1)**2-P1(2)**2-P1(3)**2 - M1 * (M1 -CI
     $ * W1))
      F1(3)= DENOM*CI*(F2(3)*(P1(0)*(-1D0)*(V3(3)+V3(6))+(P1(1)*(V3(4)
     $ +CI*(V3(5)))+(P1(2)*(V3(5)-CI*(V3(4)))+P1(3)*(V3(3)+V3(6)))))
     $ +(F2(4)*(P1(0)*(+CI*(V3(5))-V3(4))+(P1(1)*(V3(3)-V3(6))+(P1(2)
     $ *(-CI*(V3(3))+CI*(V3(6)))+P1(3)*(V3(4)-CI*(V3(5))))))+M1*(F2(5)
     $ *(V3(3)-V3(6))+F2(6)*(+CI*(V3(5))-V3(4)))))
      F1(4)= DENOM*(-CI)*(F2(3)*(P1(0)*(V3(4)+CI*(V3(5)))+(P1(1)*(-1D0)
     $ *(V3(3)+V3(6))+(P1(2)*(-1D0)*(+CI*(V3(3)+V3(6)))+P1(3)*(V3(4)
     $ +CI*(V3(5))))))+(F2(4)*(P1(0)*(V3(3)-V3(6))+(P1(1)*(+CI*(V3(5))
     $ -V3(4))+(P1(2)*(-1D0)*(V3(5)+CI*(V3(4)))+P1(3)*(V3(3)-V3(6)))))
     $ +M1*(F2(5)*(V3(4)+CI*(V3(5)))-F2(6)*(V3(3)+V3(6)))))
      F1(5)= DENOM*CI*(F2(5)*(P1(0)*(V3(3)-V3(6))+(P1(1)*(-1D0)*(V3(4)
     $ +CI*(V3(5)))+(P1(2)*(+CI*(V3(4))-V3(5))+P1(3)*(V3(3)-V3(6)))))
     $ +(F2(6)*(P1(0)*(+CI*(V3(5))-V3(4))+(P1(1)*(V3(3)+V3(6))+(P1(2)
     $ *(-1D0)*(+CI*(V3(3)+V3(6)))+P1(3)*(+CI*(V3(5))-V3(4)))))+M1
     $ *(F2(3)*(-1D0)*(V3(3)+V3(6))+F2(4)*(+CI*(V3(5))-V3(4)))))
      F1(6)= DENOM*(-CI)*(F2(5)*(P1(0)*(V3(4)+CI*(V3(5)))+(P1(1)*(V3(6)
     $ -V3(3))+(P1(2)*(-CI*(V3(3))+CI*(V3(6)))-P1(3)*(V3(4)+CI*(V3(5)))
     $ )))+(F2(6)*(P1(0)*(-1D0)*(V3(3)+V3(6))+(P1(1)*(V3(4)-CI*(V3(5)))
     $ +(P1(2)*(V3(5)+CI*(V3(4)))+P1(3)*(V3(3)+V3(6)))))+M1*(F2(3)
     $ *(V3(4)+CI*(V3(5)))+F2(4)*(V3(3)-V3(6)))))
      END


