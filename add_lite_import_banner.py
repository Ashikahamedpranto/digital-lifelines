path = 'lib/screens/home/data_discovery_screen.dart'
with open(path, 'r') as f:
    content = f.read()

original = content

old_import = "import '../../database/db_helper.dart';"
new_import = "import '../../database/db_helper.dart';\nimport '../../app_config.dart';"
if new_import not in content:
    content = content.replace(old_import, new_import)
    print("Added app_config import")
else:
    print("Import already present")

old_state = """class _DataDiscoveryScreenState extends State<DataDiscoveryScreen> {
  bool _isBackfilling = false;"""
new_state = """class _DataDiscoveryScreenState extends State<DataDiscoveryScreen> {
  bool _isBackfilling = false;
  bool _hasCheckedData = false;
  bool _hasPhotoData = false;
  bool _isImporting = false;

  @override
  void initState() {
    super.initState();
    if (AppConfig.isLiteVersion) {
      _checkExistingData();
    } else {
      _hasCheckedData = true;
    }
  }

  Future<void> _checkExistingData() async {
    final timelines = await DBHelper.instance.getTimelines();
    final exists = timelines.any((t) => t.name == 'My Places');
    if (!mounted) return;
    setState(() {
      _hasPhotoData = exists;
      _hasCheckedData = true;
    });
  }

  Future<void> _importPhotos() async {
    setState(() {
      _isImporting = true;
    });
    await DBHelper.instance.importFromPhotos();
    if (!mounted) return;
    setState(() {
      _isImporting = false;
      _hasPhotoData = true;
    });
  }"""
if old_state not in content:
    print("ERROR: state class declaration not found")
else:
    content = content.replace(old_state, new_state)
    print("Added lite-version data check and import logic")

old_banner_spot = """            const Text(
              'One question. One yes. One real answer.',
              style: TextStyle(
                fontSize: 15,
                color: AppColors.mutedText,
              ),
            ),
            const SizedBox(height: 28),"""
new_banner_spot = """            const Text(
              'One question. One yes. One real answer.',
              style: TextStyle(
                fontSize: 15,
                color: AppColors.mutedText,
              ),
            ),
            if (AppConfig.isLiteVersion &&
                _hasCheckedData &&
                !_hasPhotoData) ...[
              const SizedBox(height: 20),
              InkWell(
                borderRadius: BorderRadius.circular(14),
                onTap: _isImporting ? null : _importPhotos,
                child: Container(
                  width: double.infinity,
                  padding: const EdgeInsets.all(16),
                  decoration: BoxDecoration(
                    color: AppColors.accent.withValues(alpha: 0.1),
                    borderRadius: BorderRadius.circular(14),
                  ),
                  child: Row(
                    children: [
                      if (_isImporting)
                        const SizedBox(
                          width: 18,
                          height: 18,
                          child: CircularProgressIndicator(strokeWidth: 2),
                        )
                      else
                        const Icon(Icons.photo_library_outlined,
                            size: 20, color: AppColors.accent),
                      const SizedBox(width: 12),
                      Expanded(
                        child: Text(
                          _isImporting
                              ? 'Importing...'
                              : 'No data yet - tap to import the metadata '
                                  'from your photos. This stays only on '
                                  'your phone.',
                          style: const TextStyle(
                            fontSize: 13,
                            fontWeight: FontWeight.w600,
                            color: AppColors.appBarText,
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ],
            const SizedBox(height: 28),"""
if old_banner_spot not in content:
    print("ERROR: banner insertion spot not found")
else:
    content = content.replace(old_banner_spot, new_banner_spot)
    print("Added lite-version import banner")

if content == original:
    print("NOTHING CHANGED")
else:
    with open(path, 'w') as f:
        f.write(content)
    print("File saved.")
