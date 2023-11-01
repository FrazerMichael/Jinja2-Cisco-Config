import jinja2

routers = [
    {"hostname": "R1", "AS": "6939", "interfaces" : [
        {"ip": "10.5.1.1", "netmask": "255.255.255.255", "interface": "lo0"},
        {"ip": "10.5.14.1", "netmask": "255.255.255.252", "interface": "f1/0"}
        ],
        "advertising" : [
        {"ip": "23.26.128.", "netmask": "255.255.255.0"},
        {"ip": "50.58.3.", "netmask": "255.255.255.0"},
        {"ip": "50.58.4.", "netmask": "255.255.255.0"},
        {"ip": "27.50.32.", "netmask": "255.255.248.0"},
        {"ip": "64.62.128.", "netmask": "255.255.192.0"},
        {"ip": "65.49.104.", "netmask": "255.255.252.0"},
        {"ip": "65.49.108.", "netmask": "255.255.252.0"},
        {"ip": "66.220.0.", "netmask": "255.255.224.0"},
        {"ip": "74.82.48.", "netmask": "255.255.252.0"},
        {"ip": "184.104.176.", "netmask": "255.255.248.0"},
        {"ip": "184.105.100.", "netmask": "255.255.252.0"}
        ],
        "neighbors": [
            {"ip": "10.5.14.2", "AS": "7311"}
    ]},
    {"hostname": "R2", "AS": "3356", "interfaces" : [
        {"ip": "10.5.2.2", "netmask": "255.255.255.255", "interface": "lo0"},
        {"ip": "10.5.24.1", "netmask": "255.255.255.252", "interface": "f2/0"},
        {"ip": "10.5.25.1", "netmask": "255.255.255.252", "interface": "f3/0"}
        ],
        "advertising" : [
        {"ip": "4.0.0.", "netmask": "255.128.0.0"},
        {"ip": "4.55.0.", "netmask": "255.255.0.0"},
        {"ip": "8.0.0.", "netmask": "255.128.0.0"},
        {"ip": "8.16.0.", "netmask": "255.240.0.0"},
        {"ip": "8.4.162.", "netmask": "255.255.255.0"},
        {"ip": "8.5.160.", "netmask": "255.255.255.0"},
        {"ip": "24.75.64.", "netmask": "255.255.224.0"},
        {"ip": "24.75.128.", "netmask": "255.255.240.0"}
        ],
        "neighbors": [
            {"ip": "10.5.24.2", "AS": "7311"},
            {"ip": "10.5.25.2", "AS": "19930"}
    ]},
    {"hostname": "R3", "AS": "7018", "interfaces" : [
        {"ip": "10.5.3.3", "netmask": "255.255.255.255", "interface": "lo0"},
        {"ip": "10.5.35.1", "netmask": "255.255.255.252", "interface": "f1/0"}
        ],
        "advertising" : [
        {"ip": "12.0.0.", "netmask": "255.0.0.0"},
        {"ip": "12.128.0.", "netmask": "255.128.0.0"},
        {"ip": "12.66.80.", "netmask": "255.255.255.0"},
        {"ip": "12.66.48.", "netmask": "255.255.248.0"},
        {"ip": "12.66.58.", "netmask": "255.255.254.0"},
        {"ip": "32.128.0.", "netmask": "255.240.0.0"},
        {"ip": "32.255.0.", "netmask": "255.255.0.0"},
        {"ip": "45.40.123.", "netmask": "255.255.255.0"}
        ],
        "neighbors": [
            {"ip": "10.5.35.2", "AS": "19930"}
    ]},
    {"hostname": "R4", "AS": "7311", "interfaces" : [
        {"ip": "10.5.4.4", "netmask": "255.255.255.255", "interface": "lo0"},
        {"ip": "10.5.14.2", "netmask": "255.255.255.252", "interface": "f1/0"},
        {"ip": "10.5.24.2", "netmask": "255.255.255.252", "interface": "f2/0"},
        {"ip": "10.5.46.1", "netmask": "255.255.255.252", "interface": "f3/0"},
        {"ip": "10.5.48.1", "netmask": "255.255.255.252", "interface": "f5/0"}
        ],
        "advertising" : [
        {"ip": "24.104.160.", "netmask": "255.255.240.0"},
        {"ip": "24.104.176.", "netmask": "255.255.254.0"},
        {"ip": "24.104.178.", "netmask": "255.255.255.0"},
        {"ip": "24.104.180.", "netmask": "255.255.254.0"}
        ],
        "neighbors": [
            {"ip": "10.5.14.1", "AS": "6939"},
            {"ip": "10.5.24.1", "AS": "3356"},
            {"ip": "10.5.48.2", "AS": "65051"},
            {"ip": "10.5.46.2", "AS": "5664"}
    ]},
    {"hostname": "R5", "AS": "19930", "interfaces" : [
        {"ip": "10.5.5.5", "netmask": "255.255.255.255", "interface": "lo0"},
        {"ip": "10.5.35.2", "netmask": "255.255.255.252", "interface": "f1/0"},
        {"ip": "10.5.56.1", "netmask": "255.255.255.252", "interface": "f2/0"},
        {"ip": "10.5.25.2", "netmask": "255.255.255.252", "interface": "f3/0"},
        {"ip": "10.5.51.1", "netmask": "255.255.255.252", "interface": "f5/0"}
        ],
        "advertising" : [
        {"ip": "142.215.192.", "netmask": "255.255.248.0"},
        {"ip": "142.215.16.", "netmask": "255.255.252.0"},
        {"ip": "142.215.198.", "netmask": "255.255.255.0"},
        {"ip": "155.204.152.", "netmask": "255.255.248.0"},
        {"ip": "198.32.106.", "netmask": "255.255.255.0"}
        ],
        "neighbors": [
            {"ip": "10.5.35.1", "AS": "7018"},
            {"ip": "10.5.25.1", "AS": "3356"},
            {"ip": "10.5.51.2", "AS": "65053"},
            {"ip": "10.5.56.2", "AS": "5664"}
    ]},
    {"hostname": "R6", "AS": "5664", "interfaces" : [
        {"ip": "10.5.6.6", "netmask": "255.255.255.255", "interface": "lo0"},
        {"ip": "10.5.67.1", "netmask": "255.255.255.252", "interface": "f0/0"},
        {"ip": "10.5.56.2", "netmask": "255.255.255.252", "interface": "f2/0"},
        {"ip": "10.5.46.2", "netmask": "255.255.255.252", "interface": "f3/0"}
        ],
        "advertising" : [],
        "neighbors": [
            {"ip": "10.5.56.1", "AS": "19930"},
            {"ip": "10.5.46.1", "AS": "7311"},
            {"ip": "10.5.67.2", "AS": "65050"}
    ]},
    {"hostname": "R7", "AS": "65050", "interfaces" : [
        {"ip": "10.5.7.7", "netmask": "255.255.255.255", "interface": "lo0"},
        {"ip": "10.5.67.2", "netmask": "255.255.255.252", "interface": "f0/0"}
        ],
        "advertising" : [],
        "neighbors": [
            {"ip": "10.5.67.1", "AS": "5664"}
    ]
    }
]

environment = jinja2.Environment(loader=jinja2.FileSystemLoader("templates/"))
template = environment.get_template("internet-config.txt")

for router in routers:
    filename = f"config_{router['hostname']}.txt"
    content = template.render(
        router,
        hostname = router['hostname']
    )
    with open(filename, mode="w", encoding="utf-8") as blah:
        blah.write(content)
        print(f"... wrote {filename}")