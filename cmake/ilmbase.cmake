find_package(PkgConfig)
set( ENV{PKG_CONFIG_PATH} $ENV{PKG_CONFIG_PATH}:$ENV{REZ_ILMBASE_ROOT}/lib/pkgconfig)
pkg_check_modules (ILMBASE REQUIRED IlmBase)
set(ilmbase_INCLUDE_DIRS    ${ILMBASE_INCLUDE_DIRS};$ENV{REZ_ILMBASE_ROOT}/include)
set(ilmbase_LIBRARY_DIRS    ${ILMBASE_LIBRARY_DIRS})
set(ilmbase_LIBRARIES       ${ILMBASE_LIBRARIES})
