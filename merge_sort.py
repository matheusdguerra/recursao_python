
def merge_sort(lista):
    if len(lista) <= 1:  # Base da recursao
        return lista

    meio = len(lista) // 2

    lado_esquerto = merge_sort(lista[:meio])
    lado_direito = merge_sort(lista[meio:])

    return merge(lado_esquerto, lado_direito)


def merge(lado_esquerto, lado_direito):
    if not lado_esquerto:
        return lado_direito
    if not lado_direito:
        return lado_esquerto

    if lado_esquerto[0] < lado_direito[0]:
        return [lado_esquerto[0]] + merge(lado_esquerto[1:], lado_direito)

    return [lado_direito[0]] + merge(lado_esquerto, lado_direito[1:])


if __name__ == '__main__':
    assert merge_sort([2, 6, 3, 8, 1, 4, 9, 0, 7, 5]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
