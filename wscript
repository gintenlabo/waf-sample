APPNAME = 'waf-test'
VERSION = '1.0.0'

srcdir = '.'
blddir = 'build'

subdirs='src'

def options(opt):
    opt.load('compiler_cxx unittest_gtest')
    opt.recurse(subdirs)

def configure(conf):
    conf.load('compiler_cxx unittest_gtest')
    conf.recurse(subdirs)

def build(bld):
    bld.recurse(subdirs)

def shutdown(ctx):
    ctx.recurse(subdirs)
