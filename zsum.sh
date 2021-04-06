echo 'pthon3:\n'
find python3 -type f -name "*.*.py" | cut -f3 -d '.'| sort | uniq -c -i