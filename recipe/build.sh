#!/bin/bash

mkdir build
cd build

cmake ${CMAKE_ARGS} \
  -DCMAKE_INSTALL_PREFIX=$PREFIX \
  -DCMAKE_PREFIX_PATH=$PREFIX \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
  -DCMARK_TESTS=OFF \
  -DCMAKE_BUILD_TYPE=Release \
  ..

make -j${CPU_COUNT} VERBOSE=1
make install
