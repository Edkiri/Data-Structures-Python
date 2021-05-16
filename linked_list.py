from node import Node
from arrays import Array

class SinglyLinkedList:
    def __init__(self):
        """ initializes a empty list. """

        self.head = None
        self.tail = None
        self.size = 0


    def append(self, data):
        """ Add a node into de LinkedList with the data. """

        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            probe = self.head
            while probe.next:
                probe = probe.next
            probe.next = node
            self.tail = node

        self.size += 1

    
    def size(self):
        """ Returns the size of the list. """
        return str(self.size)

    def iter(self):
        """ Iterates through each of the node values in the list. """

        probe = self.head
        while probe:
            val = probe.data
            probe = probe.next
            yield val

            
    def search(self, data):
        """ Ensures that 'data' is on the list or not. """

        for node in self.iter():
            if data == node:
                print(f"Data {data} has been found!!")
            else:
                print(f"Data {data} has not been found.")

    
    def clear(self):
        """ Empty the list. """

        self.head = None
        self.size = 0

    
    def add_array(self, array):
        """Append the elemets of an Array into the list  as Nodes."""

        for element in array:
            node = Node(element)

            if self.head == None:
                self.head = node
            else:
                probe = self.head
                while probe.next:
                    probe = probe.next
                probe.next = node
                
            self.size += 1


    def replace(self, target_item, new_data):
        """ 
        Replaces the node with the value "target_item" with 
        a new node with a value of "new_data". 
        """
        new_node = Node(new_data) # Crea un nuevo nodo.

        probe = self.head # Variable auxiliar utilizada como el 'índice' del recorrido actual
        is_the_first_iteration = True # Verdadero solo en la primera iteración.
        previuos = self.head # Variable auxiliar que va un paso más atras del 'probe'.

        while probe.next != None and probe.data != target_item:
            """ Mientas que haya un siguiente nodo y aún no se consiga el objetivo
            se incrementa el nodo 'probe' igualándolo a su siguiente, el 'previous'
            no se incrementa sino hasta la segunda iteración."""

            probe = probe.next # Pasamos a la siguiente iteración de la lista igualando el 'probe' al nodo al que este apunta.
            
            if not is_the_first_iteration:
                previuos = previuos.next # Solo incrementamos el 'previous' si no estamos en la primera iteración.
            is_the_first_iteration = False # A partir de aquí ya no estamos en la primera iteración.

        if probe.data == target_item and is_the_first_iteration:
            """ Si encontró el item y esta es la primera iteración quiere decir que
            tenemos que cambiar la variable head para que esta ahora sea el nuevo nodo."""
            new_node.next = probe.next # Nos aseguramos que nuestro nuevo nodo apunte al mismo que apuntaba el nodo anterior.
            self.head = new_node # Actualizamos el nuevo head.
        elif probe.data == target_item:
            """ En este momento ya conseguimos el 'target_item' pero como no estamos en la primera
            iteración, significa que tenemos que reemplazar un nodo que se encuentra entre dos nodos,
            para esto nos apoyaremos de nuestra variable 'previous'."""
            new_node.next = probe.next # Que nuestro nuevo nodo apunte al mismo nodo al que apuntaba el viejo nodo.
            previuos.next = new_node # Y que el nodo anterior apunte a nuestro nuevo nodo.
            if new_node.next == None:
                self.tail = new_node # Por último actualizamos el 'self.tail' de nuestro lista en caso de que reemplacemos el úlimo nodo de nuestra lista.
        else:
            print("The target item is not in the list.") # No se encontró el item.

    
    def add_node_at_the_beginning(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        self.size += 1


    def add_node_at_the_end(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1


    def remove_node_from_the_beginning(self):
        if self.head != self.tail:
            self.head = self.head.next
        else:
            self.head = None
            self.tail = None
        self.size -= 1


    def remove_node_from_the_end(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            probe = self.head
            while probe.next != self.tail:
                probe = probe.next
            probe.next = None
            self.tail = probe
        self.size -= 1


    def append_at_target(self, target_item, data):
        new_node = Node(data)
        probe = self.head

        while probe.next != None and probe.data != target_item:
            probe = probe.next
        
        if probe.data == target_item:
            new_node.next = probe.next
            probe.next = new_node
            self.size += 1
            if new_node.next == None:
                self.tail = new_node
        else:
            print("Item target has not been found!")

    
    def remove_at_target(self, target_item):

        probe = self.head
        previous = self.head
        counter = 0

        while probe.next != None and probe.data != target_item:
            probe = probe.next
            if counter > 0:
                previous = previous.next
            counter += 1

        if probe.data == target_item:
            previous.next = probe.next
            if previous.next == None:
                self.tail = previous
            elif probe == self.head:
                self.head = probe.next
            self.size -= 1


if __name__ == '__main__':

    linked_list = SinglyLinkedList()
    for i in range(1,10):
        linked_list.append(i)

    linked_list.replace(9,8.5)
    print()
    print(f"Head: {linked_list.head.data}")
    print(f"Tail: {linked_list.tail.data}")
    print(f"Tamaño: {linked_list.size}")
    print()
    for el in linked_list.iter():
        print(el)