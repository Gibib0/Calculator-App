# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('assets/images/background.jpeg', 'assets/images'),
        ('assets/images/screamer.jpeg', 'assets/images'),
        ('assets/sounds/background_sound.wav', 'assets/sounds'),
        ('assets/sounds/clean_sound_sound.wav', 'assets/sounds'),
        ('assets/sounds/click_sound.wav', 'assets/sounds'),
        ('assets/sounds/error_sound.wav', 'assets/sounds'),
        ('assets/sounds/operation_sound.wav', 'assets/sounds'),
        ('assets/sounds/screamer_sound.wav', 'assets/sounds'),
        ('assets/icons/icon.ico', 'assets/icons'),
        ('calculator.kv', '.')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='SuperDuperCalculator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    icon='assets/icons/icon.ico',
)