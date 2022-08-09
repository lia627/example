graduation, score=map(int, input('졸업학점과 이수 학점을 입력:').split(','))
print(graduation)
print(score)
if graduation>=2 and score>=140:
  print('졸업가능')
elif graduation<2 and score>=140:
  print('졸업 불가능')
elif graduation>=2 and score<140:
  print('졸업 불가능')
else:
  print('졸업 불가능')