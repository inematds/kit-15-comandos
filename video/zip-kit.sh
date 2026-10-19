#!/usr/bin/env bash
# empacota kit/ em kit-15-comandos.zip (pasta raiz kit-15-comandos/) para a release kit-v1.0.0
set -e; cd ~/projetos/kit-15-comandos; T=$(mktemp -d); cp -r kit "$T/kit-15-comandos"
(cd "$T" && zip -qr kit-15-comandos.zip kit-15-comandos); mv "$T/kit-15-comandos.zip" ./kit-15-comandos.zip; rm -rf "$T"; unzip -l kit-15-comandos.zip | tail -1
