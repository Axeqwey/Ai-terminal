import psutil

def get_disk_info():
    info = {}
    for disk in psutil.disk_partitions():
        usage = psutil.disk_usage(disk.mountpoint)
        info[disk.mountpoint] =  {
            "used": usage.used,
            "total": usage.total,
            "percent": usage.percent,
            "free": usage.free,

        }
    return info
