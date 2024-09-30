# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_iir_nav2_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED iir_nav2_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(iir_nav2_FOUND FALSE)
  elseif(NOT iir_nav2_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(iir_nav2_FOUND FALSE)
  endif()
  return()
endif()
set(_iir_nav2_CONFIG_INCLUDED TRUE)

# output package information
if(NOT iir_nav2_FIND_QUIETLY)
  message(STATUS "Found iir_nav2: 1.3.1 (${iir_nav2_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'iir_nav2' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT iir_nav2_DEPRECATED_QUIET)
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(iir_nav2_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${iir_nav2_DIR}/${_extra}")
endforeach()
