# agent/info.py
import psutil
import platform

def cpu():
    """
    Display detailed information about the system's CPU.

    Returns:
        - Number of physical and logical cores
        - Max frequency
        - Current utilization percentage

    Example:
        >>> agent.info.cpu()
        physical_cores: 8
        total_cores: 16
        max_frequency: 4500.00 MHz
        usage_percent: 23%
    """
    info = {
        "physical_cores": psutil.cpu_count(logical=False),
        "total_cores": psutil.cpu_count(logical=True),
        "max_frequency": f"{psutil.cpu_freq().max:.2f} MHz",
        "usage_percent": f"{psutil.cpu_percent(interval=1)}%",
    }
    for k, v in info.items():
        print(f"{k}: {v}")


def ram():
    """
    Display detailed memory (RAM) usage statistics.

    Returns:
        - Total memory (GB)
        - Available memory (GB)
        - Usage percentage

    Example:
        >>> agent.info.ram()
        Total: 16.00 GB
        Available: 8.32 GB
        Used: 48%
    """
    mem = psutil.virtual_memory()
    print(f"Total: {mem.total / (1024 ** 3):.2f} GB")
    print(f"Available: {mem.available / (1024 ** 3):.2f} GB")
    print(f"Used: {mem.percent}%")


def system():
    """
    Display operating system and platform details.

    Returns:
        - OS name, release, version, node name, and processor info

    Example:
        >>> agent.info.system()
        System: Linux
        Node Name: workstation
        Release: 6.9.12
        Version: #1 SMP PREEMPT_DYNAMIC
        Processor: AMD Ryzen 7 7840HS
    """
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Processor: {platform.processor()}")
