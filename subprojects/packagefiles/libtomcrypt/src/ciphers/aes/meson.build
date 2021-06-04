all_sources += files(
  'aes.c',
)

# Recompile aes.c with ENCRYPT_ONLY macro.

aes_enc_lib = static_library('aes_enc', 'aes.c',
  include_directories : core_inc,
  c_args : ['-DENCRYPT_ONLY'])

extra_objects += [aes_enc_lib.extract_all_objects()]
