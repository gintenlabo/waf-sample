APPNAME = 'waf-test'
VERSION = '1.0.0'

srcdir = '.'
blddir = 'build'

def options(opt):
    opt.load('compiler_cxx unittest_gtest')

def configure(conf):
    conf.load('compiler_cxx unittest_gtest')

def build(bld):
    # ビルドの情報を書く
    # waf build 時に呼ばれる
    pass

def shutdown(ctx):
    # 終了時に何かをさせたいとき
    # 最後に呼ばれる
    pass
