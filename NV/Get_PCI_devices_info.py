import subprocess

def get_pci_device_info(pci_device):
    device_info = {}
    device_info['lspci_info'] = subprocess.check_output(f"lspci -s {pci_device}", shell=True).decode().strip()
    device_info['physical_slot'] = subprocess.check_output(f"lspci -s {pci_device} -vvv | grep 'Physical Slot:' | sed 's/^[ \\t]*//g'", shell=True).decode().strip()
    device_info['lnkcap_info'] = subprocess.check_output(f"lspci -s {pci_device} -vvv | gawk '/LnkCap:/ {{print$1,$4,$5,$6,$7}}'", shell=True).decode().strip()
    device_info['lnksta_info'] = subprocess.check_output(f"lspci -s {pci_device} -vvv | gawk '/LnkSta:/ {{print$1,$2,$3,$4,$5,$6,$7}}'", shell=True).decode().strip()
    device_info['devsta_info'] = subprocess.check_output(f"lspci -s {pci_device} -vvv | grep 'DevSta' | sed 's/^[ \\t]*//g' | cut -d ' ' -f 1-3 | grep -v '+'", shell=True).decode().strip()
    device_info['err_info'] = subprocess.check_output(f"lspci -s {pci_device} -vvv | grep 'DevSta' | sed 's/^[ \\t]*//g' | cut -d ' ' -f 1-3 | grep 'CorrErr+\\|NonFatalErr-\\|FatalErr-'", shell=True).decode().strip()
    device_info['cesta_info'] = subprocess.check_output(f"lspci -s {pci_device} -vvv | grep 'CESta' | sed 's/^[ \\t]*//g'", shell=True).decode().strip()
    device_info['kernel_info'] = subprocess.check_output(f"lspci -s {pci_device} -vvv | grep 'Kernel' | sed 's/^[ \\t]*//g'", shell=True).decode().strip()
    return device_info

def main():
    pci_devices = ["00:00.0", "00:01.0", "00:02.0"]  # 示例PCI设备地址列表
    for pci_device in pci_devices:
        try:
            pci_device_info = get_pci_device_info(pci_device)
            print("======================================================================================")
            print()
            print(pci_device_info['lspci_info'])
            print(pci_device_info['physical_slot'])
            print(pci_device_info['lnkcap_info'])
            print(pci_device_info['lnksta_info'])
            print(pci_device_info['devsta_info'])
            print(pci_device_info['err_info'])
            print(pci_device_info['cesta_info'])
            print(pci_device_info['kernel_info'])
            print()
            print("======================================================================================")
        except Exception as e:
            print(f"Error processing PCI device {pci_device}: {e}")

if __name__ == "__main__":
    main()
