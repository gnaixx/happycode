echo 'pthon3:'
# find python3 -type f -name "*.*.py" | cut -f3 -d '.'| sort | uniq -c -i
find python3 -type f -name "*.*.py" | cut -f3 -d '/' | sort | uniq -c