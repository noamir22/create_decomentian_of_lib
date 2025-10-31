files:
```
agent
├── agent\info.py
├── agent\__init__.py
```

commands:

<details>
<summary><code>agent.info.cpu?</code></summary>

```
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
```
</details>

<details>
<summary><code>agent.info.ram?</code></summary>

```
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
```
</details>

<details>
<summary><code>agent.info.system?</code></summary>

```
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
```
</details>

