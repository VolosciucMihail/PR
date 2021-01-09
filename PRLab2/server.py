import lib as protocol

if __name__ == "__main__":
    n = 22
    g = 42
    # x = random.random()
    # initKey = (g**x) % n

    server_handler = protocol.server_socket("localhost", 50)

    # listening for connections
    protocol.receive(server_handler)
    # computedKey = (float(protocol.receive(proto_handler))**x) % n

    value = 'Message №1'
    print(value)

    protocol.send(server_handler, value)
    value = protocol.receive(server_handler)
    print(value)

    value = 'Message №3'
    protocol.send(server_handler, value)
    val_new = protocol.receive(server_handler)
    print(val_new)
