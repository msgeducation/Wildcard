#!/bin/bash
PARSED_ARGUMENTS=$(getopt -a -n maintenance -o edo --long enable,disable,enableold -- "$@")
if [ $? != 0 ]; then
	echo "Usage: wild moodle/maintenance.sh [ --enable | --disable ]"
	exit 2
fi
eval set -- "$PARSED_ARGUMENTS"
while :
do
	case "$1" in
		-e | --enable) ARG="--enable" ; shift ;;
		-d | --disable) ARG="--disable" ; shift ;;
		-o | --enableold) ARG="--enableold"; shift ;;
		--) shift; break ;;
		*) echo "something is broken. Got $1"; break ;;
	esac
done
# echo "$ARG"
sudo -u www-data php $WILD_MOODLE_DIR/admin/cli/maintenance.php $ARG
