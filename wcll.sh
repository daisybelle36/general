#!/bin/bash
# from Kevin
#set -x
#
# $Id$

function usage
{
	rc=$1
	reason=$2
	prog=$(basename $0)
	
	exec 1>&2
	printf "==> %s <==\n" $0
	if [ "$reason" != "" ]
	then
		printf "\nERROR: %s\n" "$reason"
	fi

	cat <<-EOF

	$(basename $0) - print line counts for the given files in
	          date-modified order (like 'ls -lrt')

	Usage:
	  $0 [ -d ] [ file [ file ... ] ]
	  $0 -h
	
	Options:

	  -d  = print date-stamp as well
	  -h  = print this message
	
	EOF
	exit
}

USE_LS='ls'
#if [ "$(uname)" == "Darwin" ]; then
	#USE_LS='gls'
#fi

LS="$(which $USE_LS)"
if [ -z "$LS" ]; then
	usage 1 "Can't find ls executable for '$USE_LS'"
elif [ ! -x "$LS" ]; then
	usage 1 "Can't see ls executable '$LS'"
fi

lscmd="$LS -lrt --time-style=+%Y-%m-%d"

dateprint=0

while getopts :dh opt ; do
	case $opt in
		d) dateprint=1 ;;
		h) usage ;;
		*) usage 1 "Invalid option '-$OPTARG'" ;;
	esac
done

shift $(($OPTIND - 1))

files=$@

ls -1tr $files | while read file ; do
	# ignore anything that isn't a file
	if [ ! -f "$file" ]; then
		continue
	# grab the datestamp if required
	elif [ $dateprint -eq 1 ] ; then
		datestamp=$($lscmd "$file" | awk '{ print $6 }')
	fi
	# get the line count
	count=$(wc -l -- "$file" 2>/dev/null | awk '{ print $1 }')
	# and print the lot
	printf "%8s  " ${count:-"ERROR"}
	[ $dateprint -eq 1 ] && printf "%-12s  " "$datestamp" 
	printf "%s\n" "$file"
done

