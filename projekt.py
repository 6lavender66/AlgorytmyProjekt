import networkx as nx
import matplotlib.pyplot as plt

ekwipunek = {
    "Kamil": ["Kamera"],
    "Magda": [],
    "Ewa": ["Statyw"],
    "Piotr": ["Kamera", "Statyw"],
    "Nikodem": [],
    "Mikołaj": ["Kamera"],
    "Liliana": ["Statyw"],
    "Daniel": []
}

relacje = {
    "Kamil": ["Magda", "Piotr", "Daniel"],
    "Magda": ["Kamil", "Ewa", "Liliana",],
    "Ewa": ["Liliana", "Daniel"],
    "Piotr": ["Kamil"],
    "Nikodem": ["Mikołaj"],
    "Mikołaj": ["Nikodem", "Daniel"],
    "Liliana": ["Magda", "Ewa"],
    "Daniel": ["Kamil", "Ewa", "Mikołaj"]
}

#graf pokazujący relacje 
graf = nx.Graph()
for osoba, znajomi in relacje.items():
    graf.add_node(osoba) #dodanie osoby do grafu
    for znajomy in znajomi:
        graf.add_edge(osoba, znajomy) #lovemap

#nazwy funkcji samoopisowe
def CzySieZnaja(osoba1, osoba2):
    return nx.has_path(graf, osoba1, osoba2)

def ListaZnajomych(osoba):
    return list(graf.neighbors(osoba))

#dijkstra bez wag
def ShortesPath(osoba, przedmioty):
    osoby_z_przedmiotami = [osoba for osoba, ekwip in ekwipunek.items() if all(przedmiot in ekwip for przedmiot in przedmioty)]

    najkrotsze_sciezki = [] #tablica przechowująca trase
    for osoba_z_przedmiotem in osoby_z_przedmiotami:
        try:
            sciezka = nx.shortest_path(graf, source=osoba, target=osoba_z_przedmiotem) #funkcja wbudowana
            najkrotsze_sciezki.append(sciezka) #dodwanie trasy do tablicy
        except nx.NetworkXNoPath:
            continue  #jeśli nie ma ścieżki szukamy po innych osoba

    najkrotsza_sciezka = min(najkrotsze_sciezki, key=len) #funkcja min

    #rysowanie grafu
    pos = nx.spring_layout(graf)
    nx.draw(graf, pos, with_labels=True, node_color='lightblue', node_size=2000, edge_color='gray', linewidths=2, font_size=15)

    #wyróżnienie ścieżki
    edges_in_path = list(zip(najkrotsza_sciezka, najkrotsza_sciezka[1:]))
    nx.draw_networkx_nodes(graf, pos, nodelist=najkrotsza_sciezka, node_color='red')
    nx.draw_networkx_edges(graf, pos, edgelist=edges_in_path, edge_color='red', width=2)
    plt.title(f"Najkrótsza ścieżka dla {osoba} do osoby z {' i '.join(przedmioty)}")
    plt.show()

    print(f"Najkrótsza ścieżka do osoby z {' i '.join(przedmioty)}: {najkrotsza_sciezka}")

#przyklady
ShortesPath("Daniel", ["Kamera"])
ShortesPath("Ewa", ["Statyw", "Kamera"])

#czy sie znają
print(CzySieZnaja("Kamil", "Ewa"))

#lista znajomych
print(ListaZnajomych("Daniel"))

