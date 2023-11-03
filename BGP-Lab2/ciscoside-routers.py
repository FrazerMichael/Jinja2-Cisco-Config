import jinja2

routers = [
    {"hostname": "R8", "AS": "65051", "interfaces" : [
        {"ip": "10.5.8.8", "netmask": "255.255.255.255", "interface": "lo0"},
        {"ip": "10.5.108.1", "netmask": "255.255.255.252", "interface": "f0/0"},
        {"ip": "10.5.89.1", "netmask": "255.255.255.252", "interface": "f1/0"},
        {"ip": "144.5.96.1", "netmask": "255.255.240.0", "interface": "f2/0"},
        {"ip": "144.5.64.1", "netmask": "255.255.224.0", "interface": "f3/0"},
        {"ip": "144.5.0.1", "netmask": "255.255.192.0", "interface": "f4/0"},
        {"ip": "10.5.48.2", "netmask": "255.255.255.252", "interface": "f5/0"}
        ],
        "advertising" : [
        {"ip": "144.5.96.0", "netmask": "255.255.240.0"},
        {"ip": "144.5.64.0", "netmask": "255.255.224.0"},
        {"ip": "144.5.0.0", "netmask": "255.255.192.0"},
        ],
        "neighbors": [
            {"ip": "10.5.108.2", "AS": "65051"},
            {"ip": "10.5.89.2", "AS": "65051"},
            {"ip": "10.5.48.1", "AS": "7311"}
    ]},
    {"hostname": "R9", "AS": "65051", "interfaces" : [
        {"ip": "10.9.9.9", "netmask": "255.255.255.255", "interface": "lo0"},
        {"ip": "10.5.89.2", "netmask": "255.255.255.252", "interface": "f1/0"},
        {"ip": "10.5.109.1", "netmask": "255.255.255.252", "interface": "f2/0"},
        {"ip": "10.5.119.1", "netmask": "255.255.255.252", "interface": "f0/0"}
        ],
        "advertising" : [],
        "neighbors": [
            {"ip": "10.5.89.1", "AS": "65051"},
            {"ip": "10.5.109.2", "AS": "65051"},
            {"ip": "10.5.119.2", "AS": "65052"}
    ]},
    {"hostname": "R10", "AS": "65051", "interfaces" : [
        {"ip": "10.5.10.10", "netmask": "255.255.255.255", "interface": "lo0"},
        {"ip": "10.5.108.2", "netmask": "255.255.255.252", "interface": "f0/0"},
        {"ip": "10.5.109.2", "netmask": "255.255.255.252", "interface": "f2/0"},
        {"ip": "10.5.102.1", "netmask": "255.255.255.252", "interface": "f1/0"}
        ],
        "advertising" : [],
        "neighbors": [
            {"ip": "10.5.108.1", "AS": "65051"},
            {"ip": "10.5.109.1", "AS": "65051"},
            {"ip": "10.5.102.2", "AS": "65052"}
    ]},
    {"hostname": "R11", "AS": "65052", "interfaces" : [
        {"ip": "10.5.11.11", "netmask": "255.255.255.255", "interface": "lo0"},
        {"ip": "10.5.119.2", "netmask": "255.255.255.252", "interface": "f0/0"},
        {"ip": "10.5.112.1", "netmask": "255.255.255.252", "interface": "f2/0"},
        {"ip": "10.5.113.1", "netmask": "255.255.255.252", "interface": "f1/0"},
        {"ip": "144.5.120.1", "netmask": "255.255.252.0", "interface": "f3/0"}
        ],
        "advertising" : [
        {"ip": "144.5.120.0", "netmask": "255.255.252.0"}
        ],
        "neighbors": [
            {"ip": "10.5.119.1", "AS": "65051"},
            {"ip": "10.5.112.2", "AS": "65052"},
            {"ip": "10.5.113.2", "AS": "65052"}
    ]},
    {"hostname": "R12", "AS": "65052", "interfaces" : [
        {"ip": "10.5.12.12", "netmask": "255.255.255.255", "interface": "lo0"},
        {"ip": "10.5.112.2", "netmask": "255.255.255.252", "interface": "f2/0"},
        {"ip": "10.5.102.2", "netmask": "255.255.255.252", "interface": "f1/0"},
        {"ip": "10.5.123.1", "netmask": "255.255.255.252", "interface": "f0/0"},
        {"ip": "144.5.112.1", "netmask": "255.255.248.0", "interface": "f3/0"}
        ],
        "advertising" : [
        {"ip": "144.5.112.0", "netmask": "255.255.248.0"}
        ],
        "neighbors": [
            {"ip": "10.5.102.1", "AS": "65051"},
            {"ip": "10.5.112.1", "AS": "65052"},
            {"ip": "10.5.123.2", "AS": "65052"}
    ]},
    {"hostname": "R13", "AS": "65052", "interfaces" : [
        {"ip": "10.5.13.13", "netmask": "255.255.255.255", "interface": "lo0"},
        {"ip": "10.5.113.2", "netmask": "255.255.255.252", "interface": "f1/0"},
        {"ip": "10.5.123.2", "netmask": "255.255.255.252", "interface": "f0/0"},
        {"ip": "144.5.127.1", "netmask": "255.255.255.0", "interface": "f2/0"},
        {"ip": "144.5.126.1", "netmask": "255.255.255.0", "interface": "f3/0"},
        {"ip": "144.5.124.1", "netmask": "255.255.254.0", "interface": "f4/0"}
        ],
        "advertising" : [
        {"ip": "144.5.124.0", "netmask": "255.255.254.0"},
        {"ip": "144.5.126.0", "netmask": "255.255.255.0"},
        {"ip": "144.5.127.0", "netmask": "255.255.255.0"}
        ],
        "neighbors": [
            {"ip": "10.5.113.1", "AS": "65052"},
            {"ip": "10.5.123.1", "AS": "65052"}
    ]}
]

environment = jinja2.Environment(loader=jinja2.FileSystemLoader("templates/"))
template = environment.get_template("ciscoside-config.txt")

for router in routers:
    filename = f"config_{router['hostname']}.txt"
    content = template.render(
        router,
        hostname = router['hostname']
    )
    with open(filename, mode="w", encoding="utf-8") as blah:
        blah.write(content)
        print(f"... wrote {filename}")