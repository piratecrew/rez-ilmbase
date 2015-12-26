CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

set(openexr_version ${ILMBASE_VERSION})

set(url_openexr https://github.com/openexr/openexr.git)
set(tag_openexr v${ilmbase_version})

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

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
    UPDATE_COMMAND ./bootstrap
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX}
    BUILD_IN_SOURCE 1
)

rez_install_files(
    cmake/ilmbase.cmake
    DESTINATION .
)