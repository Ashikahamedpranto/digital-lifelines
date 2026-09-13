path = 'lib/app.dart'
with open(path, 'r') as f:
    content = f.read()

original = content

old_import = "import 'theme/app_theme.dart';"
new_import = "import 'theme/app_theme.dart';\nimport 'app_config.dart';"
if new_import not in content:
    content = content.replace(old_import, new_import)
    print("Added app_config import")

old_title = "    return MaterialApp(\n      title: 'Digital Lifelines',"
new_title = ("    return MaterialApp(\n      title: AppConfig.isLiteVersion\n"
             "          ? 'Where Have You Been All My Life?'\n"
             "          : 'Digital Lifelines',")
if old_title not in content:
    print("ERROR: title line not found")
else:
    content = content.replace(old_title, new_title)
    print("Made title dynamic based on isLiteVersion")

if content == original:
    print("NOTHING CHANGED")
else:
    with open(path, 'w') as f:
        f.write(content)
    print("File saved.")
