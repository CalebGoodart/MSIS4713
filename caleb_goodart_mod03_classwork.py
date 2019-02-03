list_one = [-423, 'Eye', 'sigh', 'Profession', 'Go', 'occupy', -51, 21, -345, 74, 'undertake', 'tiptoe', 11, -475,
            'swipe', 'Burial', 280, 343, 218, 'general']
list_two = ['Conductor', -494, 'Difficulty', -234, -325, -466, 'loot', 457, 'blast', 'equal', -387, 'Bless', 'Candle',
            'extinct', 495, 'Restless', 220, 'extinct', 'copyright', 'Bend']
list_three = ['Inject', 407, 'bless', 39, 'identification', -6, 'Adult', 172, 'difficulty', -279, 'Censorship', 163,
              'tiptoe', 407, 'Inject', 59, 'Eye', 19, 'Candle', 193]
list_of_lists = [['forest', 'Hypothesize', 135], [495, 'foreigner', 'Eye'], [141, 301, 'hope'],
                 [383, 'Adult', 'difficulty'], [-403, 'General', 'Fixture'], ['Clock', 'management']]

new_list = []
i = 0

for i in range(len(list_one)):
    new_list.append(list_one[i])
    new_list.append(list_two[i])
    i += 1
print(new_list)

odd_list = []
even_list = []

for j in range(0, len(list_three), 2):
    odd_list.append(list_three[j])
    even_list.append(list_three[j + 1])
print(odd_list)
print(even_list)

int_list = []

for k in range(len(list_one)):
    try:
        int_list.append(int(list_one[k]))
    except ValueError:
        continue
print(int_list)

items_of_all_list = []

for l in range(len(list_of_lists)):
    for m in range(len(list_of_lists[l])):
        items_of_all_list.append(list_of_lists[l][m])
print(items_of_all_list)

