#10872
def fac(N):
    result = 1
    if N > 0:
        result = N * fac(N-1)
    return result

N = int(input())
print(fac(N))

#10870
def fib(n):
    if n >= 2:
        return fib(n-1) + fib(n-2)
    else:
        return n

n = int(input())
print(fib(n))

#17478
def chatbot(i, n):
    print("____" * i + '"재귀함수가 뭔가요?"')
    if i == n:
        print("____" * i + '"재귀함수는 자기 자신을 호출하는 함수라네"')
    else:
        print("____" * i + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print("____" * i + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
        print("____" * i + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        chatbot(i+1, n)
    print("____" * i + "라고 답변하였지.")

n = int(input())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
chatbot(0, n)

#11729
def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return
    #가장 아래에 있는 원판 제외하고 나머지를 새끼 문제로 만든다 (재귀)
    hanoi(n-1, start, 6-start-end) #기둥 번호를 계산하기 위해 1+2+3=6에서 뺸다
    print(start, end)
    hanoi(n-1, 6-start-end, end)

N = int(input())
print(2**N - 1) #총 움직임
hanoi(N, 1, 3)
