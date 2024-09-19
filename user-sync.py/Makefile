output_dir = dist
output_filename = user-sync
prebuilt_dir = external

ifeq ($(OS),Windows_NT)
	rm_path := $(shell python -c "import distutils.spawn; print(distutils.spawn.find_executable('rm'))")
    ifeq ($(rm_path),None)
        RM := rmdir /S /Q
    else
	    RM := $(rm_path) -rf
    endif
else
    RM := rm -rf
endif

standalone:
	../venv/bin/pip install --upgrade pyinstaller
	../venv/bin/pip install --upgrade setuptools==72.1.0
	-$(RM) $(output_dir)
	python3 .build/pre_build.py
	../venv/bin/pyinstaller --clean --noconfirm user-sync.spec

test:
	nosetests --no-byte-compile tests
