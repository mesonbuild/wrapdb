fs = import('fs')
foreach h : aacencinclude_headers
  configure_file(
    input: h,
    output: fs.name(h),
    copy: true,
  )
endforeach
