class Node:
    left = None
    right = None
    value = None

    def __init__(self, value):
        self.value = value

#print code: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
def display(father):
    if father.right is None and father.left is None:
        line = '%s' % father.value
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    if father.right is None:
        lines, n, p, x = display(father.left)
        s = '%s' % father.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    if father.left is None:
        lines, n, p, x = display(father.right)
        s = '%s' % father.value
        u = len(s)
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    left, n, p, x = display(father.left)
    right, m, q, y = display(father.right)
    s = '%s' % father.value
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2


# Contar Nós
def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

# Contar folhas
def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)

# Pesquisar um valor
def search_value(node, value):
    if node is None:
        return 0
    if value == node.value:
        return 1

    if value < node.value:
        if node.left is None:
            return 2
        return search_value(node.left, value)

    if value > node.value:
        if node.right is None:
            return 3
        
        return search_value(node.right, value)


#Ordenar a árvore
def order_binary_heap(father, new_node):
    if father.value > new_node.value:
        if father.left is not None:
            order_binary_heap(father.left, new_node)
        else:
            father.left = new_node
    else:
        if father.right is not None:
            order_binary_heap(father.right, new_node)
        else:
            father.right = new_node

#Criar árvore
def create_tree():
    total_nodes = int(input("Digite a quantidade de nós que você deseja adicionar na sua árvore: "))
    root = None
    for _ in range(total_nodes):
        node_value = int(input("Digite o valor do nó: "))
        new_node = Node(node_value)
        if root is None:
            root = new_node
        else:
            order_binary_heap(root, new_node)
    return root



#MAIN
root = None
while True:
    print("\nOpções:")
    print("1. Criar Árvore")
    print("2. Total de Nós")
    print("3. Total de Folhas")
    print("4. Pesquisar Valor")
    print("5. Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        root = create_tree()
        print("\n\nÁrvore criada:")
        if root:
            lines, *_ = display(root)
            for line in lines:
                print(line)

    elif opcao == 2:
        if root:
            print("\n\nTotal de nós:", count_nodes(root))
        else:
            print("\n\nA árvore ainda não foi criada.")

    elif opcao == 3:
        if root:
            print("\n\nTotal de folhas:", count_leaves(root))
        else:
            print("\n\nA árvore ainda não foi criada.")

    elif opcao == 4:
        if root:
            value = int(input("\n\nDigite o valor a ser pesquisado: "))
            found = search_value(root, value)
            print("Valor encontrado." if found == 1 else "Valor não encontrado.")
        else:
            print("\n\nA árvore ainda não foi criada.")

    elif opcao == 5:
        print("\n\nSaindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")