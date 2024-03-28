'''
문제 설명
정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

제한사항
arr은 길이 1 이상, 100 이하인 배열입니다.
arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.
입출력 예
arr	return
[1,2,3,4]	2.5
[5,5]	5
'''



def solution(arr):
    answer = 0
    if 1<= len(arr) <= 100:                     #제한1
        for i in arr: 
            if -10000<=i<=10000:                #제한2
                answer = sum(arr) / len(arr)    #평균값 구하기
                return answer
