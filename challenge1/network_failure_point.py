class Network:
    def __init__(self) -> None:
        self.routers: dict[int, 'Router'] = {}

    def add_router(self, label: int) -> 'Router':
        self.routers[label] = Router(label)
        return self.routers[label]

    def add_connection(self, from_label: int, to_label: int) -> None:
        source_router = self.routers.get(from_label) or self.add_router(from_label)
        dest_router = self.routers.get(to_label) or self.add_router(to_label)

        source_router.outbound_links += 1
        dest_router.inbound_links += 1


class Router:
    def __init__(self, label: int) -> None:
        self.label = label
        self.inbound_links = 0
        self.outbound_links = 0

    @property
    def total_connections(self) -> int:
        return self.inbound_links + self.outbound_links


def identify_router(network: Network) -> list[int]:
    """This function identifies the router(s) with the maximum number of connections in a given network.

    Note:
        If multiple routers have the same maximum number of connections, all of their labels are included in the list.

    Params:
        network (Network): The network object which contains information about all the routers.

    Returns:
        list[int]: A list of router labels that have the maximum number of connections.
    """
    max_connections = 0
    routers: list[int] = []

    for _, router in network.routers.items():
        if router.total_connections > max_connections:
            max_connections = router.total_connections
            routers = [router.label]

        elif router.total_connections == max_connections:
            routers.append(router.label)

    return routers

