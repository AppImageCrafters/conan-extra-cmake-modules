from conans import ConanFile, CMake, tools


class ExtracmakemodulesConan(ConanFile):
    name = "extra-cmake-modules"
    version = "5.57.0"
    license = "MIT"
    author = "Alexis Lopez Zubieta contact@azubieta.net"
    url = "https://github.com/appimage-conan-community/conan-extra-cmake-modules"
    description = "Extra modules and scripts for CMake"
    topics = ("cmake", "ecm", "kde")
    settings = "os", "compiler", "build_type", "arch"
    build_requires = "cmake_installer/3.10.0@conan/stable"

    def source(self):
        self.run("git clone git://anongit.kde.org/extra-cmake-modules.git --depth=1 --branch=v5.57.0")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="extra-cmake-modules")
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.builddirs = ["share/ECM/cmake"]


