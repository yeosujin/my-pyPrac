'''
문제 설명
정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.

제한사항
0 < n ≤ 1000

입출력 예
n	result
10	30
4	6
입출력 예 설명
입출력 예 #1

n이 10이므로 2 + 4 + 6 + 8 + 10 = 30을 return 합니다.
입출력 예 #2

n이 4이므로 2 + 4 = 6을 return 합니다.
'''



def solution(n):
    answer = 0
    #제한
    if 0<n<=1000:
        #n+1까지 순서대로 숫자 i
        for i in range(n+1):
            #i를 2로 나눈 값이 그 값을 정수화한 값고 동일할 때 즉, 짝수일 때
            if i/2==int(i/2):
                #answeer에 i를 더해준다
                answer += i
            #i가 홀수일 때
            else:
                #반복문으로 돌아간다
                continue
    return answer
