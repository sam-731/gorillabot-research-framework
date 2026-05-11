def classify_attack(pkt_size, proto):
    if proto == "UDP" and pkt_size > 1200:
        return "udp_plain"

    if proto == "TCP":
        return "tcp_syn"

    return "unknown"
