fig_sources = {
  'pic-frame.pdf': files('pic-frame.fig'),
  'hilbert-mb.pdf': files('hilbert-mb.fig'),
  'hilbert-block.pdf': files('hilbert-block.fig'),
  'xifish.pdf': files('xifish.fig'),
  'superblock.pdf': files('superblock.fig'),
  'macroblock.pdf': files('macroblock.fig'),
  'raster-block.pdf': files('raster-block.fig'),
  'reference-frames.pdf': files('reference-frames.fig'),
  'pixel444.pdf': files('pixel444.fig'),
  'pixel422.pdf': files('pixel422.fig'),
  'pixel420.pdf': files('pixel420.fig'),
  'idct.pdf': files('idct.fig'),
  'fdct.pdf': files('fdct.fig'),
  'pic_even.pdf': files('pic_even.fig'),
  'pic_even_odd.pdf': files('pic_even_odd.fig'),
  'pic_odd.pdf': files('pic_odd.fig'),
  'pic_odd_even.pdf': files('pic_odd_even.fig'),
  'lflim.pdf': files('lflim.fig'),
}

fig_pdfs = []

foreach fig_name, fig_source : fig_sources
  pdf = custom_target(
    fig_name,
    command: [transfig_exe, '-L', 'pdf', '@INPUT@'],
    output: fig_name,
    input: fig_source,
    capture: true,
  )
  fig_pdfs += [pdf]
endforeach

vp3huff_sources = files('vp3huff.c')

vp3huff_exe = executable(
  'vp3huff',
  vp3huff_sources,
  native: true,
  install: false,
)

vp3huff_tex = custom_target(
  'vp3huff.tex',
  command: [vp3huff_exe],
  capture: true,
  output: 'vp3huff.tex',
)

spec_file = configure_file(
  input: 'spec.tex',
  output: 'spec.tex',
  copy: true,
)
bib_file = configure_file(
  input: 'spec.bib',
  output: 'spec.bib',
  copy: true,
)

latexmk_wrapper = find_program(
  'latexmk-wrapper.py',
  required: true,
)

built_docs = custom_target(
  'Theora.pdf',
  command: [latexmk_wrapper, latexmk_exe, '@INPUT@'],
  console: true,
  input: [spec_file],
  depend_files: [bib_file],
  depends: [fig_pdfs, vp3huff_tex],
  output: 'Theora.pdf',
  install: true,
  install_dir: get_option('datadir') / 'doc' / meson.project_name(),
)
