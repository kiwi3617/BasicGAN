# BasicGAN
GAN basic
1. GAN 구현 ( 가장 기초적인 형태 )

 * image preprecessing  == matplot,numpy,scipy 같은 모듈 사용
 - image resize 
 - (edge detection)
 - 폴더 내부의 이미지 *.jpg 읽어들여서 변환 ( 다중 이미지 처리 )
 
 * discriminator == tensorflow
 * generator	 == tensorflow
  
 * tangenth ==
 
 = mode collapse problem



Idea 1
 사과 사진

1 . X -> 흑백 사진

    사과 사진-> 흑백 사과 사진 -> 학습

2. 흑백 사진 -> 빨간 사과색 

  사과 사진 , 흑백 사과 사진 -> 학습
  생성된 흑백 사과 사진 -> 색칠

5/22
- preprocess ( line 5 )
- image resize ( line 6 )
- 폴더 내부의 이미지 *.jpeg 읽어들여서 변환 ( line 8 )
