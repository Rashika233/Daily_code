eng_num = int(raw_input())
eng_set = set(map(int, raw_input().split()))
fren_num = int(raw_input())
fren_set = set(map(int, raw_input().split()))

print len(eng_set.difference(fren_set))