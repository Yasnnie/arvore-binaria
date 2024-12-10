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
def insert(father, new_node):
    if father.value > new_node.value:
        if father.left is not None:
            insert(father.left, new_node)
        else:
            father.left = new_node
    else:
        if father.right is not None:
            insert(father.right, new_node)
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
            insert(root, new_node)
    return root

def pre_order(root):
    print(root.value, end = " ")
    if root.left is not None:
        pre_order(root.left)
    if root.right is not None:
        pre_order(root.right)


def post_order(root):
    if root.left is not None:
        post_order(root.left)
    if root.right is not None:
        post_order(root.right)
    print(root.value, end = " ")


def simetric_order(root):
    if root.left is not None:
        simetric_order(root.left)

    print(root.value, end = " ")
    if root.right is not None:
        simetric_order(root.right)


def locate_min(node):
    current = node
    while current.left is not None:
        current = current.left
        
    return current

def remove_node(value, node):
    if node is None:
        return None
    elif value < node.value:
         node.left = remove_node(value, node.left)
    elif value > node.value:
        node.right = remove_node(value,node.right)
    elif node.left is not None and node.right is not None:
        node_aux = locate_min(node.right)
        print(node_aux)
        node.value = node_aux.value
        node.right = remove_node(node.value, node.right)
    else:
   
        if node.left is not None:
            return node.left
        else:
            return node.right
    
    return node

#MAIN
root = None
while True:
    print("\nOpções:")
    print("1. Criar Árvore")
    print("2. Total de Nós")
    print("3. Total de Folhas")
    print("4. Pesquisar Valor")
    print("5. Pré-ordem")
    print("6. Pós-ordem")
    print("7. Simétrica")
    print("8. Remover nó")
    print("9. Sair")
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
        if root:
            print("\n\n")
            pre_order(root)
        else:
            print("\n\nA árvore ainda não foi criada.")


    elif opcao == 6:
        if root:
            print("\n\n")
            post_order(root)
        else:
            print("\n\nA árvore ainda não foi criada.")

    elif opcao == 7:
        if root:
            print("\n\n")
            simetric_order(root)
        else:
            print("\n\nA árvore ainda não foi criada.")

    elif opcao == 8:
        if root:
            value = int(input("\n\nDigite o valor a ser removido: "))
            remove_node(value,root)

            lines, *_ = display(root)
            for line in lines:
                print(line)
        else:
            print("\n\nA árvore ainda não foi criada.")

    elif opcao == 9:
        print("\n\nSaindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")
