import 'package:flutter/material.dart';

import 'screens/about/about_screen.dart';
import 'screens/home/home_screen.dart';
import 'screens/record/record_screen.dart';
import 'screens/home/data_discovery_screen.dart';
import 'theme/app_theme.dart';
import 'app_config.dart';

class DigitalLifelinesApp extends StatelessWidget {
  const DigitalLifelinesApp({super.key});
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: AppConfig.isLiteVersion
          ? 'Where Have You Been All My Life?'
          : 'Digital Lifelines',
      theme: AppTheme.lightTheme,
      home: AppConfig.isLiteVersion
          ? const DataDiscoveryScreen()
          : const RootNavScreen(),
    );
  }
}

class RootNavScreen extends StatefulWidget {
  const RootNavScreen({super.key});
  @override
  State<RootNavScreen> createState() => _RootNavScreenState();
}

class _RootNavScreenState extends State<RootNavScreen> {
  int _currentIndex = 0;
  final List<Widget> _screens = const [
    HomeScreen(),
    RecordScreen(),
    DataDiscoveryScreen(),
    AboutScreen(),
  ];
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: IndexedStack(index: _currentIndex, children: _screens),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _currentIndex,
        onTap: (index) {
          setState(() {
            _currentIndex = index;
          });
        },
        showUnselectedLabels: true,
        selectedFontSize: 12,
        unselectedFontSize: 12,
        selectedItemColor: AppColors.primary,
        unselectedItemColor: Colors.grey,
        type: BottomNavigationBarType.fixed,
        items: const [
          BottomNavigationBarItem(
            icon: Icon(Icons.auto_graph_outlined),
            activeIcon: Icon(Icons.auto_graph),
            label: 'Lifelines',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.edit_note_outlined),
            activeIcon: Icon(Icons.edit_note),
            label: 'Record',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.search_outlined),
            activeIcon: Icon(Icons.search),
            label: 'Data discovery',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.settings_outlined),
            activeIcon: Icon(Icons.settings),
            label: 'About',
          ),
        ],
      ),
    );
  }
}
