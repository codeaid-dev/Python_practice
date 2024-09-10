import ball

r = int(input('半径 >>'))
volume = ball.volume(r)
area = ball.area(r)
print(f'半径{r}cmの球の体積は{volume:.2f}立方cm、表面積は{area:.2f}平方cm')