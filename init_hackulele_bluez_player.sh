#! /bin/sh
### BEGIN INIT INFO
# Provides: hackulele_bluez_player
# Required-Start: $syslog bluetooth
# Required-Stop: $syslog
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Short-Description: hackulele_bluez_player
# Description:
### END INIT INFO

case "$1" in
    start)
        /usr/bin/python /usr/share/hackulele/bluez_player.py >/dev/null &
        echo "$!" > /tmp/hackulele.pid
        ;;
    stop)
        if [ -f "/tmp/hackulele.pid" ]; then
            pid="$(cat /tmp/hackulele.pid)"
	    while sudo kill "$pid" 2>/dev/null; do
	      sleep 0.1
	    done
            rm /tmp/hackulele.pid
        else
            echo "No PID file"
        fi
        ;;
    *)
        echo "$0 {start|stop}"
        exit 1
        ;;
esac

exit 0
