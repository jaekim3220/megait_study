20230613_2.py(문제)의 개요와 풀이\
----------------------
곱하기 혹은 더하기\
각 자리가 숫자(0~9)로만 이루어진 문자열 S가 주어졌을 때,
왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에\
* 혹은 + 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성
이때 연산은 +보다 *를 우선 계산하는 일반적인 계산 방식이 아닌\
모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정\
----------------------
예를 들어 02984라는 문자열이 주어질 경우 만들어질 수 있는 가장 큰 수는\
((((0 + 2) * 9) * 8) * 4 ) = 576이다\
또한 가장 큰 수는 항상 20억 이하의 정수가 되도록 입력이 주어진다.