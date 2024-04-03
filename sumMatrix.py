'''
문제 설명
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

제한 조건
행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.
입출력 예
arr1	arr2	return
[[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
[[1],[2]]	[[3],[4]]	[[4],[6]]
'''



def solution(arr1, arr2):
    answer = []
    #제한
    if len(arr1)<=500 and len(arr2)<=500:
        #arr1과 arr2의 각 값을 더하는 zip()사용
        for a, b in zip(arr1, arr2):
            #결과를 담을 리스트 초기화
            sum = []
            #각 입력값을 같은 위치릐 값끼리 더하여 리스트 sum에 추가
            for i, j in zip(a, b):
                sum.append(i + j)
            #추가된 값의 리스트 sum을 answer리스트로 정렬
            answer.append(sum)
    return answer
