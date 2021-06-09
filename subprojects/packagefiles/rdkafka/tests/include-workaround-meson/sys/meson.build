# For some reason, rdkafka includes a copy of queue.h, but still includes it as <sys/queue.h>, not using it
# This is a workaround for creating a sys/ folder with the queue header in it
# See https://github.com/mesonbuild/meson/issues/2546 for where the technique comes from
configure_file(
  copy: true,
  input: '../../../src/queue.h',
  output: '@PLAINNAME@',
)
