#-*- coding: utf-8 -*-

# 
if __name__ == "__main__":
  N = int(input())
  conditions = [list(map(int, input().split())) for i in range(N)]
  M = int(input())
  mentaikos  = [list(map(int, input().split())) for i in range(M)]
  purchased = [0 for i in range(M)]
  kiseki    = [0] # 奇跡の明太子
  max_purchased_num = 0
  # 奇跡の明太子を調べる
  for i in range(M):
    # 奇跡の明太子と同じならスキップ
    is_skip = False
    for k in kiseki:
      if k == 0:
        break
      if mentaikos[i] == mentaikos[k-1]:
        kiseki.append(i+1)
        is_skip = True
        break
    if is_skip:
      continue
    
    # 値段と辛さを走査する
    for j in range(N):
      if mentaikos[i][0] > conditions[j][0]:
        # 値段高いなら
        continue
      if mentaikos[i][1] < conditions[j][1]:
        # 辛くないなら
        continue
      purchased[i] += 1
    if purchased[i] > max_purchased_num:
      max_purchased_num = purchased[i]
      kiseki = []
      kiseki.append(i+1)
    elif purchased[i] == max_purchased_num and max_purchased_num != 0:
      kiseki.append(i+1)
  # 出力
  for i in kiseki:
    print(i)
