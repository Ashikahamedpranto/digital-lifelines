path = 'lib/app.dart'
with open(path, 'r') as f:
    content = f.read()

original = content

old_import = "import 'app_config.dart';"
new_import = "import 'app_config.dart';\nimport 'screens/home/data_discovery_screen.dart';"
if new_import not in content:
    content = content.replace(old_import, new_import)
    print("Added data_discovery_screen import")
else:
    print("Import already present")

old_home = "      home: const RootNavScreen(),"
new_home = ("      home: AppConfig.isLiteVersion\n"
            "          ? const DataDiscoveryScreen()\n"
            "          : const RootNavScreen(),")
if old_home not in content:
    print("ERROR: home line not found")
else:
    content = content.replace(old_home, new_home)
    print("Made home screen conditional on isLiteVersion")

if content == original:
    print("NOTHING CHANGED")
else:
    with open(path, 'w') as f:
        f.write(content)
    print("File saved.")
