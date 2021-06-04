

saxparser_chunk_parsing_inconsistent_state = executable('saxparser_chunk_parsing_inconsistent_state',
						       join_paths('saxparser_chunk_parsing_inconsistent_state', 'main.cc'),
						       dependencies: libxmlpp_dep)

test('saxparser_chunk_parsing_inconsistent_state', saxparser_chunk_parsing_inconsistent_state)

saxparser_parse_double_free = executable('saxparser_parse_double_free',
					 join_paths('saxparser_parse_double_free', 'main.cc'),
					 dependencies: libxmlpp_dep)
test('saxparser_parse_double_free', saxparser_parse_double_free)

saxparser_parse_stream_inconsistent_state = executable('saxparser_parse_stream_inconsistent_state',
						       join_paths('saxparser_parse_stream_inconsistent_state', 'main.cc'),
						       dependencies: libxmlpp_dep)
test('saxparser_parse_stream_inconsistent_state', saxparser_parse_stream_inconsistent_state)
