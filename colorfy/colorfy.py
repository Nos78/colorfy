# @Author: Noscere
# @Email: noscere1978@gmail.com
# @Date: 2022-11-19 23:07:28.856
# @Last Modified by:   undefined
# @Last Modified time: 2022-11-19 23:07:28.856
# @Description: colorfy package
# The overriding aim when developing this package was efficiency. To that end,
# although it would otherwise seem logical to implement the package as a class,
# it uses basic data types and simple functions where possible.
# The interface to an imported package/library acts very like a class would,
# with functions and variables accessed via a '.'(dot) operator , as though
# they where methods and properties of a named class.
# e.g. import colorfy
#      myColourfulString = colorfy.WARNING + "A colourful string"
#      colorfy.print("I am a blue string", "blue")
# With that in mind, there was no real benefit to adding more layers to the
# implementation.

# ANSI 
