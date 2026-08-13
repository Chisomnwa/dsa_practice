import heapq
from collections import deque


class Graph:
    def __init__(self, directed=True):
        """
        Initialize the Graph. (Given: do not change.)
        directed: routes are one way by default.
        adj_list: maps each city to a dict of {destination: cost},
        in the order the routes were added.
        """
        self.directed = directed
        self.adj_list = {}

    def add_edge(self, source, destination, weight=1):
        """
        Add a route from source to destination with the given cost.
        Create either city in adj_list if it is not there yet.
        Adding a route that already exists overwrites its cost.
        If the graph is undirected, also add the reverse route.
        Returns None.
        Milestone 1.
        
        - - -

        For example:

        graph.add_edge("Lagos", "Abuja", 500)

        - If graph is directed, should produce:

        {
            "Lagos": {"Abuja":500}
            "Abuja": {}
        }

        - If graph is not directed, should produce:

        {
            "Lagos": {"Abuja":500}
            "Abuja": {"Lagos":500}
        }

        Pseudocode:
        1. If source doesn't exists, create it
        2. If destination doesn't exist, create it
        3. Add destination to source's neighbor's dictionary with the weight
        4. if the graph is undirected, add the reverse route too
        5. Return None
        """
        if source not in self.adj_list:
            self.adj_list[source] = {}

        if destination not in self.adj_list:
            self.adj_list[destination] = {}

        self.adj_list[source][destination] = weight

        if not self.directed:
            self.adj_list[destination][source] = weight



    def remove_edge(self, source, destination):
        """
        Remove the route from source to destination.
        If the graph is undirected, also remove the reverse route.
        If the route does not exist, do nothing. Do not crash.
        Returns None.
        Milestone 1.

        - - -
        The idea is to remove the route in the forward direction, and if the graph is
        undirected, remove the reverse route too.

        Say we have: graph.remove_edge("ATL",  "JKF")

        We remove the route ATL -> JFK

        if the graph is undirected,
        We also remove: JFK -> ATL

        If the route doesn't exist, do nothing, don't crash.

        Pseudocode:
        if  source exists in the group
            if destination exists in the soources;s neighbors
                remove destination from source's neighbors

        if the graph is undirected
            if destination exists i graph
                if source exsts in destinations's neigbors

        return None
        """
        if source in self.adj_list:
            if destination in self.adj_list[source]:
                del self.adj_list[source][destination]

        if not self.directed:
            if destination in self.adj_list:
                if source in self.adj_list[destination]:
                    del self.adj_list[destination][source]

    def get_neighbors(self, vertex):
        """
        Return a list of vertex's direct destinations, in the order
        their routes were added.
        Unknown city returns [].
        Milestone 1.

        - - -
        For example:
        self.adj_list = {
            "Lagos": {"Abuja": 500, "Kano": 700, "Ibadan": 200}
        }

        graph.get_neighbors("Lagos")

        Should return: ["Abuja", "Kano", "Ibadan"]

        And if the city doesn't exist, like:

        graph.get_neighbors("Enugu")

        Returns []

        Pseudocode:
        if vertex does not exist in graph
            return []

        retuurn the list of keys (neighbours) in adj_list[vertex]
        """
        if vertex not in self.adj_list:
            return []

        return list(self.adj_list[vertex].keys())

    def bfs(self, start_vertex):
        """
        Breadth-first search from start_vertex using a queue.
        Visit neighbors in the order their routes were added, and use a
        visited set so cycles cannot trap you.
        Return the list of cities in the order they were visited.
        Unknown start returns [].
        Milestone 1.

        - - -
        We need three things:
        1. A queue because BFS if FIFO
        2. A visited set - to prevent cycles from making us visit forever
        3. A result list -> to recrd the order we visit cities

        Suppose we have:

                         A
                        / \
                       B   C
                      /    /
                     D    E

        Starting bfs("A")

        Initially:
        queue = [A]
        visited = {A}
        result = []

        Take A out:
        queue = []
        result = [A]

        Its neighbors are B and C, so we add them:
        queue = [B, C]
        visited = {A, B, C}

        Take B:
        queue = [C]
        result = [A, B]

        Take C:
        queue = [D]
        visited = {A, B, C, D}

        Take D:
        queue = [E]
        result = [A, B, C, D]

        Take E:
        queue = []
        visited = {A, B, C, D, E}
        result = [A, B, C, D, E]

        Pseudocode:
        If start_vertex does not exist in the graph
            return []

        create a queue
        add start_vertex to the queue

        create a visited set
        add start_vertex to visited
        
        create an empty result list

        while the queue is not empty

            remove the first item from the queue
            cal it current

            add current to result

            for each neighbor of current

                if neighbor has not been visited
                    add neighbor to visited
                    add neighbor to the queue

        return result
        """
        if start_vertex not in self.adj_list:
            return []

        queue = deque([start_vertex])
        visited = {start_vertex}
        result = []

        while queue:
            current = queue.popleft()
            result.append(current)

            for neighbor in self.adj_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result

    def shortest_path_length(self, source, destination):
        """
        Return the fewest number of flights from source to destination.
        Same city is 0. If destination is unreachable, or either city
        is unknown, return -1.
        Milestone 1.

        - - -
        In regular BFS, the queue contains just:
        queue = deque(["Lagos"]")

        Here we also need to rememeber how many flights we've taken, so we store:
        queue = deque([("Lagos", 0)])

        Meaning:

        ("Lagos", 0) -> Lagos is 0 flights away
        ("Abuja", 1) -> Abuja is 1 flight away
        ("Kano", 2) -> Kano is 2 flights away

        Because BFS explores ring by ring, the first time we reach the destination, we've found the shortest path.

        For eample:

                         A       distance 0
                        / \      distance 1
                       B   C     distance 2
                      /     \
                     D      E
        
        So: shortest_path_length("A", "D") returns 2

        Pseudocode:
        if source or destination does not exists:
            return -1

        if source == destination:
            return 0

        create a queue
        add (source, 0) to the queue

        create a visited set
        add source to visited

        while the queue is not empty
            
            remove the first (current, distance) from the queue

            for each neighbor of current

                if neighbor is the destination
                    return distance +1

                if neighbor has not been visited
                    add neighbor to visited
                    add (neighbor, distace + 1) to the queue

        return -1  
        """
        if source not in self.adj_list or destination not in self.adj_list:
            return -1

        if source == destination:
            return 0

        queue = deque([(source, 0)])
        visited = {source}

        while queue:
            current, distance = queue.popleft()

            for neighbor in self.adj_list[current]:
                if neighbor == destination:
                    return distance + 1

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))

        return -1


    def dfs(self, start_vertex):
        """
        Depth-first search from start_vertex using a stack or recursion.
        Visit neighbors in the order their routes were added, and use a
        visited set.
        Return the list of cities in the order they were visited.
        Unknown start returns [].
        Milestone 2.

        - - -
        The goal here is to start at a city and explore as deeply as possible along
        one path before coming back and exploring another path.

        Unlike BFS which uses a queue, DFS uses a stack.

        Why stack? Because current = stack.pop() removes the last item added -> LIFO

        So, if we have:

        stack = [B, C]

        Pseudocode:
        if start_vertex does not exists in the graph
            return []

        create a stack
        add start_vertex to the stack

        create a visited set
        add start_vertex to visited

        create an empty result list

        while the stack is not empty

            remove the last item from the stack
            call it current

            add current to result

            for each neighbor of current

                if neither has not been visited
                    add neighbor to visited
                    add neighbor to the stack
        """
        if start_vertex not in self.adj_list:
            return []

        stack = [start_vertex]
        visited = {start_vertex}
        result = []

        while stack:
            current = stack.pop()
            result.append(current)

            for neighbor in reversed(self.adj_list[current]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

        return result

    def has_route(self, source, destination):
        """
        Return True if destination is reachable from source with any
        number of stops, else False.
        If either city is unknown, return False. A city always has a
        route to itself.
        Milestone 2.

        - - -
        The goal here is to answer: "Can I get from source to destination by following the graph's route?"

        For eaxmple:

                     A
                    /
                   B   
                  / \
                 C  D

        If we call:
        has_route("A", "D")

        We return tRUE BECAUSE:
        a -> b -> d

        If we call:
        has_route("A", "X")

        We return False because X doesn't exist/reachability isn't possible.

        We can use BFS here. We start at source, put it in a queue, and keep 
        exploring its neighbors. If we find destination, we return True. If
        the queue becomes empty without finding it, we return False.

        Also if we call:
        has_route("A", "A")

        we return True because a city always has a route to itself.

        Pseudocode:
        if source or destination doesn not exists in the graph
            return False

        if source == destination
            Retrun True

        create a queue
        add source to visited

        while the queue is not empty

            remove the first item from the queue
            call it current

            for each neighbor of current

                if neighbor == destination
                    return True

                if neighbor has not been visited
                    add neighbor to visited
                    add neighbor to the queue
            
        return False
        """
        if source not in self.adj_list or destination not in self.adj_list:
            return False

        if source == destination:
            return True

        queue = deque([source])
        visited = {source}

        while queue:
            current = queue.popleft()

            for neighbor in self.adj_list[current]:
                if neighbor == destination:
                    return True

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False

    def dijkstra(self, source):
        """
        Return a dict mapping every reachable city to its minimum total
        cost from source. source maps to 0. Unreachable cities are
        left out. Unknown source returns {}.
        Milestone 3.

        - - -
        The goal of dijkstra(source) is to find the cheapest total route from source to every reachable city.

        Unlike shortest_path_length, which counts the numbe of flights Dijkstra cares about the total 
        cost/weight of the routes.

        For xample:

        A --2--> B
        A --5--> C
        B --1--> C
        B --4--> D
        C --2--> D

        Starting from A:
        - A -> B costs 2
        - A -> C directly costs 5
        - But A -> B -> C costs 2 + 1 = 3, so that's cheaper
        - A -> B -> C -> D costs 2 + 1 + 2 = 5

        So the result is:

        {
            "A": 0,
            "B": 2,
            "C": 3,
            "D": 5
        }

       The important idead:

       We use a min-hip priority queue.

       The heap always gives us the city with the smallest known total cost so far.

       When we reach a city, we check wether going throgh that city gives us a 
       cheaper route to its neighbors.

       For example, when we reach B with cost 2:

       A -> B - C
       2 + 1 = 3

       We discover that C can actually be reached for 3, which is better than the previously known 5.

       That's called relaxing an edge.

       Pseudocode:
       if source does not exist in the graph
            return {}

        create an empty min-heap
        add (0, source) to the heap

        create an empty distances dictionaty
        set distances[source] = 0

        while the heap is not empty

            remove the city with the smallest cost
            call them current_cost and current

            if current_cost is grater than distances[current]
                skip this entry

            for each neighbor and edge_weight of current

                new_cost = current_cost + edge_weight

                if neighbor has not been seen
                    OR new_cost is cheaper than distance[neighbor]

                    distance[neighbor] = new_cost
                    add (new_cost, eighbor) to the heap

            return distances
        """
        if source not in self.adj_list:
            return {}

        heap = [(0, source)]
        distances = {source: 0}

        while heap:
            current_cost, current = heapq.heappop(heap)

            if current_cost > distances[current]:
                continue

            for neighbor, weight in self.adj_list[current].items():
                new_cost = current_cost + weight
                
                if neighbor not in distances or new_cost < distances[neighbor]:
                    distances[neighbor] = new_cost
                    heapq.heappush(heap, (new_cost, neighbor))

        return distances
