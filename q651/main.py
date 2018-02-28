#-*- coding:utf-8 -*-

if __name__ == "__main__":
  # 時速100km = 分速(100/60)km
  v = 100/60
  now_h = 10
  now_m = 0
  a = int(input())
  # 着くのに何時間何分かかるの？
  ellapsed_h = 0
  ellapsed_m = a/v  # 経過分
  while 1:
    if ellapsed_m >= 60:
      ellapsed_m -= 60
      ellapsed_h += 1
      continue
    break
  # 結局何時に着くの？
  arrived_h = now_h + ellapsed_h
  arrived_m = now_m + ellapsed_m
  while 1:
    if arrived_h >= 24:
      arrived_h -= 24
      continue
    break
  print("{0:02d}:{1:02d}".format(int(arrived_h), int(arrived_m)))
