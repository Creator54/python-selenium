with import <nixpkgs> { };

pkgs.mkShell rec {
  name = "impurePythonEnv";
  venvDir = "./.venv";
  buildInputs = [
    python38Packages.python
    zlib
  ];

  shellHook = ''
    set -h #remove "bash: hash: hashing disabled" warning !
    SOURCE_DATE_EPOCH=$(date +%s)

    if ! [ -d "${venvDir}" ]; then
      ${python38Packages.python.interpreter} -m venv "${venvDir}"
    fi
    export LD_LIBRARY_PATH="${lib.makeLibraryPath [ zlib stdenv.cc.cc ]}":LD_LIBRARY_PATH;
    source "${venvDir}/bin/activate"
    pip install -r requirements.txt
  '';
}
