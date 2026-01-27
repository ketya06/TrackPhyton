def find_common_participants(group1, group2, separator=","):
    participants1 = group1.split(separator)
    participants2 = group2.split(separator)

    common_participants = list(set(participants1) & set(participants2))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common = find_common_participants(participants_first_group, participants_second_group, "|")
print(f"Общие участники: {common}")


group1_comma = "Иванов,Петров,Сидоров"
group2_comma = "Петров,Сидоров,Смирнов"

common_comma = find_common_participants(group1_comma, group2_comma)
print(f"Общие участники (с запятой): {common_comma}")


