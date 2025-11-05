def separar_pares_impares(lista):
    pares = [n for n in lista if n % 2 == 0]
    impares = [n for n in lista if n % 2 != 0]
    return pares, impares

def main():
    print("=== Particionador de IDs por Shard (A/B) ===\n")

    ids = []
    for i in range(1, 21):
        while True:
            try:
                id_num = int(input(f"Digite o {i}º ID: "))
                ids.append(id_num)
                break
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

    pares, impares = separar_pares_impares(ids)

    print("\n--- Resultados ---")
    print(f"Lista (entrada): {ids}")
    print(f"Shard A (PAR): {pares}  | total: {len(pares)}")
    print(f"Shard B (ÍMPAR): {impares}  | total: {len(impares)}")

if __name__ == "__main__":
    main()
