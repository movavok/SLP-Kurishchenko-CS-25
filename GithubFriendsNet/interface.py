import networkx as nx
import matplotlib.pyplot as plt

def handleUsername():
    username = input("Введіть ім'я користувача: ")
    if not username:
        print("Ім'я користувача не може бути порожнім.")
        return None
    return username

def main_menu():
    print("GitHub друзі — інтерфейс")
    print("1. Вивести користувачів")
    print("2. Вивести дружні зв’язки")
    print("3. Вивести граф соціальної мережі")
    print("4. Додати користувача до мережі")
    print("5. Видалити користувача з мережі")
    print("0. Вийти")

    choice = input("Виберіть опцію (0-5): ")
    if not (choice >= "0" and choice <= "5"):
        print("Невірний вибір. Спробуйте ще раз.")
        return main_menu()
    return choice

def draw_social_graph(network):
    G = nx.Graph()
    main_user_id = None
    
    # Добавляем узлы и ребра
    for user_id, user in network.users.items():
        if main_user_id is None:
            main_user_id = user_id
        G.add_node(user_id, label=user.username)

    # Добавляем ребра с весами
    for user_id, friends in network.friendships.items():
        for friend_id in friends:
            if not G.has_edge(user_id, friend_id):
                # Вычисляем вес ребра на основе общих друзей
                common_friends = len(set(network.friendships[user_id]) & 
                                  set(network.friendships[friend_id]))
                # Чем больше общих друзей, тем меньше вес (ближе узлы)
                weight = 1.0 / (common_friends + 1)
                G.add_edge(user_id, friend_id, weight=weight)

    # Создаем список уровней для shell layout
    shortest_paths = nx.single_source_shortest_path_length(G, main_user_id)
    shells = []
    max_level = max(shortest_paths.values())
    
    # Группируем узлы по уровням для shell layout
    shell_radius = 1.0  # Начальный радиус
    for level in range(max_level + 1):
        shell = [node for node, path_length in shortest_paths.items() if path_length == level]
        if level == 0:  # Главный пользователь
            shell_radius = 0.1
        elif level == 1:  # Прямые друзья
            shell_radius = 0.4
        else:  # Остальные уровни
            shell_radius = 0.8
        shells.append(shell)

    # Настраиваем визуализацию
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111)
    
    # Используем spring_layout с учетом весов и начальным положением из shell_layout
    pos_shell = nx.shell_layout(G, shells)
    pos = nx.spring_layout(G, 
                          pos=pos_shell,
                          weight='weight',
                          k=0.5,  # Сила отталкивания
                          iterations=50)
    
    # Настраиваем цвета и размеры узлов
    node_colors = []
    node_sizes = []
    
    for node in G.nodes():
        if node == main_user_id:
            node_colors.append("#DDC45D")  # Желтый для главного пользователя
            node_sizes.append(3000)
        else:
            level = shortest_paths.get(node, None)
            if level == 1:
                node_colors.append("#2F6FCE")  # Синий для прямых друзей
                node_sizes.append(2000)
            else:
                node_colors.append("#274169")  # Синий для прямых друзей
                node_sizes.append(1000)

    # Рисуем граф
    nx.draw(G, pos,
            node_color=node_colors,
            node_size=node_sizes,
            edge_color='gray',
            width=1,
            with_labels=False,
            ax=ax)
    
    # Добавляем метки
    labels = {node: G.nodes[node]['label'] for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels,
                           font_size=8,
                           font_weight='bold')

    plt.title("Граф друзів GitHub")
    ax.set_axis_off()
    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)
    plt.show()

def loop(parser):
    network = parser.fetch_user_and_friends(handleUsername())
    while True:
        if not network:
            print("Не вдалося отримати дані користувача або його друзів.")
            continue
            
        match main_menu():
            case "1":  # Вивести користувачів
                for uid, user in network.users.items():
                    print(f"ID: {uid}, Користувач: {user.username}")
                    
            case "2":  # Вивести дружні зв'язки
                print("Дружні зв'язки користувачів:")
                print("=" * 40)
                for uid, friends in network.friendships.items():
                    username = network.users[uid].username
                    if friends:
                        print(f"[{username}]")
                        for fid in friends:
                            friend_name = network.users[fid].username
                            print(f"  └─ {friend_name}")
                        print("-" * 40)
                    else:
                        print(f"[{username}] не має друзів.")
                        print("-" * 40)
                    
            case "3":  # Вивести граф
                draw_social_graph(network)

            case "4": # Додати користувача
                username = handleUsername()
                if username:
                    new_network = parser.fetch_user_and_friends(username)
                    if new_network:
                        network.users.update(new_network.users)
                        network.friendships.update(new_network.friendships)
                        print(f"Користувач {username} та його друзі додані.")
                    else:
                        print(f"Не вдалося додати користувача {username}.")
                continue

            case "5":
                username = handleUsername()
                if username:
                    user_data = parser.get_user_data(username)
                    if user_data and "id" in user_data:
                        user_id = user_data["id"]
                        if user_id in network.users:
                            network.deleteUser(user_id)
                            print(f"Користувач {username} видалений.")

                            # Видалити користувачів без друзів
                            orphan_ids = [uid for uid, friends in network.friendships.items() if not friends]
                            for orphan_id in orphan_ids:
                                network.deleteUser(orphan_id)
                                orphan_name = network.users[orphan_id].username if orphan_id in network.users else "невідомий"
                                print(f"Користувач {orphan_name} видалений, бо не має друзів.")
                        else:
                            print(f"Користувач {username} не знайдений.")
                    else:
                        print(f"Не вдалося знайти користувача {username}.")
                continue
                
            case "0":  # Вийти
                print("До побачення!")
                return
                
            case _:  # Невірний вибір
                print("Невірний вибір. Спробуйте ще раз.")
                continue