import rumps
import hid

class BatteryApp(rumps.App):
    def __init__(self):
        super(BatteryApp, self).__init__("", icon="headset.png")
        self.menu = [rumps.MenuItem("Update", callback=self.update_battery_status)]
        self.timer = rumps.Timer(self.update_battery_status, 1)  
        self.timer.start()
        self.last_battery_level = 100  
        self.update_battery_status()

    def find_device(self):
        target_manufacturer = "Kingston"
        target_product = "HyperX Cloud Flight Wireless"
        devices = hid.enumerate()
        for device_info in devices:
            manufacturer = device_info.get("manufacturer_string", "")
            product = device_info.get("product_string", "")
            if manufacturer == target_manufacturer and product == target_product:
                try:
                    h = hid.device()
                    h.open_path(device_info["path"])
                    return h
                except Exception as e:
                    print(f"Error opening device: {e}")
                    continue
        return None

    def battery_percent(self, charge_state, value):
        ranges = {
            0x0E: [(89, 10), (119, 15), (148, 20), (159, 25), (169, 30), (179, 35),
                   (189, 40), (199, 45), (209, 50), (219, 55), (239, 60), (255, 65)],
            0x0F: [(19, 70), (49, 75), (69, 80), (99, 85), (119, 90), (129, 95), (255, 100)]
        }
        for max_val, percent in ranges.get(charge_state, []):
            if value <= max_val:
                return percent
        return 0

    def read_battery(self, device):
        if not device:
            return None
        try:
            device.write([0x21, 0xFF, 0x05])
            data = device.read(128, timeout_ms=5000)
            if len(data) < 5:
                return None
            charge_state, value = data[3], data[4]
            return self.battery_percent(charge_state, value)
        except Exception as e:
            return None

    def get_icon(self, battery_level):
        level_ranges = [
            (10, "battery-00.png"), (20, "battery-20.png"),
            (40, "battery-40.png"), (60, "battery-60.png"),
            (80, "battery-80.png"), (100, "battery-100.png")
        ]
        for max_level, icon_path in level_ranges:
            if battery_level <= max_level:
                return icon_path
        return "battery-100.png"

    def update_battery_status(self, _=None):
        device = self.find_device()
        if device:
            battery_level = self.read_battery(device)
            if battery_level is not None:
                if battery_level < self.last_battery_level:
                    self.last_battery_level = battery_level
                icon_path = self.get_icon(self.last_battery_level)
                self.icon = icon_path
                self.title = f"~{self.last_battery_level}%"
            device.close()
        else:
            self.icon = "offline.png"
            self.title = ""

if __name__ == "__main__":
    app = BatteryApp()
    app.run()
