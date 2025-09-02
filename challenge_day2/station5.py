def solution_station_5():
    learning_teams = {
        "LT1": [
            "Daeho", "David", "Kaisa", "Oliver", "Sara", "Dan", "Ivar", "Lotte", "Riya", "Vassil",
            "Twan", "Ester", "Karolina", "Lena", "Margarita", "Anna", "Kien", "Klaudia", "Maliah", "Todd"
        ],
        "LT2": [
            "Oumaima", "Mathilde", "Marie", "Anita", "Ziyan", "Bernardo", "Eleanor", "Lorijn", "Maria",
            "Younes", "Yvan", "Henning", "Liangyu", "Maciej", "Toprak", "Chris", "GengXin", "Mingze", "Phoebe"
        ],
        "LT3": [
            "Betija", "Haider", "Kacper", "Sophie", "Amir", "Baltasar", "Isar", "Jelle", "Nicolas", "David",
            "Ipek", "Juan", "Marfa", "Maria", "Alissa", "Leopoldo", "Mies", "Jiaying", "Kaixin", "Mai", "Sem", "Tibbe"
        ],
        "LT4": [
            "Justus", "Julia", "Philip", "Uli", "Vanessa", "Anna", "Ekaterina", "Thessa", "Tongfei", "Yang",
            "Benedikt", "Jan", "Nadee", "Osjah", "Tim", "Eliana", "Joana", "Peilin", "Pija", "Wenhao"
        ],
        "LT5": [
            "Afua", "Cristina", "Greta", "Jace", "Laura", "Anna", "Bassant", "Ivan", "Juriaan", "Kiavash"
        ],
        "LT6": [
            "Keitaro", "Nohemi", "Norina", "Yifan", "Yinan", "Luo", "Nikola", "Olesya", "Sophie", "Tom"
        ]
    }


    name_to_team = {}
    for team, members in learning_teams.items():
        for person in members:
            if person in name_to_team:
                if isinstance(name_to_team[person], list):
                    name_to_team[person].append(team)
                else:
                    name_to_team[person] = [name_to_team[person], team]
            else:
                name_to_team[person] = team


    def find_learning_team(name: str):
        if name in name_to_team:
            return f"{name} belongs to {name_to_team[name]}"
        else:
            return f"{name} is not in any learning team."


    print(find_learning_team("Betija"))
    print(find_learning_team("Anna"))
    print(find_learning_team("Tom"))
    print(find_learning_team("Unknown"))
