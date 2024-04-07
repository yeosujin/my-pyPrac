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


#1
def solution(arr):
    
    if 1<= len(arr) <= 100:                     #제한1
        for i in arr: 
            if -10000<=i<=10000:                #제한2
                answer = sum(arr) / len(arr)    #평균값 구하기
                return answer


#2
def solution(arr):
    answer = 0
    #제한1
    if 1<= len(arr) <= 100:
        #arr의 갯수만큼 반복
        for i in range(len(arr)): 
            #제한2
            if -10000<=i<=10000:
                #arr배열의 수를 answer에 넣기
                answer += arr[i]
        #arr의 값들이 다 더해진 answer를 arr의 길이만큼 나누어 평균 계산
        answer = answer / len(arr)
        return answer
