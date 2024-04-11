'''
문제 설명
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

재한사항
s는 길이가 1 이상, 100이하인 스트링입니다.
입출력 예
s	return
"abcde"	"c"
"qwer"	"we"
'''



def solution(s):
    #제한
    if 1<=len(s)<=100:
        #s의 길이가 홀수일 때
        if len(s) % 2 == 1:
            #중간값 return
            return s[len(s)//2]
        #s의 길이가 짝수일 때
        else :
            #중간 두 자리 return
            return s[len(s)//2-1:len(s)//2+1]
            
