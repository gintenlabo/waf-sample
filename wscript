APPNAME = 'waf-test'
VERSION = '1.0.0'

srcdir = '.'
blddir = 'build'

subdirs='src'

def options(opt):
  opt.load('compiler_cxx unittest_gtest')

  opt.add_option('--enable-gcov',
                 dest='enable_gcov', action='store_true', default=False,
                 help='enable gcov to measure coverage')

  opt.recurse(subdirs)

def configure(conf):
  conf.load('compiler_cxx unittest_gtest')

  if conf.options.enable_gcov:
    conf.env.CXXFLAGS += ['-fprofile-arcs', '-ftest-coverage']
    conf.env.LINKFLAGS += ['-fprofile-arcs']

  conf.recurse(subdirs)

def build(bld):
  bld.recurse(subdirs)

def shutdown(ctx):
  ctx.recurse(subdirs)
