echo 'pthon3:'
# find python3 -type f -name "*.*.py" | cut -f3 -d '.'| sort | uniq -c -i
find python3 -type f -name "*.*.py" | cut -f3 -d '/' | sort | uniq -c
easy=$(find python3 -type f -name "*.*.py" | cut -f3 -d '/' | sort | uniq -c | grep easy | cut -f3 -d ' ')
medium=$(find python3 -type f -name "*.*.py" | cut -f3 -d '/' | sort | uniq -c | grep medium | cut -f3 -d ' ')
echo 'total: '$[$easy+$medium]