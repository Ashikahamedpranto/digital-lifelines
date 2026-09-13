path = 'ios/Runner/Info.plist'
with open(path, 'r') as f:
    content = f.read()

original = content

old_display = """        <key>CFBundleDisplayName</key>
        <string>Digital Lifelines</string>"""
new_display = """        <key>CFBundleDisplayName</key>
        <string>$(PRODUCT_NAME)</string>"""
if old_display not in content:
    print("ERROR: CFBundleDisplayName not found")
else:
    content = content.replace(old_display, new_display)
    print("Fixed CFBundleDisplayName")

old_name = """        <key>CFBundleName</key>
        <string>Digital Lifelines</string>"""
new_name = """        <key>CFBundleName</key>
        <string>$(PRODUCT_NAME)</string>"""
if old_name not in content:
    print("ERROR: CFBundleName not found")
else:
    content = content.replace(old_name, new_name)
    print("Fixed CFBundleName")

if content == original:
    print("NOTHING CHANGED")
else:
    with open(path, 'w') as f:
        f.write(content)
    print("File saved.")

