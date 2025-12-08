import socket

import psutil


def get_network_info():
    info = {}
    info['hostname'] = socket.gethostname()
    try:
        info["local_ip"] = socket.gethostbyname(info["hostname"])
    except:
        info["local_ip"] = "Не удалось получить"

    # Сетевая активность
    net = psutil.net_io_counters()
    info["bytes_sent"] = net.bytes_sent
    info["bytes_recv"] = net.bytes_recv

    return info
