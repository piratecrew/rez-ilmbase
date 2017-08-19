CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

set(boost_STATIC ON)
set(boost_COMPONENTS python)
rez_find_packages(python PREFIX pkgs AUTO)

set(openexr_version ${ILMBASE_VERSION})

set(url_openexr https://github.com/openexr/openexr.git)
set(tag_openexr v${openexr_version})

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

message(STATUS "BOOST_ROOT=$ENV{BOOST_ROOT} -DBOOST_INCLUDEDIR=${boost_INCLUDE_DIRS} -DBOOST_LIBRARYDIR=${boost_LIBRARY_DIRS} -DBoostLIBRARIES=${boost_LIBRARIES}")
# Just Clone and checkout the right tag.
# The build is made in the next External Command.
ExternalProject_add(
  openexr
  GIT_REPOSITORY ${url_openexr}
  GIT_TAG ${tag_openexr}
  PREFIX openexr
  UPDATE_COMMAND ""
  CONFIGURE_COMMAND ""
  BUILD_COMMAND ""
  INSTALL_COMMAND ""
)

ExternalProject_add(
    ilmbase
    DEPENDS openexr
    PREFIX ilmbase
    DOWNLOAD_COMMAND ""
    SOURCE_DIR ${PROJECT_BINARY_DIR}/openexr/src/openexr/IlmBase
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} -DNAMESPACE_VERSIONING=OFF
    BUILD_IN_SOURCE 0
)

ExternalProject_add(
    pyilmbase
    DEPENDS ilmbase
    PREFIX pyilmbase
    DOWNLOAD_COMMAND ""
    PATCH_COMMAND ${CMAKE_CURRENT_SOURCE_DIR}/patch_pyilmbase_cmake.sh CMakeLists.txt #Don't really know why i need to do this
    SOURCE_DIR ${PROJECT_BINARY_DIR}/openexr/src/openexr/PyIlmBase
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} -DNAMESPACE_VERSIONING=OFF -DBoost_DEBUG=1 -DILMBASE_PACKAGE_PREFIX=${CMAKE_INSTALL_PREFIX} -DBoost_PYTHON_LIBRARY=boost_python -DPYTHON_INCLUDE_DIR=${python_INCLUDE_DIRS} -DPYTHON_LIBRARY=${python_LIBRARIES}
    BUILD_IN_SOURCE 1
)

rez_install_files(
    cmake/ilmbase.cmake
    DESTINATION .
)
