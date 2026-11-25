.PHONY: tests/libtest tests/server tests/unit tests/tunit

# Variables shared by the unity bundle recipes (see tests/*/Makefile.am).
define extract_bundle
$(eval include $1/Makefile.inc)
$(info BUNDLE=$(BUNDLE))
$(info FIRST_C=$(FIRST_C))
$(info UTILS_C=$(UTILS_C))
$(info CURLX_C=$(CURLX_C))
$(info TOOLX_C=$(TOOLX_C))
$(info TESTS_C=$(TESTS_C))
endef

tests/libtest:
	$(call extract_bundle,$@)

tests/server:
	$(call extract_bundle,$@)

tests/unit:
	$(call extract_bundle,$@)

tests/tunit:
	$(call extract_bundle,$@)
