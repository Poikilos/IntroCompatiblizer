# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a
Changelog](https://keepachangelog.com/en/1.0.0/).


## [git] - 2020-06-18
### Changed
- Stop using ListView since it is not in Kivy 2.0rc3-git.
- Begin conforming to PEP8.
- Move the example `ffmpeg concat` list to the readme.

### Added
- Add alternative methods of displaying output (using labels in a
  `BoxLayout` instead of items in a `ListView`): `pushS`, `changeLastS`.
- Add install instructions to readme that work on Fedora 32.


## [git] - 2018-01-10
- Allow running without MP4Box but show error on trying to add MP4 files
  (`require_MP4Box_enable`, a hard coded option set to False, still
  exists--If True, it will show an error, pause, then exit if
  MP4Box (gpac) is missing).


## [git] - 2017-05-29
### Added
- Add separate Delay button.
- Allow multiple filetypes for intro (For all types in Intro folder,
  the matching videos will be listed).
  - Deprecate `introVideoFileString` and `required_dotext`.

### Changed
- Deprecate `done_flag` in favor of `done_flags` and `flag_index`.
- Change MP4Box command to use `-cat` for both video files (instead of
  `-add <file1> -cat <file2>`) so that delay works properly (not sure
  why didn't, but some sites suggest `-cat <file1> -cat <file2>` is
  proper syntax)
- Go back to preferring MP4Box (revert to MP4Box, if present, when about
  to operate on an MP4)
  - Deprecate `converter_exe_path` (instead, use
    `exe_by_package[converter_package]`).
- Use `splitext` for `get_dotext` and `get_filenamenoext`.
- `get_dotext` should return nothing (not filename) when no dot is
  present.
- Change methods and many variables to underscore naming instead of
  camelhump.


## [git] - 2017-02-26
### Changed
- Detect profile path and use cross-platform pathing.
- Create folders needed, to avoid a crash when moving file when the
  destination folder didn't exist.
- The blank version of the Add Intro button should show a message
  instead of crashing when no files are present.
- Switch from ffmpeg to MP4Box (only when run on linux) to avoid
  outdated packages which have concat errors and slowness (due to the
  distro retaining old versions of ffmpeg).
