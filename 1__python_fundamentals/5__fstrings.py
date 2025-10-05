# Using f-strings 

name = "Alice"
score = 95.1
date = "2025-07-09"
print(f"{name} scored {score}% on {date}")

val = 3.1415926
print(f"Pi rounded: {val:.2f}")

# Column alignment width and thousand separators
# items is a list of tuples
items =  [
    ("GPU RTX 5090", 1999.9, 2),
    ("NVMe 8GB", 649.49, 1),
    ("Case Fans", 12.5, 6)
]

print(f"{"Item":<15} {"Qty":>3} {"Price":>10} {"Subtotal":>12}")
for name,price,qty in items:
    print(f"{name:<15} {qty:>3d} {price:>10,.2f} {price*qty:>12,.2f}")  #< means left align, 15 means use a width of 15 chars
total =sum(price*qty for _,price,qty in items)                          #.2f means round off to 2 decimals
print(f"{"Total":<30}{total:>13,.2f}")

# Datetime formatting
from datetime import datetime, timezone, timedelta

dt = datetime(2025,7,9,16,45,3, tzinfo=timezone(timedelta(hours=2)))    #UTC(+02:00) timedelta(hours=2) gives a fixed offset of 2 hrs UTC +02:00
deadline = datetime(2025,7,15,9,0, tzinfo=timezone.utc)

# %A and %B - Day and month in words, %d,%m,%Y - date in numbers, %H,%M,%S - time in numbers, %Z - Timezone type, %z - Timezone in numbers (+02:00)
print(f"Local:            {dt:%A, %d %B %Y at %H:%M:%S %Z (UTC%z)}")
print(f"UTC:              {dt.astimezone(timezone.utc):%Y-%m-%d %H:%M:%S %Z}")
print(f"Time to deadline: {(deadline - dt.astimezone(timezone.utc)).days}")     # Here dt is converted to UTC format to calculate

# Debug prints, numeric bases, scientific and percent
x=42
y=7
print(f"{x=} {y=} {x*y=}")

n=255
# 08b - 8 bits (binary), #06x - hex value in 6 digits (0x00ff)
print(f"Binary: {n:08b}, Hex: {n:#06x}, Sci: {123456789:.3e} Percent: {0.875:.2%}")

cfg = {"user":"sahan", "home":"/home/sahan"}    #Dictionary
print(f"User: {cfg['user']!r} lives in {cfg['home']}")

print(f"{name}")      # Alice
print(f"{name!s}")    # Alice          (same as above)
print(f"{name!r}")    # 'Alice'        (note the quotes)
print(f"{'a\tb\n'}")# 'a\tb\n'       
print(f"{'a\tb\n'!r}")# 'a\tb\n'       (escapes are visible)
print(f"{'mañana'!a}")# 'ma\xf1ana'    (non-ASCII escaped)