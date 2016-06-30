from spack import *

class TrivialOuter(Package):
    """Description"""

    homepage = "http://www.example.com"

    version('git', git='https://github.com/DavidPoliakoff/trivial_outer.git', branch='master')
    depends_on_git("https://github.com/DavidPoliakoff/trivial_outer")

    def install(self, spec, prefix):
        cmake('.',*std_cmake_args)
        make()
        make("install")

