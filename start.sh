#!/bin/sh

spotifystats start &
spotifystats run-api &

tail -f /dev/null
