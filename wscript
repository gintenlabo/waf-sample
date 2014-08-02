APPNAME = 'waf-test'
VERSION = '1.0.0'

srcdir = '.'
blddir = 'build'

def options(opt):
    # プロジェクトのオプションを設定する
    # 最初に呼ばれる
    pass

def configure(conf):
    # ライブラリのチェックなど
    # waf configure 時に呼ばれる
    pass

def build(bld):
    # ビルドの情報を書く
    # waf build 時に呼ばれる
    pass

def shutdown(ctx):
    # 終了時に何かをさせたいとき
    # 最後に呼ばれる
    pass
