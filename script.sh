#!/bin/bash

domain=$(cat domains.txt)
for LINE in $domain
do
    assetfinder --subs-only $domain >> 1.txt
    subfinder -silent -d $domain -all >> 2.txt
    ./findomain-linux -r -q -t $domain >> 3.txt
    curl -s "https://api.hackertarget.com/hostsearch/?q=$domain" | cut -d ',' -f1 >> 4.txt
    curl -s "https://riddler.io/search/exportcsv?q=pld:$domain" | cut -d ',' -f6 | sed 's/Keywords//' | sed '/^$/d' >> 5.txt
    curl -s "https://crt.sh/?q=%25.$domain&output=json" | jq -r '.[].name_value' 2>/dev/null | sed 's/\*\.//g' >> 6.txt
done     
  cat *.txt > all.txt
  cat all.txt | sort -u > allUnique.txt
