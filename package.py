name = "ilmbase"

version = "2.2.0"

description = \
    """
    IlmBase
    """

variants = [
    ["platform-linux"]
]

requires = [
    "python-2.7",
    "boost-1.54+"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python2.7/site-packages")
    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
