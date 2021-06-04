# https://github.com/mesonbuild/meson/issues/2546
install_headers(api, subdir: 'yajl')
foreach h: api
	configure_file(
		copy: true,
		input: h,
		output: '@PLAINNAME@',
	)
endforeach

configure_file(configuration: version,
	input: versionh,
	output: 'yajl_version.h',
	format: 'cmake',
	install: true,
	install_dir: 'include/yajl',
)
