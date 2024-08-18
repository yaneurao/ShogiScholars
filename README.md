# ShogiScholars

本スクリプトは、USIプロトコル対応、詰将棋エンジンとの合議用スクリプトです。

例えば、詰将棋エンジン(KomoringHeightsを想定)とやねうら王とを組み合わせて、長手数の詰将棋が解ける思考エンジンを手に入れることができます。

# 特長

- すべてPythonのみで書かれている。
- Pythonのスクリプトに型アノテーションがきちんとつけられている。
- 他の外部ライブラリ(cshogiなど)に依存していない。
- 改造しやすいようになるべく簡潔に書かれている。
- スクリプト本体がとても短い(わずか100行！)

# 使い方

## 詰将棋エンジンとやねうら王との合議

1. Python本体をインストール。(手順略)

2. 次のようにフォルダを編成する。

enginesというフォルダを作成し、そのなかにエンジン名(任意)でフォルダを作成。そこにエンジン本体を配置する。エンジン本体の実行ファイル(拡張子は.exe)は、そのフォルダに一つだけ配置する。(複数配置するとそれらすべての合議となってしまう。)

⚠ エンジンは一度直接起動して、`bench`コマンドが実行できることを確認しておくこと。(KomoringHeightsに関しては、`usi`コマンドが実行できることを確認しておくこと。)

⚠ engine_options.txt は、やねうら王のエンジン設定の表記に従って書くこと。[エンジンオプションのデフォルト値の変更 - やねうら王Wiki](https://github.com/yaneurao/YaneuraOu/wiki/%E9%9A%A0%E3%81%97%E6%A9%9F%E8%83%BD#%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%B3%E3%82%AA%E3%83%97%E3%82%B7%E3%83%A7%E3%83%B3%E3%81%AE%E3%83%87%E3%83%95%E3%82%A9%E3%83%AB%E3%83%88%E5%80%A4%E3%81%AE%E5%A4%89%E6%9B%B4)

```
📂 ShogiScholars
  shogi-scholars-yane-komori.bat
  shogi-scholars.py
  📂 engines ⇐ このフォルダ名でフォルダを作成する。(名前変更不可)
    📂 YaneuraOu ⇐ このフォルダ名は任意
       YaneuraOu_NNUE_halfkp_512x2_8_64-V832DEV_AVX2.exe ⇐ 思考エンジンをここに配置
       📂 eval
         nn.bin ⇐ やねうら王から使う評価関数ファイル
    📂 KomoringHeights ⇐ このフォルダ名は任意
       user-normal-clang++-avx2.exe ⇐ KomoringHeightsの実行ファイルを配置する。
       engine_options.txt ⇐ 必要ならば、エンジン設定はここに書いておく。
```

3. shogi-scholars.bat をGUIから思考エンジンとして登録する。

※ GUIとは、ShogiHome、ShogiGUI、将棋所など。

# 関連リンク

- [やねうら王 GitHub](https://github.com/yaneurao/YaneuraOu)
- [KomoringHeights](https://github.com/komori-n/KomoringHeights)
- [ShogiHome](https://sunfish-shogi.github.io/electron-shogi/)
- [ShogiGUI](http://shogigui.siganus.com/)
- [将棋所](http://shogidokoro.starfree.jp/)

# ライセンス

MIT License
