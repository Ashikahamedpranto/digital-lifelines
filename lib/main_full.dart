import 'package:flutter/material.dart';

import 'app_config.dart';
import 'app.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  AppConfig.isLiteVersion = false;
  runApp(const DigitalLifelinesApp());
}
