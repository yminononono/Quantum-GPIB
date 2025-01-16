import pyvisa, time, copy
rm = pyvisa.ResourceManager()
gpib_address = "GPIB0::1::INSTR"
for resource in rm.list_resources():
    if "GPIB" in resource:
        print("GPIB address : ", resource)
        gpib_address = copy.copy(resource)
device=rm.open_resource(gpib_address)
# device.query("IDN?")

device.query("I1") # 1mA range
device.query("D0.0000")
device.query("E") # Operation mode
for i in range(10):
    device.query("K0") # Increment first digit  (corresponds to 100nA in 1mA range)
    # device.query("K1") # Increment second digit (corresponds to 1mA in 1mA range)
    # device.query("K2") # Increment third digit  (corresponds to 10mA in 1mA range)
    time.sleep(1)
device.query("H") # Standby mode
device.query("C") # Reset
