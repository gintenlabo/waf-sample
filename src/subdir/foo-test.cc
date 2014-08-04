#include "foo.hpp"

#include <gtest/gtest.h>

TEST(foo, call) {
  EXPECT_NO_THROW({ waf_sample::subdir::another_function(); });
}
