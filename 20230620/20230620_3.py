'''
무지의 먹방 라이브
주어진 food_times 배열을 오름차순으로 정렬합니다. 정렬된 배열에서 가장 작은 값부터 처리
정렬된 food_times 배열을 순회하면서 각 음식을 섭취하는 시간을 모두 빼준다
(빼는 시간은 이전 음식을 섭취하는데 걸린 시간과 현재 음식을 섭취하는데 걸리는 시간의 차이)
k가 현재 음식의 섭취 시간보다 작거나 같으면, 
중단된 시점인 k초가 현재 음식을 섭취해야 하는 시간보다 작거나 같다는 의미
따라서, 현재 음식부터 섭취
k가 현재 음식의 섭취 시간보다 크다면, 현재 음식을 섭취한 후에도 아직 k초 동안 섭취해야 할 음식이 남음
따라서, k를 현재 음식의 섭취 시간만큼 감소시킨 후 다음 음식으로 넘어감
음식을 순회하면서 k가 0보다 작아지거나 모든 음식을 다 섭취한 경우 반복문을 종료
반복문을 모두 순회한 후에도 k가 0보다 크다면, 
음식을 모두 섭취한 후에도 아직 k초 동안 섭취해야 할 음식이 남아있다는 의미
중단된 시점 이후부터 다시 섭취해야 할 첫 번째 음식의 번호를 반환
'''
def solution(food_times, k):
    # 남은 시간이 k보다 작아질 때까지 반복
    for a in range(k):
        # 음식을 순서대로 확인하면서 먹을 수 있는 음식 찾기
        for i in range(len(food_times)):
            # 현재 음식을 먹는 시간이 0보다 크다면 섭취
            if food_times[i] > 0:
                food_times[i] -= 1 # 음식을 먹을 때마다 줄어든다
                # 다음 음식으로 넘어가기
    
    # 남은 음식 중에서 다시 먹을 음식 찾기
    # 즉, 아직 남은 음식 중 다음으로 섭취해야 할 가장 가까운 번호의 음식
    for i in range(len(food_times)):
         if food_times[i] > 0:
                food_times[i] -= 1