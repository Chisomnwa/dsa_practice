# Project: Build Your Own File System
# You implement the six methods marked TODO inside FileSystem.
# Everything else (FileNode, parse_path, render_tree) is provided. Do not change it.
#
# There is also an OPTIONAL STRETCH section at the bottom (not graded, extra credit).
# See the project write-up for what to build and how to self-check it.


class FileNode:
    """One item in the file system: a file or a folder.

    name:     the item's name, like "docs" or "resume.pdf"
    size:     size in bytes. Folders are always 0.
    is_file:  True for files, False for folders.
    children: this folder's contents, mapped name -> FileNode. Files have no children.
    """
    def __init__(self, name, size=0, is_file=False):
        self.name = name
        self.size = size
        self.is_file = is_file
        self.children = {}


def parse_path(path):
    """Turn "root/docs/resume.pdf" into ["root", "docs", "resume.pdf"].

    Every path in this project starts with "root".
    """
    return [part for part in path.split("/") if part != ""]


def render_tree(node, indent=0):
    """Return a printable picture of the tree. Handy while you build.

    Try: print(render_tree(fs.root)) after a few add_path calls.
    """
    label = node.name + (" (" + str(node.size) + ")" if node.is_file else "/")
    lines = ["  " * indent + label]
    for child in node.children.values():
        lines.append(render_tree(child, indent + 1))
    return "\n".join(lines)


class FileSystem:
    def __init__(self):
        # The file system always starts with one folder named "root".
        self.root = FileNode("root")

    # ================= GRADED METHODS (implement these six) =================

    def add_path(self, path, size=0):
        """Milestone 1. Walk the path from root, creating folders as needed.

        The last segment becomes a file when size > 0, otherwise a folder.
        Every segment in the middle is a folder.
        If the full path already exists, do nothing.
        """
        # TODO: implement

        """
        Input: 
         - path: str. e.g "root/docs/resume.pdf" or ""root/photos"
         - size: int = 0

        Output: None (we modify the tree instead)

        Goal: Walk from the root to the destination.
            - If a folder along the path doesn't exist, create it.
            - The last segment is:
                - a file if size > 0
                - a folder if size == 0
            - if the full path alreaady exists, do nothing.

        Step 1: Parse the path
        parts = parse_path(path)

        e.g "root/docs/resume.pdf" becomes ["root", "docs", "resume.pdf"]

        Step 2: Start at the root
        current = self.root

        current keeps track of whre you are as you walk down the tree.

        current 
          |
        root/

        step 3: Walk through every segment after "root"

        for i in range(1, len(parts)):

        We start at index 1 because: parts[0] == "root" and we are here already

        Step 4: Get the current segmentb

        name = parts[i]

        For our example:
        - first iteration: "docs"
        - second iteration: "resume.pdf"

        Step 5: Is this the last segment?

        This tells us wether we're creating:
        - a folder (middle of the path), or
        - the final item (file or folder)

        Step 6: Create it if iit's missing
        if name not in current.children:
        
        if it already exists, do nothing (per the spec)

        Otherwise, create it.

        For the last segment:

        current.children[name] = fileNode(
            name,
            size=size if if_last else 0,
            is_file=is_las and size > 0
        )

        Notice:
        - Middle segment are always folders
        - The last segment is:
            - a file if size > 0
            - otherwise a folder

        Step 7: Move to the chold

        Wether we created it or it laready exiisted, we now move into it:

        current = current.children[name]

        Think of it like changing directories:
        root/
          |
        docs/
          |
        resume.pdf

        - - -
        Pseudocode:
        Split the parts into parts

        Start at the root

        for each part after "root":
            check if this is the last part of the path

            if the current folder does not contain this child:

                if this is the last part:
                    create a file if size is > 0
                    otherwise create a folder

                Otherwise:
                    Create a folder

                Move to that child
        
        Done
        """
        parts = parse_path(path)
        current = self.root

        for i in range(1, len(parts)):
            name = parts[i]
            is_last = (i == len(parts) - 1)

            if name not in current.children:
                current.children[name] = FileNode(
                    name,
                    size=size if is_last else 0,
                    is_file=is_last and size > 0
                )

            current = current.children[name]

    def list_all(self):
        """Milestone 2. Return the full path of every item, sorted.

        Includes "root" itself, every folder, and every file.
        """
        # TODO: implement


        """
        Input: No input parameters

        Output: A ist of strings containing the full path of every item in the file system, sorted alphabetically.

        Example:

        [
            "root",
            "root/docs",
            "root/docs/a.txt",
            root/pics"
        ]

        Goal: Visit every node in the tree and record its full path.

        The traversal should be preorder:

        1. Record the current node
        2. Then visit each child

        Edge cases:
        - Only the root exists -> return ["root"]
        - A folder has no children -> include the folder in the list
        - An empty folder and files exist -> include both

        Walkthrough:

        Suppose the tree is:

        root/
        |-- docs
        |  |-- a.txt
        |  |__ b.txt
        |__ pics/

        start at root
        First, record -> root

        Then, go into docs
        Record -> root/docs

        Then, visit its children
        Record -> root/docs/a.txt

        Then, record root/docs/b.txt

        Come back to root.

        Now visit pics.

        Record root/pics

        The final result:

        [
        "root",
        "root/docs",
        "root/docs/a.txt",
        "root/docs/b.txt",
        "root/pics"
        ]

        Pseudocode:
        Create an empty resukt list

        Define a recursive helper(node, current_path):
            Add current_path to the result

            For each child (in alphebetical order):
                Build the child's full path
                Recursively visit the child

        Start the recursion from the root using root

        Return the result
        """
        result = []

        def dfs(node, current_path):
            result.append(current_path)

            for name in sorted(node.children):
                child = node.children[name]
                dfs(child, f"{current_path}/{name}")

        dfs(self.root, "root")
        return result

    def max_depth(self):
        """Milestone 2. The number of nodes on the longest root-to-leaf path.

        A brand new file system (just the root) has depth 1. Counts nodes.
        """
        # TODO: implement

        """
        Input: No input parameters.

        Output: An integer representing the maximum depth of the file system.

        Goal: Return the number of nodes on the longest path from the root to any leaf.

        Remember, this project counts nodes, not edges.

        Edge case:
        - Only root exists -> return 1
        - One folder -> return 2
            e.g root/
                  |__ docs/
        
        - Nested folsers/files -> reyrn the number of nodes
            e.g root/
                  |__ docs/
                     |__ work/
                        |__ report.pdf
        
        Output here will be 4

        Walkthrough:
        Suppose the tree is:

        root/
          |-- docs/
          |   |__ report.pdf
          |___pics/

        We start at root.

        We ask: "what's the maximum depth of my children?"

        docs says: "My depth is 2" i.e (docs -> report.pdf)

        pic says: "My depth is 1"

        Since we want the longest path, root returns: 1 + max(2, 1) = 3

        So, the pattern is:
        - add the children first
        - Then combine their answers

        That is DFS Postoredr

        Pseudocode:
        Define a recursive helper(node):

            If node is empty:
                Return 0
            
            Return 1 + larger of:

                helper(left child)

                helper(right child)

        Start the recursion from the root

        Return the result

        - - -
        Since this is an n-ary tree, not a binary tree, we need to adapt it slightly:

        Define a recursive helper(node):

            If node is empty:
                return 0

            If node has no children:
                return 1

            Find the largest depth among all children

            Return 1 + that largest depth

        Start from the root

        Return the result
        """
        def dfs(node):
            if node is None:
                return 0

            if not node.children:
                return 1

            deepest = 0

            for child in node.children.values():
                deepest =  max(deepest, dfs(child))

            return 1 + deepest

        return dfs(self.root)
    

    def total_size(self, path):
        """Milestone 3. Total bytes stored at or below this path.

        A folder's size is the sum of everything inside it, all the way down.
        That is post-order thinking, and it is how the real "du" command works.
        Return -1 if the path does not exist.
        """
        # TODO: implement

        """
        Input: path: str e.g "root/docs"

        Output: an integer representing the total size of everything stored at or below that path.

        Goal:
        - If the path points to a file, return its size
        - If it points to a folder, return the sum of all files inside it (incluisng files in nested folders).
        - if the path doesn't exist, return -1.

        Edge cases:
        - Path doesn't exist -> eturn -1
        - Path is a file -> return the file's size
        - Empty folder -> return 0
        - File system contains only root
            total_size("root") == 0

        Walkthrough:
        Suppose the tree is:

        root/
        ├── docs/
        │   ├── a.txt (10)
        │   ├── b.txt (20)
        │   └── work/
        │       └── c.txt (30)
        └── pics/

        We call :

        total_size("root/docs")

        We first find the docs folder and now ask:

        How big is docs? -> You cannot answer immediately.

        Instead, ask each child: - How big are you?

        a.txt says: 10

        b.txt says: 20

        Work doesn't know yet, it asks its child:

        c.txt says: 30

        So, work returns: 30

        Now, docs finally knows:

        10 + 20 + 30 = 60

        Notice that the children answer before the parent

        That's why this is DFS Postorder

        - - -

        Pseudocode:

        Find the node for the given path.

        If the node doesn't exist:
            return -1

        Define a recursive helper(node):

            If the node is a file:
                Return its size

            total = 0

            For each child:
                total += helper(child)

            Return total

        Return helper(node)
        """
        parts = parse_path(path)
        current = self.root

        for name in parts[1:]:
            if name not in current.children:
                return -1
            current = current.children[name]

        def dfs(node):
            if node.is_file:
                return node.size
            
            total = 0

            for child in node.children.values():
                total += dfs(child)

            return total

        return dfs(current)

    def find(self, path):
        """Milestone 4. Follow the path one segment at a time.

        Return the FileNode at the end of the path, or None if any
        segment along the way does not exist. find("root") returns the root.
        A guided walk: at each step you know exactly which child to move to.
        """
        # TODO: implement

        """
        Inputh : path: str   e.g "root/docs/resume.pdf"

        Output: The filenode at the end of the path, or None if the path doesn;st exist

        Goal: Starting from the root, follow the path one segment at a time. If any segment is missing, return None.

        Edge cases:
        - "root" -> return self.root
        - Missing folder -> return None
        - Missing file -> return None
        - Existing file/folder -> return its FileNode

        Walkthrough:
        Suppose the tree is:
        root/
        |-- docs/
        |   |__ resume.pdf
        |___ pics/

        Call: find("root/docs/resume.pdf")

        Walk the path:
            root
              |
            docs
              |
            resume.pdf
        
        You successfully reach the end, now return resume.pdf

        Now, suppose you call: find("root/docs/notes.txt")

        You walk again:
            root
             |
            docs

        Then look for notes.txt

        It doesn't exist.

        Return None

        Pseudocode:

        Split the path

        Start at the root

        For each part after the "root":

            If the child doesn't exist:
                Return None
            
            Move to that child

        Return the current node
        """
        parts = parse_path(path)
        current = self.root
        for name in parts[1:]:
            if name not in current.children:
                return None

            current = current.children[name]

        return current

    def delete(self, path):
        """Milestone 5. Remove the item at this path, and everything inside it.

        Deleting a folder removes its whole subtree. Return True when
        something was deleted. Return False when the path does not exist.
        The root itself can never be deleted; return False for "root".
        """
        # TODO: implement

        """
        Input: path: str   e.g "root/docs"

        Output: A boolean value
        - True if something was deleted
        - False if:
            - the path doesn't exist, or
            - the user tries to delete "root"

        Goal: Remove the node at the given path
        - if it's a file, remove just the file
        - if it's a folder, remove the entire subtree

        Edge cases:
        - Dellete a file -> True
        - Delete. folder -> True
        - Path doesn't exist -> False
        - Delete "root" -> False
        - Delete an empty folder -> True

        Walkthrough:
        Suppose the tree is:

        root/
        |-- docs/
        |   |-- a.txt
        |   |__ work/
        |       |__ b.txt
        |__ pics/

        Now call: delete("root/docs")

        First, walk the path:
            root
             |
            docs

        But, here's the importtant realization: 
        We don't stop at docs. We want to sytop at its parent(root)

        Why? Because the deletion happens from the parent's children dictionary

        The parent currently has:

        {
            "docd":  FileNode(...),
            "pics": FileNode(...)
        }

        Deleting docs is simply:

        del parent.children("docs")

        Afterwards:
            roor/
            |__ pics/

        Everything under docs disappears automatically because nothing points to it anymore.

        Pseudocode:

        If the path is just "root":
            Return False

        Split the path

        Walk to the parent of the node to delete

        If any folder along the way doesn't exist:
            Return False

        If the item to delete doens't exist:
            Return False

        Remove it from the parent's children

        Return True
        """
        parts = parse_path(path)

        if len(parts) == 1:
            return False

        current = self.root

        for name in parts[1:-1]:

            if name not in current.children:
                return False

            current = current.children[name]

        target = parts[-1]

        if target not in current.children:
            return False

        del current.children[target]

        return True
        

    # ================= OPTIONAL STRETCH (not graded, extra credit) =================
    # These are bonus. The core project is complete without them.
    # See the "Stretch goals" section of the write-up for the full description
    # and a self-check snippet you can paste into your own editor to test them.

    def search_by_name(self, name):
        """OPTIONAL STRETCH (not graded). Find every item with this exact name.

        A full DFS: visit every node, collect the full path of every match,
        sorted alphabetically. Files and folders both count.
        Return an empty list when nothing matches.
        """
        # TODO (optional): implement

        """
        Input: str  e.g "notes.txt"

        Output: A list of full paths where that name appears, sorted alphabetically
         e.g 
         [
            "root/backup/notes.txt",
            "root/docs/notes.txt"
         ]

        Goal:
        - Visit every node in the tree
        - If a node's name matches the given name, record its full path

        Edge cases:
        - No matches -> return []
        - One match -> return a list with one path
        - Multiple matches: return all matching paths, sorted alphabetically
        - Search for "root" -> return ["root"]

        Walkthrough:
        Suppose thetree is:

        root/
        |--docs/
        |  |-- notes.txt
        |  |__ report.pdf
        |__ backup/
            |__ notes.txt

        Search for: "notes.txt"

        Start at root:
        - Is the root named "notes.txt"? No.
        - Visit docs.
        - Is docs named "notes.txt"? No.
        - Visit notes.txt. Match! Save its path.
        - Visit reprt.pdf. No match.
        - Go back
        - Visit backup
        - Visit notes.txt. Match! Save its path

        Return:
        [
            "root/backup/notes.txt"
            "root/docs/notes.txt"
        ]

        This is a DFS preorder traversal.

        Pseudocode:

        Create an empty result list

        Define a recursive helper(node, current_path):

            If node's name matches:
                Add current_path to the result

            For each child (alphabetically):
                Recursively visit every child

        Start from the root

        Return the result
        """
        result = []

        def dfs(node, current_path):
            if node.name == name:
                result.append(current_path)

            for child_name in sorted(node.children):
                child = node.children[child_name]
                dfs(child, f"{current_path}/{child_name}")

        dfs(self.root, "root")
        return result
