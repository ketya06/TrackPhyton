
def count_letters(text):

    letters_count = {}
    text_lower = text.lower()
    for char in text_lower:
        if char.isalpha():
            if char in letters_count:
                letters_count[char] += 1
            else:
                letters_count[char] = 1

    return letters_count

def calculate_frequency(letters_dict):

    total_letters = sum(letters_dict.values())
    frequency_dict = {}
    for letter, count in letters_dict.items():
        frequency = count / total_letters
        frequency_dict[letter] = frequency
    return frequency_dict



def get_letter_order(text):

    text_lower = text.lower()
    order = []
    seen = set()

    for char in text_lower:
        if char.isalpha() and char not in seen:
            seen.add(char)
            order.append(char)

    return order


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""


letters_count = count_letters(main_str)
frequency_dict = calculate_frequency(letters_count)
letter_order = get_letter_order(main_str)

for letter in letter_order:
    frequency = frequency_dict.get(letter, 0)
    print(f"{letter}: {frequency:.2f}")