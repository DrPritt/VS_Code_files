def otsi_kaupa(järjend, otsitav):
    def counter(uus_järjend, otsitav, counter1, min_kaugus):
        if otsitav in uus_järjend:
            #if min_kaugus > counter2:
                #min_kaugus = counter2 ---- Lihtsam on kirjutada min funktsiooniga, mis võtab väärtuseks väiksema numbri
            min_kaugus = min(min_kaugus, counter1)
        else:
            for item in uus_järjend:
                if isinstance(item, list):
                    # funktsioonile tuleb anda ka ju muutujat counter() returnib min_kauguse, mis on asetatud muutujasse, min_kaugus!
                    min_kaugus = counter(item, otsitav, counter1 + 1, min_kaugus)
        return min_kaugus

    tulemus = counter(järjend, otsitav, 0, float("inf"))
    return tulemus if tulemus != float("inf") else -1

print(otsi_kaupa(["Kapsas", "Porgand", ["Kartul"]], "Kartul"))  # Should return 1
print(otsi_kaupa(["Kapsas", ["Porgand", ["Kapsas"]], "Naeris"], "Porgand"))  # Should return 1
print(otsi_kaupa(["Kapsas", [[["Porgand"]], ["Porgand", "Cowabunga"], "Naeris"], "Kartul"], "Porgand"))  # Should return 2


























"""
def otsi_kaupa(järjend, otsitav):
    def search(item_list, target, current_depth):
        min_depth = float('inf')  # Initialize with a large value
        if target in item_list:
            min_depth = current_depth
        
        for item in item_list:
            if isinstance(item, list):
                result = search(item, target, current_depth + 1)
                if result != -1:
                    min_depth = min(min_depth, result)
        
        return min_depth if min_depth != float('inf') else -1

    # Start the search with initial depth of 0
    return search(järjend, otsitav, 0)

# Test cases
print(otsi_kaupa(["Kapsas", "Porgand", "Naeris"], "Kartul"))  # Should return -1
print(otsi_kaupa(["Kapsas", ["Porgand", ["Kapsas]], "Naeris"], "Porgand"))  # Should return 1
print(otsi_kaupa(["Kapsas", [[["Porgand"]], ["Porgand", "Cowabunga"], "Naeris"], "Kartul"], "Porgand"))  # Should return 2
"""