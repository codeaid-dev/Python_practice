def func(hp, status="正常", action="移動", job="戦士"):
    print("キャラクターの行動は", action, "です。")
    print("現在の体力は", hp, "なので、", action, "できるか確認ください。")
    print("職業は、", job)
    print("状態は、", status)

func(1000)
print("-" * 5)
func("少し")
print("-" * 5)
func(hp=1000)
print("-" * 5)
func(hp=10000, action='回復')
print("-" * 5)
func(action="休憩", hp=999)
print("-" * 5)
func("満タン", "強化", "戦闘")
print("-" * 5)
func("半分", status="弱体")

#func() # 引数hpは必須となるのでエラーとなる。
#func(99, hp=100) # 第１引数が引数hpとなるのでエラーとなる。
#func(hp=10, '戦闘不能') # 
