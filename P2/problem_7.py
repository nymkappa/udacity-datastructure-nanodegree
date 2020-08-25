# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, path, handler):
        # Initialize the node with children as before, plus a handler
        self.path = path
        self.handler = handler
        self.children = []

    def insert(self, path, handler):
        # Insert the node as before
        # print("RouteTrieNode::insert, current: '{0}', path: '{1}', handler: '{2}'".format(self.path, path, handler))
        new_child = RouteTrieNode(path, handler)
        self.children.append(new_child)
        return new_child


    def find_child(self, path):
        idx = 0
        while idx < len(self.children):
            if self.children[idx].path == path:
                return idx
            idx += 1

        return None


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page nodes
        self.root = RouteTrieNode(root, root_handler)


    def insert(self, parts, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        idx = 0
        current_node = self.root
        while idx < len(parts):
            # print("=> Looking for '{0}' in node '{1}'".format(parts[idx], current_node.path))
            match_idx = current_node.find_child(parts[idx])
            if match_idx is None:
                # print("'{0}' not found, adding it".format(parts[idx]))
                current_node = current_node.insert(parts[idx], (handler if idx == len(parts) - 1 else None))
            else:
                # print("'{0}' found, go deeper")
                current_node = current_node.children[match_idx]
            idx += 1

        # print()

    def find(self, parts):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        idx = 0
        current_node = self.root
        while idx < len(parts):
            match_idx = current_node.find_child(parts[idx])
            if match_idx is None:
                return None
            else:
                current_node = current_node.children[match_idx]
            idx += 1

        return current_node.handler


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routes = RouteTrie("/", root_handler)
        self.not_found_handler = not_found_handler


    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        parts = self.split_path(path)
        self.routes.insert(parts, handler)


    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        parts = self.split_path(path)
        handler = self.routes.find(parts)
        if handler is None:
            return self.not_found_handler
        else:
            return handler


    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return [part for part in path.split("/") if part != '']


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/about/us", "about us handler")  # add a route
router.add_handler("/account/me", "my account handler")  # add a route
router.add_handler("/account/me/login", "my account login handler")  # add a route
router.add_handler("/test1/test2/test3/test4", "test handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/us")) # should print 'about us handler'
print(router.lookup("/account/me")) # should print 'my account handler'
print(router.lookup("/account/me/login")) # should print 'my account login handler'
print(router.lookup("/test1/test2/test3/test4")) # should print 'test handler'
print(router.lookup("/test1/test2")) # should print 'not found handler'
