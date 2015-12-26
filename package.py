name = "ilmbase"

version = "2.1.0"

description = \
    """
    IlmBase
    """

variants = [
    ["platform-linux"]
]

uuid = "repository.ilmbase"

def commands():
    env.CMAKE_MODULE_PATH.append("{root}/cmake")
    env.LD_LIBRARY_PATH.append("{root}/lib")
