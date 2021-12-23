# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

data=[("Icons/*.png", "Icons"), ("logo_urls/*.CSV", "logo_urls")]
bin = [("lib/*", "lib")]


a = Analysis(['main.py'],
             pathex=['C:\\Users\\t7user\\PycharmProjects\\music_player'],
             binaries=bin,
             datas=data,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=True,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False, icon='Icons\\app.ico')

