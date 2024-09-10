from spheric import ball,circle

r = int(input('半径 >>'))
b_area = ball.area(r)
c_area = circle.area(r)
print(f'半径{r}cmの球の表面積は{b_area:.2f}平方cm、円の面積は{c_area:.2f}平方cm')