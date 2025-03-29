cppunit_dep = dependency(
  'cppunit',
  required: get_option('tests'),
)
if not cppunit_dep.found()
  subdir_done()
endif

test_src = files(
  'main.cpp',
  'test_aiff.cpp',
  'test_ape.cpp',
  'test_apetag.cpp',
  'test_asf.cpp',
  'test_bytevector.cpp',
  'test_bytevectorlist.cpp',
  'test_bytevectorstream.cpp',
  'test_complexproperties.cpp',
  'test_dsdiff.cpp',
  'test_dsf.cpp',
  'test_file.cpp',
  'test_fileref.cpp',
  'test_flac.cpp',
  'test_flacpicture.cpp',
  'test_flacunknownmetadatablock.cpp',
  'test_id3v1.cpp',
  'test_id3v2.cpp',
  'test_id3v2framefactory.cpp',
  'test_info.cpp',
  'test_it.cpp',
  'test_list.cpp',
  'test_map.cpp',
  'test_mod.cpp',
  'test_mp4.cpp',
  'test_mp4coverart.cpp',
  'test_mp4item.cpp',
  'test_mpc.cpp',
  'test_mpeg.cpp',
  'test_ogg.cpp',
  'test_oggflac.cpp',
  'test_opus.cpp',
  'test_propertymap.cpp',
  'test_riff.cpp',
  'test_s3m.cpp',
  'test_sizes.cpp',
  'test_speex.cpp',
  'test_string.cpp',
  'test_synchdata.cpp',
  'test_trueaudio.cpp',
  'test_variant.cpp',
  'test_versionnumber.cpp',
  'test_wav.cpp',
  'test_wavpack.cpp',
  'test_xiphcomment.cpp',
  'test_xm.cpp',
)

test_runner = executable(
  'test_runner',
  test_src,
  cpp_args: '-DTESTS_DIR="@0@/"'.format(meson.current_source_dir()),
  dependencies: [cppunit_dep, taglib_dep],
)

test('test_runner', test_runner)
