#!/usr/bin/bash -x

readonly LIST="py36 py37 py38"

for v in $LIST
do
	.tox/${v}/bin/python -m pip install --upgrade pytest pytest-cov sphindexer
done

