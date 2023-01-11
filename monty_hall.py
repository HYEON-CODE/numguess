from random import shuffle, choice

# 문을 바꿨을 때와 안 바꿨을 때 카운트 변수 생성
stay=0
switch=0
# 시뮬레이션 횟수 변수
simulation_count = 10000
# 시뮬레이션 반복문 작성
for i in range(simulation_count):
    # 리스트로 문 생성 염소는 0 스포츠카는 1
    doors = [0,0,1]
    shuffle(doors)
    # 나의 선택 결과를 리스트에서 pop
    user_choice = doors.pop()
    doors.remove(0) # 남은 문 하나에서 염소를 보여줌
    if user_choice == 1: # 문을 바꾸지 않았다면 stay + 1
        stay += 1
    else:
        switch += 1 # 문을 바꿨다면 switch + 1
