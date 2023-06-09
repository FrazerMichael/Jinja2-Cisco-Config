import jinja2

routers = [
    {"hostname": "R1", "interfaces" : [
        {"ip": "81.81.0.1", "netmask": "255.255.255.255", "wc-mask": "0.0.0.0", "area": "1"},
        {"ip": "81.0.0.2", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "0"},
        {"ip": "81.0.0.9", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "1"},
        {"ip": "81.0.0.13", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "1"},
        {"ip": "81.0.0.17", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "0"},
    ]},
    {"hostname": "R2", "interfaces" : [
        {"ip": "81.81.0.2", "netmask": "255.255.255.255", "wc-mask": "0.0.0.0", "area": "2"},
        {"ip": "81.0.0.6", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "0"},
        {"ip": "81.0.0.21", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "2"},
        {"ip": "81.0.0.25", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "2"},
        {"ip": "81.0.0.18", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "0"},
    ]},
    {"hostname": "R3", "interfaces" : [
        {"ip": "81.81.0.3", "netmask": "255.255.255.255", "wc-mask": "0.0.0.0", "area": "1"},
        {"ip": "81.0.0.10", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "1"},
        {"ip": "81.0.0.29", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "1"},
        {"ip": "81.0.0.33", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "1"},
        {"ip": "81.0.0.37", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "1"},
        {"ip": "81.0.0.41", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "1"},
    ]},
    {"hostname": "R4", "interfaces" : [
        {"ip": "81.81.0.4", "netmask": "255.255.255.255", "wc-mask": "0.0.0.0", "area": "1"},
        {"ip": "81.0.0.42", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "1"},
        {"ip": "81.0.0.45", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "1"},
        {"ip": "81.0.0.49", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "1"},
        {"ip": "81.0.0.53", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "1"},
        {"ip": "81.0.0.22", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "2"},
    ]},
    {"hostname": "R5", "interfaces" : [
        {"ip": "81.81.0.5", "netmask": "255.255.255.255", "wc-mask": "0.0.0.0", "area": "2"},
        {"ip": "81.0.0.14", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "1"},
        {"ip": "81.0.0.57", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "2"},
        {"ip": "81.0.0.61", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "2"},
        {"ip": "81.0.0.65", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "2"},
        {"ip": "81.0.0.69", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "2"},
    ]},
    {"hostname": "R6", "interfaces" : [
        {"ip": "81.81.0.6", "netmask": "255.255.255.255", "wc-mask": "0.0.0.0", "area": "2"},
        {"ip": "81.0.0.26", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "2"},
        {"ip": "81.0.0.70", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "2"},
        {"ip": "81.0.0.73", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "2"},
        {"ip": "81.0.0.77", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "2"},
        {"ip": "81.0.0.81", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "2"},
    ]},
    {"hostname": "R7", "interfaces" : [
        {"ip": "81.81.0.7", "netmask": "255.255.255.255", "wc-mask": "0.0.0.0", "area": "1"},
        {"ip": "81.0.0.38", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "1"},
        {"ip": "81.0.0.54", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "1"},
        {"ip": "11.81.0.1", "netmask": "255.255.255.0", "wc-mask": "0.0.0.255", "area": "1"},
    ]},
    {"hostname": "R8", "interfaces" : [
        {"ip": "81.81.0.8", "netmask": "255.255.255.255", "wc-mask": "0.0.0.0", "area": "2"},
        {"ip": "81.0.0.58", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "2"},
        {"ip": "81.0.0.82", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "2"},
        {"ip": "11.81.1.1", "netmask": "255.255.255.0", "wc-mask": "0.0.0.255", "area": "2"},
    ]},
    {"hostname": "R9", "interfaces" : [
        {"ip": "81.81.0.9", "netmask": "255.255.255.255", "wc-mask": "0.0.0.0", "area": "1"},
        {"ip": "81.0.0.30", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "1"},
        {"ip": "81.0.0.46", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "1"},
        {"ip": "11.81.2.1", "netmask": "255.255.255.0", "wc-mask": "0.0.0.255", "area": "1"},
    ]},
    {"hostname": "R10", "interfaces" : [
        {"ip": "81.81.0.10", "netmask": "255.255.255.255", "wc-mask": "0.0.0.0", "area": "2"},
        {"ip": "81.0.0.62", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "2"},
        {"ip": "81.0.0.78", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "2"},
        {"ip": "11.81.3.1", "netmask": "255.255.255.0", "wc-mask": "0.0.0.255", "area": "2"},
    ]},
    {"hostname": "R11", "interfaces" : [
        {"ip": "81.81.0.11", "netmask": "255.255.255.255", "wc-mask": "0.0.0.0", "area": "2"},
        {"ip": "81.0.0.66", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "2"},
        {"ip": "81.0.0.74", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "2"},
        {"ip": "11.81.4.1", "netmask": "255.255.255.0", "wc-mask": "0.0.0.255", "area": "2"},
    ]},
    {"hostname": "R12", "interfaces" : [
        {"ip": "81.81.0.12", "netmask": "255.255.255.255", "wc-mask": "0.0.0.0", "area": "1"},
        {"ip": "81.0.0.34", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "1"},
        {"ip": "81.0.0.50", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "1"},
        {"ip": "11.81.5.1", "netmask": "255.255.255.0", "wc-mask": "0.0.0.255", "area": "1"},
    ]},
    {"hostname": "R13", "interfaces" : [
        {"ip": "81.81.0.13", "netmask": "255.255.255.255", "wc-mask": "0.0.0.0", "area": "0"},
        {"ip": "81.0.0.1", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "0"},
        {"ip": "81.0.0.5", "netmask": "255.255.255.252", "wc-mask": "0.0.0.3", "area": "0"}
    ]}
]

interfaceLabels = ["loopback0", "g0/0", "g1/0", "g2/0", "g3/0", "g4/0"]

environment = jinja2.Environment(loader=jinja2.FileSystemLoader("templates/"))
template = environment.get_template("cisco-config.txt")

for router in routers:
    filename = f"config_{router['hostname']}.txt"
    content = template.render(
        router,
        hostname = router['hostname'],
        interfaceLabels = interfaceLabels
    )
    with open(filename, mode="w", encoding="utf-8") as blah:
        blah.write(content)
        print(f"... wrote {filename}")