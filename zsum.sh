echo 'pthon3:'
# find python3 -type f -name "*.*.py" | cut -f3 -d '.'| sort | uniq -c -i
find python3 -type f -name "*.*.py" | cut -f3 -d '/' | sort | uniq -c

easy=$(find python3 -type f -name "*.*.py" | cut -f3 -d '/' | sort | uniq -c | grep easy | tr -cd '[0-9]')
medium=$(find python3 -type f -name "*.*.py" | cut -f3 -d '/' | sort | uniq -c | grep medium | tr -cd '[0-9]')
hard=$(find python3 -type f -name "*.*.py" | cut -f3 -d '/' | sort | uniq -c | grep hard | tr -cd '[0-9]')
echo 'total: '$(( $easy+$medium+$hard ))

   