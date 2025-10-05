# Unpacking variables from lists, tuples, and dictionaries

vals = [5,10,15,20,25]
# the * in assignment is starred unpacking. It means: “grab all remaining items here and put them into a list.”
a, b, *rest = vals
print(a,b,rest)

data = {'x':1, 'y':2, 'z':3}
x, y, z = data.values()
print(x,y,z)

# 📦 Telemetry “Packet” Decoder (dict + nested/variable unpack)
# Each packet is a dict with required keys and optional extras. Values are mixed: some tuples, some lists.

packets = [
    {
        "id": 101,
        "stamp": (2025, 7, 9, 6, 45, 3),        # (Y,M,D,h,m,s)
        "path":  ["towers", "T2", "sensors", "EC", "raw", "ch1", "ch2"],
        "vals":  (1.92, 1.88, 1.91),            # tuple of floats
        "meta":  {"site": "GH-North", "ok": True},   # may contain extra keys
    },
    {
        "id": 102,
        "stamp": (2025, 7, 9, 6, 47, 0),
        "path":  ["towers", "T0", "sensors", "pH", "raw"],
        "vals":  (6.1, 6.2),
        "meta":  {"site": "GH-North", "ok": False, "reason": "drift"},
    },
]


# Your goals (use unpacking smartly; avoid index soup):

# Destructure the path as:
# root, tower, _, sensor, *rest = packet["path"]

# Expect root == "towers", tower like "T2", sensor in {"EC","pH",...}.

# *rest gathers variable tail ("raw", "ch1", ...).

# Unpack the timestamp tuple:
# Y, M, D, h, m, s = packet["stamp"] and build YYYY-MM-DD HH:MM:SS.

# Unpack values flexibly:
# v1, *vrest = packet["vals"]

# Produce a display string:
# If only 1 value → v1
# If 2 → v1, last
# If ≥3 → v1, ..., last (use *mid, last = vrest when needed)

# Safely extract dict fields in order (even if extras exist):
# Build (site, ok) using ordered key selection—don’t rely on values() order.
# (Think: (packet["meta"][k] for k in ("site","ok")) or itemgetter.)

# Print one line per packet with aligned columns and a compact path tail:

# 101  2025-07-09 06:45:03  T2  EC   raw/ch1/ch2   1.92,...,1.91   GH-North  OK


# Join rest with slashes; show OK/FAIL from ok.
# Use width/alignment with f-strings (e.g., id right 4, tower 3, sensor 4, tail 15, values 14, site 10).

# Acceptance checks:
# Uses starred unpacking both for path and for vals.
# Never indexes with magic numbers like path[0] in your final version.
# “Values” field respects the 1/2/≥3 display rule.
# Works if a packet appends extra keys in meta (you only pull named ones).

print(f"{"ID":^5} {"STAMP":^25} {"TOWER":^9} {"SENSOR":^8} {"REST":^15} {"VALUES":^15} {"SITE":^10} {"OK_STATUS":^10}")

for item in packets:
    Y, M, D, h, m, s = item["stamp"]
    datestring = f"{Y}-{M}-{D} {h}:{m}:{s}"
    root, tower, _, sensor, *rest = item["path"]
    reststring = " ".join(rest)


    v1, *vrest = item["vals"]
    *mid, last = vrest

    metadata = item["meta"]
    site, ok, *reason = metadata
    valstring = ""

    if len(item["vals"]) == 1:
        printvals = v1
    elif len(item["vals"]) == 2:
        printvals = [v1, last]
        # for a in printvals:
        #     valstring = valstring + f"{a} "
        strconv = [str(x) for x in printvals]
        valstring = " ".join(strconv)
    else:
        printvals = [v1, *mid, last]
        # for a in printvals:
        #     if isinstance(a, list):
        #         for b in a:
        #             valstring = valstring + f"{b} "
        #     else:
        #         valstring = valstring + f"{a} "
        flatlist = [str(x) for a in printvals for x in (a if isinstance(a,list) else [a])]
        valstring = " ".join(flatlist)

    print(f"{item["id"]:<5} {datestring:<25} {tower:<9} {sensor:<8} {reststring:<15} {valstring:<15} {site:<10} {ok:<10}")

    

# print(f"{root}")

# root, tower, _, sensor, *rest = packets["path"]
# Y, M, D, h, m, s = packets['stamp']
# v1, *vrest = packets['vals']
# *mid, last = vrest
