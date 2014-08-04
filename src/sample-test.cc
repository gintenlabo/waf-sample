#include "sample.hpp"

#include <gtest/gtest.h>

TEST(sample, trivial) {
  EXPECT_NO_THROW({ waf_sample::some_function(); });
}
