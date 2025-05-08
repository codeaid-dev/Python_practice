from choices import advice, prefectures
import choices.sub.subtest as sub

print(f'{prefectures.pick()}へ行きましょう')
print(f'アドバイス: {advice.give()}')

sub.func()