# 단순화 제거 레이어
# 우리가 복원하고자 하는 데이터(그림)는 사진에서 특정 부분을 그리는 대상(화가) 가 단순화하여 표현하였다고 가정하자.
# 이 상태에서 원본사진으로 복원하기 위해서 단순화된 영역을 찾아내고, 이를 일반적인 사물을 담은 사진의 영역과 비교하여 훈련된 단순화-일반화 필터를 적용한다.
#
# *** 단순화-일반화 필터 ***
# 색상은 고려하지않는다.
# 이 필터는 아마도 supervised mode로 학습시켜야 할 것이다.


# state 1
# 단순화 처리된 이미지 (A)
# 미리학습된 단순화-일반화 필터 ( Simplication-to-Generalization Filter , F )
# 단순화된 영역을 스캔해주는 모듈 ( Simplification Scanner , S )
#
# 이 단계에서는 단순화 처리된 이미지에서 단순화 된 영역을 검색한다


# state 2
# 단순화 된 영역이 표시된 이미지 ( S(A) )
#
# 이 단계에서는 단순화 된 영역에 단순화-일반화 필터를 적용하여 단순화 된 영역을 일반화 시켜준다.


# state 3
# 단순화 된 영역을 일반화시킨 이미지 ( F(S(A)) )
#
# 앞서 처리한 두 단계를 통과하여 생성된 이미지와
# 원본 물체의 사진이 갖는 색의 분포와 그림에서 갖는 색의 분포를 사용한 GAN에서 얻은 필터값( Color filter , C )을 적용한다.

# final state
# 1.색상의 분포 -- 원본 물체와 유사
# 2.이미지의 형상 -- 원본 물체와 유사
# 위 2가지의 특성을 갖는 이미지 ( C(F(S(A))) )  를 얻는다.

# 생성된 이미지는 원본사진과 유사하다고 할 수 있는가?



if __name__ == "_main_":
    print("hi")