path = 'android/app/build.gradle.kts'
with open(path, 'r') as f:
    content = f.read()

original = content

old_block = """    defaultConfig {
        // TODO: Specify your own unique Application ID (https://developer.android.com/studio/build/application-id.html).
        applicationId = "edu.clarkson.cs550.digital_lifelines"
        // You can update the following values to match your application needs.
        // For more information, see: https://flutter.dev/to/review-gradle-config.
        minSdk = flutter.minSdkVersion
        targetSdk = flutter.targetSdkVersion
        versionCode = flutter.versionCode
        versionName = flutter.versionName
    }"""

new_block = """    defaultConfig {
        // TODO: Specify your own unique Application ID (https://developer.android.com/studio/build/application-id.html).
        applicationId = "edu.clarkson.cs550.digital_lifelines"
        // You can update the following values to match your application needs.
        // For more information, see: https://flutter.dev/to/review-gradle-config.
        minSdk = flutter.minSdkVersion
        targetSdk = flutter.targetSdkVersion
        versionCode = flutter.versionCode
        versionName = flutter.versionName
    }

    flavorDimensions += "version"
    productFlavors {
        create("full") {
            dimension = "version"
            applicationId = "edu.clarkson.cs550.digital_lifelines"
            resValue("string", "app_name", "Digital Lifelines")
        }
        create("lite") {
            dimension = "version"
            applicationId = "edu.clarkson.cs550.digital_lifelines.lite"
            resValue("string", "app_name", "Where Have You Been All My Life?")
        }
    }"""

if old_block not in content:
    print("ERROR: defaultConfig block not found")
else:
    content = content.replace(old_block, new_block)
    print("Added productFlavors block for full/lite versions")

if content == original:
    print("NOTHING CHANGED")
else:
    with open(path, 'w') as f:
        f.write(content)
    print("File saved.")
