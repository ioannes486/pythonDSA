def counting_sort(arr,k):
    cnt = [0] * (k+1)
    temp = [0] * len(arr)

    # 카운팅 배열 만들기
    for i in range(len(arr)):
        cnt[arr[i]] += 1
    # 카운팅 배열을 누적배열로 바꾸기
    for i in range(1, len(arr)+1):
        cnt[i] += cnt[i-1]

    #자리 찾기
    for i in range(len(arr)-1,-1,-1): # 원본 배열의 길이가 7일 경우 : i = 6 to -1
        cnt[arr[i]] -= 1
        temp[cnt[arr[i]]] = arr[i]

    return temp

