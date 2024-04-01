'''
문제 설명
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

제한 조건
n은 10,000,000,000이하인 자연수입니다.
입출력 예
n	return
12345	[5,4,3,2,1]
'''



def solution(n):
    answer = []
    #제한
    if 0<=n<=10000000000:
        #숫자 n을 문자열로 변환한 것을 뒤집어 list로 만든 값을 새로운 문자열 변주인 str_n에 대입
        str_n=list(reversed(str(n)))
        #str_n에 있는 정수들을 []배열 형식으로 바꿔 answer에 저장
        answer = [int(x) for x in str_n]
    return answer
