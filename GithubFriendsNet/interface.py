import networkx as nx
import matplotlib.pyplot as plt

def handleUsername():
    username = input("Введіть ім'я користувача: ")
    if not username:
        print("Ім'я користувача не може бути порожнім.")
        return None
    return username

def main_menu():
    print("Вітаємо у соціальній мережі GitHub!")
    print("1. Вивести користувачів")
    print("2. Вивести дружні зв’язки")
    print("3. Вивести граф соціальної мережі")
    print("0. Вийти")

    choice = input("Виберіть опцію (0-3): ")
    if not (choice >= "0" and choice <= "3"):
        print("Невірний вибір. Спробуйте ще раз.")
        return main_menu()
    return choice

def draw_social_graph(network):
    # Виводимо користувачів
    for uid, user in network.users.items():
        print(user)

    # Виводимо дружні зв’язки
    for uid, friends in network.friendships.items():
        uname = network.users[uid].username
        friend_names = [network.users[fid].username for fid in friends]
        print(f"{uname} -> {friend_names}")

    # Створюємо граф
    G = nx.Graph()

    for user_id, user in network.users.items():
        G.add_node(user_id, label=user.username)

    for user_id, friends in network.friendships.items():
        for friend_id in friends:
            if G.has_edge(user_id, friend_id) or user_id == friend_id:
                continue
            G.add_edge(user_id, friend_id)

    labels = {node: G.nodes[node]['label'] for node in G.nodes()}

    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, seed=42)

    nx.draw(G, pos, with_labels=False, node_color='skyblue', node_size=1500, edge_color='gray')
    nx.draw_networkx_labels(G, pos, labels, font_size=10)

    plt.title("Соціальна мережа GitHub")
    plt.axis('off')
    plt.tight_layout()
    plt.show()

def loop(parser):
    network = parser.fetch_extended_network(handleUsername())
    if not network:
        print("Не вдалося отримати дані користувача або його друзів.")
        return loop()
    match main_menu():
        case "1": return
        case "2": return
        case "3": draw_social_graph(network)
        case "0": return
        case _: loop(parser)