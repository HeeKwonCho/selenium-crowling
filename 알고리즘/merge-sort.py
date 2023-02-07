def merge_sort(a):
    def sort(unsorted_list): # 리스트 입력받기
        if len(unsorted_list) <= 1: # 리스트길이가 1보다 작거나 같으면 리턴
            return
       
        mid = len(unsorted_list) // 2 # 리스트 2분할
        left = unsorted_list[:mid]
        right = unsorted_list[mid:]
        merge_sort(left)             # 분리한 두개의 리스트를 merge_sort의 인자로 전달
        merge_sort(right)
        merge(left, right)
        
    def merge(left, right): # 병합정렬
        i = 0
        j = 0
        k = 0
        while (i < len(left)) and (j < len(right)): # merge_sort를 하는과정
            if left[i] < right[j]: # left, right 길이 안에서 각각 0번째 자리부터
                a[k] = left[i]     # 비교하고 작은 값을 sorted_listed에 집어넣는 작업
                i += 1
                k += 1
            else:
                a[k] = right[j]
                j += 1
                k += 1
        # 남은 데이터 삽입
        while i < len(left):
            a[k] = left[i]
            i += 1
            k+= 1
        while j < len(right):
            a[k] = right[j]
            j += 1
            k+= 1
        print(a)
    sort(a)

    # 배열 입력할때 array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
    # merge_sort(array)