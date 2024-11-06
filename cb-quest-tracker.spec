# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['CBQuestTracker.py'],
    pathex=[],
    binaries=[],
    datas=[('vocabulary.json', '.'), ('templates', 'templates'), ('static', 'static'), ('Tesseract-OCR', 'Tesseract-OCR')],
    hiddenimports=['engineio.async_drivers.gevent'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='CB Quest Tracker',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    icon='logo.icns',
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
